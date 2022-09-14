import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# y, sr = librosa.load('./mel_spec/test.wav')

# n_fft = 2048
# ft = np.abs(librosa.stft(y[:n_fft], hop_length = n_fft+1))

# mel_spect = librosa.feature.melspectrogram(y=y, sr=sr, n_fft=2048, hop_length=1024)
# mel_spect = librosa.power_to_db(mel_spect, ref=np.max)

# librosa.display.specshow(mel_spect, y_axis='mel', fmax=8000, x_axis='time');

# plt.title('Mel Spectrogram');
# plt.colorbar(format='%+2.0f dB');

names = [
    "bird_1", "bird_2", "bird_3", "bird_4", "bird_5", "bird_6",
    "city_1", "city_2", "city_3", "city_4", "city_5", "city_6",
    "storm_1", "storm_2", "storm_3", "storm_4", "storm_5", "storm_6"
    ]

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

fig, ax = plt.subplots()

hl = 256 # number of samples per time-step in spectrogram
hi = 500 # Height of image
wi = 500 # Width of image

# Loading demo track
for name in names:
    y, sr = librosa.load(f'./mel_spec/{name}.wav')
    window = y[0:wi*hi]

    S = librosa.feature.melspectrogram(y=window, sr=22050, hop_length=hl)
    S_dB = librosa.power_to_db(S, ref=np.max)
    img = librosa.display.specshow(S_dB, sr=22050, ax=ax)

    plt.savefig(f"f_{name}.png")
    # plt.show()
