# TO-DO

- [ ] Pull narratives to make into shorts from Reddit.
  - [x] Decide on what qualifies to be pulled into a short.
    - [x] Minimum word count = 100.
  - [x] Decide on a word limit to split into multiple shorts = 140
  - [ ] Fix the issue with scraping Reddit
    - It seems that the bot doesn't find all the posts on Reddit. Is there a way to "scroll down" and load more posts?

- [ ] Video synthesis.
  - [ ] From the pre-downloaded Minecraft parkour videos, randomly select one to use as the background gameplay.
  - [ ] Randomly select time congruent to the length of the narrative within the gameplay video.
  - [ ] Add audio captions to the gameplay video.
    - [ ] Use OpenAI Whisper and moviepy to generate and add captions.
      - [ ] Burn captions into the video as text, maybe even highlight the words as they are spoken.
  - [ ] Stitch the narrative and gameplay video together.
    - [ ] Use moviepy to stitch the videos together.