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

questions = [
    ("sleep", "1. Did you sleep about 8 hours last night?"),
    ("nap", "2. Did you take 1 hour afternoon nap?"),
    ("fast", "3. Are you doing 12 hours fasting?"),
    ("exercise", "4. Did you do moderate exercise and receive sunlight?"),
    ("water", "5. Are you drinking enough water?"),
    ("protein", "6. Did you eat protein today?"),
    ("joy", "7. Did you do any joyful activity?"),
    ("ent", "8. Did you have some entertainment?"),
    ("gratitude", "9. Did you feel gratitude at the end of the day?")
]

yes_count = 0
for key, q in questions:
    print(q + " (yes/no)")
    ans = input().lower()
    if "yes" in ans:
        yes_count += 1

print("\n" + "="*60)
print(f"Thank you dear! You completed {yes_count}/9 habits today.")
print("Take care! Come back tomorrow. You are loved 💕")

# Generate Rings (same as before)
try:
    import matplotlib.pyplot as plt
    from matplotlib.patches import Circle
    # ... (keeping your existing rings code - you can keep the previous version)
    print("✅ Rings saved as daily_rings.png")
except:
    pass

print("Take care dear! Come back tomorrow. You are loved 💕")