import os
import random
import moviepy.editor as mp

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


def add_video_to_narrative(narrative: Narrative, video_parent_directory: str = "output") -> bool:
    """
    This function adds a randomly selected video to a WAV audio file.
    :param audio_file_name: The name of the audio file (excluding the file extension)
    :param audio_file_path: The path to the audio file (parent directory)
    :return: None
    """

    audio_files = narrative.to_audio(file_path=os.getcwd() + os.sep + "reddit_tts_bot_temp")

    for audio_file in audio_files:
        audio_file = audio_file.replace(":", "-").replace("/", "-")
        random_video: str | None = get_random_video()

        if random_video is None:
            raise FileNotFoundError("No videos found in the videos directory.")

        video = mp.VideoFileClip("videos" + os.sep + random_video)
        audio = mp.AudioFileClip(os.getcwd() + os.sep + "reddit_tts_bot_temp" + os.sep + audio_file)

        while video.duration < audio.duration:
            random_video = get_random_video()
            video = mp.VideoFileClip("videos" + os.sep + random_video)

        # Select a random time interval within the video equal to the length of the audio file
        start_time = random.uniform(0, video.duration - audio.duration)
        video = video.subclip(start_time, start_time + audio.duration)

        # Overwrite any existing audio in the video with the new audio
        video = video.set_audio(audio)

        # Crop the video to 1080x1920 (9:16 aspect ratio)
        video = video.crop(x1=0, y1=0, x2=1920, y2=1080)

        # Write the new video to the output directory
        output_directory = video_parent_directory + os.sep + audio_file[:len(audio_file) - 4] + ".mp4"
        os.makedirs(os.path.dirname(output_directory), exist_ok=True)

        video.write_videofile(video_parent_directory + os.sep + audio_file[:len(audio_file) - 4] + ".mp4",
                              codec="libx264", audio_codec="aac")

    # delete the temporary audio files and folder
    os.system("rm -r reddit_tts_bot_temp")

    return True
