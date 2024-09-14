import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('payloads.csv')


df['payload'] = df['payload'].fillna('')


vectorizer = TfidfVectorizer(max_features=1000)
X = vectorizer.fit_transform(df['payload'])
y = df['is_malicious']


model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

def predict_email(email):
    new_payload = email
    new_payload_vectorized = vectorizer.fit_transform([new_payload])
    prediction = model.predict(new_payload_vectorized)
    return prediction[0]

def predict_password(password):
    new_payload = password
    new_payload_vectorized = vectorizer.transform([new_payload])
    prediction = model.predict(new_payload_vectorized)
    return prediction[0]
