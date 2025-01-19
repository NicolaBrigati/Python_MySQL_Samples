import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Creazione di un piccolo dataset di esempio
data = {
    'Feature1': [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],
    'Feature2': [1, 1, 2, 3, 5, 8, 13, 21, 34, 55],
    'Target': [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

# Separare le variabili indipendenti (X) dalla variabile dipendente (y)
X = df[['Feature1', 'Feature2']]  # Usa entrambe le features
y = df['Target']

# Suddividere il dataset in training e testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Creazione del modello di regressione logistica con regolarizzazione L2
model = LogisticRegression(penalty='l2', solver='liblinear')

# Fit del modello
model.fit(X_train, y_train)

# Previsione sui dati di test
y_pred = model.predict(X_test)

# Calcolare la precisione
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

# Riepilogo dei coefficienti
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
