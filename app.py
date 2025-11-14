"""
app.py

Streamlit front-end for the LLMOps Travel Itinerary Planner.

This application:
    • Collects user inputs (city + interests)
    • Integrates with the TravelPlanner core logic
    • Generates a fully personalised, LLM-powered day-trip itinerary
    • Displays the itinerary with clean formatting in a styled container
"""

# --------------------------------------------------------------
# Imports
# --------------------------------------------------------------

import streamlit as st
from dotenv import load_dotenv
from src.core.planner import TravelPlanner


# --------------------------------------------------------------
# Page Setup
# --------------------------------------------------------------

# Configure Streamlit page properties
st.set_page_config(page_title="LLMOps Travel Planner", layout="centered")

# Display main title using custom HTML styling
st.markdown(
    "<h1 style='text-align:center;'>🌍 AI Travel Itinerary Planner</h1>",
    unsafe_allow_html=True
)

# Short introduction message
st.info(
    "Select a destination and choose your interests to generate a personalised day-trip itinerary."
)

# Load environment variables from .env
load_dotenv()


# --------------------------------------------------------------
# Available Interests (editable list)
# --------------------------------------------------------------

# List of user-selectable interests
INTEREST_OPTIONS = [
    "History",
    "Art",
    "Museums",
    "Food",
    "Coffee",
    "Nightlife",
    "Beaches",
    "Viewpoints",
    "Architecture",
    "Nature",
    "Shopping",
    "Music",
]


# --------------------------------------------------------------
# Input Form
# --------------------------------------------------------------

with st.form("planner_form"):

    # Trip Details Header
    st.markdown("### 📝 Trip Details")

    # City name input field
    city = st.text_input(
        "🏙️ City",
        placeholder="e.g., Lisbon, Tokyo, Barcelona"
    )

    # Interests Header
    st.markdown("### 🎯 Select Your Interests")

    # Prepare list to store selected interests
    selected_interests = []

    # Create a 3-column layout for interest checkboxes
    cols = st.columns(3)

    # Render checkboxes in a grid pattern
    for idx, interest in enumerate(INTEREST_OPTIONS):
        col = cols[idx % 3]
        if col.checkbox(interest):
            selected_interests.append(interest)

    # Submit button
    submitted = st.form_submit_button("✨ Generate Itinerary")


    # ----------------------------------------------------------
    # Handle Submission
    # ----------------------------------------------------------

    if submitted:

        # Validate inputs
        if city and selected_interests:

            # Create planner instance
            planner = TravelPlanner()

            # Store city
            planner.set_city(city)

            # Convert selected interests → comma-separated string
            interests_str = ", ".join(selected_interests)
            planner.set_interests(interests_str)

            # Generate itinerary output
            itinerary = planner.create_itinerary()

            # Display output header
            st.markdown("## 📄 Your Itinerary")

            # Styled container for Markdown itinerary
            st.markdown(
                f"""
                <div style="
                    padding: 1.2rem;
                    background-color: #1e1e1e;
                    border-radius: 10px;
                    border: 1px solid #444;
                ">
                    {itinerary}
                </div>
                """,
                unsafe_allow_html=True,
            )

        else:
            # User input missing
            st.warning("⚠️ Please enter a city and select at least one interest.")
