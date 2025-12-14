🚀 AI‑Powered Personalized Learning Mentor with Adaptive Assessments

TEAM‑133 — DATA DETECTIVES
GenAI Hackathon Project

📘 Project Overview
Traditional education often follows a one‑size‑fits‑all model. Students learn at different speeds and face unique challenges, but teachers cannot personalize content for everyone.

Our solution introduces an AI‑Powered Personalized Learning Mentor that:

Understands student learning behavior

Generates simplified concept explanations

Builds adaptive assessments

Tracks progress and recommends next topics

Essentially, it works like a 24×7 intelligent personal tutor.

🎯 Problem Statement
Students often struggle with:

Complex concepts

Lack of personalized guidance

No adaptive assessments

Difficulty identifying weak areas

Teachers cannot scale personalized learning for every student.

📌 This project solves the gap by providing an AI mentor that adapts to each learner.

💡 Proposed Solution
Our system combines GenAI + RAG (Retrieval-Augmented Generation) + Adaptive Evaluation to create a full learning experience.

🔹 Intelligent Concept Understanding (RAG)
Reads learning material

Splits into meaningful chunks

Retrieves context‑relevant sections for answers

🔹 Adaptive Assessment Engine
Generates personalized quizzes

Adjusts difficulty based on performance

Provides step‑by‑step explanations

🔹 Student Progress Insights
Detects weak topics

Suggests what to learn next

Improves learning effectiveness

🧠 Tech Stack
Core Technologies
Python

Google Colab

LangChain (0.1.x)

ChromaDB

HuggingFace Transformers

FLAN‑T5 (LLM)

MiniLM‑L6‑v2 Embedding Model

Supporting Libraries
sentence-transformers

NumPy

SciPy

Torch

Pydantic v1

📂 Project Structure
TEAM-133-DATA_DETECTIVES/
│
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
│── .gitignore
🛠️ How the System Works
1️⃣ Upload Learning Material
The system processes textbooks, notes, or custom text.

2️⃣ RAG Pipeline Understands Concepts
Chunks material

Creates embeddings

Stores in ChromaDB

3️⃣ Students Ask Questions
The system retrieves context and generates simple explanations.

4️⃣ AI Generates Adaptive Assessments
Personalized quizzes

Auto-adjusted difficulty

Feedback‑rich answers

5️⃣ Tracks Student Progress
Recommends topics to focus on based on performance.

