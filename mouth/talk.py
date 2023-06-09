from dotenv import load_dotenv
import os
from elevenlabs import voices, generate, play, stream, VoiceSettings, Voice
from elevenlabs import set_api_key

load_dotenv()
set_api_key(os.getenv("ELEVENLABS_API_KEY"))

# https://github.com/elevenlabs/elevenlabs-python/blob/main/elevenlabs/simple.py
TRUMP = Voice(
    voice_id="gmut4Cg2ETt22PmNEFqD",
    name="Donald Trump",
    settings=VoiceSettings(stability=0.25, similarity_boost=0.25),
)
BIDEN = Voice(
    voice_id="HguquQKL7RuXe28HVoKH",
    name="Donald Trump",
    settings=VoiceSettings(stability=0.25, similarity_boost=0.25),
)
MEENA = Voice(
    voice_id="NSAJG90pyo8tqAbySPLH",
    name="Meena",
    settings=VoiceSettings(stability=0.35, similarity_boost=0.45),
)
# make it STREAM live


# audio = generate(
#     text="hey there, how are you doing?",
#     voice=TRUMP,
# )


def speak(words, voice):
    if voice == "ARNOLD":
        audio = generate(text=words, voice="Arnold", model="eleven_monolingual_v1")
        play(audio)

    if voice == "TRUMP":
        audio = generate(text=words, voice=TRUMP, model="eleven_monolingual_v1")
        play(audio)

    if voice == "BIDEN":
        audio = generate(
            text=words,
            voice=BIDEN,
            model="eleven_monolingual_v1",
        )
        play(audio)

    if voice == "MEENA":
        audio = generate(
            text=words,
            voice=MEENA,
            model="eleven_multilingual_v1",
        )
        play(audio)

    if voice == "mac":
        os.system(f"say {words}")
