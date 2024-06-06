# Video Frame Extractor

This script extracts frames from a video at a specified frames-per-second (FPS) rate and saves them to an output folder.

## Requirements

- Python 3.x
- OpenCV

## Installation

1. Clone the repository or download the script.
2. Install the required packages using pip:

```bash
pip install -r requirements.txt
```

## Usage

To run the script, use the following command:

```bash
python extract_frames.py --video_path <path_to_video> --output_folder <output_folder_path> --fps <fps>
```

Arguments

- `--video_path`: Path to the input video file.
- `--output_folder`: Path to the output folder where the extracted frames will be saved.
- `--fps`: Frames per second at which to extract frames. The FPS value must be a multiple of 0.2.

Example

```bash
python extract_frames.py --video_path sample_video.mp4 --output_folder frames --fps 1.2
```

This command will extract frames from `sample_video.mp4` at 1.2 frames per second and save them in the `frames` folder.

## Notes

- Ensure that the specified FPS value is a multiple of 0.2 to avoid errors.
- The script will create the output folder if it does not exist.
- Frames are saved in the JPEG format with filenames frame_0000.jpg, frame_0001.jpg, etc.