"""
itinerary_chain.py

LangChain-based itinerary generator for the LLMOps Travel Itinerary Planner.

This module connects a Groq chat model to a simple function that produces a
concise, bulleted **day-trip itinerary** for a given city and list of interests.

Functions
---------
generate_itinerary(city: str, interests: list[str]) -> str
    Produce a brief, bulleted itinerary using the configured Groq chat model.
"""

# --------------------------------------------------------------
# Imports
# --------------------------------------------------------------
# Import Groq chat model wrapper for LangChain integration
from langchain_groq import ChatGroq

# Import structured chat prompt builder
from langchain_core.prompts import ChatPromptTemplate

# Import Groq API key securely from config
from src.config.config import GROQ_API_KEY


# --------------------------------------------------------------
# Model Configuration
# --------------------------------------------------------------
# Create a Groq-backed chat model instance
llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,            # API key string
    model="llama-3.3-70b-versatile",      # Groq model identifier
    temperature=0.3                       # Mild creativity for natural output
)


# --------------------------------------------------------------
# Prompt Template
# --------------------------------------------------------------
# Define the chat prompt for itinerary generation
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful travel assistant. Create a 1-day itinerary for {city} "
        "based on the user's interests: {interests}. Respond with a brief, "
        "bulleted itinerary with time-of-day groupings."
    ),
    (
        "human",
        "Please create a day-trip itinerary."
    ),
])


# --------------------------------------------------------------
# Public API
# --------------------------------------------------------------
def generate_itinerary(city: str, interests: list[str]) -> str:
    """
    Generate a concise, bulleted day-trip itinerary.

    Parameters
    ----------
    city : str
        Target city for the itinerary (e.g., "Lisbon").
    interests : list[str]
        User interests to bias the plan (e.g., ["history", "coffee", "viewpoints"]).

    Returns
    -------
    str
        The model's text output containing a brief, bulleted itinerary.
    """
    # Format prompt into a sequence of chat messages
    messages = prompt.format_messages(
        city=city,
        interests=", ".join(interests)  # Join interests into a readable list
    )

    # Invoke the chat model with the prepared messages
    response = llm.invoke(messages)

    # Return the generated text content
    return response.content
