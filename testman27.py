# test tts module

import reddit_tts_bot.tts as tts
import os


def test_tts():
    tts.tts('Hello, world!', file_path=os.getcwd() + "/testmantests/audiotests", file_name="test_tts")
    assert os.path.exists(os.getcwd() + "/testmantests/audiotests/test_tts.wav")


# Run the test
test_tts()
