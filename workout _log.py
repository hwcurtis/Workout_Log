import pandas as pd

# 1. Define the column names
columns = [
    "DATE",
    "WORKOUT TYPE",
    "WORKOUT TOTAL TIME",
    "DISTANCE",
    "SPLIT TIMES",
    "Avg.Pace",
    "TOTAL CALORIES",
    "HEART RATE",
    "WEATHER",
]

# 2. Create an empty dataset with 2 rows (you can change 2 to 30 if you want)
data = [{col: "" for col in columns} for _ in range(30)]

# 3. Turn it into a DataFrame
df = pd.DataFrame(data)

# 4. Save as CSV file
df.to_csv("Workout_Log.csv", index=False)

print("Workout log CSV created! Check your folder for Workout_Log.csv")
