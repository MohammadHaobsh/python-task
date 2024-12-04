def mood_tracker():
    print("Welcome to the Mood Tracker!")
    print("Input your mood each day (e.g., happy, sad, stressed, etc.).")
    
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    mood_log = []
    
    # Collect mood input for each day
    for day in days_of_week:
        mood = input(f"How do you feel on {day}? ").strip().lower()
        mood_log.append(mood)
    
    # Count occurrences of each mood
    mood_counts = {}
    for mood in mood_log:
        if mood in mood_counts:
            mood_counts[mood] += 1
        else:
            mood_counts[mood] = 1
    
    # Calculate percentages
    print("\nMood Breakdown for the Week:")
    total_days = len(days_of_week)
    for mood, count in mood_counts.items():
        percentage = (count / total_days) * 100
        print(f"{mood.capitalize()}: {percentage:.2f}%")
    
    print("\nThank you for using the Mood Tracker!")

# Run the Mood Tracker
mood_tracker()
#teat
