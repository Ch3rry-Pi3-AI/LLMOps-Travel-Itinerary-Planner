"""
itinerary_chain.py

Defines the itinerary generation chain for the LLMOps Travel Itinerary Planner.
This module builds a runnable sequence using LangChain Expression Language (LCEL),
combining a prompt template, a Groq chat model, and a string output parser to
produce clean, strictly formatted Markdown travel itineraries.

Functions
---------
generate_itinerary(city: str, interests: list[str]) -> str
    Generate a 1-day travel itinerary based on a city and list of interests.

Objects
-------
itinerary_chain : RunnableSequence
    LCEL pipeline composed of: Prompt → Groq Model → StrOutputParser.
"""

# --------------------------------------------------------------
# Imports
# --------------------------------------------------------------

# Groq LLM wrapper for LangChain
from langchain_groq import ChatGroq

# Structured chat prompt builder
from langchain_core.prompts import ChatPromptTemplate

# Converts model output to a plain string
from langchain_core.output_parsers import StrOutputParser

# Load API key from configuration module
from src.config.config import GROQ_API_KEY


# --------------------------------------------------------------
# Model Configuration
# --------------------------------------------------------------

# Create the Groq model instance
llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,         # API key loaded from .env
    model="llama-3.3-70b-versatile",   # Latest Groq Llama-3.3 model
    temperature=0.3                    # Balanced creativity level
)


# --------------------------------------------------------------
# Strict Markdown System Prompt
# --------------------------------------------------------------

SYSTEM_INSTRUCTIONS = """
You are an expert travel assistant who ALWAYS responds in clean, well-structured Markdown.

Follow these EXACT formatting rules. Do not deviate:

1. Your entire output MUST start with a blank line, followed by:

Your {city} 1-Day Itinerary is ...

#### Morning
* Time: Activity
* Time: Activity
* Time: Activity

#### Afternoon
* Time: Activity
* Time: Activity

#### Evening
* Time: Activity
* Time: Activity

2. ALWAYS include a blank line before each heading.
3. EACH bullet point must be on its own line starting with "* ".
4. NEVER merge or combine headings on the same line.
5. NEVER collapse bullet points into a single line.
6. Do NOT add any text outside the formatted itinerary.

Generate a polished and helpful itinerary based on the given city and user interests.
"""


# --------------------------------------------------------------
# Prompt Template
# --------------------------------------------------------------

# Build the chat prompt using system and human messages
prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_INSTRUCTIONS),
    ("human", "Generate a one-day itinerary for {city} based on these interests: {interests}")
])


# --------------------------------------------------------------
# Runnable Chain (LCEL)
# --------------------------------------------------------------

# Compose the pipeline: Prompt → LLM → Output Parser
itinerary_chain = prompt | llm | StrOutputParser()


# --------------------------------------------------------------
# Public API
# --------------------------------------------------------------
def generate_itinerary(city: str, interests: list[str]) -> str:
    """
    Generate a strictly formatted Markdown travel itinerary.

    Parameters
    ----------
    city : str
        The city for which the itinerary should be generated.
    interests : list[str]
        User interests such as ["museums", "coffee", "art"].

    Returns
    -------
    str
        A clean, Markdown-formatted itinerary generated through LCEL.
    """
    # Prepare inputs for the prompt variables
    input_data = {
        "city": city,
        "interests": ", ".join(interests)
    }

    # Invoke the runnable chain (Prompt → Model → Parser)
    result = itinerary_chain.invoke(input_data)

    return result


# --------------------------------------------------------------
# Standalone Test Runner
# --------------------------------------------------------------
if __name__ == "__main__":
    # Simple standalone execution for quick testing
    sample_city = "Lisbon"
    sample_interests = ["history", "coffee", "viewpoints"]

    print("\n🧪 Testing itinerary generation...\n")
    output = generate_itinerary(sample_city, sample_interests)
    print(output)
    print("\n✅ Done.\n")
