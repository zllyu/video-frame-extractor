import cv2
import os
import argparse

def extract_frames(video_path, output_folder, fps):
    # make sure fps is a multiple of 0.2
    if (fps*10) % (0.2*10) != 0:  # *10 is to avoid floating-point precision issue
        raise ValueError("FPS must be a multiple of 0.2")

    # load video
    video = cv2.VideoCapture(video_path)
    if not video.isOpened():
        raise IOError("Error opening video file")

    # get original fps
    original_fps = video.get(cv2.CAP_PROP_FPS)
    frame_interval = int(original_fps / fps)
    print(original_fps, fps, frame_interval)

    # create output folder if not existed
    os.makedirs(output_folder, exist_ok=True)
    
    frame_count = 0
    extracted_count = 0

    while True:
        ret, frame = video.read()
        if not ret:
            break

        # extract subsets every frame_interval frame
        if frame_count % frame_interval == 0:
            output_frame_path = os.path.join(output_folder, f"frame_{extracted_count:04d}.jpg")
            cv2.imwrite(output_frame_path, frame)
            print(f"Extracted frame {extracted_count:04d}")
            extracted_count += 1
        
        frame_count += 1

    video.release()
    print("Done extracting frames.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract frames from video at specified FPS")
    parser.add_argument("--video_path", type=str, help="Path to the input video file")
    parser.add_argument("--output_folder", type=str, help="Path to the output folder for extracted frames")
    parser.add_argument("--fps", type=float, required=True, help="Frames per second at which to extract frames")

    args = parser.parse_args()
    extract_frames(args.video_path, args.output_folder, args.fps)
