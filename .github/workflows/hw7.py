import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Load data
url = 'https://raw.githubusercontent.com/yourusername/glass.csv'
data = pd.read_csv(url)

# Preprocess data
# Handle missing values if any
# Convert categorical variables to numerical if any

# Split data into features and target
X = data.drop(columns=['target_column'])  # replace 'target_column' with the actual target column name
y = data['target_column']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Compute predictions
# Example for 'Al' column
threshold = 0.5  # default threshold
probs = model.predict_proba(X_test)[:, 1]
y_pred = (probs > threshold).astype(int)

# Evaluate metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print(f"Accuracy: {accuracy}, Precision: {precision}, Recall: {recall}")

