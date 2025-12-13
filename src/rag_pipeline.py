import os
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import OpenAI
from langchain.chains import RetrievalQA


# ------------------------------------------------------------
# 1. Load API Key
# ------------------------------------------------------------
# Make sure to set your environment variable before running:
# export OPENAI_API_KEY="your_api_key"
# OR uncomment below and paste your key directly (NOT recommended for GitHub)

# os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY_HERE"


# ------------------------------------------------------------
# 2. Load Learning Material
# ------------------------------------------------------------
def load_learning_material(path="data/learning_material.txt"):
    with open(path, "r", encoding="utf-8") as f:
        data = f.read()
    return data


# ------------------------------------------------------------
# 3. Prepare Text Chunks
# ------------------------------------------------------------
def create_chunks(text):
    splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=300,
        chunk_overlap=50
    )
    return splitter.split_text(text)


# ------------------------------------------------------------
# 4. Create Vector Database (Chroma)
# ------------------------------------------------------------
def create_vector_db(chunks):
    embeddings = OpenAIEmbeddings()
    vectordb = Chroma.from_texts(chunks, embedding=embeddings)
    return vectordb.as_retriever()


# ------------------------------------------------------------
# 5. Build the RAG Model
# ------------------------------------------------------------
def build_rag_model(retriever):
    llm = OpenAI(temperature=0)
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever
    )
    return qa


# ------------------------------------------------------------
# 6. Adaptive Assessment Logic
# ------------------------------------------------------------
def adaptive_question(qa_model, student_correct):
    if student_correct:
        prompt = "Give me a harder question about this topic."
    else:
        prompt = "Give me an easier question with explanation."

    return qa_model.run(prompt)


# ------------------------------------------------------------
# 7. Demo Run
# ------------------------------------------------------------
if __name__ == "__main__":
    print("🔹 Loading learning material...")
    text = load_learning_material()

    print("🔹 Creating text chunks...")
    chunks = create_chunks(text)

    print("🔹 Creating vector database...")
    retriever = create_vector_db(chunks)

    print("🔹 Building RAG QA system...")
    rag_model = build_rag_model(retriever)

    print("\n📘 Example Query:")
    query = "Explain photosynthesis in simple words."
    answer = rag_model.run(query)
    print("AI Answer:", answer)

    print("\n📘 Adaptive Question Example:")
    print(adaptive_question(rag_model, student_correct=False))

