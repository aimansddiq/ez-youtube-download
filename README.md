# YouTube Video Downloader

This is a simple Python program that downloads a YouTube video in the highest quality available and saves it to a specified directory.

## Prerequisites

- Python 3.x
- `yt_dlp` library

You can install the `yt_dlp` library using `pip`:

```
pip install youtube_dl
```

## Usage

1. Clone or download this repository to your computer.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the following command, replacing `VIDEO_URL` with your own values:

```
python download.py VIDEO_URL
```


For example, to download the video at `https://www.youtube.com/watch?v=dQw4w9WgXcQ`, you would run:

```
python download.py https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

The video will be downloaded in the highest quality available and saved to `/video`.

## Contributing

If you have any suggestions or issues, feel free to open an issue or pull request in this repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
