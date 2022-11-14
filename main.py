import time
from moviepy.editor import *
import pyttsx3
from PIL import Image, ImageDraw, ImageFont
# from textss import quotes
from text_process import text_wrap
from web_extractor import quotesList

img_path = "elon-musk.png"
url = ""
imgName = img_path[:img_path.index('.')]

print("scraping Quotes from url--------")
quotes = quotesList()

print("Generating Images-------------------------")


def create_image_with_text(text, font):
    img = Image.open(img_path)
    x = img.width // 2
    y = img.height // 3
    line_hyt = font.getbbox('hg')[-1]

    lines = text_wrap(text=text, font=font, max_width=x)
    draw = ImageDraw.Draw(img)
    for line in lines:
        draw.text((x, y), line, font=font)
        y += line_hyt

    return img


fnt = ImageFont.truetype("arial.ttf", 50, encoding="unic")
frameList = []

for i in range(len(quotes)):
    im = create_image_with_text(quotes[i], fnt)
    Name = f"img/{i}-{imgName}.png"
    print(f'{Name} is successfully saved')
    im.save(Name, 'PNG')
    frameList.append(Name)

print("Image generating Done ----------------------")
time.sleep(1)

print("Generating Mp3 Files _________________________________________")

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.setProperty('rate', 110)
audioList = []

for i in range(len(quotes)):
    name = f"mp3/{i}-{imgName}.mp3"
    engine.save_to_file(quotes[i], name)
    engine.runAndWait()
    print(name + 'generated')
    audioList.append(name)

print('Mp3 generated successfully ------------------------------')
time.sleep(1)
print("Final Video Clip generating--------------------------------------------------")

vclips = []
for i in range(len(audioList)):
    clip = ImageClip(f'img/{i}-{imgName}.png')
    audio_clip = AudioFileClip(f'mp3/{i}-{imgName}.mp3')
    clip1 = clip.set_duration(audio_clip.duration + 2)
    clip = clip.set_duration(1.2)
    clip1 = clip1.set_audio(audio_clip)
    f = concatenate_videoclips([clip, clip1])
    vclips.append(f)
    print(f"{i} video is created successfully")
print(vclips)
if vclips:
    final_clips = concatenate_videoclips([vclips[0]] + [vclips[i].crossfadein(0.3) for i in range(1, len(vclips))],
                                         method="compose", padding=0.3)
    audio = AudioFileClip('audio.mp3').subclip(2,)
    audio = audio.audio_loop(duration=final_clips.duration).volumex(0.2).audio_fadein(1.0).audio_fadeout(1.0)
    new_aud_clip = CompositeAudioClip([final_clips.audio, audio])
    final_clips = final_clips.set_audio(new_aud_clip)

    final_clips.resize((1920, 1080)).write_videofile(f'output/{imgName}.mp4', bitrate='500K', fps=24, codec='libx264',
                                                     threads=32, preset='medium')
else:
    raise "Vclips empty"
