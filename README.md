🐍 Snake-Water-Gun Game
📝 Overview
This is an interactive Snake-Water-Gun game where the user plays against the computer. The game is built in Python with a Streamlit frontend, providing a clean and user-friendly interface. The computer makes random choices, and the outcome (Win, Lose, Draw) is displayed instantly.

It’s a beginner-friendly project to learn randomization, conditional logic, user input handling, and building simple web-based games with Python.

🛠️ Tech Stack
Programming Language: Python 3

Frontend: Streamlit

Randomization: Python random module

Logic: Conditional statements & dictionaries

📂 Game Rules
🐍 Snake vs 🌊 Water: Snake drinks the water → Snake wins

🌊 Water vs 🔫 Gun: Gun sinks in water → Water wins

🔫 Gun vs 🐍 Snake: Gun kills the snake → Gun wins

Same Choice: The game is a Draw 🤝

🚀 Features
Interactive GUI using Streamlit

Random computer choice generation

Displays both user and bot choices

Shows the outcome immediately (Win, Lose, Draw)

Beginner-friendly and lightweight

Ready for enhancements like score tracking and multiplayer

⚙️ Installation & Setup
1. Clone the Repository

Bash

git clone https://github.com/Chankit13/snake-water-gun
cd snake-water-gun
2. Install Dependencies

Bash

pip install streamlit
3. Run the Game

Bash

streamlit run app.py
Open the Local URL in your browser. Choose Snake 🐍, Water 🌊, or Gun 🔫 and click Play.

🎨 Project Structure
snake-water-gun/
│
├── app.py        # Streamlit frontend
├── game.py       # Core game logic
├── README.md     # Project description
🏆 Future Enhancements
Add scoreboard for multiple rounds

Include animations & sound effects

Implement online multiplayer mode

Add theme customization (dark/light mode)
