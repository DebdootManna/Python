import os
import cv2
import numpy as np
import imageio

def extract_frames_opencv(video_path, output_folder, num_frames):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return False  # Signal fallback

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_indices = np.linspace(0, total_frames - 1, num_frames, dtype=int)

    os.makedirs(output_folder, exist_ok=True)
    saved = 0

    for i, idx in enumerate(frame_indices):
        cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
        ret, frame = cap.read()
        if ret:
            out_path = os.path.join(output_folder, f"frame_{i:04d}.jpg")
            cv2.imwrite(out_path, frame)
            saved += 1
        else:
            print(f"Warning: Could not read frame at index {idx}")

    cap.release()
    print(f"[OpenCV] Saved {saved}/{num_frames} frames to: {output_folder}")
    return True

def extract_frames_imageio(video_path, output_folder, num_frames):
    try:
        reader = imageio.get_reader(video_path, "ffmpeg")
        total_frames = reader.count_frames()
        frame_indices = np.linspace(0, total_frames - 1, num_frames, dtype=int)

        os.makedirs(output_folder, exist_ok=True)
        saved = 0

        for i, idx in enumerate(frame_indices):
            frame = reader.get_data(idx)
            out_path = os.path.join(output_folder, f"frame_{i:04d}.jpg")
            imageio.imwrite(out_path, frame)
            saved += 1

        print(f"[ImageIO] Saved {saved}/{num_frames} frames to: {output_folder}")
    except Exception as e:
        print(f"[ImageIO Error] {e}")
    finally:
        reader.close()

def extract_video_frames(video_path, output_folder="output_frames", num_frames=300):
    if not os.path.exists(video_path):
        print(f"❌ File not found: {video_path}")
        return

    print(f"📂 Video: {video_path}")
    print(f"📸 Target Frames: {num_frames}")

    success = extract_frames_opencv(video_path, output_folder, num_frames)
    if not success:
        print("⚠️ OpenCV failed. Trying with imageio+ffmpeg...")
        extract_frames_imageio(video_path, output_folder, num_frames)

# ====== Example Usage ======
if __name__ == "__main__":
    video_path = "/Users/debdootmanna/VSCode/Python/python-screenshot-script/20250125_210853.mp4"
    extract_video_frames(video_path, output_folder="output_frames", num_frames=300)
