import streamlit as st
import random

def first(name):
    return name.split(' ')[0]

# TODO: curl this from somewhere, Gusto or Slack or something?
# Adjectives from "One Takeaway" https://www.notion.so/streamlit/Q-A-Doc-c2353d2fff984211a8831a8dbe18db80
adjectives = ["Focused", "Fearless", "Challenging", "Brainstorming", "Immortal", "Optimistic", "OG", "Alcoholic", "Motivated", "Enthusiastic", "Sleep-deprived", "Warm-and-fuzzy", "Communal", "Passionate", "Baby", "Excited", "Magical", "Growing", "Cultural", "Scrappy", "Opportunistic", "Scaling", "Exponential", "Gelling", "Hacker"]
people = {
    "Abhi Saini": "Core PM",
    "Adrien Treuille": "Cofounder & CEO",
    "Amanda Kelly": "Cofounder & COO",
    "Amey Deshpande": "Cloud Eng",
    "Austin Chen": "Core TL",
    "Brandon Hsiao": "Core Eng",
    "Brandon Williams": "Cloud Eng",
    "Corey Bradford": "Eng Resident",
    "Emiliano Rosso": "Cloud Eng",
    "Guido Rainuzzo": "Cloud Eng",
    "Henrikh Kantuni": "Core Eng",
    "James Thompson": "Cloud PM",
    "Jessica Smith": "Marketer",
    "Jonathan Rhone": "Cloud Eng",
    "Jon Roes": "VP of Eng",
    "Ken McGrady Jr": "Core Eng",
    "Matteo Monchiero": "Cloud Eng",
    "Naomi Most": "Core TPM",
    "Karrie Song": "Core Eng",
    "Marisa Smith": "DevRel",
    "Randy Zwitch": "Head of DevRel",
    "Sammy Kauser": "Exec Assistant",
    "TC Ricks": "Marketer",
    "Thiago Teixeira": "Cofounder & Head of Product",
    "Tim Conkling": "Core Eng"
}
printable = {
    name: f"{random.choice(adjectives)} {role}" for name, role in people.items()
}
shufflable = [f"{random.choice(adjectives)} {first(name)}" for name, role in people.items()]

st.title(f"{len(people)} people work at Streamlit!")

st.sidebar.title("Controls")

with st.beta_container():
    if st.sidebar.button("Pick someone randomly"):
        random_name = random.choice(list(people.keys()))
        st.balloons()
        adj, role = random.choice(adjectives), people[random_name]
        st.header(f"{first(random_name)}, the {adj} {role}")

    if st.sidebar.button("Get a random list of Streamlitians"):
        random.shuffle(shufflable)
        shufflable

printable
