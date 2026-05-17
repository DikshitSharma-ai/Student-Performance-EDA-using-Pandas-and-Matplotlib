import pandas as pd
import matplotlib.pyplot as plt

# =========================
# Load CSV File
# =========================

df = pd.read_csv("students.csv")

print("===== FIRST 5 ROWS =====")
print(df.head())

# =========================
# Basic Information
# =========================

print("\n===== DATA INFO =====")
print(df.info())

print("\n===== SHAPE =====")
print(df.shape)

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# =========================
# Handle Missing Values
# =========================

df["marks"] = df["marks"].fillna(df["marks"].mean())

df["hours"] = df["hours"].fillna(df["hours"].mean())

# =========================
# Basic Insights
# =========================

print("\n===== AVERAGE MARKS =====")
print(df["marks"].mean())

print("\n===== TOP SCORER =====")
print(df[df["marks"] == df["marks"].max()])

# =========================
# Pass / Fail Column
# =========================

df["result"] = df["marks"] >= 40

print("\n===== UPDATED DATA =====")
print(df)

# =========================
# Groupby Analysis
# =========================

print("\n===== CITY WISE AVERAGE MARKS =====")

city_avg = df.groupby("city")["marks"].mean()

print(city_avg)

# =========================
# Correlation
# =========================

print("\n===== CORRELATION =====")

corr = df[["marks", "hours"]].corr()

print(corr)

# =========================
# Graphs
# =========================

plt.figure(figsize=(12, 8))

# -------------------------
# 1 Line Plot
# -------------------------

plt.subplot(2,2,1)

plt.plot(df["marks"], marker="o")

plt.title("Marks Line Plot")

plt.xlabel("Student Index")

plt.ylabel("Marks")

# -------------------------
# 2 Bar Plot
# -------------------------

plt.subplot(2,2,2)

plt.bar(df["name"], df["marks"])

plt.title("Student Marks")

plt.xlabel("Students")

plt.ylabel("Marks")

# -------------------------
# 3 Scatter Plot
# -------------------------

plt.subplot(2,2,3)

plt.scatter(df["hours"], df["marks"])

plt.title("Hours vs Marks")

plt.xlabel("Study Hours")

plt.ylabel("Marks")

# -------------------------
# 4 Histogram
# -------------------------

plt.subplot(2,2,4)

plt.hist(df["marks"], bins=5)

plt.title("Marks Distribution")

plt.xlabel("Marks")

plt.ylabel("Frequency")

# =========================
# Adjust Layout
# =========================

plt.tight_layout()

plt.show()

# =========================
# Save Final CSV
# =========================

df.to_csv("final_output.csv", index=False)

print("\nFinal CSV Saved Successfully")