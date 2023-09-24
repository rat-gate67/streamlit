import streamlit as st


st.title("streamlit入門")
st.write("文章")

"""
---
### マークダウン記法も使える
---
```python
import streamlit as st
st.title("streamlit入門")
st.write("文章")
"""

st.latex("\int a x^2 \,dx")
clicked = st.button("Click me!")
if clicked:
    "thanks!"
    st.snow()

st.download_button("Download file","this is file")

import requests
geo_request_url = 'https://get.geojs.io/v1/ip/geo.json'
data = requests.get(geo_request_url).json()
lat = data['latitude']
lon = data['longitude']
f"lat = {lat},lon = {lon}"

if st.toggle("do you like me?"):
    "thanks!"
    