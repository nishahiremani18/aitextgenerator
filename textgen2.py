import streamlit as st #for web dev
from aitextgen import aitextgen #for ai text gen


st.title("AI content generator")

# instantiate the model / download
ai = aitextgen()



prompt_text = st.text_input(label = "Enter your  text...",
            value = "Computer is beautiful")
prompt_number = st.number_input(label = "Enter a number",min_value=50, max_value=1000, value=100, step=50, format=None, key=prompt_text)

with st.spinner("AI is at Work........"):
    # text generation
    gpt_text = ai.generate_one(prompt=prompt_text,
            max_length=prompt_number)
st.success("AI Successfully generated the below text ")
st.balloons()
# print ai generated text
st.text(gpt_text)
