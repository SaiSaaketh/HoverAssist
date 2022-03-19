from ast import keyword
import struct
import pyaudio
import pvporcupine
import winsound
from hover import *

porcupine = None
pyaud = None
audio_stream = None

try:
    porcupine = pvporcupine.create(
        access_key='NC8a7H5PNDrDbG3qQJwVYdaPruOM0QLxLajtHNgpCzioI9Q0OM7zIA==',
        keyword_paths=['D:\Programming\HoverAssist\Hey-Hover_en_windows_v2_1_0.ppn'])
    paud = pyaudio.PyAudio()
    audio_stream = paud.open(rate=porcupine.sample_rate,
                             channels=1, format=pyaudio.paInt16, input=True)
    while True:
        keyword = audio_stream.read(porcupine.frame_length)
        keyword = struct.unpack_from("h"*porcupine.frame_length, keyword)
        keyword_index = porcupine.process(keyword)
        if keyword_index >= 0:
            print("Hotword detected")
            winsound.PlaySound(
                'D:\\Programming\\HoverAssist\\startup_sound.wav', winsound.SND_FILENAME)
            query()
            break

finally:
    if porcupine is not None:
        porcupine.delete()
    if audio_stream is not None:
        audio_stream.close()
    if pyaud is not None:
        paud.terminate()
