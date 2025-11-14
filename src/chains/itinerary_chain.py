"""
itinerary_chain.py

Defines the itinerary generation chain for the LLMOps Travel Itinerary Planner.
This module builds a runnable sequence using LangChain Expression Language (LCEL),
combining a prompt template, a Groq chat model, and a string output parser to
produce clean, Markdown-formatted travel itineraries.

Functions
---------
generate_itinerary(city: str, interests: list[str]) -> str
    Generate a day-trip itinerary using the runnable chain.

Objects
-------
itinerary_chain : RunnableSequence
    Composed LCEL pipeline: Prompt → Model → StrOutputParser
"""

# --------------------------------------------------------------
# Imports
# --------------------------------------------------------------

# Groq-based chat model wrapper for LangChain
from langchain_groq import ChatGroq

# Prompt template builder for chat formatting
from langchain_core.prompts import ChatPromptTemplate

# Parses model output into a final string (good for Markdown)
from langchain_core.output_parsers import StrOutputParser

# Securely load API keys from config
from src.config.config import GROQ_API_KEY


# --------------------------------------------------------------
# Model Configuration
# --------------------------------------------------------------

# Instantiate the Groq chat model with deterministic generation
llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,         # API key loaded via .env + config.py
    model="llama-3.3-70b-versatile",   # Current Groq Llama 3.3 model
    temperature=0.3                    # Balanced creativity + reliability
)


# --------------------------------------------------------------
# Prompt Template
# --------------------------------------------------------------

# Define the message structure for itinerary creation
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful travel assistant. Create a concise 1-day itinerary "
        "for {city} based on the user's interests: {interests}. "
        "Respond in clear Markdown with short bullet points grouped by "
        "time of day (Morning, Afternoon, Evening)."
    ),
    (
        "human",
        "Please generate the itinerary."
    ),
])


# --------------------------------------------------------------
# Runnable Chain (LCEL)
# --------------------------------------------------------------

# Compose: Prompt → LLM → OutputParser as a repeatable pipeline
itinerary_chain = prompt | llm | StrOutputParser()


# --------------------------------------------------------------
# Public API
# --------------------------------------------------------------
def generate_itinerary(city: str, interests: list[str]) -> str:
    """
    Generate a concise, Markdown-formatted day-trip itinerary.

    Parameters
    ----------
    city : str
        The target city for the itinerary (e.g., "Vienna").
    interests : list[str]
        List of user interests (e.g., ["art", "coffee", "architecture"]).

    Returns
    -------
    str
        A Markdown itinerary produced by the Groq LLM via the runnable chain.
    """
    # Format runtime values for the prompt
    input_data = {
        "city": city,
        "interests": ", ".join(interests)
    }

    # Execute the runnable chain (Prompt → LLM → Parser)
    result = itinerary_chain.invoke(input_data)

    return result


# --------------------------------------------------------------
# Standalone Test Runner
# --------------------------------------------------------------
if __name__ == "__main__":
    # Simple manual test without requiring Streamlit or Planner class
    sample_city = "Lisbon"
    sample_interests = ["history", "coffee", "viewpoints"]

    print("\n🧪 Testing itinerary generation...\n")
    output = generate_itinerary(sample_city, sample_interests)
    print(output)
    print("\n✅ Done.\n")
