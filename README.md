# OpenAI Text Completion Tool

This is a Python script that uses the OpenAI API to generate text completions based on prompts copied to the clipboard. It uses the `pyperclip` library to access the clipboard and the `openai` library to interact with the OpenAI API.

## Installation

1. Clone or download this repository to your local machine.
2. Navigate to the project directory in your terminal or command prompt.
3. Run `pip install -r requirements.txt` to install the required dependencies.
4. Set your OpenAI API key and model engine by replacing the values in the `openai.api_key` and `model_engine` variables in the `openai_text_completion.py` file.
5. Run the script by running `python openai_text_completion.py`.

**Note**: You may need to use `pip3` instead of `pip` if you have multiple Python versions installed on your system.

## Adding Your OpenAI API Key

To use this tool, you will need to have an OpenAI API key. If you don't have one yet, you can sign up for the OpenAI GPT-3 beta program [here](https://beta.openai.com/signup/).

Once you have your API key, you can add it to the script by replacing the placeholder value `"YOUR_API_KEY"` in the `openai.api_key` variable with your actual API key. Be sure to keep your API key secure and do not share it with others.

## Usage

1. Copy a prompt to your clipboard.
2. The script will automatically generate a text completion based on the prompt and copy it to your clipboard.
3. Paste the text completion wherever you need it.

To stop the script, simply copy the word "Kinder" to your clipboard.
