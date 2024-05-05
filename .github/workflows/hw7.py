import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.preprocessing import StandardScaler

# Load data
data_url = "https://github.com/abirami1998/NYU-Data-Science-Bootcamp-Spring-2024/raw/main/Week%206/employee.csv"
df = pd.read_csv(data_url)

# Preprocessing
X = df.drop(columns=['Salary'])
y = df['Salary']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Linear Regression
linear_reg = LinearRegression()
linear_reg.fit(X_train_scaled, y_train)
linear_pred = linear_reg.predict(X_test_scaled)

# Compute evaluation metrics for Linear Regression
linear_mae = mean_absolute_error(y_test, linear_pred)
linear_mse = mean_squared_error(y_test, linear_pred)

print("Linear Regression:")
print("Mean Absolute Error:", linear_mae)
print("Mean Squared Error:", linear_mse)

# Ridge Regression
ridge_reg = Ridge(alpha=1.0)
ridge_reg.fit(X_train_scaled, y_train)
ridge_pred = ridge_reg.predict(X_test_scaled)

# Compute evaluation metrics for Ridge Regression
ridge_mae = mean_absolute_error(y_test, ridge_pred)
ridge_mse = mean_squared_error(y_test, ridge_pred)

print("\nRidge Regression:")
print("Mean Absolute Error:", ridge_mae)
print("Mean Squared Error:", ridge_mse)

# Lasso Regression
lasso_reg = Lasso(alpha=1.0)
lasso_reg.fit(X_train_scaled, y_train)
lasso_pred = lasso_reg.predict(X_test_scaled)

# Compute evaluation metrics for Lasso Regression
lasso_mae = mean_absolute_error(y_test, lasso_pred)
lasso_mse = mean_squared_error(y_test, lasso_pred)

print("\nLasso Regression:")
print("Mean Absolute Error:", lasso_mae)
print("Mean Squared Error:", lasso_mse)
