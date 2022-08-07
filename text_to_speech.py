from gtts import gTTS
import os

def TextToSpeech():
        text = 'Hello Dev! How are you'
        language = 'en'
        speech = gTTS(text=text, lang=language, slow=False)
  
        speech.save("TextToSpeech.mp3")
        os.system("TextToSpeech.mp3")
        print('Code compiled successfuly!')

TextToSpeech()