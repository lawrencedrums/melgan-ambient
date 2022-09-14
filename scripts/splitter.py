from pydub import AudioSegment
import random, os

#########################
SOURCE_FILE = "birdsong"
ADDON = "_2"
#########################

SOURCE_FILE_FULLNAME = SOURCE_FILE + ADDON
LOADED_AUDIO_FILE = AudioSegment.from_wav(f"sources/{SOURCE_FILE_FULLNAME}.wav")

# increment clip number to prevent overwriting existing clips
i = 1
while os.path.exists(f"wavs_{SOURCE_FILE}/{SOURCE_FILE}-{str(i).rjust(5, '0')}.wav"):
    i += 1

first_clip_name = f"{SOURCE_FILE}-{str(i).rjust(5, '0')}"
print(f"Source file: {SOURCE_FILE_FULLNAME}")
print(f"Splitting begin. First clip: {first_clip_name}")

total_clips = 0
for _, clip in enumerate(LOADED_AUDIO_FILE[50000:-50000:10000]):

    clip_start = random.randrange(1000, 2000)
    clip_end = random.randrange(9000, 9999)
    clip_name = f"{SOURCE_FILE}-{str(i).rjust(5, '0')}"

    with open(f"wavs_{SOURCE_FILE}/{clip_name}.wav", "wb") as f:
        clip_segment = clip[clip_start:clip_end].set_channels(1).set_frame_rate(22050)
        # clip_segment = clip.set_channels(1).set_frame_rate(22050)
        clip_segment.export(f, format="wav")

    i += 1
    total_clips += 1

print(f"Splitting done. Total clips: {total_clips}.")
