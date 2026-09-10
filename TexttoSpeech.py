import speech_recognition as sr
import os
import tempfile
from gtts import gTTS
from playsound import playsound
from googletrans import Translator  # Google Translate API


# Text-to-Speech using gTTS (supports Hindi, Marathi, Tamil, etc. natively)
def speak(text, language="en"):
    if not text:
        print("DEBUG: speak() called with empty text, skipping.")
        return

    try:
        tts = gTTS(text=text, lang=language)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            temp_path = fp.name
        tts.save(temp_path)
        print(f"DEBUG: saved audio to {temp_path}, playing now...")
        playsound(temp_path)
        os.remove(temp_path)
    except Exception as e:
        print(f"DEBUG: gTTS speak failed: {e}")


# Speech-to-Text: Recognize spoken language (English)
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak now in English...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        print("Recognizing speech...")
        text = recognizer.recognize_google(audio, language="en-US")
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand the audio.")
    except sr.RequestError as e:
        print(f"API Error: {e}")
    return ""


# Translate text using Google Translate API
def translate_text(text, target_language="es"):
    try:
        translator = Translator()
        translation = translator.translate(text, dest=target_language)
        print(f"Translated text: {translation.text}")
        return translation.text
    except Exception as e:
        print(f"DEBUG: Translation failed with error: {e}")
        return ""


# Display language options to the user
def display_language_options():
    print("Available translation languages: ")
    print("1. Hindi (hi)")
    print("2. Tamil (ta)")
    print("3. Telugu (te)")
    print("4. Bengali (bn)")
    print("5. Marathi (mr)")
    print("6. Gujarati (gu)")
    print("7. Malayalam (ml)")
    print("8. Punjabi (pa)")

    choice = input("Please select the target language number (1-8): ")
    language_dict = {
        "1": "hi",
        "2": "ta",
        "3": "te",
        "4": "bn",
        "5": "mr",
        "6": "gu",
        "7": "ml",
        "8": "pa"
    }

    return language_dict.get(choice, "es")  # Default to Spanish if invalid input


# Main function to combine all steps
def main():
    target_language = display_language_options()
    print(f"DEBUG: target_language = {target_language}")

    original_text = speech_to_text()
    print(f"DEBUG: original_text = '{original_text}'")

    if original_text:
        translated_text = translate_text(original_text, target_language=target_language)
        print(f"DEBUG: translated_text = '{translated_text}'")

        speak(translated_text, language=target_language)
        print("Translation spoken out!")
    else:
        print("DEBUG: original_text was empty, skipping translation/speech")


if __name__ == "__main__":
    main()