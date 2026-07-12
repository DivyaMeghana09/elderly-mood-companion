print("🌸 Welcome to Elderly Mood Companion 🌸")
print("Hello dear! How are you feeling today?")

mood = input("Reply with: happy, sad, tired, okay, or lonely: ").lower()

if "happy" in mood:
    print("That's wonderful! Keep smiling 😊")
elif "sad" in mood or "lonely" in mood:
    print("I'm here with you. Would you like to hear a joke?")
    print("Why did the scarecrow win an award? Because he was outstanding in his field! 😂")
elif "tired" in mood:
    print("Rest is important. Try sitting near a window and breathing slowly.")
else:
    print("Thank you for sharing. You are never alone. ❤️")

print("\nSuggestion for today:")
print("• Drink a glass of warm water")
print("• Listen to your favourite old song")
print("• Talk to a friend or family member")

print("\nTake care! Come back anytime. 💕")