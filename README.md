# AI-Powered Personalized Learning Mentor with Adaptive Assessments

## Problem Statement
In traditional education systems, students follow the same learning path regardless of
their individual learning speed, strengths, or weaknesses. Teachers are often unable to
provide personalized feedback and adaptive assessments due to time and scale constraints.
As a result, many students struggle to understand concepts effectively and lose motivation.

There is a need for an intelligent system that can personalize learning content, continuously
assess student understanding, and adapt assessments based on individual performance.

---

## Proposed Solution
This project proposes an **AI-Powered Personalized Learning Mentor** that leverages
**Generative AI and Machine Learning** to provide adaptive learning support.

The system:
- Acts as a virtual mentor available 24/7
- Uses **Retrieval-Augmented Generation (RAG)** to answer questions from trusted
  educational content
- Generates personalized explanations and practice questions
- Conducts adaptive assessments based on student performance
- Identifies learning gaps and recommends focused revision topics

---

## System Design / Architecture
**Workflow:**
1. Student inputs a query or selects a learning topic
2. Relevant learning materials are retrieved using embeddings (RAG)
3. A Large Language Model generates a personalized explanation
4. Adaptive assessment questions are generated
5. Student responses are evaluated to adjust difficulty levels

**Core Components:**
- LLM (OpenAI / Gemini / Local LLM)
- Embedding model
- Vector Database (ChromaDB / FAISS)
- LangChain for orchestration
- Python-based backend (Notebook / FastAPI)

---

## Technologies Used
- Python
- Generative AI (LLMs)
- LangChain
- Retrieval-Augmented Generation (RAG)
- Embeddings
- ChromaDB / FAISS
- Jupyter Notebook / FastAPI

---

## Data Sources
- Public educational datasets
- Open-source textbooks and learning materials
- Sample Q&A datasets for assessment generation  
*(Dataset links will be updated)*

---

## Assumptions
- Users have basic internet access
- Educational content used is publicly available
- The system supports learning assistance only
- Outputs are advisory and not a replacement for teachers

---

## Evaluation & Guardrails
- RAG is used to reduce hallucinations
- Prompt constraints ensure educational relevance
- Manual test cases to evaluate answer accuracy
- Limitations are documented for transparency

---

## Expected Impact
- Improves personalized learning outcomes
- Helps students learn at their own pace
- Reduces teacher workload
- Encourages continuous self-assessment and improvement

---

## Future Enhancements
- Multilingual support
- Voice-based learning interaction
- Student performance analytics dashboard
- Integration with LMS platforms
