import pyttsx3
from textss import quotes
from web_extractor import match_results
quotes = match_results

# txt = '"Dream, dream, dream. Dreams transform into thoughts and thoughts result in action"'

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

engine.setProperty('rate',110)
audioList = []

for i in range(len(quotes)):
    name = f"mp3/{i}.mp3"
    engine.save_to_file(quotes[i],name)
    engine.runAndWait()
    print(name,'done')
    audioList.append(name)


print('done')
