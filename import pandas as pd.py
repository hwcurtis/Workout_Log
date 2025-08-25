import pandas as pd

# 1. Define the column names
columns = [
    "DATE",
    "WORK OUT TIME",
    "DISTANCE",
    "TOTAL CALORIES",
    "AVERAGE HEART RATE",
    "MILES",
    "TIMES"
]

# 2. Create an empty dataset with 2 rows (you can change 2 to 30 if you want)
data = [{col: "" for col in columns} for _ in range(2)]

# 3. Turn it into a DataFrame
df = pd.DataFrame(data)

# 4. Save as CSV file
df.to_csv("Workout_Log.csv", index=False)

print("Workout log CSV created! Check your folder for Workout_Log.csv")
