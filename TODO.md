# TO-DO

- [x] Pull narratives to make into shorts from Reddit.
  - [x] Decide on what qualifies to be pulled into a short.
    - [x] Minimum word count = 100.
  - [x] Decide on a word limit to split into multiple shorts = 140
  - [x] Fix the issue with scraping Reddit
    - It seems that the bot doesn't find all the posts on Reddit. Is there a way to "scroll down" and load more posts?
      - Yes. Simply use Selenium to scroll down the page by executing JavaScript.
  - [x] Add functionality to export the narratives to a WAV file.

- [ ] Video synthesis.
  - [ ] Find Subway Surfers gameplay to use, too!
  - [x] From the pre-downloaded Minecraft parkour videos and Subway Surfers gameplay videos, randomly select one to use as the background gameplay.
  - [x] Randomly select time congruent to the length of the narrative within the gameplay video.
  - [x] Stitch the narrative and gameplay video together.
  - [ ] Fix the cropping code so that the gameplay video is cropped to the correct size.
  - [ ] Add audio captions to the gameplay video.
    - [ ] Use OpenAI Whisper and moviepy to generate and add captions.
      - [ ] Burn captions into the video as text, maybe even highlight the words as they are spoken.
  - [ ] Use moviepy to stitch the videos together.