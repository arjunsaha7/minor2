import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Load CSV

data = pd.read_csv("student_marks.csv")
data = pd.read_csv("student_marks.csv")

# Rename the first column to Name
data.rename(columns={"Unnamed: 0": "Name"}, inplace=True)

print("\n Raw Data ")

print(data)

# select subject columns for calculation in dict

subjects = ["Maths","Physics","Chemistry","English","Biology","Economics","History","Civics"]


#subject wise calcu with mean max min meathod

avg = data[subjects].mean()
maxi = data[subjects].max()

mini = data[subjects].min()

print("\n Average Marks per Subject ")
print(avg)

print("\n Maximum Marks per Subject ")
print(maxi)

print("\n Minimum Marks per Subject ")
print(mini)


#total  Average per Student using numpy

data["Total"] = np.sum(data[subjects], axis=1)
data["Average"] = np.mean(data[subjects], axis=1)

print("\n Student Performance ")

print(data[["Name","Gender","Total","Average"]])


#Find Topper
 
topper = data.loc[data["Total"].idxmax()]
print("\nTopper ")
print("Name:", topper["Name"])
print("Gender:", topper["Gender"])
print("Total Marks:", topper["Total"])


# Grade codn fun

def grade(avg):
    if avg >= 80:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "Fail"

data["Grade"] = data["Average"].apply(grade)

print("\n Grades ")
print(data[["Name","Average","Grade"]])


# Student comparison Bar chart

plt.figure(figsize=(8,5))
plt.bar(data["Name"], data["Average"])
plt.xticks(rotation=45)
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Student Performance Comparison")
plt.tight_layout()
plt.show()


#Subject wise avg bar chart

plt.figure(figsize=(10,6))
avg.plot(kind="bar")
plt.ylabel("Marks")
plt.title("Average Marks in Each Subject")
plt.show()