# Accent Aware SRT using Deep Learning and Speaker Adaptation

## Overview

The **Accent Aware SRT** project leverages deep learning techniques and speaker adaptation to build an accurate, real-time Speech-to-Text (SRT) system. The system enhances the traditional speech recognition process by taking into account the speaker's accent and adjusting the model to improve accuracy and robustness.

This project can be used in applications such as:

- Real-time transcription services
- Accessibility for hearing-impaired users
- Virtual assistants with improved speech recognition accuracy

## Features

- **Accent-Aware Speech Recognition**: The system adapts to different accents, improving speech-to-text accuracy.
- **Deep Learning Model**: Uses state-of-the-art models for better understanding and transcribing speech.
- **Speaker Adaptation**: Customizes the recognition model based on the user's voice, increasing accuracy.
- **Real-Time Processing**: Enables real-time transcription of speech to text.
- **Integration with SRT**: Provides Subtitle (SRT) file generation for real-time captions.

## Requirements

The project requires the following dependencies:

- `torch` - Deep Learning library for model training and inference
- `transformers` - HuggingFace Transformers for pre-trained models
- `speech_recognition` - To convert speech to text
- `pyttsx3` - For text-to-speech responses
- `sounddevice` - To capture microphone input
- `vosk` - To improve speech recognition accuracy

You can install the necessary dependencies with:

```bash
pip install -r requirements.txt
