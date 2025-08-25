import pandas as pd

# 1. Define the column names
columns = [
    "DATE",
    "WORK OUT TOTAL  TIME",
    "SPLIT TIMES",
    "DISTANCE",
    "TOTAL CALORIES",
    " HEART RATE",
    "MILES TIME TOTAL"
]
# 2. Create sample data (empty or with example rows)
data = [{col: "" for col in columns}
        for _ in range(30)]  # Empty row as placeholder

# 3. Turn it into a DataFrame
df = pd.DataFrame(data, columns=columns)

# 4. Save as CSV file
df.to_csv("Workout_Log.csv", index=False)

print("Workout log CSV created! Check your folder for Workout_Log.csv")
