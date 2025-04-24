import streamlit as st # type: ignore
import pandas as pd # type: ignore

# BMI calculator
st.title("BMI Calculator 🧮")

# slider for weight
weight = st.slider("Weight in kg", 40, 200, 70)

# slider for height
height = st.slider("Height in cm", 100, 250, 175)

# calculate BMI
bmi = weight / ((height/100)**2)

# display BMI
st.write(f"Your BMI is rounded to {bmi:.2f}")

# display BMI category
st.write(f"BMI Categories:")
st.write("Underweight: BMI LESS THAN 18.5")
st.write("Normal: BMI BETWEEN 18.5 AND 24.9")
st.write("Overweight: BMI BETWEEN 25 AND 29.9")
st.write("Obesity: BMI GREATER THAN 30")

# display BMI category using pandas







