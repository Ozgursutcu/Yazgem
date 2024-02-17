"""-----------------------  Model Seçimi ve Hiperparametre Ayarlama
En iyi modeli ve hiperparametreleri otomatik olarak seçmek için çapraz doğrulama ve 
grid search kullanabilirsiniz.
"""

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

# Veri ve etiketler
X, y = [[0, 1], [1, 1], [2, 1]], [0, 1, 0]

# Eğitim ve test setlerine bölme
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Modeli başlat ve eğit
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Modelin performansını değerlendir
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Doğruluk oranı: {accuracy}")
    
