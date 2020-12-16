import streamlit as st
import random

def first(name):
    return name.split(' ')[0]

# TODO: curl this from somewhere, Gusto or Slack or something?
# Adjectives from "One Takeaway" https://www.notion.so/streamlit/Q-A-Doc-c2353d2fff984211a8831a8dbe18db80
people = {
    "Abhi Saini": ["Focused", "Core PM"],
    "Adrien Treuille": ["Fearless", "Cofounder & CEO"],
    "Amanda Kelly": ["Challenging", "Cofounder & CFO"],
    "Amey Deshpande": ["Brainstorming", "Cloud Eng"],
    "Austin Chen": ["Immortal", "Core TL"],
    "Brandon Hsiao": ["Optimistic", "Core Eng"],
    "Brandon Williams": ["OG", "Cloud Eng"],
    "Corey Bradford": ["Alcoholic", "Eng Resident"],
    "Emiliano Rosso": ["Motivated", "Cloud Eng"],
    "Guido Rainuzzo": ["Enthusiastic", "Cloud Eng"],
    "Henrikh Kantuni": ["Sleep-deprived", "Core Eng"],
    "James Thompson": ["Warm-and-fuzzy", "Cloud PM"],
    "Jessica Smith": ["Communal", "Marketer"],
    "Jonathan Rhone": ["Passionate", "Cloud Eng"],
    "Jon Roes": ["Baby", "VP of Eng"],
    "Ken McGrady Jr": ["Excited", "Core Eng"],
    "Matteo Monchiero": ["Magical", "Cloud Eng"],
    "Naomi Most": ["Growing", "Core TPM"],
    "Karrie Song": ["Cultural", "Core Eng"],
    "Marisa Smith": ["Scrappy", "DevRel"],
    "Randy Zwitch": ["Opportunistic", "Head of DevRel"],
    "Sammy Kauser": ["Scaling", "Exec Assistant"],
    "TC Ricks": ["Exponential", "Marketer"],
    "Thiago Teixeira": ["Gelling", "Cofounder & CTO"],
    "Tim Conkling": ["Hacker", "Core Eng"],
}
printable = {
    first(name): f"{adj} {role}" for name, [adj, role] in people.items()
}
shufflable = [f"{first(name)} {adj}" for name, [adj, role] in people.items()]

st.title(f"{len(people)} people work at Streamlit!")

st.sidebar.title("Controls")

with st.beta_container():
    if st.sidebar.button("Pick someone randomly"):
        random_name = random.choice(list(people.keys()))
        st.balloons()
        adj, role = people[random_person]
        st.header(f"{first(random_name)}, the {adj} {role}")

    if st.sidebar.button("Get a random list of Streamlitians"):
        random.shuffle(shufflable)
        shufflable

printable
