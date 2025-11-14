"""
config.py

Configuration module for the LLMOps Travel Itinerary Planner project.
Loads environment variables and defines core API credentials.

Attributes
----------
GROQ_API_KEY : str
    API key for the Groq inference service.
"""

# --------------------------------------------------------------
# Imports
# --------------------------------------------------------------
import os
from dotenv import load_dotenv


# --------------------------------------------------------------
# Load environment variables
# --------------------------------------------------------------
load_dotenv()


# --------------------------------------------------------------
# Environment Variables
# --------------------------------------------------------------
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
