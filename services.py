import streamlit as st
import json
import random
from api_client import call_gemini_api

def generate_rag_response(user_query: str, db) -> str:
    if db is None:
        return "Knowledge base is not available."

    try:
        # 1. Search the vector database for relevant documents
        with st.spinner("Searching knowledge base..."):
            relevant_docs = db.similarity_search(user_query, k=4) 

        context = ""
        if relevant_docs:
            context = "\n\n".join([f"Document {i+1}:\n{doc.page_content}"
                                  for i, doc in enumerate(relevant_docs)])

        # 2. Create a new, more advanced prompt
        prompt = f"""You are an expert AI assistant with extensive knowledge about technology, AI, and cryptocurrency projects. Your task is to answer the user's question comprehensively.

First, draw upon your own built-in knowledge to formulate an answer.
Then, carefully review the following context, which is from the Sentient project's specific knowledge base. Use this context to add specific details, correct any of your own outdated information, and enhance your response.

If the context is empty or not relevant, rely solely on your own knowledge. Your final answer should be a synthesis of your general knowledge and the specific details from the provided context.

Context from the Sentient knowledge base:
---
{context if context else "No specific context found."}
---

User Question: {user_query}

Provide a clear, medium length, and helpful answer:"""

        # 3. Call the Gemini API with the new prompt
        with st.spinner("🤖 Dobby is thinking..."):
            return call_gemini_api(prompt)

    except Exception as e:
        st.error(f"An error occurred while processing your question: {e}")
        return f"An error occurred: {e}"

def generate_flashcards(db, num_flashcards: int = 5) -> list:
    if db is None:
        return []

    try:
        # Get a random sample of documents to create flashcards from
        all_docs = list(db.docstore._dict.values())
        if not all_docs:
            st.warning("The knowledge base is empty. Cannot generate flashcards.")
            return []
            
        sample_size = min(len(all_docs), num_flashcards * 2)
        selected_docs = random.sample(all_docs, sample_size)

        context = "\n\n---DOCUMENT SEPARATOR---\n\n".join([doc.page_content for doc in selected_docs])

        # Create the prompt for the Gemini API
        prompt = f"""Based on the context provided below about the Sentient crypto AI project, create {num_flashcards} educational flashcards.

Each flashcard should:
- Have a clear, specific question on the front.
- Have a comprehensive and accurate answer on the back.
- Focus on key concepts, technical details, important facts about Sentient or random general knowledge.

Context:
---
{context}
---

Generate exactly {num_flashcards} flashcards in the specified JSON format."""

        # Define the expected JSON schema for the response
        schema = {
            "type": "ARRAY",
            "items": {
                "type": "OBJECT",
                "properties": {
                    "question": {"type": "STRING"},
                    "answer": {"type": "STRING"}
                },
                "required": ["question", "answer"]
            }
        }

        with st.spinner("🎴 Generating flashcards..."):
            response_text = call_gemini_api(prompt, use_json_schema=True, schema=schema)

        try:
            # Attempt to parse the JSON response
            return json.loads(response_text)
        except json.JSONDecodeError:
            st.error("Failed to parse the flashcard response from the API.")
            st.code(response_text) # Show the raw response for debugging
            return []
        except Exception as e:
            st.error(f"An unexpected error occurred while processing flashcards: {e}")
            return []


    except Exception as e:
        st.error(f"Error generating flashcards: {e}")
        return []
