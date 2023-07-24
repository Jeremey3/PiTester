import speech_recognition as sr

def record_and_transcribe():
    # Create a speech recognition object
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something...")
        # Adjust for ambient noise to reduce background interference
        recognizer.adjust_for_ambient_noise(source, duration=1)

        # Record audio for 5 seconds
        audio = recognizer.listen(source, timeout=5)

    try:
        # Use the Google Web Speech API to recognize the audio
        transcribed_text = recognizer.recognize_google(audio)
        print("You said: ", transcribed_text)
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

if __name__ == "__main__":
    record_and_transcribe()
