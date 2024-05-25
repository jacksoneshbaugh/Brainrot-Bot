# Brainrot Bot

Brainrot Bot is a driver for my Python module [`reddit-tts-bot`](https://github.com/jacksoneshbaugh/reddit-tts-bot). It is a bot that scrapes Reddit for narratives, converts them to speech, and synthesizes them with video gameplay. 

## Usage

To use Brainrot Bot, you must first install the Python module `reddit-tts-bot`. You can do this by running the following command:

```bash
pip install reddit-tts-bot
```

Please see the [README.md file](https://github.com/jacksoneshbaugh/Reddit-TTS-Bot#installation) at the repository for `reddit-tts-bot` for more information on how to use the module, and some **required dependencies** (that aren't Python packages) that you will need to install.

Then, you can run the bot by executing the following command in the directory where `main.py` is located:

```bash
python main.py
```

## Configuration

In `config.py`, you can configure the bot to scrape from different subreddits, and you can choose the parameters for the bot to use when scraping Reddit (the minimum word count for a narrative, the maximum word count for a narrative before it is split into multiple parts), and the output directory for the bot to save the video files.

## License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.

## Contributing

I would *love* for you to contribute! Please fork the repository and make a pull request. I will review the pull request and merge it if it is a good fit (which it probably will be).

## Contact

If you have any questions or concerns, please feel free to reach out to me at
[jacksoneshbaugh@gmail.com](mailto:jacksoneshbaugh@gmail.com). You can find my other projects on GitHub at [jacksoneshbaugh](https://github.com/jacksoneshbaugh), and my website is at [jacksoneshbaugh.github.io](https://jacksoneshbaugh.github.io).