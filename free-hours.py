import streamlit as st
import pandas as pd

st.set_page_config(page_title = "Free Hours", page_icon=":bulb:")

hours = {
    "M1": [0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1],
    "M2": [0,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    "M3": [0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0],
    "M4": [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0],
    "M5": [0,0,0,0,0,1,1,1,1,1,1,1,1,0,1,1,0,0,0,0,0,0,1,0,0],
    "M6": [0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,0],
    "M7": [0,0,0,0,0,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1],
    "M8": [0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0],
    "M9": [0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,0,0,1,1,0],
    "T1": [0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0],
    "T2": [0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,1,1,0,0,1,0,1,0],
    "T3": [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,1,0,1],
    "T4": [0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,1,0,1,1,0,0,1,1],
    "T5": [0,0,0,0,0,1,0,1,0,1,1,0,0,1,0,1,0,0,1,1,0,1,0,0,1],
    "T6": [0,0,0,0,0,1,1,1,1,1,1,0,0,1,0,1,1,1,0,1,1,0,1,1,1],
    "T7": [0,0,0,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1,0,1,1,1,0,1],
    "T8": [0,0,0,0,0,1,1,0,1,0,0,1,1,1,1,0,0,0,0,0,1,0,0,0,0],
    "T9": [0,0,0,0,0,1,1,0,1,0,0,1,1,1,1,0,0,0,1,0,0,1,0,0,0],
    "W1": [0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,1,0,1,0,0,0,0],
    "W2": [0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,1,0,1,1,0,0,0],
    "W3": [0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,1,0,0,0,1,1,0,0,0,1],
    "W4": [0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
    "W5": [0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,1,0,1,1,0,1],
    "W6": [0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,1,1,0,0,0,0,0,1,0],
    "W7": [0,0,0,0,0,1,1,1,1,1,1,1,1,0,1,1,0,0,1,1,1,1,1,0,1],
    "W8": [0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,0,0,1,0,1],
    "W9": [0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0],
    "Th1": [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
    "Th2": [0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0],
    "Th3": [0,0,0,0,0,0,1,0,1,0,0,1,1,1,1,1,1,1,1,0,0,1,0,1,0],
    "Th4": [0,0,0,0,0,1,1,0,1,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0],
    "Th5": [0,0,0,0,0,1,0,1,0,1,1,0,0,1,0,1,0,0,0,0,0,0,1,0,0],
    "Th6": [0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,0],
    "Th7": [0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,1,1,1,1,1,0,1],
    "Th8": [0,0,0,0,0,1,1,0,1,0,0,0,0,1,0,1,0,0,1,0,0,1,0,0,0],
    "Th9": [0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,1,0,0,1,1,0,1,0,0,1],
    "F1": [0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
    "F2": [0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,1,0,1,0,0,0,0],
    "F3": [0,0,0,0,0,1,0,0,0,0,0,1,1,0,1,1,1,0,0,0,0,0,0,0,0],
    "F4": [0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,1,0],
    "F5": [0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1,0]
}

people = {
    "0":"Anurag",
    "1":"Aman",
    "3":"Krish",
    "3":"Sarah",
    "4":"Dhruv",
    "5":"Thahir",
    "6":"Aaryan",
    "7":"Alan",
    "8":"Husam",
    "9":"Jassi",
    "10":"Muneeb",
    "11":"Rahul",
    "12":"Riddhi",
    "13":"Tushar",
    "14":"Vansh",
    "15":"Aadish",
    "16":"Asfiya",
    "17":"Drisya",
    "18":"Kaveri",
    "19":"Muqaram",
    "20":"Nishit",
    "21":"Omer",
    "22":"Sivaa",
    "23":"Shivaani",
    "24":"Vennela"
}

text='''
The most possible number of free council members at a given time is 18, and the hour is M7. The other 
hours include W7 (16), T6 (15), M1, M6 and Th6 (14), Th3 (12), M5 (11), and T4 and T5 (10).
'''

st.title("Who's free?")
st.subheader("Council Version | Semester II, 2023-24")
st.write(text)

selected_hour = st.selectbox("Select hour:", list(hours.keys()))

free_people_indices = [i for i, status in enumerate(hours[selected_hour]) if status == 1]

free_people_names = [people[str(index)] for index in free_people_indices]

st.subheader(f"Available Council during {selected_hour}:")
if not free_people_names:
    st.write("No one is free at this hour.")
else:
    st.write(free_people_names)
