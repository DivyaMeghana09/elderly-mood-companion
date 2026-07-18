import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

st.set_page_config(page_title="Elderly Mood Companion", page_icon="❤️", layout="centered")

st.title("🌸 Elderly Mood Companion 🌸")
st.markdown("Hello dear! Let's talk about your day together ❤️")

# Mood Check
mood = st.text_input("How are you feeling today? (happy, sad, tired, okay, lonely)", key="mood")

if mood:
    mood = mood.lower()
    if "happy" in mood:
        st.success("Wonderful! I'm so glad 😊")
    elif "sad" in mood or "lonely" in mood:
        st.info("I'm here with you. Here's a small joke:")
        st.write("Why did the scarecrow win an award? Because he was outstanding in his field! 😂")
    elif "tired" in mood:
        st.info("Rest well dear. Take it easy today.")
    else:
        st.info("Thank you for sharing. You are never alone 💕")

    st.divider()
    st.subheader("Now let's do a simple Q&A about your 24-hour day:")

    # ... (Keep your existing Q&A and rings code here)
    # You can copy the Q&A + rings part from your previous app.py

    questions = [
        "1. Did you sleep about 8 hours last night?",
        "2. Did you take 1 hour afternoon nap?",
        "3. Are you doing 12 hours fasting?",
        "4. Did you do moderate exercise and receive sunlight?",
        "5. Are you drinking enough water?",
        "6. Did you eat protein today?",
        "7. Did you do any joyful activity?",
        "8. Did you have some entertainment?",
        "9. Did you feel gratitude at the end of the day?"
    ]

    labels = ["Sleep 8hr", "Afternoon Nap", "12hr Fasting", "Exercise", "Hydration", "Protein", "Joyful Activity", "Entertainment", "Gratitude"]

    tips_dict = {
        0: ["Go to bed at same time daily", "Avoid phone before sleep", "Keep room dark & quiet", "Drink warm milk", "Listen to soft music"],
        1: ["Rest 20-30 min after lunch", "Lie down in quiet place", "Close eyes and breathe slowly", "Set gentle alarm", "Nap in chair if needed"],
        2: ["Finish dinner by 7-8 PM", "Drink warm water in morning", "Avoid late night snacks", "Have light dinner", "Eat fruits if hungry"],
        3: ["Walk 15-20 min in morning", "Do simple stretches", "Sit in sunlight 10 min", "Move every hour", "Breathe fresh air"],
        4: ["Keep bottle nearby", "Drink after waking up", "Take small sips hourly", "Add lemon for taste", "Drink before meals"],
        5: ["Drink milk or curd daily", "Eat dal or eggs", "Have handful of nuts", "Add paneer in meals", "Eat sprouts"],
        6: ["Listen to favourite songs", "Talk to family", "Do prayer 10 min", "Water plants", "Look at old photos"],
        7: ["Watch funny video", "Listen to old songs", "Call a friend", "Watch birds from window", "Read few pages"],
        8: ["Think of 3 good things", "Say thank you to God", "Remember happy moments", "Tell someone you are grateful", "Write one good thing"]
    }

    answers = []
    yes_count = 0

    for i, q in enumerate(questions):
        ans = st.radio(q, ["Yes", "No"], horizontal=True, key=f"q{i}")
        answers.append(ans == "Yes")
        if ans == "Yes":
            yes_count += 1
        else:
            st.warning("Here are 5 simple tips to improve:")
            for tip in tips_dict[i]:
                st.write(f"• {tip}")

    if st.button("Show My Daily Wellness Rings", type="primary"):
        # Your rings code here (3x3 grid)
        st.divider()
        st.subheader(f"Your 9 Healthy Habit Rings ❤️\n{yes_count}/9 Completed Today")
        
        fig, ax = plt.subplots(figsize=(13, 13))
        ax.set_xlim(0, 13)
        ax.set_ylim(0, 13)
        ax.axis('off')

        positions = [(3,10), (6.5,10), (10,10), (3,6.5), (6.5,6.5), (10,6.5), (3,3), (6.5,3), (10,3)]

        for i, (x, y) in enumerate(positions):
            color = 'lightgreen' if answers[i] else 'lightgray'
            outer = Circle((x, y), 1.25, color=color, alpha=0.3)
            ax.add_patch(outer)
            inner = Circle((x, y), 0.95, color=color, alpha=0.9)
            ax.add_patch(inner)
            ax.text(x, y, labels[i], ha='center', va='center', fontsize=9.5, fontweight='bold')

        st.pyplot(fig, use_container_width=True)
        fig.savefig("daily_rings.png", dpi=300, bbox_inches='tight')
        st.success("✅ Rings saved as daily_rings.png")

st.caption("Made with love for seniors 💕")