import datetime


persona_art = r"""
       .--.
      /    \
     |      |
      \    /
       '--'
    /|      |\
   / |      | \
     |______|
     |  ||  |
     |  ||  |
     |__||__|
"""

# --- The Standard Data for your Profile ---
# (A simplified version of your data stack)
my_stack = """
- **C#, Python, Java**
- Gamer turned game developer
- Exploring AI projects
"""

# --- Create the Welcome Greeting and Combine Everything ---
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
greeting_text = f"\n### Hi, I'm BinaryGhost45! 👋\n#### Welcome to my GitHub Profile! (Updated: {now})\n"

# Wrap the text in a code block for proper formatting
complete_data = f"```text\n{persona_art}\n{greeting_text}\n```\n### About Me\n{my_stack}\n[Visit my portfolio repository](https://binaryghost45.github.io/BinaryGhost45-Unity_Store_-portfolio_Website/)"

# --- Write the final data to the README.md ---
with open("README.md", "w") as file:
    file.write(complete_data)

print("Profile generated!")
