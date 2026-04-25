import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

n = int(input("Enter number of students: "))
std = []
marks = []

for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    mark = float(input(f"Enter marks of {name}: "))
    std.append(name)
    marks.append(mark)

m_array = np.array(marks)
data = pd.DataFrame({
    "Student": std,
    "Marks": m_array
})

print("\nStudent Data:\n")
print(data)
print("\nStatistics:")
print("Average Marks:", round(np.mean(m_array), 2))
print("Highest Marks:", np.max(m_array))
print("Lowest Marks:", np.min(m_array))

plt.figure(figsize=(8,5))
sns.barplot(x="Student", y="Marks", data=data)
plt.title("Student Marks Analysis")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.xticks(rotation=30)
plt.tight_layout()

plt.show()