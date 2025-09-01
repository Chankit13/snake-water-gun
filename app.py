
import streamlit as st
import game  

st.title("🐍 Snake - 🌊 Water - 🔫 Gun")

# Radio buttons for user choice
choice_map = {"Snake 🐍": "s", "Water 🌊": "w", "Gun 🔫": "g"}
user_choice = st.radio("Choose your option:", list(choice_map.keys()))

if st.button("Play"):
    # Call your original game logic
    result = game.play(choice_map[user_choice])

    if "error" in result:
        st.error(result["error"])
    else:
        st.write(f"**You chose:** {result['user_choice']}")
        st.write(f"**Bot chose:** {result['bot_choice']}")
        st.success(result["outcome"])
