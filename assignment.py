pip install streamlit
import streamlit as st
import openai
from datetime import datetime

def get_itinerary(destination, days, budget, interests):
    # Simulating an AI-generated response
    itinerary = f"Here's your {days}-day itinerary for {destination} on a {budget} budget:\n\n"
    for day in range(1, days + 1):
        itinerary += f"Day {day}:\n"
        itinerary += f"- Morning: Explore a famous landmark in {destination}.\n"
        itinerary += f"- Afternoon: Enjoy a local restaurant with {interests} cuisine.\n"
        itinerary += f"- Evening: Relax at a popular cultural spot or nightlife area.\n\n"
    return itinerary

st.title("AI-Powered Travel Planner ✈️")

st.sidebar.header("Tell us about your trip")

destination = st.sidebar.text_input("Where are you traveling to?")
days = st.sidebar.number_input("How many days?", min_value=1, max_value=30, value=3)
budget = st.sidebar.selectbox("Select your budget", ["Budget", "Mid-range", "Luxury"])
interests = st.sidebar.text_input("What are your main interests? (e.g., history, adventure, food, nature)")

if st.sidebar.button("Generate Itinerary"):
    if destination and days and budget and interests:
        itinerary = get_itinerary(destination, days, budget, interests)
        st.subheader("Your Personalized Travel Itinerary")
        st.text(itinerary)
    else:
        st.warning("Please fill in all the details to generate an itinerary.")
