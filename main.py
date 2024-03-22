import streamlit as st
import speech_recognition as sr
from time import sleep
import pyttsx3
import os
import shutil
import datetime
import socket
from pydub import AudioSegment
from pydub.silence import split_on_silence

# Function to listen to audio for a specified duration and convert it to text
def listen(duration):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        text = recognizer.record(source, duration=duration)
        try:
            return recognizer.recognize_google(text)
        except:
            return "Didn't hear perfectly!"

# Function to handle microphone activation, speech recognition, and text display
def write_text():
    if (socket.gethostbyname(socket.gethostname()) == "127.0.0.1"):
        st.error("Your device is not connected to the internet")
    else:
        st.text("Click the button and start speaking...")
        text = listen(5)
        st.write("You said:", text)

# Function to convert text to speech and speak it aloud
def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function to save text to a file
def save_text(text):
    filename = st.text_input("Enter filename:")
    if filename:
        filename = filename + ".txt"
        with open(filename, "a") as file:
            file.write(text)
        st.success(f"File '{filename}' saved successfully.")
    else:
        st.warning("Please enter a filename.")

def main():
    st.title("Speech Processing App")

    menu = ["Home", "Save Text"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Speak into Microphone")
        if st.button("Activate Microphone"):
            write_text()

        text_to_speak = st.text_area("Text to Speak")
        if st.button("Speak", key="speak_button"):
            if text_to_speak:
                speak_text(text_to_speak)
            else:
                st.warning("Please enter text to speak.")

    elif choice == "Save Text":
        st.subheader("Save Text to File")
        text_to_save = st.text_area("Text to Save")
        if st.button("Save", key="save_button"):
            if text_to_save:
                save_text(text_to_save)
            else:
                st.warning("Please enter text to save.")

if __name__ == "__main__":
    main()
