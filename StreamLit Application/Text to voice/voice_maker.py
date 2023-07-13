import streamlit as st
from gtts import gTTS
from tempfile import TemporaryFile


st.title("Text to Speech Converter")
st.header("Voice Maker")

text = st.text_input('Enter any text', placeholder='Hello! How are you?')

result = st.button("Convert To Speech")

try:
    tts = gTTS(text,slow = False)
    tts.save("audio.mp3")
    file = "./audio.mp3"
    st.audio(file, format='audio/mp3')
except:
    st.write(":smile:")

