__author__ = "Jackson Eshbaugh"
__version__ = "05/24/2024"
"""
This file contains code pertaining to video generation for the Reddit TTS Bot.
"""

import os
import random
import pandas as pd

import cv2
import moviepy.editor as mp
import whisper
from moviepy.video.VideoClip import VideoClip, TextClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.VideoClip import VideoClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.tools.subtitles import SubtitlesClip

from reddit_tts_bot.narrative import Narrative


def get_random_video() -> str | None:
    """
    This function returns a random video from the videos directory.
    :return: The name of the video file or None if no videos are available
    """

    if not os.path.exists("videos"):
        raise FileNotFoundError("The videos directory does not exist.")

    videos = os.listdir("videos")
    if not videos:
        raise FileNotFoundError("No videos found in the videos directory.")

    return random.choice(videos)


def subtitle_video(video_file: str, video_directory: str) -> None:
    """
    Uses OpenAI's Whisper model to generate subtitles for a video.

    This function is modified from Gradient AI's Whisper-AutoCaption repository: https://github.com/gradient-ai/Whisper-AutoCaption/blob/main/app.py
    :param video_file: The video file to subtitle (including the file extension)
    :param video_directory: The directory containing the video file
    :return: None
    """
    my_clip = mp.VideoFileClip(os.getcwd() + os.sep + '.temp_video' + os.sep + video_file)

    # Create a temporary directory for the audio file
    os.makedirs(os.getcwd() + os.sep + '.temp_subtitle', exist_ok=True)

    if len(os.listdir(os.getcwd() + os.sep + '.temp_subtitle' + os.sep)) == 0:
        my_clip.audio.write_audiofile(os.getcwd() + os.sep + '.temp_subtitle' + os.sep + 'audio.mp3',
                                      codec="libmp3lame")

    # Instantiate whisper model using model_type variable
    model = whisper.load_model('medium')

    # Get text from speech for subtitles from audio file
    result = model.transcribe(os.getcwd() + os.sep + '.temp_subtitle' + os.sep + 'audio.mp3', task='translate')

    # create Subtitle dataframe, and save it
    dict1 = {'start': [], 'end': [], 'text': []}
    for i in result['segments']:
        dict1['start'].append(int(i['start']))
        dict1['end'].append(int(i['end']))
        dict1['text'].append(i['text'])
    df = pd.DataFrame.from_dict(dict1)
    vidcap = cv2.VideoCapture(os.getcwd() + os.sep + '.temp_video' + os.sep + video_file)
    success, image = vidcap.read()
    height = image.shape[0]
    width = image.shape[1]

    # Instantiate MoviePy subtitle generator with TextClip, subtitles, and SubtitlesClip
    generator = lambda txt: TextClip(txt, font='P052-Bold', fontsize=width / 20, stroke_width=1, color='white',
                                     stroke_color='black', size=(width, height * .25), method='caption')
    subs = tuple(zip(tuple(zip(df['start'].values, df['end'].values)), df['text'].values))
    subtitles = SubtitlesClip(subs, generator)

    # Create final video directory if it doesn't exist
    os.makedirs(video_directory, exist_ok=True)

    video: VideoFileClip = VideoFileClip(os.getcwd() + os.sep + '.temp_video' + os.sep + video_file)
    final: CompositeVideoClip = CompositeVideoClip([video, subtitles.set_pos(('center', 'center'))])
    final.write_videofile(video_directory + os.sep + video_file, fps=video.fps, remove_temp=True, codec="libx264",
                          audio_codec="aac")

    # remove the temporary audio files and folder
    os.system("rm -r .temp_subtitle")


def add_video_to_narrative(narrative: Narrative, video_directory: str = "output") -> bool:
    """
    This function adds a randomly selected video to a WAV audio file.
    :param audio_file_name: The name of the audio file (excluding the file extension)
    :param audio_file_path: The path to the audio file (parent directory)
    :return: None
    """

    audio_files = narrative.to_audio(file_path=os.getcwd() + os.sep + ".temp_audio")

    os.makedirs('.temp_video', exist_ok=True)

    for audio_file in audio_files:
        audio_file = audio_file.replace(":", "-").replace("/", "-")
        random_video: str | None = get_random_video()

        if random_video is None:
            raise FileNotFoundError("No videos found in the \"videos\" directory.")

        video: VideoFileClip(VideoClip) = mp.VideoFileClip("videos" + os.sep + random_video)
        audio: AudioFileClip = mp.AudioFileClip(os.getcwd() + os.sep + ".temp_audio" + os.sep + audio_file)

        while video.duration < audio.duration:
            random_video = get_random_video()
            video = mp.VideoFileClip("videos" + os.sep + random_video)

        # Select a random time interval within the video equal to the length of the audio file
        start_time = random.uniform(0, video.duration - audio.duration)
        video = video.subclip(start_time, start_time + audio.duration)

        # Overwrite any existing audio in the video with the new audio
        video = video.set_audio(audio)

        # Resize the video to the desired height while maintaining aspect ratio
        video = video.resize(height=1920)

        # Crop the video to 1080x1920 (9:16 aspect ratio)
        # The crop will be centered, so x1 will be (video.size[0]-1080)/2
        video = video.crop(x1=(video.size[0] - 1080) / 2, width=1080)

        # Write the new video to the output directory
        output = os.getcwd() + os.sep + '.temp_video' + os.sep + audio_file[:len(audio_file) - 4] + ".mp4"
        os.makedirs(os.path.dirname(output), exist_ok=True)

        video.write_videofile(output, codec="libx264", audio_codec="aac")
        subtitle_video(video_file=audio_file[:len(audio_file) - 4] + ".mp4", video_directory=video_directory)

    # delete the temporary audio files and folder
    os.system("rm -r .temp_audio")
    os.system("rm -r .temp_video")

    return True
