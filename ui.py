import streamlit as st
import services
from styles import CUSTOM_CSS

def apply_custom_css():
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

def sidebar_info():
    with st.sidebar:
        st.image("sentient.jpg", use_container_width=True)
        st.markdown("## 🤖 Sentient educator")
        st.markdown("*learn about sentient*")

        # Display flashcard score if there is any
        if st.session_state.flashcard_score["total"] > 0:
            score = st.session_state.flashcard_score
            percentage = round((score["correct"] / score["total"]) * 100)
            st.markdown("### 📊 Learning Progress")
            st.markdown(f"""
            <div class="score-display">
                <strong>Score: {score["correct"]}/{score["total"]}</strong><br>
                <strong>Accuracy: {percentage}%</strong>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("### 🛠️ Quick Actions")
        if st.button("🔄 Reset Chat History", use_container_width=True):
            st.session_state.chat_history = []
            st.success("Chat history cleared!")
            st.rerun()

        if st.button("📈 Reset Flashcard Score", use_container_width=True):
            st.session_state.flashcard_score = {"correct": 0, "total": 0}
            st.success("Flashcard score reset!")
            st.rerun()

def chat_interface(db):
    st.markdown("## 💬 Chat with Dobby")
    st.markdown("*Ask me anything about Sentient and its AI, Dobby*")

    # Display chat history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input field
    if prompt := st.chat_input("Ask me about Sentient..."):
        # user message to history and display it
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate and display assistant's response
        with st.chat_message("assistant"):
            response = services.generate_rag_response(prompt, db)
            st.markdown(response)
        
        # Add assistant response to history
        st.session_state.chat_history.append({"role": "assistant", "content": response})

def flashcard_interface(db):
    st.markdown("## 🎴 Knowledge Flashcards")
    st.markdown("*Test your knowledge about Sentient*")

    # Display current score
    score = st.session_state.flashcard_score
    if score["total"] > 0:
        percentage = round((score["correct"] / score["total"]) * 100)
        st.markdown(f"""
        <div class="score-display">
            <h3>📊 Your Progress</h3>
            <h2>{score["correct"]}/{score["total"]} correct ({percentage}%)</h2>
        </div>
        """, unsafe_allow_html=True)

    # Button to generate new flashcards
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🎲 Generate New Flashcards", use_container_width=True, type="primary"):
            with st.spinner("Creating personalized flashcards..."):
                st.session_state.generated_flashcards = services.generate_flashcards(db, 5)
                st.session_state.current_flashcard_index = 0
                st.session_state.show_definition = False
                if st.session_state.generated_flashcards:
                    st.success(f"✅ Generated {len(st.session_state.generated_flashcards)} new flashcards!")
                st.rerun()

    flashcards = st.session_state.generated_flashcards
    
    if flashcards:
        # Logic to display and navigate flashcards
        current_index = st.session_state.current_flashcard_index
        current_card = flashcards[current_index]

        st.markdown(f'<div class="flashcard-progress">Flashcard {current_index + 1} of {len(flashcards)}</div>', unsafe_allow_html=True)

        if not st.session_state.show_definition:
            # Display the question side of the flashcard
            st.markdown(f'<div class="flashcard"><div><h2>❓ Question</h2><h3>{current_card["question"]}</h3></div></div>', unsafe_allow_html=True)
            if st.button("🔄 Show Answer", use_container_width=True):
                st.session_state.show_definition = True
                st.rerun()
        else:
            # Display the answer side of the flashcard
            st.markdown(f'<div class="flashcard-answer"><div><h2>✅ Answer</h2><p>{current_card["answer"]}</p></div></div>', unsafe_allow_html=True)
            st.markdown("**How did you do?**")
            c1, c2 = st.columns(2)
            if c1.button("✅ I knew it!", type="primary", use_container_width=True):
                st.session_state.flashcard_score["correct"] += 1
                st.session_state.flashcard_score["total"] += 1
                if current_index < len(flashcards) - 1:
                    st.session_state.current_flashcard_index += 1
                    st.session_state.show_definition = False
                st.rerun()
            if c2.button("❌ Need to review", use_container_width=True):
                st.session_state.flashcard_score["total"] += 1
                if current_index < len(flashcards) - 1:
                    st.session_state.current_flashcard_index += 1
                    st.session_state.show_definition = False
                st.rerun()
    else:
        # Initial message when no flashcards are generated yet
        st.markdown("""
        <div class="flashcard">
            <div>
                <h2>🚀 Ready to test your knowledge?</h2>
                <p>Click "Generate New Flashcards" to create personalized questions based on the Sentient documentation!</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

def render_mode_selection():
    st.markdown("## 🎯 Choose Your Learning Mode")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### 💬 Interactive Chat
        Ask questions and get detailed answers about the Sentient project.
        """)
        if st.button("Start Chatting", use_container_width=True, type="primary"):
            st.session_state.app_mode = 'chat'
            st.rerun()
    with col2:
        st.markdown("""
        ### 🎴 Knowledge Flashcards  
        Test your understanding with flashcards and track your progress.
        """)
        if st.button("Generate Flashcards", use_container_width=True, type="secondary"):
            st.session_state.app_mode = 'flashcards'
            st.rerun()
