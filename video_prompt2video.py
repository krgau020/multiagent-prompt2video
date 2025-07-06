
### CPU CONSTRAINT--- Not working 





##Model Scope model


# import os
# import re
# import cv2
# import torch
# from gtts import gTTS
# from modelscope.pipelines import pipeline
# from modelscope.utils.constant import Tasks

# # Function to extract narration and visual prompts from the visual file
# def extract_narration_and_visuals(visual_file):
#     with open(visual_file, "r", encoding="utf-8") as f:
#         content = f.read()
#     # Extract Narrator and Visual sections
#     # pattern = r'"Narrator":\s*"(.+?)",\s*"Visual":\s*"(.+?)"'
#     pattern = r'Narrator:\s*(.*?)\nVisual:\s*(.*?)(?=\nNarrator:|\Z)'

#     matches = re.findall(pattern, content, flags=re.DOTALL)
#     narrations = [match[0].strip() for match in matches]
#     visuals = [match[1].strip() for match in matches]
#     return narrations, visuals

# # Function to generate videos from visual prompts
# def generate_videos(visuals, output_dir="video_assets/videos", fps=24, resolution=(512, 512), duration=5):
#     print("🎬 Generating videos from visual prompts...")

#     # Set device to 'cpu' to avoid CUDA-related issues
#     device = 'cpu'

#     # Load the pipeline with map_location set to CPU
#     pipe = pipeline(
#         Tasks.text_to_video_synthesis,
#         model='damo/text-to-video-synthesis',
#         model_kwargs={"device_map": "cpu", "map_location": torch.device("cpu")},
#         device=device
#     )



#     os.makedirs(output_dir, exist_ok=True)
#     video_paths = []

#     for i, prompt in enumerate(visuals):
#         print(f"\n🎞️ Generating Video {i+1}")
#         print(f"📜 Prompt used: \"{prompt}\"")

#         # Generate video frames using the pipeline
#         result = pipe({'text': prompt})
#         video_frames = result['video']  # Assuming the pipeline returns a list of frames

#         # Save video using OpenCV
#         video_path = os.path.join(output_dir, f"video_{i+1}.mp4")
#         fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#         out = cv2.VideoWriter(video_path, fourcc, fps, resolution)

#         for frame in video_frames:
#             frame_resized = cv2.resize(frame, resolution)
#             out.write(frame_resized)

#         out.release()
#         video_paths.append(video_path)
#         print(f"✅ Saved video: {video_path}")

#     return video_paths

# # Function to generate audio from narration
# def generate_audio(narrations, output_path="video_assets/audio.mp3"):
#     print("🔊 Generating audio from narration...")

#     if not narrations:
#         print("❌ No narration lines provided.")
#         return None

#     narration_text = " ".join(narrations)
#     tts = gTTS(narration_text)
#     os.makedirs(os.path.dirname(output_path), exist_ok=True)
#     tts.save(output_path)

#     if os.path.exists(output_path):
#         print(f"✅ Audio saved at: {output_path} ({os.path.getsize(output_path)} bytes)")
#         return output_path
#     else:
#         print("❌ Failed to generate audio.")
#         return None

# # Function to create a final video from video segments and audio
# def create_final_video(video_paths, audio_path, output_path="video_assets/final_video.mp4"):
#     print("🎞️ Creating final video using OpenCV...")

#     os.makedirs(os.path.dirname(output_path), exist_ok=True)

#     # Concatenate video segments using ffmpeg
#     temp_video_list = "video_assets/video_list.txt"
#     with open(temp_video_list, "w") as f:
#         for path in video_paths:
#             f.write(f"file '{os.path.abspath(path)}'\n")

#     temp_video_path = "video_assets/temp_video.mp4"
#     concat_cmd = f'C:/Users/admin/Desktop/ffmpeg/bin/ffmpeg -f concat -safe 0 -i "{temp_video_list}" -c copy "{temp_video_path}"'
#     os.system(concat_cmd)

#     # Combine with audio using ffmpeg
#     final_cmd = f'C:/Users/admin/Desktop/ffmpeg/bin/ffmpeg -y -i "{temp_video_path}" -i "{audio_path}" -c:v copy -c:a aac -strict experimental "{output_path}"'
#     os.system(final_cmd)

#     if os.path.exists(output_path):
#         print(f"✅ Final video saved at: {output_path} ({os.path.getsize(output_path)} bytes)")
#         os.remove(temp_video_path)
#         os.remove(temp_video_list)
#     else:
#         print("❌ Final video was not created.")

# # Main function to orchestrate the process
# def main():
#     visual_file = "outputs/03_visuals_output.txt"
#     video_dir = "video_assets/videos"

#     # Extract narrations and visuals from the visual file
#     narrations, visuals = extract_narration_and_visuals(visual_file)

#     # Generate videos from visual prompts
#     video_paths = generate_videos(visuals, video_dir)

#     # Generate audio from narrations
#     audio_path = generate_audio(narrations)

#     if audio_path:
#         # Create final video combining video segments and audio
#         create_final_video(video_paths, audio_path)

# if __name__ == "__main__":
#     main()




























# from huggingface_hub import snapshot_download
# from modelscope.pipelines import pipeline
# from modelscope.outputs import OutputKeys
# import pathlib
# import torch

# model_dir = pathlib.Path('weights')
# snapshot_download('damo-vilab/modelscope-damo-text-to-video-synthesis',
#                    repo_type='model', local_dir=model_dir)

# # Patch torch.load to always load on CPU
# torch_load_orig = torch.load
# def torch_load_cpu(*args, **kwargs):
#     kwargs['map_location'] = torch.device('cpu')
#     return torch_load_orig(*args, **kwargs)

# torch.load = torch_load_cpu  # Override globally

# # Initialize pipeline
# pipe = pipeline('text-to-video-synthesis', model_dir.as_posix())
# test_text = {
#     'text': 'A panda eating bamboo on a rock.',
# }
# output_video_path = pipe(test_text)[OutputKeys.OUTPUT_VIDEO]
# print('output_video_path:', output_video_path)










































### COG video model , cpu not enough


# import os
# import re
# import cv2
# import torch
# from gtts import gTTS
# import numpy as np
# from PIL import Image
# from torchvision import transforms

# # Assuming CogVideo inference function is available from imported cogvideo module
# from cogvideo.inference import generate_video_from_text

# # Function to extract narration and visual prompts from the visual file
# def extract_narration_and_visuals(visual_file):
#     with open(visual_file, "r", encoding="utf-8") as f:
#         content = f.read()
#     pattern = r'Narrator:\s*(.*?)\nVisual:\s*(.*?)(?=\nNarrator:|\Z)'
#     matches = re.findall(pattern, content, flags=re.DOTALL)
#     narrations = [match[0].strip() for match in matches]
#     visuals = [match[1].strip() for match in matches]
#     return narrations, visuals

# # Function to generate videos from visual prompts using CogVideo
# def generate_videos(visuals, output_dir="video_assets/videos", fps=24, resolution=(512, 512), duration=5):
#     print("🎬 Generating videos from visual prompts...")

#     os.makedirs(output_dir, exist_ok=True)
#     video_paths = []

#     for i, prompt in enumerate(visuals):
#         print(f"\n🎞️ Generating Video {i+1}")
#         print(f"📜 Prompt used: \"{prompt}\"")

#         # Generate video using CogVideo
#         video_path = os.path.join(output_dir, f"video_{i+1}.mp4")
#         generate_video_from_text(
#             prompt=prompt,
#             output_path=video_path,
#             duration=duration,
#             resolution=resolution,
#             fps=fps
#         )

#         if os.path.exists(video_path):
#             print(f"✅ Saved video: {video_path}")
#             video_paths.append(video_path)
#         else:
#             print("❌ Failed to generate video.")

#     return video_paths

# # Function to generate audio from narration
# def generate_audio(narrations, output_path="video_assets/audio.mp3"):
#     print("🔊 Generating audio from narration...")

#     if not narrations:
#         print("❌ No narration lines provided.")
#         return None

#     narration_text = " ".join(narrations)
#     tts = gTTS(narration_text)
#     os.makedirs(os.path.dirname(output_path), exist_ok=True)
#     tts.save(output_path)

#     if os.path.exists(output_path):
#         print(f"✅ Audio saved at: {output_path} ({os.path.getsize(output_path)} bytes)")
#         return output_path
#     else:
#         print("❌ Failed to generate audio.")
#         return None

# # Function to create a final video from video segments and audio
# def create_final_video(video_paths, audio_path, output_path="video_assets/final_video.mp4"):
#     print("🎞️ Creating final video using OpenCV...")

#     os.makedirs(os.path.dirname(output_path), exist_ok=True)

#     # Concatenate video segments using ffmpeg
#     temp_video_list = "video_assets/video_list.txt"
#     with open(temp_video_list, "w") as f:
#         for path in video_paths:
#             f.write(f"file '{os.path.abspath(path)}'\n")

#     temp_video_path = "video_assets/temp_video.mp4"
#     concat_cmd = f'C:/Users/admin/Desktop/ffmpeg/bin/ffmpeg -f concat -safe 0 -i "{temp_video_list}" -c copy "{temp_video_path}"'
#     os.system(concat_cmd)

#     # Combine with audio using ffmpeg
#     final_cmd = f'C:/Users/admin/Desktop/ffmpeg/bin/ffmpeg -y -i "{temp_video_path}" -i "{audio_path}" -c:v copy -c:a aac -strict experimental "{output_path}"'
#     os.system(final_cmd)

#     if os.path.exists(output_path):
#         print(f"✅ Final video saved at: {output_path} ({os.path.getsize(output_path)} bytes)")
#         os.remove(temp_video_path)
#         os.remove(temp_video_list)
#     else:
#         print("❌ Final video was not created.")

# # Main function to orchestrate the process
# def main():
#     visual_file = "outputs/03_visuals_output.txt"
#     video_dir = "video_assets/videos"

#     # Extract narrations and visuals from the visual file
#     narrations, visuals = extract_narration_and_visuals(visual_file)

#     # Generate videos from visual prompts
#     video_paths = generate_videos(visuals, video_dir)

#     # Generate audio from narrations
#     audio_path = generate_audio(narrations)

#     if audio_path:
#         # Create final video combining video segments and audio
#         create_final_video(video_paths, audio_path)

# if __name__ == "__main__":
#     main()































