import pandas as pd
import numpy as np
import math
from scipy import stats
import matplotlib.pyplot as plt  # 📌 for graph

# Step 1: Create simple data
data = {
    'study_hours': [1, 2, 3, 4, 5],
    'exam_score': [35, 40, 50, 55, 60]
}

df = pd.DataFrame(data)

# Step 2: Get X and Y
X = df['study_hours'].values
Y = df['exam_score'].values

# Step 3: Find the average
mean_x = np.mean(X)
mean_y = np.mean(Y)

# Step 4: Calculate slope (b1) and intercept (b0)
numerator = np.sum((X - mean_x) * (Y - mean_y))
denominator = np.sum((X - mean_x) ** 2)
b1 = numerator / denominator
b0 = mean_y - b1 * mean_x

# Step 5: Predict score for a new student
new_hours = 6
predicted_score = b0 + b1 * new_hours

print(f"Prediction formula: exam_score = {b0:.2f} + {b1:.2f} * study_hours")
print(f"Predicted exam score for {new_hours} hours of study = {predicted_score:.2f}")

# Step 6: Plot the graph
plt.scatter(X, Y, color='blue', label='Actual Scores')  # actual data
plt.plot(X, b0 + b1 * X, color='red', label='Prediction Line')  # regression line
plt.scatter(new_hours, predicted_score, color='green', label='Predicted Score (6 hrs)', marker='x', s=100)

plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.title("Study Hours vs Exam Score")
plt.legend()
plt.grid(True)
plt.show()
