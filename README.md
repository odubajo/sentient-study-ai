🤖 Sentient AI Assistant
Welcome to the Sentient AI Assistant! This is a Streamlit web application that I (discord: .qoyyum) built, serving as a knowledge exploration tool for the Sentient crypto AI project. It leverages a powerful combination of Google's Gemini Pro and a local FAISS vector database to provide users with two main learning modes: an interactive chat and a flashcard generation system.

The application is designed with a futuristic, cyberpunk-inspired UI to create an engaging user experience.

✨ Features
🧠 Intelligent Chat Assistant: Engage in a conversation with "Dobby," an AI assistant that answers questions about the Sentient project. It uses its general knowledge, augmented and verified by specific information from a local knowledge base.

🎴 Dynamic Flashcards: Automatically generate educational flashcards based on the project's documentation to test and improve your knowledge.

📊 Progress Tracking: The app keeps track of your flashcard score, showing your accuracy and the number of questions answered.

🎨 Custom UI: A sleek, custom-styled interface with futuristic animations and a dark theme.

📁 Local Knowledge Base: Utilizes a FAISS vector store (faiss_index folder) to perform fast, local similarity searches for Retrieval-Augmented Generation (RAG).

🛠️ Tech Stack
Frontend: Streamlit

LLM: Google Gemini Pro

Vector Database: FAISS (Facebook AI Similarity Search)

Embeddings: Hugging Face Sentence Transformers

API Communication: Requests

Environment Management: python-dotenv

