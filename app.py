import streamlit as st
import utils
import ui

def main():
    st.set_page_config(
        page_title="Sentient AI Assistant",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    utils.initialize_session_state()
    ui.apply_custom_css()

    st.markdown("# 🤖 Sentient Assistant")
    st.markdown("*what do you want to know about sentient?*")
    ui.sidebar_info()

    db = utils.get_vector_db()
    if not db:
        st.error("❌ Cannot proceed without vector database. Please check the setup instructions in README.md.")
        st.stop()

    if st.session_state.app_mode is None:
        ui.render_mode_selection()
    else:
        if st.button("⬅️ Back to Menu"):
            st.session_state.app_mode = None
            st.rerun()

        if st.session_state.app_mode == 'chat':
            ui.chat_interface(db)
        elif st.session_state.app_mode == 'flashcards':
            ui.flashcard_interface(db)

if __name__ == "__main__":
    main()
