import gradio as gr
from transformers import pipeline
import coqui_tts
from coqui_tts.TTS.api import TTS
import os
import soundfile as sf
import numpy as np

# Initialize KinyaWhisper ASR model
asr = pipeline("automatic-speech-recognition", model="benax-rw/KinyaWhisper")

# Initialize Coqui TTS model (multilingual for Kinyarwanda)
tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2", progress_bar=False)

# QA dictionary for NLP matching
qa_pairs = {
    "Rwanda Coding Academy iherereye he?": "Iherereye mu Karere ka Nyabihu, mu Ntara y’Iburengerazuba.",
    "Umurwa mukuru w’u Rwanda ni uwuhe?": "Ni Kigali.",
    "Perezida w’u Rwanda ni nde?": "Ni Paul Kagame.",
    "U Rwanda rufite provinsi zingahe?": "Rufite provinsi eshanu.",
    "Amarushanwa ya Tour du Rwanda yabereye ryari bwa mbere?": "Yabereye mu 1988."
}

# Function to transcribe audio using KinyaWhisper
def transcribe_audio(audio_path):
    try:
        # Read audio file
        audio, sample_rate = sf.read(audio_path)
        if sample_rate != 16000:
            # Resample to 16kHz for Whisper compatibility
            from scipy import signal
            audio = signal.resample(audio, int(len(audio) * 16000 / sample_rate))
            sample_rate = 16000
        # Save temporary file
        temp_path = "temp.wav"
        sf.write(temp_path, audio, sample_rate)
        # Transcribe
        transcription = asr(temp_path)["text"]
        os.remove(temp_path)
        return transcription.strip()
    except Exception as e:
        return f"Error in transcription: {str(e)}"

# Function for NLP: Match question to answer
def match_question(transcription):
    transcription = transcription.lower().strip()
    for question, answer in qa_pairs.items():
        if transcription == question.lower():
            return answer
    return "Ndabizi, wongere ushyireho ikibazo."

# Function to generate speech from text using Coqui TTS
def text_to_speech(text):
    try:
        output_path = "output.wav"
        tts.tts_to_file(text=text, file_path=output_path, speaker_wav=None, language="rw")
        return output_path
    except Exception as e:
        return f"Error in TTS: {str(e)}"

# Main function for Gradio interface
def voice_assistant(audio):
    if audio is None:
        return "Please provide an audio input."
    
    # Save input audio
    input_path = "input.wav"
    sf.write(input_path, audio[1], audio[0])
    
    # Step 1: Transcribe audio
    transcription = transcribe_audio(input_path)
    
    # Step 2: Match question to answer
    answer = match_question(transcription)
    
    # Step 3: Convert answer to speech
    output_audio = text_to_speech(answer)
    
    return transcription, answer, output_audio

# Gradio interface
iface = gr.Interface(
    fn=voice_assistant,
    inputs=gr.Audio(type="numpy", label="Speak in Kinyarwanda"),
    outputs=[
        gr.Textbox(label="Transcription"),
        gr.Textbox(label="Answer"),
        gr.Audio(label="Spoken Answer")
    ],
    title="Mini Kinyarwanda Voice Assistant with KinyaWhisper",
    description="Speak a question in Kinyarwanda, and the assistant will transcribe it using KinyaWhisper, find an answer, and respond with speech."
)

# Launch the interface (comment out for GitHub submission)
# iface.launch()

if __name__ == "__main__":
    print("Run this script locally with Gradio to test the voice assistant.")