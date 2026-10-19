import streamlit as st
import google.generativeai as genai
from PIL import Image

genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-flash-latest")  # use a current Gemini model name

st.title("LabelLens")
st.caption("Informational only, not medical advice.")

allergens = st.text_input("Your allergens or sensitivities (optional)")
photo = st.file_uploader("Upload a product label", type=["jpg", "jpeg", "png"])

if photo:
    img = Image.open(photo)
    st.image(img)
    prompt = (
        "Extract the ingredients from this label. Flag potentially harmful "
        f"additives and anything related to: {allergens}. Give a safety score "
        "(green/yellow/red) with a simple explanation for each flag."
    )
    with st.spinner("Analyzing..."):
        st.write(model.generate_content([prompt, img]).text)