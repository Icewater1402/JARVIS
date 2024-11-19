import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import os

class TextResponder:
    def __init__(self):
        # Use the local path to the model if it exists in the cache
        model_name = "microsoft/DialoGPT-medium"
        model_cache_dir = os.path.expanduser("~/.cache/huggingface")  # Update path if needed
        
        # Load model and tokenizer from the cache directory
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=model_cache_dir)
        self.model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir=model_cache_dir)
        self.chat_history = []

    def generate_response(self, user_input):
        try:
            # Tokenize user input and add to chat history
            new_input_ids = self.tokenizer.encode(user_input + self.tokenizer.eos_token, return_tensors="pt")
            self.chat_history.append(new_input_ids)

            # Concatenate all inputs in the chat history
            input_ids = torch.cat(self.chat_history, dim=-1)

            # Create an attention mask
            attention_mask = torch.ones_like(input_ids)

            # Generate a response
            response_ids = self.model.generate(
                input_ids,
                attention_mask=attention_mask,
                max_length=1000,
                pad_token_id=self.tokenizer.eos_token_id
            )
            response = self.tokenizer.decode(response_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)

            # Update chat history
            self.chat_history.append(response_ids)

            return response
        except Exception as e:
            print(f"Error generating response: {e}")
            return "Sorry, I couldn't generate a response."
