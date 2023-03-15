# OpenAI Text Completion Script

This script uses OpenAI's GPT-3 language model to generate text based on the contents of your clipboard. It monitors the clipboard for changes and automatically generates a response when it detects a new input. 

## Requirements

Make sure you have the following Python libraries installed:

- openai
- pyperclip

You can install these libraries by running the following command:

pip install -r requirements.txt

Note: If you have multiple Python versions installed on your system, you may need to use `pip3` instead of `pip`.

## Usage

To use the script, simply run the `open_ai.py` file in your Python environment. The script will automatically start monitoring your clipboard for changes and generating responses based on the input.

To stop the script, simply copy the word "Kinder" to your clipboard and the script will exit.

When prompted, respond with whether the statement is true or false and provide an argument for your answer in approximately 20-30 words.

