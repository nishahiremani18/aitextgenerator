import streamlit as st #for web dev
from aitextgen import aitextgen #for ai text gen


st.title("AI content generator")

# instantiate the model / download
ai = aitextgen()


#prompt_text = "Python is awesome"
prompt_text = st.text_input(label = "Enter your  text...",
            value = "Computer is beautiful") #default value

with st.spinner("AI is at Work........"):
    # text generation
    gpt_text = ai.generate_one(prompt=prompt_text,
            max_length = 150 )
st.success("AI Successfully generated the below text ")
st.balloons()
# print ai generated text
print(gpt_text)

st.text(gpt_text)
