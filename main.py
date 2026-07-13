print("🌸 Welcome to Elderly Mood Companion 🌸")
print("Hello dear! Let's talk about your day together ❤️\n")

# Mood Check
mood = input("How are you feeling today? (happy, sad, tired, okay, lonely): ").lower()

if "happy" in mood:
    print("Wonderful! I'm so glad 😊\n")
elif "sad" in mood or "lonely" in mood:
    print("I'm here with you. Here's a small joke:")
    print("Why did the scarecrow win an award? Because he was outstanding in his field! 😂\n")
elif "tired" in mood:
    print("Rest well dear. Take it easy today.\n")
else:
    print("Thank you for sharing. You are never alone 💕\n")

print("Now let's do a simple Q&A about your 24-hour day:\n")

# Questions
questions = [
    ("sleep", "1. Did you sleep about 8 hours last night?"),
    ("nap", "2. Did you take 1 hour afternoon nap?"),
    ("fast", "3. Are you doing 12 hours fasting?"),
    ("exercise", "4. Did you do moderate exercise and recieve sunligh?"),
    ("water", "5. Are you drinking enough water?"),
    ("protein", "6. Did you eat protein today?"),
    ("joy", "7. Did you do any joyful activity?"),
    ("ent", "8. Did you have some entertainment?"),
    ("gratitiude", "9. Did you felt gratitude at the end of the day?")
]

answers = {}
yes_count = 0

for key, q in questions:
    print(q + " (yes/no)")
    ans = input().lower()
    answers[key] = ans
    if "yes" in ans:
        yes_count += 1

# Final Message
print("\n" + "="*60)
print("Thank you for answering dear! You are doing good.\n")

# Generate Apple-style 9 Rings
try:
    import matplotlib.pyplot as plt
    from matplotlib.patches import Circle
    
    print("Generating your 9 Healthy Habit Rings (like Apple rings)...")
    
    fig, ax = plt.subplots(figsize=(12, 12))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 12)
    ax.axis('off')
    
    labels = ["Sleep 8hr", "Afternoon Nap", "12hr Fasting", "Exercise", 
              "Hydration", "Protein", "Joyful Activity", "Entertainment", "Gratitude"]
    
    # 3x3 Grid positions
    positions = [(3,9), (6,9), (9,9), (3,6), (6,6), (9,6), (3,3), (6,3), (9,3)]
    
    for i, (x, y) in enumerate(positions):
        color = 'lightgreen' if "yes" in answers[list(answers.keys())[i]] else 'lightgray'
        # Outer ring
        outer = Circle((x, y), 1.2, color=color, alpha=0.3)
        ax.add_patch(outer)
        # Inner filled circle
        inner = Circle((x, y), 0.9, color=color, alpha=0.9)
        ax.add_patch(inner)
        
        ax.text(x, y-1.8, labels[i], ha='center', va='center', fontsize=9, fontweight='bold')
    
    ax.set_title(f"Your 9 Healthy Habit Rings ❤️\n{yes_count}/9 Completed Today", 
                 fontsize=16, pad=30, color='darkblue')
    
    plt.savefig("daily_rings.png")
    print("✅ Rings saved as 'daily_rings.png' ! Open the image file.")
    
except ImportError:
    print(f"You completed {yes_count}/9 healthy habits today! ✅")

print("\nTake care dear! Come back tomorrow. You are loved 💕")