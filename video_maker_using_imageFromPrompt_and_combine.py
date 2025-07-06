# # ##generate image based on visual text given by ai. prompt to image(then combine image to)



## stable diffusion model
#we can generate multiple image from one prompt and and combine it.
#for each of prompt we can craete multiple image


## use better model for better generation of image

#here we have single image for each prompt



import os
import re
import cv2
from gtts import gTTS
from diffusers import StableDiffusionPipeline
import torch

# Function to extract narration and visual prompts from the visual file
def extract_narration_and_visuals(visual_file):
    with open(visual_file, "r", encoding="utf-8") as f:
        content = f.read()
    # Extract Narrator and Visual sections
    pattern = r'"Narrator":\s*"(.+?)",\s*"Visual":\s*"(.+?)"'
    matches = re.findall(pattern, content, flags=re.DOTALL)
    narrations = [match[0].strip() for match in matches]
    visuals = [match[1].strip() for match in matches]
    return narrations, visuals

# Function to generate images from visual prompts
def generate_images(visuals, output_dir="video_assets/images"):
    print("🎨 Generating images from visual descriptions...")

    if not visuals:
        print("❌ No visual prompts provided.")
        return []

    # Initialize the Stable Diffusion pipeline
    pipe = StableDiffusionPipeline.from_pretrained(
        "CompVis/stable-diffusion-v1-4",
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
    ).to("cuda" if torch.cuda.is_available() else "cpu")

    os.makedirs(output_dir, exist_ok=True)
    image_paths = []

    for i, prompt in enumerate(visuals):
        print(f"\n🖼️ Generating Image {i+1}")
        print(f"📜 Prompt used: \"{prompt}\"")
        image = pipe(prompt).images[0]
        img_path = os.path.join(output_dir, f"image_{i+1}.png")
        image.save(img_path)
        image_paths.append(img_path)
        print(f"✅ Saved image: {img_path}")

    return image_paths

# Function to generate audio from narration
def generate_audio(narrations, output_path="video_assets/audio.mp3"):
    print("🔊 Generating audio from narration...")

    if not narrations:
        print("❌ No narration lines provided.")
        return None

    narration_text = " ".join(narrations)
    tts = gTTS(narration_text)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    tts.save(output_path)

    if os.path.exists(output_path):
        print(f"✅ Audio saved at: {output_path} ({os.path.getsize(output_path)} bytes)")
        return output_path
    else:
        print("❌ Failed to generate audio.")
        return None

# Function to create a video from images and audio
def create_video(image_dir, audio_path, output_path="video_assets/final_video.mp4", duration_per_image=4):
    print("🎞️ Creating video using OpenCV...")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    image_paths = sorted([
        os.path.join(image_dir, f) for f in os.listdir(image_dir)
        if f.lower().endswith(('.png', '.jpg', '.jpeg'))
    ])

    if not image_paths:
        print("❌ No images found in image directory.")
        return

    first_frame = cv2.imread(image_paths[0])
    if first_frame is None:
        print(f"❌ Could not read the first image: {image_paths[0]}")
        return

    height, width, _ = first_frame.shape
    fps = 24
    frames_per_image = duration_per_image * fps

    temp_video_path = "video_assets/temp_video.avi"
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(temp_video_path, fourcc, fps, (width, height))

    for img_path in image_paths:
        img = cv2.imread(img_path)
        img = cv2.resize(img, (width, height))
        for _ in range(frames_per_image):
            out.write(img)

    out.release()
    print("🖼️ Video frames created.")

    # Combine with audio using ffmpeg
    final_cmd = f'C:/Users/admin/Desktop/ffmpeg/bin/ffmpeg -y -i "{temp_video_path}" -i "{audio_path}" -c:v copy -c:a aac -strict experimental "{output_path}"'
    os.system(final_cmd)

    if os.path.exists(output_path):
        print(f"✅ Final video saved at: {output_path} ({os.path.getsize(output_path)} bytes)")
        os.remove(temp_video_path)
    else:
        print("❌ Final video was not created.")

# Main function to orchestrate the process
def main():
    visual_file = "outputs/03_visuals_output.txt"
    image_dir = "video_assets/images"

    # Extract narrations and visuals from the visual file
    narrations, visuals = extract_narration_and_visuals(visual_file)

    # # Generate images from visual prompts
    generate_images(visuals, image_dir)

    # # Generate audio from narrations
    audio_path = generate_audio(narrations)

    if audio_path:
        # Create video combining images and audio
        create_video(image_dir, audio_path)

if __name__ == "__main__":
    main()
