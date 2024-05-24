__author__ = 'Jackson Eshbaugh'
__version__ = '05/24/2024'
"""
This is the entry point to run the Reddit TTS Bot.
"""

import reddit_tts_bot as rtb
import config


def generate_brainrot(num_brainrot: int = 1):
    """
    This function generates a video from a random Reddit post, with text-to-speech narration and subtitles. It also has background video.
    :return: None
    """

    if not config.OUTPUT_DIRECTORY or not config.REDDIT_SUBREDDITS or not config.MAX_WORDS_PER_PART or not config.MIN_WORD_COUNT:
        raise ValueError("Please set the configuration settings in config.py. See the README for more information.")

    print("Eye-eye, Captain! Generating " + str(num_brainrot) + " brainrot video(s)...")

    narratives = rtb.narrative.scrape_narratives(num_brainrot, min_word_count=config.MIN_WORD_COUNT, locations=config.REDDIT_SUBREDDITS)
    for narrative in narratives:
        narrative.to_audio(config.OUTPUT_DIRECTORY)
        rtb.video.add_video_to_narrative(narrative=narrative, video_directory=config.OUTPUT_DIRECTORY)

    print("Brainrot video(s) generated! Enjoy, but don't get too brainrotted!")


if __name__ == '__main__':
    while True:
        num_brainrot = int(input("How many brainrot videos would you like to generate? "))
        generate_brainrot(num_brainrot)
        conf: str = input("Would you like to generate more brainrot videos? ([y]es/[n]o) ").lower()
        if conf != 'y' and conf != 'yes':
            break
