🚀 AI‑Powered Personalized Learning Mentor with Adaptive Assessments
TEAM‑133 — DATA DETECTIVES
GenAI Hackathon Project

📘 Project Overview
Traditional education often follows a one‑size‑fits‑all approach. Students learn at different speeds, have different strengths, and struggle with concepts that others may find easy.

Teachers cannot provide personalized learning paths or adaptive assessments to every student due to time and workload constraints.

Our project solves this with an AI‑Powered Personalized Learning Mentor that:

✔ Understands student learning patterns
✔ Generates tailored explanations
✔ Adapts assessments based on student performance
✔ Helps students improve continuously using AI insights
This mentor behaves like a personal tutor, available anytime.

🎯 Problem Statement
Students face challenges such as:

Difficulty understanding complex concepts

Lack of personalized guidance

No adaptive assessments based on their performance

Reduced motivation when they fall behind

Teachers cannot scale personalized feedback to all students.

📌 There is a need for an intelligent mentor system that personalizes learning and dynamically evaluates student progress.

💡 Proposed Solution
We build a GenAI‑powered Personalized Learning Mentor with:

🔹 Retrieval‑Augmented Generation (RAG)
Extracts concepts from learning material

Retrieves relevant content to answer questions

Provides simplified explanations

🔹 Adaptive Assessment Engine
Creates quizzes tailored to student strengths/weaknesses

Adjusts difficulty based on performance

Gives step‑by‑step solutions

🔹 Progress Tracking System
Identifies weak topics

Recommends next lessons

Shows improvement over time

🔹 Motivational & Personalized Feedback
AI mentor encourages, coaches, and supports the learner

🧠 Tech Stack
⚙️ Core Technologies
Python

Google Colab

LangChain 0.1.x

ChromaDB (Vector Store)

HuggingFace Transformers

FLAN‑T5 (LLM)

MiniLM‑L6‑v2 Embedding Model

📦 Additional Libraries
Sentence‑Transformers

NumPy

SciPy

Pydantic v1

📂 Project Structure
TEAM-133-DATA_DETECTIVES/
│── notebooks/
│     └── adaptive_learning_rag.ipynb
│
│── src/
│     ├── data/
│     │     └── learning_material.txt
│     └── models/
│           └── rag_pipeline.py
│
│── README.md
│── GUIDELINES.md
│── requirements.txt
🛠️ How the System Works
1️⃣ Upload Learning Material
The model processes textbooks, notes, or custom text content.

2️⃣ RAG Pipeline Understands Concepts
Splits text into semantic chunks

Generates vector embeddings

Stores them in ChromaDB for retrieval

3️⃣ Student Asks Questions
The mentor retrieves relevant chunks + generates context‑aware explanations.

4️⃣ AI Generates Adaptive Assessments
Creates personalized quizzes

Adjusts difficulty automatically

Provides corrective feedback

5️⃣ Tracks Student Progress
Continuously monitors weak areas and recommends what to learn next.
