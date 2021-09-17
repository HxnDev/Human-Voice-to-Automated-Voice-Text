# Human Voice to Automated Voice & Text

## Introduction:
In this project, whenever you'll speak, it will turn your voice into a robot voice and furthermore it will also generate a transcript of the input.

## Requirements:
Inorder for this project to run, you need to have the following two modules installed:
- gTTS (pip install gTTS)
- SpeechRecognition (pip install SpeechRecognition)

## SpeechRecognition:
SpeechRecognition creates a new microphone instance. It further performs speech recognition on the human input voice coming from the microphone. It then converts the input voice into its corresponding text. This can also be referred to as creating a transcript of an input. 
If you want to input voice straight from the microphone like i have in this project, then you need to install "PyAudio version 0.2.11+".

## gTTS (Google Text To Speech):
gTTS is a Python library to interface with the Google Text To Speech API. In this project, its being used to convert the transcript of the input (that we got from SpeechRecognition module) to a robotic voice and then save the file as mp3.

## Note:
All the files have been commented for your ease. Furthermore you may also add further comments if you may.

## Contact Info:
For further queries contact me at : chhxnshah@gmail.com
