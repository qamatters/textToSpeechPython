# Import the required module for text
# to speech conversion
from gtts import gTTS

# The text that you want to convert to audio
with open('GhandhiChapter86.txt', 'r') as file:
    data = file.read().replace('\n', '')

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=data, lang=language, slow=False)


# Saving the converted audio in a mp3 file named
# welcome
myobj.save("GhandhiChapter86.mp3")

