from voice_listener import VoiceListener
from text_responder import TextResponder
import speech_recognition as sr

class JarvisController:
    def __init__(self, mic_index=4):
        # initialization
        self.voiceListener = VoiceListener()
        self.textResponder = TextResponder()  # No API key needed now

    def start(self):
        command = self.voiceListener.listen()
        if command:
            print(f"Command received: {command}")
            response = self.textResponder.generate_response(command)
            print(f"Response from JARVIS: {response}")

if __name__ == "__main__":
    mic_index = 4
    jarvis = JarvisController(mic_index)
    jarvis.start()
