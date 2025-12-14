🚀 AI‑Powered Personalized Learning Mentor with Adaptive Assessments
TEAM‑133 — DATA DETECTIVES
GenAI Hackathon Project

📘 Project Overview
Traditional education often follows a one‑size‑fits‑all model. Students learn at different speeds and face unique challenges, while teachers cannot personalize learning for every student.

This project introduces an AI‑Powered Personalized Learning Mentor that:

Understands student learning behavior

Generates simplified concept explanations

Builds adaptive assessments

Tracks progress and recommends next topics

It works like a 24×7 intelligent personal tutor.

🎯 Problem Statement
Students often struggle with:

Complex concepts

Lack of personalized guidance

No adaptive assessments

Difficulty identifying weak areas

Teachers cannot scale personalized learning for every student.

📌 Our AI mentor adapts to each student's needs and fills this gap.

💡 Proposed Solution
The system uses GenAI + RAG (Retrieval-Augmented Generation) + Adaptive Evaluation to deliver a personalized learning experience.

🔹 Intelligent Concept Understanding (RAG)
Reads learning material

Splits it into meaningful chunks

Retrieves relevant content for answers

🔹 Adaptive Assessment Engine
Generates personalized quizzes

Adjusts difficulty automatically

Provides step-by-step explanations

🔹 Student Progress Insights
Detects weak areas

Suggests what to study next

Enhances learning effectiveness

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
Chunks the content

Generates embeddings

Stores vectors in ChromaDB

3️⃣ Students Ask Questions
AI retrieves context and explains topics in simple language.

4️⃣ AI Generates Adaptive Assessments
Personalized quiz generation

Automatic difficulty adjustment

Feedback‑rich answers

5️⃣ Tracks Student Progress
Recommends next topics based on performance.
