import openai

class TextResponder:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def generate_response(self, prompt):
        try:
            # Use the new `chat-completions` endpoint with `gpt-3.5-turbo` or `gpt-4`
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # or use "gpt-4" for the newer, more powerful version
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response['choices'][0]['message']['content'].strip()  # Extracting the generated text
        except Exception as e:
            print(f"Error generating response: {e}")
            return "Sorry, I couldn't generate a response."
