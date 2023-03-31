# medical-chatbot
assistant chatbot for managing patients

# Setup
For Voice Recognition, we need to install SpeechRecognition,
PyAudio, pyttsx3, gTTS libraries with following commands.
  - pip install speechrecognition
  - pip install pyaudio
  - pip install pyttsx3
  - pip install gTTS

For Plots, we install the matplotlib library:
  - pip install matplotlib

Run the program:
  - python chat.py

# Functionality:
In The main window you can ask for reports of certain patients. Use send button or enter key to send text messages to the bot, use talk button to send
a voice message, example:
- Input: "Give me my report" 
- Output: "Okay, I'll look for it. but first, what's the patient's id? 
- Input: "id is 3"
- Output: John's condition of emergency severity can lead to Ashtma, Diabetes.

If you give an ID that doesn’t exist, it’ll ask you to add patient. Press Add button to open the Register menu. After registering, you can ask for the report again. 

When the number of patients added approaches the max, the user is warned, when the number of patients added is at max, the user can no longer add patients.

You can ask the bot to show you some graphs/plots of your data, or directly press the plot button from the main menu.


