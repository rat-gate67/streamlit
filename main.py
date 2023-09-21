import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image
import time

st.title("streamlit 入門")


st.write("プログレスバー")
latest_interation = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_interation.text(f"{i+1}%")
    bar.progress(i +1)
    time.sleep(0.05)


st.write("Interavtice Widgets")

condition = st.slider("What up !?",0 ,100, 50)

left_column, right_column = st.columns(2)

button = left_column.button("lest")
if button :
    right_column.write("右？")

expander = st.expander("問い合わせ")
expander.write("問い合わせを書く")
st.color_picker("what is it?")

str = st.text_input(
    "What is your hobby ?"
)

option = st.selectbox(
    "What is your favorite number?",
    list(range(10))
)

"Your favorite number is " ,option
"Your favorite hobby is " ,str
"Your condition is " ,condition