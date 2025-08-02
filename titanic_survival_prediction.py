import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

# Load dataset (seaborn has a built-in Titanic dataset)
import seaborn as sns
titanic = sns.load_dataset('titanic')

# Preview data
print(titanic.head())

# Select features and target
features = ['pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked']
target = 'survived'

# Drop rows with missing target
titanic = titanic.dropna(subset=[target])

# Handle missing values in features
titanic['age'] = titanic['age'].fillna(titanic['age'].median())
titanic['embarked'] = titanic['embarked'].fillna(titanic['embarked'].mode()[0])

# Encode categorical features
le_sex = LabelEncoder()
titanic['sex'] = le_sex.fit_transform(titanic['sex'])

le_embarked = LabelEncoder()
titanic['embarked'] = le_embarked.fit_transform(titanic['embarked'])

X = titanic[features]
y = titanic[target]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print(f'Accuracy: {accuracy_score(y_test, y_pred):.4f}')
print('Classification Report:')
print(classification_report(y_test, y_pred))
