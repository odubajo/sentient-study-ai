import streamlit as st
import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

def initialize_session_state():
    defaults = {
        "chat_history": [],
        "app_mode": None,
        "generated_flashcards": [],
        "current_flashcard_index": 0,
        "show_definition": False,
        "flashcard_score": {"correct": 0, "total": 0}
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

@st.cache_resource
def get_vector_db():
    DB_FOLDER_PATH = "faiss_index"

    if not os.path.exists(DB_FOLDER_PATH):
        st.error(f"Vector database folder '{DB_FOLDER_PATH}' not found!")
        return None

    required_files = ["index.faiss", "index.pkl"]
    missing_files = [f for f in required_files if not os.path.exists(os.path.join(DB_FOLDER_PATH, f))]

    if missing_files:
        st.error(f"📁 Missing files in '{DB_FOLDER_PATH}': {', '.join(missing_files)}")
        return None

    try:
        with st.spinner("🔄 Loading vector database..."):
            embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
            vector_db = FAISS.load_local(
                folder_path=DB_FOLDER_PATH,
                embeddings=embedding_model,
                allow_dangerous_deserialization=True
            )
        st.success("Vector database loaded successfully!")
        return vector_db
    except Exception as e:
        st.error(f"Error loading vector database: {e}")
        st.info("Try regenerating the database with the PDF processing script.")
        return None