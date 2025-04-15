
import streamlit as st

st.set_page_config(page_title="Unit Converter", layout="centered")

st.title("🔁 Unit Converter")

# Define conversion functions
def length_converter(value, from_unit, to_unit):
    units = {
        "meters": 1,
        "kilometers": 1000,
        "centimeters": 0.01,
        "millimeters": 0.001,
        "miles": 1609.34,
        "yards": 0.9144,
        "feet": 0.3048,
        "inches": 0.0254
    }
    return value * units[from_unit] / units[to_unit]

# Choose category
category = st.selectbox("Choose conversion category:", ["Length"])

if category == "Length":
    st.subheader("Length Converter")
    units = ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet", "inches"]
    
    value = st.number_input("Enter value:", min_value=0.0, format="%.4f")
    from_unit = st.selectbox("From:", units)
    to_unit = st.selectbox("To:", units)
    
    if st.button("Convert"):
        result = length_converter(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

