# MiniKinyaVA
🎤 Kinya Voice Assistant
An intelligent voice assistant designed to understand and respond in Kinyarwanda, offering seamless speech interaction through advanced speech-to-text and text-to-speech capabilities.

🌟 Key Features
🎙 Voice Input – Captures spoken Kinyarwanda

✍️ Speech-to-Text (STT) – Converts Kinyarwanda speech into text using NeMo-based models

🧠 Natural Language Understanding – Processes queries via rule-based logic and ChatGPT

🔊 Text-to-Speech (TTS) – Synthesizes high-quality Kinyarwanda speech with MB-iSTFT-VITS2

💬 Interactive Interface – Gradio-powered web interface for real-time conversations

📝 Overview
Kinya Voice Assistant enables natural, fluid conversations in Kinyarwanda. It operates through a three-step pipeline:

Speech Recognition – Transcribes spoken input into text

Query Analysis – Understands intent and formulates responses

Speech Synthesis – Converts responses into natural-sounding audio

🖼️ Demo Snapshots
Terminal Execution


Gradio UI


Usage Example


🛠️ Technical Architecture
🔹 Speech-to-Text (STT)
Powered by NVIDIA NeMo

Utilizes pretrained Kinyarwanda models from RW-DEEPSPEECH-API

Supports multiple audio input formats

🔹 Natural Language Processing
Hybrid approach combining:

Rule-based matching for simple commands

ChatGPT for complex conversation handling

Custom intent detection

Supports greetings, general queries, and contextual dialogue

🔹 Text-to-Speech (TTS)
Based on KinyaTTS

Employs the MB-iSTFT-VITS2 architecture

Outputs natural and expressive Kinyarwanda speech

⚙️ Installation & Setup
Prerequisites
Python 3.x

NVIDIA GPU (for local deployment)

Google Colab (recommended for ease)

Installation
bash
Copy
Edit
pip install -e /path/to/Inference/  # KinyaTTS
pip install "numpy<2.1.0,>1.26.0"
pip install Cython
pip install gradio
pip install openai  # Required for ChatGPT integration
🚀 Running the Assistant
Open kin_assistant.ipynb in Google Colab

Mount Google Drive containing model files

Execute all cells to initialize the environment

Use the Gradio UI to start interacting via voice

⚠️ Limitations
Audio Quality Sensitivity
Performs best in quiet environments; may struggle with background noise

Language Confusion
May occasionally misinterpret Kinyarwanda as Kiswahili
Example: "niyume" detected as Kiswahili

Sampling Rate Mismatches
Initial compatibility issues with benax-rw/kinyawishper resolved through workarounds

📂 Resources
📁 Source Code & TTS Models

📓 Notebook File: kin_assistant.ipynb

🙌 Acknowledgements
💻 Platform: Google Colab

🧑‍🔬 STT: RW-DEEPSPEECH-API

🔉 TTS: KinyaTTS by Rwanda MIT researchers

💬 NLP: OpenAI ChatGPT integration

