from voice_listener import VoiceListener
from text_responder import TextResponder 
import speech_recognition as sr
from dotenv import load_dotenv 
import os 

class JarvisController:
    def __init__ (self, mic_index = 4):
        #initialization 
        load_dotenv() 
        self.api_key = os.getenv("API_KEY")
        if not self.api_key:
            raise ValueError("API_KEY not found in .env file")
        
        self.voiceListener = VoiceListener()
        self.textResponder = TextResponder(self.api_key)

    def start(self):
        command = self.voiceListener.listen() 
        if command:
            print(f"Command received: {command}")
            response = self.textResponder.generate_response(command)
            print(f"Response from GPT: {response}")

if __name__ == "__main__":
    mic_index = 4
    jarvis = JarvisController(mic_index) #Pass api key
    jarvis.start()

    # microphones = sr.Microphone.list_microphone_names()
    # for index, mic_name in enumerate(microphones):
    #     print(f"Microphone {index}: {mic_name}")
    # recognizer = sr.Recognizer()
    # microphone = sr.Microphone(4)

    # with microphone as source:
    #     print("Please say something...")
    #     try:
    #         audio = recognizer.listen(source, 5)
    #         print("You said: " + recognizer.recognize_google(audio))
    #     except sr.UnknownValueError:
    #         print("Sorry, I could not understand the audio.")
    #     except sr.RequestError:
    #         print("Could not request results from the speech recognition service.")