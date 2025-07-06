
# ### ask for approval after creating flow chart, if not accepted, it will also aske for  change needed.


import os
from crewai import Crew, Process, Task
from tasks import (
    research_task,
    script_task,
    visual_task,
    review_task,
    evaluation_task,
    video_generation_task
)
from agents import (
    research_agent,
    script_agent,
    visual_agent,
    flowchart_agent,
    review_agent,
    evaluation_agent,
    video_generator_agent
)
from dotenv import load_dotenv
import shutil

load_dotenv()

# 📥 Ask user for input
print("🎯 Welcome to the Agentic Video Generator!")
topic = input("Enter a topic for your video: ").strip()
if topic == "":
    topic = "How to make a smoothie"  # fallback default

# ✅ Ensure output folder exists
output_folder = "outputs"
os.makedirs(output_folder, exist_ok=True)

# 🔁 FLOWCHART APPROVAL LOOP
approved = False
flowchart_round = 0
previous_flowchart = ""

while not approved:
    temp_output_path = os.path.join(output_folder, f"00_flowchart_output_{flowchart_round}.txt")

    if flowchart_round == 0:
        description = f"Create a logical flowchart for the video content based on the topic: {topic}"
    else:
        description = (
            f"You are revising the following previous flowchart:\n\n"
            f"{previous_flowchart}\n\n"
            f"Please improve it based on this feedback: {feedback}"
        )

    flowchart_task = Task(
        description=description,
        expected_output="A revised bullet or markdown-style video structure flowchart.",
        agent=flowchart_agent,
        output_file=temp_output_path
    )

    print("\n📌 [STEP 1] Generating Flowchart...")
    flowchart_crew = Crew(
        agents=[flowchart_agent],
        tasks=[flowchart_task],
        process=Process.sequential,
        verbose=True
    )
    flowchart_result = flowchart_crew.kickoff(inputs={"topic": topic})

    with open(temp_output_path, "w", encoding="utf-8") as f:
        f.write(flowchart_result)

    print(f"\n📋 Generated Flowchart:\n{flowchart_result}")
    approval = input("\n✅ Do you approve this flowchart? (yes/no): ").strip().lower()

    if approval == "yes":
        # ✅ Save the approved version as the main flowchart file
        final_flowchart_path = os.path.join(output_folder, "00_flowchart_output.txt")
        shutil.copy(temp_output_path, final_flowchart_path)
        approved = True
    else:
        feedback = input("🛠️ What would you like to change or improve in the flowchart?\n> ")
        previous_flowchart = flowchart_result
        flowchart_round += 1

# 🧠 Main crew with remaining tasks
crew = Crew(
    agents=[
        research_agent,
        script_agent,
        visual_agent,
        review_agent,
        evaluation_agent,
        video_generator_agent
    ],
    tasks=[
        research_task,
        script_task,
        visual_task,
        review_task,
        evaluation_task,
        video_generation_task
    ],
    process=Process.sequential,
    verbose=True
)

# 🚀 Run the rest of the pipeline
result = crew.kickoff(inputs={"topic": topic})

# 📂 Generate README summarizing all outputs
readme_path = os.path.join(output_folder, "README.md")

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(f"# 📽️ Agentic Video Generator Output\n\n")
    f.write(f"**Topic:** `{topic}`\n\n")
    f.write(f"## Generated Outputs\n")
    for filename in sorted(os.listdir(output_folder)):
        if filename.endswith(".txt"):
            f.write(f"- [{filename}](./{filename})\n")
    f.write(f"\n_This README was auto-generated._\n")

print("\n✅ All tasks complete. Check the 'outputs/' folder for results.")

















############3FULLY automated --> no review from person






# import os
# from crewai import Crew, Process, Task
# from tasks import (
#     research_task,
#     script_task,
#     visual_task,
#     review_task,
#     evaluation_task,
#     video_generation_task
# )
# from agents import (
#     research_agent,
#     script_agent,
#     visual_agent,
#     flowchart_agent,
#     review_agent,
#     evaluation_agent,
#     video_generator_agent
# )
# from dotenv import load_dotenv

# load_dotenv()

# # 📥 Ask user for input
# print("🎯 Welcome to the Agentic Video Generator (Automated)!")
# topic = input("Enter a topic for your video: ").strip()
# if topic == "":
#     topic = "How to make a smoothie"  # fallback default

# # ✅ Ensure output folder exists
# output_folder = "outputs"
# os.makedirs(output_folder, exist_ok=True)

# # ✅ Generate flowchart without manual approval
# flowchart_output_path = os.path.join(output_folder, "00_flowchart_output.txt")
# flowchart_description = f"Create a logical flowchart for the video content based on the topic: {topic}"

# flowchart_task = Task(
#     description=flowchart_description,
#     expected_output="A bullet or markdown-style sequence showing the logical video structure.",
#     agent=flowchart_agent,
#     output_file=flowchart_output_path
# )

# print("\n📌 [STEP 1] Generating Flowchart Automatically...")
# flowchart_crew = Crew(
#     agents=[flowchart_agent],
#     tasks=[flowchart_task],
#     process=Process.sequential,
#     verbose=True
# )
# flowchart_result = flowchart_crew.kickoff(inputs={"topic": topic})

# with open(flowchart_output_path, "w", encoding="utf-8") as f:
#     f.write(flowchart_result)

# # 🧠 Main crew with remaining tasks
# crew = Crew(
#     agents=[
#         research_agent,
#         script_agent,
#         visual_agent,
#         review_agent,
#         evaluation_agent,
#         video_generator_agent
#     ],
#     tasks=[
#         research_task,
#         script_task,
#         visual_task,
#         review_task,
#         evaluation_task,
#         video_generation_task
#     ],
#     process=Process.sequential,
#     verbose=True
# )

# # 🚀 Run the rest of the pipeline
# result = crew.kickoff(inputs={"topic": topic})

# # 📂 Generate README summarizing all outputs
# readme_path = os.path.join(output_folder, "README.md")

# with open(readme_path, "w", encoding="utf-8") as f:
#     f.write(f"# 📽️ Agentic Video Generator Output (Automated)\n\n")
#     f.write(f"**Topic:** `{topic}`\n\n")
#     f.write(f"## Generated Outputs\n")
#     for filename in sorted(os.listdir(output_folder)):
#         if filename.endswith(".txt"):
#             f.write(f"- [{filename}](./{filename})\n")
#     f.write(f"\n_This README was auto-generated._\n")

# print("\n✅ All tasks complete. Check the 'outputs/' folder for results.")
