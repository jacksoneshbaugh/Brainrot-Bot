# test tts module

import reddit_tts_bot.tts as tts
import reddit_tts_bot.narrative as narrative
import os


def test_tts():
    tts.tts('Hello, world!', file_path=os.getcwd() + "/testmantests/audiotests", file_name="test_tts")
    assert os.path.exists(os.getcwd() + "/testmantests/audiotests/test_tts.wav")


def test_narrative():
    narratives = narrative.scrape_narratives(5)
    assert len(narratives) == 5


# Run the tests
test_narrative()
test_tts()
