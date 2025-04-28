import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


data = np.array([
    [1500, 3, 20, 300000],
    [1600, 3, 15, 320000],
    [1700, 4, 10, 350000],
    [1800, 4, 5, 370000],
    [1900, 5, 2, 400000],
    [2000, 5, 1, 420000]
])


X_multi = data[:, :3]    
y = data[:, 3]            


X_simple = X_multi[:, [0]]  

model_simple = LinearRegression()
model_simple.fit(X_simple, y)
y_pred_simple = model_simple.predict(X_simple)

print("=== Simple Linear Regression ===")
print("Coefficient (slope):", model_simple.coef_[0])
print("Intercept:", model_simple.intercept_)
print("R² Score:", r2_score(y, y_pred_simple))


plt.figure(figsize=(6, 4))
plt.scatter(X_simple, y, color='blue', label='Actual')
plt.plot(X_simple, y_pred_simple, color='red', label='Predicted')
plt.title('Simple Linear Regression: Area vs Price')
plt.xlabel('Area (sq.ft)')
plt.ylabel('Price')
plt.legend()
plt.tight_layout()
plt.show()

# Multiple Linear Regression

model_multi = LinearRegression()
model_multi.fit(X_multi, y)
y_pred_multi = model_multi.predict(X_multi)

print("\n=== Multiple Linear Regression ===")
print("Coefficients:", model_multi.coef_)
print("Intercept:", model_multi.intercept_)
print("R² Score:", r2_score(y, y_pred_multi))
print("Predicted Prices:", y_pred_multi)
