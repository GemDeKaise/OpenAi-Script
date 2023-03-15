import openai
import pyperclip
import time

# Set your OpenAI API key and model engine
openai.api_key = "YOUR_API_KEY"
model_engine = "text-davinci-002"

# Function to get the clipboard text
def get_clipboard_text():
    return pyperclip.paste()

# Initialize the message variable
message = ""

# Loop to continuously monitor the clipboard
while True:
    time.sleep(3)
    prompt = get_clipboard_text()
    
    if prompt == "Kinder": # Force stop if prompt is "Kinder"
        break
    
    # If the prompt is not empty and is not the same as the previous message or "1"
    if prompt and prompt != message:
        prompt += ". Say if the statement is true or false, and argue why in approximately 20-30 words."
        completions = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=256,
            n=1,
            stop=None,
            temperature=0.5,
        )
        message = completions.choices[0].text
        pyperclip.copy(message)
        time.sleep(5)
