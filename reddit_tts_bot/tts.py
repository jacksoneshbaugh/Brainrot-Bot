__author__ = "Jackson Eshbaugh"
__version__ = "05/22/2024"
"""
This file contains code pertaining to text-to-speech (TTS) functionality for the Reddit TTS Bot.
"""

import os

from voicebox import SimpleVoicebox
from voicebox.tts import gTTS
from voicebox.sinks import Distributor, WaveFile


def tts(text: str, file_path: str, file_name: str) -> None:
    """
    This function takes a string of text and saves it as a .wav file.
    :param text: The text to be spoken
    :param file_path: The path to save the .wav file (parent directory)
    :param file_name: The name of the .wav file (excluding the file extension)
    :return: None
    """

    # Create directory if it doesn't exist
    if not os.path.exists(file_path):
        os.makedirs(file_path)

    sink = Distributor([
        WaveFile(file_path + os.sep + file_name + ".wav")
    ])
    voicebox = SimpleVoicebox(tts=gTTS(), sink=sink)
    voicebox.say(text)
