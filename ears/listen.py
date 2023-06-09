import whisper
import speech_recognition as sr
import sounddevice as sd
from scipy.io.wavfile import write
import os
import time
import glob


def record_audio(seconds):
    # Record audio
    fs = 16000  # Sample rate
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is finished
    file_name = str(time.time()) + ".wav"
    # Save as WAV file
    write(f"speech-to-text/audio/{file_name}", fs, myrecording)  # Save as WAV file


def get_current_audio_file_path():
    list_of_files = glob.glob("speech-to-text/audio/*.wav")
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file


def stt_whisper():
    model = whisper.load_model("base")
    latest_audio = get_current_audio_file_path()
    result = model.transcribe(latest_audio, no_speech_threshold=0.467)
    print("\n\n" + result["text"])


def stt_google():
    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()
    r.energy_threshold = 350  # minimum audio energy to consider for recording
    r.dynamic_energy_threshold = True
    r.dynamic_energy_adjustment_damping = 0.15
    r.dynamic_energy_ratio = 1.5
    r.pause_threshold = (
        1.0  # seconds of non-speaking audio before a phrase is considered complete
    )
    r.operation_timeout = None  # seconds after an internal operation (e.g., an API request) starts before it times out, or ``None`` for no timeout

    r.phrase_threshold = 0.2  # minimum seconds of speaking audio before we consider the speaking audio a phrase - values below this are ignored (for filtering out clicks and pops)
    r.non_speaking_duration = (
        0.3  # seconds of non-speaking audio to keep on both sides of the recording
    )

    # Reading Microphone as source
    # listening the speech and store in audio_text variable

    with sr.Microphone() as source:
        # https://www.geeksforgeeks.org/hotword-detection-with-python/# : Snowboy Hotword Detection
        audio_text = r.listen(source, phrase_time_limit=20, timeout=20)
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        try:
            # using google speech recognition
            return r.recognize_google(audio_text)
        except:
            return None


def main():
    pass


if __name__ == "__main__":
    main()
