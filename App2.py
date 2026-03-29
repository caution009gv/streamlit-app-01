import streamlit as st

# Function to analyze the number
def analyze_number(num):
    square = num ** 2
    cube = num ** 3
    even_or_odd = "Even" if num % 2 == 0 else "Odd"
    return square, cube, even_or_odd

st.title("Number Analyzer App-2")

number = st.number_input("Enter a number:")

if st.button("Analyze"):
    square, cube, result = analyze_number(number)
    st.write(f"Square: {square}")
    st.write(f"Cube: {cube}")
    st.write(f"The number is: {result}")
