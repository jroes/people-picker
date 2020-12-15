import streamlit as st
import random


# TODO: curl this from somewhere, Gusto or Slack or something?
people = [
	'Abhi Saini',
	'Adrien Treuille',
	'Amanda Kelly',
	'Amey Deshpande',
	'Austin Chen',
	'Brandon Hsiao',
	'Brandon Williams',
	'Emiliano Rosso',
	'Guido Rainuzzo',
	'Henrikh Kantuni',
	'James Thompson',
	'Jonathan Rhone',
	'Jon Roes',
	'Ken McGrady Jr',
	'Matteo Monchiero',
	'Naomi Most',
	'Karrie Song',
	'Randy Zwitch',
	'Sammy Kauser',
	'TC Ricks',
	'Thiago Teixeira',
	'Tim Conkling'
]

st.title(f'{len(people)} people work at Streamlit!')

people

st.sidebar.title('Controls')

with st.beta_container():
	if st.sidebar.button('Pick someone randomly'):
		random_person = random.choice(people)
		st.balloons()
		st.header(random_person)

	if st.sidebar.button('Get a random list of Streamlitians'):
		shuffled_people = random.sample(people, len(people))
		st.write(shuffled_people)
