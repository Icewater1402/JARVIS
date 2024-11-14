import speech_recognition as sr

class VoiceListener:
    def __init__(self, device_index=4):
        # Initialize the recognizer
        self.recognizer = sr.Recognizer()
        
        # Set up the microphone with the given device index
        self.microphone = sr.Microphone(device_index=device_index)

    def listen(self):
        # Start listening to the microphone
        with self.microphone as source:
            print("Calibrating ambient noise...")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)  # Calibrate ambient noise
            print("Listening for command...")
            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                command = self.recognizer.recognize_google(audio)
                return command  # Return the recognized command
            except sr.WaitTimeoutError:
                print("Error: Timeout while waiting for phrase.")
                return None
            except sr.UnknownValueError:
                print("Error: Could not understand audio.")
                return None
            except sr.RequestError as e:
                print(f"Error: Could not request results from Google Speech Recognition service; {e}")
                return None
