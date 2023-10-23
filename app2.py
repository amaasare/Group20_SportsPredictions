import streamlit as st
import pickle
from datetime import date

# Define the 'model' variable
model = None

try:
    # Load the saved model
    with open('model2.pkl', 'rb') as file:
        model = pickle.load(file)

    # Rest of your code

except Exception as e:
    st.error(f"An error occurred: {str(e)}")

st.title("⚽ EliteRater: Unleashing the Power of AI for FIFA Player Ratings!")


# The features with unique key values
wage_eur = st.sidebar.number_input("Wage (EUR)", 0.0, 1000000.0, 50000.0, key="wage_eur")
age = st.sidebar.number_input("Age", 0, 100, 25, key="age")
release_clause_eur = st.sidebar.number_input("Release Clause (EUR)", 0.0, 1000000000.0, 1000000.0, key="release_clause_eur")
skill_long_passing = st.sidebar.number_input("Skill: Long Passing", 0.0, 100.0, 50.0, key="skill_long_passing")
movement_reactions = st.sidebar.number_input("Movement: Reactions", 0.0, 100.0, 50.0, key="movement_reactions")
mentality_composure = st.sidebar.number_input("Mentality: Composure", 0.0, 100.0, 50.0, key="mentality_composure")
lcm = st.sidebar.number_input("Left Central Midfield", 0.0, 100.0, 50.0, key="lcm")
cm = st.sidebar.number_input("Central Midfield", 0.0, 100.0, 50.0, key="cm")
rcm = st.sidebar.number_input("Right Central Midfield", 0.0, 100.0, 50.0, key="rcm")
lwb = st.sidebar.number_input("Left Wing-Back", 0.0, 100.0, 50.0, key="lwb")
rwb = st.sidebar.number_input("Right Wing-Back", 0.0, 100.0, 50.0, key="rwb")
physical_aggregate = st.sidebar.number_input("Physical Aggregate", 0.0, 100.0, 50.0, key="physical_aggregate")
value_to_potential_ratio = st.sidebar.number_input("Value to Potential Ratio", 0.0, 10.0, 5.0, key="value_to_potential_ratio")
skill_score = st.sidebar.number_input("Skill Score", 0.0, 100.0, 50.0, key="skill_score")
midfielder_skill = st.sidebar.number_input("Midfielder Skill", 0.0, 100.0, 50.0, key="midfielder_skill")
importance_score = st.sidebar.number_input("Importance Score", 0.0, 100.0, 50.0, key="importance_score")

# Now you can use these variables in your input data for prediction
if st.sidebar.button("Predict"):
    if model is not None:
        inputs = [
            [
                wage_eur, age, release_clause_eur, skill_long_passing,
                movement_reactions, mentality_composure, lcm, cm, rcm, lwb, rwb,
                physical_aggregate, value_to_potential_ratio, skill_score, midfielder_skill, 
                importance_score
            ]
        ]
        prediction = model.predict(inputs)
        st.write("The player's overall rating prediction is:")
        st.write(prediction)


