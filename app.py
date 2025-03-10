import streamlit as st
import numpy as np
from PIL import Image


youtube_url='https://youtu.be/gyIyukLYqAs'
# Set up page configuration
st.set_page_config(page_title="Bee Hive", layout="wide")
st.title("Depiction of Clustering as a Bee Hive")
st.video(youtube_url)
