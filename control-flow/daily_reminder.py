# daily_reminder.py

# Prompt for task input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match case to determine base reminder
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unknown priority level"

# Add urgency if the task is time-sensitive
if time_bound == "yes" and priority in ["high", "medium", "low"]:
    message += " that requires immediate attention today!"
elif time_bound == "no" and priority in ["high", "medium", "low"]:
    message += ". Consider completing it when you have time."

# Display the final reminder
print("\n" + message)
