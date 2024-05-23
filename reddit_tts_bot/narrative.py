__author__ = "Jackson Eshbaugh"
__version__ = "05/23/2024"

import os.path

import random
import time

import requests
from bs4 import BeautifulSoup, ResultSet, PageElement

from reddit_tts_bot.tts import tts

MAX_WORDS_PER_PART = 140


class Narrative:
    """
    This class represents a narrative object, which will eventually be converted to an audio file.
    """

    def __init__(self, text: str, title: str):
        """
        This function initializes a Narrative object.
        :param text: The text to be spoken
        :param title: The title of the story
        """
        self.text = text
        self.title = title
        self.word_count = len(text.split())

    def title(self) -> str:
        """
        This function returns the title of the story.
        :return: The title of the story
        """
        return self.title

    def word_count(self) -> int:
        """
        This function returns the word count of the story.
        :return: The word count of the story
        """
        return self.word_count

    def text(self) -> str:
        """
        This function returns the text of the story.
        :return: The text of the story
        """
        return self.text

    def to_audio(self, file_path: str) -> None:
        """
        This function converts the text of the story to an audio file.
        :param file_path: The path to save the .wav file (parent directory)
        :return: None
        """

        if self.word_count > MAX_WORDS_PER_PART:
            # Split the story into parts
            parts = []
            words = self.text.split()
            part = ""
            for word in words:
                if len(part.split()) < MAX_WORDS_PER_PART:
                    part += word + " "
                else:
                    parts.append(part)
                    part = word + " "
            parts.append(part)

            # Save each part as an audio file
            for i, part in enumerate(parts):
                tts(part, file_path, self.title + "_part" + str(i + 1))
        else:
            tts(self.text, file_path, self.title)


# Scrape narratives from Reddit

locations: tuple = ("r/tifu", "r/entitledparents", "r/AmItheAsshole")

DEFAULT_MIN_WORD_COUNT: int = 100


def scrape_narratives(num_narratives: int, min_word_count: int = DEFAULT_MIN_WORD_COUNT, locations: list = locations) -> list:
    """
    This function scrapes narratives from Reddit.
    :param num_narratives: The number of narratives to scrape
    :param min_upvotes: The minimum number of upvotes for a post
    :param min_word_count: The minimum word count for a post
    :return: A list of Narrative objects
    """

    # Create a file to hold the names of all the narratives ever scraped
    if not os.path.exists("narrative_names.txt"):
        with open("narrative_names.txt", "w") as file:
            file.write("")

    narratives = []

    for i in range(num_narratives):
        # Choose a random location to pull stories from
        location = random.choice(locations)

        print("Scraping from " + location)

        # Scrape the story
        time.sleep(5)
        page: requests.Response = requests.get("https://www.reddit.com/" + location + "/top/?t=all")
        soup: BeautifulSoup = BeautifulSoup(page.content, "html.parser")
        posts: ResultSet = soup.find_all("article", class_="w-full m-0")

        # Choose a random post
        post: PageElement = random.choice(posts)

        # Check if the post has already been scraped
        while post["aria-label"] in open("narrative_names.txt").read():
            # Choose a random location to pull stories from
            location = random.choice(locations)

            print("[DUPLICATE FOUND] Scraping from " + location)

            # Scrape the story
            time.sleep(5)
            page: requests.Response = requests.get("https://www.reddit.com/" + location + "/top/?t=all")
            soup: BeautifulSoup = BeautifulSoup(page.content, "html.parser")
            posts: ResultSet = soup.find_all("article", class_="w-full m-0")

            # Choose a random post
            post = random.choice(posts)

        # Get the title (stored in the aria-label attribute of each post)
        title: str = post["aria-label"]

        # Write the title to the file to keep track of which posts have been scraped
        with open("narrative_names.txt", "a") as file:
            file.write(title + "\n")

        # Get the content: go to the post's page and scrape the content
        post_url: str = "https://reddit.com/" + post.find_next("a")["href"]
        time.sleep(5)
        post_page: requests.Response = requests.get(post_url)
        post_soup: BeautifulSoup = BeautifulSoup(post_page.content, "html.parser")
        content: str = post_soup.select_one('.md.text-14').text.strip()
        content = content.replace('\n', ' ')
        
        # Check if the post meets the minimum word count requirement
        if len(content.split()) < min_word_count:
            i -= 1
            continue

        # Create a Narrative object
        narrative = Narrative(content, title)
        narratives.append(narrative)

    return narratives

