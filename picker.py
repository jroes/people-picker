import streamlit as st
import random
import subprocess

def first(name):
    return name.split(' ')[0]

# TODO: curl this from somewhere, Gusto or Slack or something?
# Adjectives from "One Takeaway" https://www.notion.so/streamlit/Q-A-Doc-c2353d2fff984211a8831a8dbe18db80
adjectives = ["Focused", "Fearless", "Challenging", "Brainstorming", "Immortal", "Optimistic", "OG", "Motivated", "Enthusiastic", "Sleep-deprived", "Warm-and-fuzzy", "Communal", "Passionate", "Baby", "Excited", "Magical", "Growing", "Cultural", "Scrappy", "Opportunistic", "Scaling", "Exponential", "Gelling", "Hacker"]
people = {
    "Abhi Saini": { 'role': "Core PM", 'github': "asaini" },
    "Adrien Treuille": { 'role': "Cofounder & CEO", 'github': "treuille" },
    "Amanda Kelly": { 'role': "Cofounder & COO", 'github': "kellyamanda" },
    "Amanda Walker": { 'role': "Core Eng", 'github': "AnOctopus" },
    "Amey Deshpande": { 'role': "Cloud Eng", 'github': "Amey-D" },
    "Brandon Williams": { 'role': "Cloud Eng", 'github': "williamsbdev" },
    "Emiliano Rosso": { 'role': "Cloud Eng", 'github': "arraydude" },
    "Henrikh Kantuni": { 'role': "Core Eng", 'github': "kantuni" },
    "James Thompson": { 'role': "Cloud PM", 'github': "astrojams1" },
    "Jessica Smith": { 'role': "Marketer", 'github': "" },
    "Jon Roes": { 'role': "VP of Eng", 'github': "jroes" },
    "Ken McGrady Jr": { 'role': "Core Eng", 'github': "kmcgrady" },
    "Matteo Monchiero": { 'role': "Cloud Eng", 'github': "monchier" },
    "Marisa Smith": { 'role': "DevRel", 'github': "mesmith027" },
    "Randy Zwitch": { 'role': "Head of DevRel", 'github': "randyzwitch" },
    "Sammy Kauser": { 'role': "Exec Assistant", 'github': "" },
    "TC Ricks": { 'role': "Marketer", 'github': "tc87" },
    "Thiago Teixeira": { 'role': "Cofounder & Head of Product", 'github': "tvst" },
    "Tim Conkling": { 'role': "Core Eng", 'github': "tconkling" },
    "Vincent Donato": { 'role': "Core Eng", 'github': "vdonato" }
}

printable = {
    name: f"{random.choice(adjectives)} {details['role']}" for name, details in people.items()
}
shufflable = [f"{random.choice(adjectives)} {first(name)}" for name, details in people.items()]

st.title(f"{len(people)} people work at Streamlit!")

result = subprocess.run(['which', 'pkexec'], stdout=subprocess.PIPE)
result.stdout
result.stderr

st.sidebar.title("Controls")

with st.container():
    if st.sidebar.button("Pick someone randomly"):
        a = 5 / 0 # force error
        random_name = random.choice(list(people.keys()))
        st.balloons()
        adj, role = random.choice(adjectives), people[random_name]['role']
        st.header(f"{first(random_name)}, the {adj} {role}")

    if st.sidebar.button("Get a random list of Streamlitians"):
        random.shuffle(shufflable)
        shufflable

    if st.sidebar.button("Get our github ids"):
        [person['github'] for person in people.values()]

printable
