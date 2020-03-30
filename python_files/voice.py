#!/usr/bin/env python3

"""
Learn speech_recognition.

THIS FILE WILL NOT EXECUTE. Package not installed:
    speechrecognition needs pyaudio
    pyaudio needs portaudio (header file for c compile)
    do not have portaudio; installing removes jack
"""

import speech_recognition

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Say something!")
    audio = recognizer.listen(source)

print("Google Speech Recognition thinks you said:")
print(recognizer.recognize_google(audio))

