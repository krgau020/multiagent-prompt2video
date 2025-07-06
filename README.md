# 📽️ Prompt2Video Multi-Agent System — CrewAI + Gemini + Stable Diffusion

An end-to-end Agentic AI system that transforms a simple text prompt into a fully narrated video.  
Combining CrewAI, Google Gemini Pro, Stable Diffusion, and robust orchestration, this project demonstrates how multiple specialized agents can collaborate autonomously to research, script, design, and produce a video.

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository  
git clone https://github.com/yourusername/prompt2video-Multi-agents.git  
cd prompt2video-Multi-agents

---

### 2️⃣ (Optional) Create a Virtual Environment  
Creating a virtual environment is recommended.

Create venv:  
python -m venv venv

Activate it:  
Linux/Mac:  
source venv/bin/activate

Windows:  
venv\Scripts\activate

---

### 3️⃣ Install Dependencies  
Install required Python packages:

pip install -r requirements.txt

or

crewai  
langchain-google-genai  
diffusers  
torch  
gtts  
opencv-python  
python-dotenv

---

### 4️⃣ Add Your Google Gemini API Key  
Create a `.env` file in the project root:

GOOGLE_API_KEY=YOUR_GEMINI_API_KEY

---

## 🚀 Usage

Run the multi-agent pipeline to generate your video step by step.

Run the multi-agent workflow:  
python crew.py

Run the video generation to convert text outputs into visuals, audio, and final video:  
python video_generation.py

---

## 🧩 Agent Roles

| Agent | Responsibility |
|----------------------|------------------------------------------------------------------------------------------|
| Topic Research Agent | Research the prompt topic using Gemini and web search to generate subtopics. |
| Script Writer Agent | Write a detailed, informative video script from the research output. |
| Visual Designer Agent | Create scene-by-scene visual descriptions for each part of the script. |
| Flowchart Planner Agent | Build a logical step-by-step video flowchart. |
| Response Reviewer Agent | Review script & visuals for factual accuracy and tone. |
| Evaluation Agent | Evaluate the overall quality of the script and visuals. |
| Video Generator Agent | Trigger final video generation via mock tool or local pipeline. |

---

## 🧩 Tech Stack

| Layer | Tool | Purpose |
|---------------------|-------------------------------|------------------------------------------------------------------|
| Agentic Orchestration | CrewAI | Multi-agent pipeline with sequential tasks |
| LLM | Google Gemini Pro | Research, script writing, QA, evaluations |
| Web Research | web_search_tool | Search online for factual info |
| Text-to-Image | Stable Diffusion | Generate scene images |
| Text-to-Speech | gTTS | Generate narration audio |
| Video Editing | OpenCV, FFmpeg | Combine images & audio into final video |
| Env Management | python-dotenv | Securely handle API keys |

---

## 📂 Project Structure

├── agent.py             # Defines all agents & tools  
├── crew.py              # Flowchart approval loop + main CrewAI pipeline  
├── tasks.py             # Task definitions for each agent  
├── video_maker_using_imageFromPrompt_and_combine.py  # Transforms text outputs to final video  
├── outputs/             # Stores flowchart, script, visuals text  
├── video_assets/        # Stores generated images, audio, final video  
├── .env                 # Store API keys  
└── README.md            # This file

---

## ✅ Example Workflow

1️⃣ Input Prompt → Example: “The rise of AI in everyday life”  
2️⃣ Flowchart Planner drafts a logical video structure → you approve or revise it.  
3️⃣ Research Agent gathers insights → Script Agent writes narration → Visual Agent drafts scene prompts.  
4️⃣ Review & Evaluation Agents check quality.  
5️⃣ Stable Diffusion generates scene images → gTTS creates narration audio.  
6️⃣ OpenCV + FFmpeg combine everything → final .mp4 video output.

---

## 🗂️ Outputs

outputs/ → Flowchart, research, script, visuals text files  
video_assets/ → Generated images, narration audio, final video

---

## 🌟 Future Improvements

- Use more advanced text-to-image models (SDXL, DALL·E 3, MidJourney)  
- Use realistic AI voice tools (ElevenLabs, Google Cloud TTS)  
- Add background music, video transitions, and subtitles  
- Deploy as a Streamlit or FastAPI web app
- 
---



## 🧑‍💻 Author

Kumar Gaurav

---

Ready to turn your ideas into videos with the power of agents and AI? Start now! 🚀
