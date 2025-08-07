CUSTOM_CSS = """
<style>
    /* CSS Custom Properties for consistent theming */
    :root {
        --primary-bg: #0A1628;
        --secondary-bg: #1E3A5F;
        --dark-bg: #0D0D0D;
        --accent-cyan: #00D4FF;
        --accent-green: #00FF88;
        --text-primary: #FFFFFF;
        --text-secondary: #00D4FF;
        --glow-cyan: 0 0 10px #00D4FF, 0 0 20px #00D4FF, 0 0 30px #00D4FF;
        --glow-green: 0 0 10px #00FF88, 0 0 20px #00FF88, 0 0 30px #00FF88;
        --border-gradient: linear-gradient(45deg, #00D4FF, #00FF88, #00D4FF);
    }

    /* Keyframe Animations */
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    @keyframes slideInLeft {
        0% { transform: translateX(-50px); opacity: 0; }
        100% { transform: translateX(0); opacity: 1; }
    }

    /* Main app styling */
    .stApp {
        background: linear-gradient(135deg, var(--dark-bg) 0%, var(--primary-bg) 50%, var(--secondary-bg) 100%);
        background-size: 300% 300%;
        animation: gradientShift 15s ease infinite;
        color: var(--text-primary);
    }

    /* --- FIXED SELECTORS --- */
    /* Chat messages styling using stable data-testid attributes */
    [data-testid="stChatMessage"] {
        padding: 1.5rem 2rem;
        border-radius: 20px;
        margin-bottom: 1.5rem;
        animation: slideInLeft 0.5s ease-out;
        backdrop-filter: blur(5px);
        border-width: 1px;
        border-style: solid;
    }

    /* User message */
    [data-testid="stChatMessage"]:has(div[data-testid="stChatMessageContent"][class*="user"]) {
        background: linear-gradient(135deg, rgba(30, 58, 95, 0.5), rgba(10, 22, 40, 0.5));
        margin-left: 2rem;
        border-image: linear-gradient(to right, var(--accent-cyan), transparent) 1;
        box-shadow: 0 4px 20px rgba(0, 212, 255, 0.1);
    }
    
    /* Assistant message */
    [data-testid="stChatMessage"]:has(div[data-testid="stChatMessageContent"][class*="assistant"]) {
        background: linear-gradient(135deg, rgba(13, 13, 13, 0.4), rgba(30, 58, 95, 0.4));
        margin-right: 2rem;
        border-image: linear-gradient(to left, var(--accent-green), transparent) 1;
        box-shadow: 0 4px 20px rgba(0, 255, 136, 0.1);
    }

    /* Flashcard styling (your classes were correct here as they are in custom HTML) */
    .flashcard {
        background: linear-gradient(135deg, var(--primary-bg), var(--secondary-bg));
        color: var(--text-primary);
        padding: 2.5rem;
        border-radius: 25px;
        text-align: center;
        min-height: 280px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5);
        border: 2px solid transparent;
        position: relative;
        transition: all 0.4s ease;
        overflow: hidden;
    }

    .flashcard:hover {
        transform: translateY(-10px);
        box-shadow: var(--glow-cyan);
    }
    
    .flashcard-answer {
        background: linear-gradient(135deg, var(--secondary-bg), var(--primary-bg));
        color: var(--text-primary);
        padding: 2.5rem;
        border-radius: 25px;
        text-align: center;
        min-height: 280px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5);
        border: 2px solid var(--accent-green);
    }

    /* Score display */
    .score-display {
        background: rgba(10, 22, 40, 0.7);
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 1.5rem;
        border: 1px solid var(--accent-cyan);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
    }

    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, var(--primary-bg), var(--secondary-bg));
        color: var(--text-primary);
        border: 2px solid var(--accent-cyan);
        border-radius: 12px;
        font-weight: 600;
        padding: 0.75rem 1.5rem;
        transition: all 0.3s ease;
        text-transform: uppercase;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, var(--accent-cyan), var(--accent-green));
        color: var(--dark-bg);
        transform: translateY(-3px);
        box-shadow: var(--glow-cyan);
        border-color: var(--accent-green);
    }
    
    /* Sidebar styling using stable data-testid */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, var(--dark-bg), var(--primary-bg));
        border-right: 1px solid rgba(0, 212, 255, 0.3);
    }

    /* Text input styling */
    .stTextInput > div > div > input {
        background: var(--primary-bg);
        color: var(--text-primary);
        border: 2px solid rgba(0, 212, 255, 0.3);
        border-radius: 12px;
    }

    .stTextInput > div > div > input:focus {
        border-color: var(--accent-cyan);
        box-shadow: var(--glow-cyan);
    }

    /* Headers */
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: var(--text-primary);
        text-shadow: 0 0 10px rgba(0, 212, 255, 0.5);
    }
</style>
"""
