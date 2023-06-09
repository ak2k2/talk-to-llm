## What is this?
Utilize ElevenLabs, Google Speech Recognition, and OpenAI APIs to enable interactive conversations with a Language Model (LLM) in various voices, including cloned voices.

## Prerequisites
- Python 3.x
- pip package manager

## Installation
1. Clone this repository to your local machine.
   ```
   git clone https://github.com/your/repository.git
   ```
2. Navigate to the project directory.
   ```
   cd repository
   ```
3. Install the required Python packages using pip.
   ```
   pip install -r requirements.txt
   ```

## Configuration
1. Create a new file named `.env` in the project directory.
2. Open the `.env` file in a text editor and add the following lines:
   ```
   ELEVENLABS_API_KEY='...'
   OPENAI_API_KEY='sk-...'
   ```
   Replace the values `'...'` and `'sk-...'` with your actual API keys.

## Running the Application
To start a new conversation, specify a voice and then execute the following,
```
python GO.py
```

## Plan:
- [Snowboy Hotword Detection](https://www.geeksforgeeks.org/hotword-detection-with-python/#)
- ElevenLabs TTS true streaming
- local inference with WizardLM based
- upgraded escape sequences (Weather, Time, etc.)
