__author__ = "Jackson Eshbaugh"
__version__ = "05/24/2024"
"""
This file contains the configuration settings for the Reddit TTS Bot.
"""

OUTPUT_DIRECTORY: str = 'output'
# A tuple is denoted by parentheses, but if you want only one element in the tuple, you need to add a comma after the
# element. Example: ('r/example',)
REDDIT_SUBREDDITS: tuple = ("r/tifu", "r/entitledparents", "r/AmItheAsshole")
MAX_WORDS_PER_PART: int = 140
MIN_WORD_COUNT: int = 100
