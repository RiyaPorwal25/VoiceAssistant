# VoiceAssistant
This is a voice assistant application that listens to your speech, recognizes commands, and responds with appropriate actions such as speaking back text, opening websites, or telling jokes.
Here's a breakdown of the script:
Libraries:
->pyttsx3: A library for converting text to speech.
->speech_recognition (sr): A library for speech recognition (listens to your voice commands).
->webbrowser: A built-in module to open URLs in the default web browser.
->datetime: A module for working with dates and times.
->pyjokes: A module to fetch jokes.
->os: A module to interact with the operating system (though not used in this specific script).
->time: A module used to introduce delays in the program.
Functions:
  1.sptext():Listens to audio input from the user via the microphone.
It uses Google’s speech recognition API to convert the speech into text and returns the recognized text.
Handles errors if the speech is not understood or if there is a connection issue.


  2.speechtx(x):Converts the input text x into speech using the pyttsx3 library.
Sets the voice and speaking rate for the speech engine.
Speaks the provided text out loud.

Main Code Flow:
  While Loop:
  The program runs indefinitely until you say "exit".

  The program listens for your speech continuously, processes the command, and performs a specific action based on the command:
  
  "your name": Responds with "my name is Alina."
  "old are you": Responds with "I am 2 years old."
  "time": Speaks out the current time.
  "youtube": Opens YouTube in a browser.
  "google": Opens Google in a browser.
  "chatgpt": Opens the ChatGPT website in a browser.
  "joke": Tells a joke from pyjokes.
  "play song": Opens a YouTube link with a song.
  "exit": Ends the program with a "thank you" message.
  After executing each command, it waits for 5 seconds before listening again.

Things to note:
The script uses a microphone to capture the voice, so the system needs to have a working microphone.
The speech recognition and text-to-speech systems depend on external services (Google’s speech recognition and pyttsx3).
The program introduces a slight delay (5 seconds) after each action, preventing it from listening constantly without a break.
The code continuously listens for your voice and responds with actions, so it can be used as a simple voice assistant for basic tasks like telling the time, opening websites, or telling jokes.
