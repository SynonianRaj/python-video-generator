# frames = ['img/0-ratan-tata.png', 'img/1-ratan-tata.png', 'img/2-ratan-tata.png', 'img/3-ratan-tata.png',
#           'img/4-ratan-tata.png', 'img/5-ratan-tata.png', 'img/6-ratan-tata.png', 'img/7-ratan-tata.png',
#           'img/8-ratan-tata.png']
#
# aud = ['mp3/0.mp3', 'mp3/1.mp3', 'mp3/2.mp3', 'mp3/3.mp3', 'mp3/4.mp3', 'mp3/5.mp3', 'mp3/6.mp3']

from moviepy.editor import *

# clips = [ImageClip(frames[m]).set_duration(AudioFileClip(aud[m]).duration + 3)
#          for m in range(len(frames))]

# concat_clip = concatenate_videoclips(clips, method="compose", padding=0.2)

# audio = AudioFileClip('audio.mp3').set_duration(concat_clip.duration)
# new_audioclip = CompositeAudioClip([audio])
# vid = concat_clip.set_audio(new_audioclip)

# vid.write_videofile("output/test.mp4", fps=24, codec='mpeg4')


vclips = []
for i in range(len(aud)):
    clip = ImageClip(f'img/{i}-ratan-tata.png')
    audio_clip = AudioFileClip(f'mp3/{i}.mp3')
    clip1 = clip.set_duration(audio_clip.duration + 2)
    clip = clip.set_duration(1.2)
    clip1 = clip1.set_audio(audio_clip)
    f = concatenate_videoclips([clip, clip1])
    vclips.append(f)
    print(f"{i} video is created successfully")
print(vclips)
if vclips:
    var = [i for i in range(len(vclips))]
    final_clips = concatenate_videoclips([vclips[0]] + [vclips[i].crossfadein(0.3) for i in range(1, len(vclips))],
                                         method="compose", padding=0.3)

    audio = AudioFileClip('audio.mp3').volumex(0.2).subclip(2, final_clips.duration + 5).audio_fadein(
        1.0).audio_fadeout(1.0)
    new_aud_clip = CompositeAudioClip([final_clips.audio, audio])
    final_clips = final_clips.set_audio(new_aud_clip)

    final_clips.resize((1920,1080)).write_videofile('output/video1.mp4', bitrate='500K', fps=24, codec='libx264',
                                                    threads=32, preset='medium')
else:
    raise "Vclips empty"
