import os
os.environ['LIBROSA_CACHE_DIR'] = '/tmp/librosa_cache'
import librosa

librosa.cache.clear()