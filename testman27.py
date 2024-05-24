import reddit_tts_bot.tts as tts
import reddit_tts_bot.narrative as narrative
import reddit_tts_bot.video as video
import os


def test_tts():
    tts.tts('Hello, world!', file_path=os.getcwd() + "/testmantests/audiotests", file_name="test_tts")
    assert os.path.exists(os.getcwd() + "/testmantests/audiotests/test_tts.wav")


def test_narrative():
    narratives = narrative.scrape_narratives(5)

    for n in narratives:
        n.to_audio(file_path=os.getcwd() + "/testmantests/audiotests/narrativetests")


def test_video():
    narrative_ = narrative.scrape_narratives(1)[0]
    video.add_video_to_narrative(narrative=narrative_,
                                 video_directory=os.getcwd() + "/testmantests/videotest/narrativetests"
                                                                      "/videooutput")


# Run the tests
# test_narrative()
# test_tts()
test_video()
