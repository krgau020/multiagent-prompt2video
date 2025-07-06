

# import os
# from crewai import Task
# from agents import (
#     research_agent,
#     script_agent,
#     visual_agent,
#     flowchart_agent,
#     review_agent,
#     evaluation_agent,
#     video_generator_agent
# )
# from tools import VideoGeneratorTool

# output_dir = "outputs"
# os.makedirs(output_dir, exist_ok=True)

# video_tool = VideoGeneratorTool()

# research_task = Task(
#     description="Research the topic '{topic}' and break it down into key subtopics and facts.",
#     expected_output="List of 4-6 subtopics and insights related to the main topic.",
#     agent=research_agent,
#     output_file=os.path.join(output_dir, "01_research_output.txt")
# )

# script_task = Task(
#     description=(
#         "Using the researched subtopics on '{topic}', write a well-structured video script "
#         "in the format:\n\n"
#         "- Start with an engaging intro\n"
#         "- Add informative narration broken into sections\n"
#         "- Mark each line spoken by narrator using: Narrator: <text>\n"
#         "- Ensure the script flows logically and ends with a conclusion"
#     ),
#     expected_output="An engaging, informative video script with all lines prefixed as 'Narrator:'.",
#     agent=script_agent,
#     output_file=os.path.join(output_dir, "02_script_output.txt")
# )

# visual_task = Task(
#     description=(
#         "Based on the script for '{topic}', generate visual scene descriptions.\n"
#         "- For every scene or narration segment, provide a corresponding visual prompt.\n"
#         "- Format each visual using this style: **(Visual: description of the scene)**"
#     ),
#     expected_output="A list of visual prompts matching each part of the script, each formatted as '**(Visual: ...)**'.",
#     agent=visual_agent,
#     output_file=os.path.join(output_dir, "03_visuals_output.txt")
# )

# flowchart_task = Task(
#     description="Create a logical flowchart for the video content on the topic '{topic}'.",
#     expected_output="A sequence of steps in bullet or markdown format representing the video plan.",
#     agent=flowchart_agent,
#     output_file=os.path.join(output_dir, "00_flowchart_output.txt")
# )

# review_task = Task(
#     description="Review the script, visuals, and flowchart for topic '{topic}' for completeness and accuracy.",
#     expected_output="Feedback and corrections, or a statement that all content is approved.",
#     agent=review_agent,
#     output_file=os.path.join(output_dir, "04_review_output.txt")
# )

# evaluation_task = Task(
#     description=(
#         "You are evaluating a video script and its corresponding visuals. "
#         "Provide a comprehensive assessment that includes:\n"
#         "- An overall rating out of 10\n"
#         "- Strengths of the content and visuals\n"
#         "- Weaknesses or areas needing improvement\n"
#         "- Specific, actionable suggestions to enhance the video's quality, creativity, and engagement"
#     ),
#     expected_output="A structured review covering rating, feedback, strengths, weaknesses, and improvement suggestions.",
#     agent=evaluation_agent,
#     output_file=os.path.join(output_dir, "05_evaluation_output.txt")
# )

# video_generation_task = Task(
#     description=(
#         "Use the reviewed script and visuals for '{topic}' to simulate a final video output.\n"
#         "- Include a summary of the narrator's script\n"
#         "- Include a summary of visual scenes\n"
#         "- Simulate the video output as a preview"
#     ),
#     expected_output="A mock video output including script preview and visuals summary.",
#     agent=video_generator_agent,
#     tools=[video_tool],
#     output_file=os.path.join(output_dir, "06_final_video_output.txt")
# )











import os
from crewai import Task
from agents import (
    research_agent,
    script_agent,
    visual_agent,
    flowchart_agent,
    review_agent,
    evaluation_agent,
    video_generator_agent
)
from tools import VideoGeneratorTool

# Directory to store output files
output_dir = "outputs"
os.makedirs(output_dir, exist_ok=True)

# Initialize the video generation tool
video_tool = VideoGeneratorTool()

# Task 1: Research
research_task = Task(
    description="Research the topic '{topic}' and break it down into key subtopics and facts.",
    expected_output="A list of 4-6 subtopics and insights related to the main topic.",
    agent=research_agent,
    output_file=os.path.join(output_dir, "01_research_output.txt")
)

# Task 2: Script Writing
script_task = Task(
    description=(
        "Using the researched subtopics on '{topic}', write a well-structured video script.\n"
        "Format:\n"
        "- Start with an engaging introduction.\n"
        "- Provide informative narration broken into sections.\n"
        "- Prefix each line spoken by the narrator with 'Narrator: '.\n"
        "- Ensure the script flows logically and concludes effectively."
    ),
    expected_output="An engaging, informative video script with all narration lines prefixed by 'Narrator: '.",
    agent=script_agent,
    output_file=os.path.join(output_dir, "02_script_output.txt")
)

# Task 3: Visual Planning
visual_task = Task(
    description=(
        "Based on the script for '{topic}', generate visual scene descriptions.\n"
        "For each narration segment:\n"
        "- Include the narrator's text.\n"
        "- Provide a corresponding visual prompt.\n"
        "Format:\n"
        "Narrator: <narration text>\n"
        "Visual: <description of the visual scene>"
    ),
    expected_output="A list of narration segments with corresponding visual prompts, each formatted as 'Narrator: ...' followed by 'Visual: ...'.",
    agent=visual_agent,
    output_file=os.path.join(output_dir, "03_visuals_output.txt")
)

# Task 4: Flowchart Creation
flowchart_task = Task(
    description="Create a logical flowchart for the video content on the topic '{topic}'.",
    expected_output="A sequence of steps in bullet or markdown format representing the video plan.",
    agent=flowchart_agent,
    output_file=os.path.join(output_dir, "00_flowchart_output.txt")
)

# Task 5: Content Review
review_task = Task(
    description="Review the script, visuals, and flowchart for the topic '{topic}' for completeness and accuracy.",
    expected_output="Feedback and corrections, or a statement that all content is approved.",
    agent=review_agent,
    output_file=os.path.join(output_dir, "04_review_output.txt")
)

# Task 6: Evaluation
evaluation_task = Task(
    description=(
        "Evaluate the video script and its corresponding visuals.\n"
        "Provide a comprehensive assessment that includes:\n"
        "- An overall rating out of 10.\n"
        "- Strengths of the content and visuals.\n"
        "- Weaknesses or areas needing improvement.\n"
        "- Specific, actionable suggestions to enhance the video's quality, creativity, and engagement."
    ),
    expected_output="A structured review covering rating, feedback, strengths, weaknesses, and improvement suggestions.",
    agent=evaluation_agent,
    output_file=os.path.join(output_dir, "05_evaluation_output.txt")
)

# Task 7: Video Generation
video_generation_task = Task(
    description=(
        "Use the reviewed script and visuals for '{topic}' to simulate a final video output.\n"
        "Include:\n"
        "- A summary of the narrator's script.\n"
        "- A summary of visual scenes.\n"
        "- A simulated video output as a preview."
    ),
    expected_output="A mock video output including a script preview and visuals summary.",
    agent=video_generator_agent,
    tools=[video_tool],
    output_file=os.path.join(output_dir, "06_final_video_output.txt")
)
