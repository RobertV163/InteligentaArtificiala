import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from   sklearn.datasets import load_diabetes

x=np.array([[1],[2],[3],[4]])
y=np.array([5,6,7,8])
model=LinearRegression()
model.fit(x,y)
print(model.predict([[5]]))


print("Ex2:Afișați primele 5 rânduri într-un DataFrame Pandas.")
diabetes=load_diabetes()
df=pd.DataFrame(diabetes.data,columns=diabetes.feature_names)
df['target']=diabetes.target
print(df.head())

print("Ex3:Listați toate caracteristicile disponibile (feature_names)")
print(diabetes.feature_names)

print("Ex4:Cum putem accesa informatii statistice precum media, deviatia standard sau valoarea minima? ")
print(df.describe())

print("Ex5:Creati o histograma pentru caracteristica BMI.")
plt.figure(figsize=(8,6))
plt.hist(df["bmi"],bins=20)
plt.title("Histograma BMI")
plt.xlabel("BMI")
plt.ylabel("Frecventa")
plt.show()

print("Ex6:Creati graficul pentru BMI și vârstă în funcție de variabila țintă.")
plt.figure(figsize=(8,6))
plt.scatter(df["bmi"],df["age"],c=df["target"],cmap="viridis")
plt.xlabel("BMI")
plt.ylabel("varsa")
plt.title("Creati graficul pentru BMI și vârstă în funcție de variabila țintă")
plt.colorbar(label="target")
plt.show()

print("Ex 7 Regresie liniară simplă folosind bmi:")
print("7.a Selectați doar coloana bmi ca input (X) și scorul diabetului ca target (y)")
X = df[["bmi"]]
y = df["target"]

print("7.b Împărțiți datele în set de antrenare și set de testare (80%-20%)")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("7.c Antrenați un model de regresie liniară folosind datele de antrenare")
regresie = LinearRegression()
regresie.fit(X_train, y_train)

print("7.d Reprezentați grafic datele de testare și linia de regresie.")
y_prezis = regresie.predict(X_test)
plt.figure(figsize=(8, 6))
plt.scatter(X_test, y_test, color="blue", label="Date reale (Test)", alpha=0.7)
plt.plot(X_test, y_prezis, color="red", linewidth=2, label="Linia de regresie")
plt.title("Regresie liniară simplă: BMI vs Target")
plt.xlabel("BMI ")
plt.ylabel("Target ")
plt.legend()
plt.show()

print("7.e Calculați eroarea pătratică medie (MSE) folosind datele de testare (y_test și y_pred)")
mse = mean_squared_error(y_test, y_prezis)
print(mse)

print("8 Regresie pe două caracteristici (bmi și bp):")
print("8.a Selectați bmi și bp ca input (X)")
X_8 = df[["bmi", "bp"]]
y_8 = df["target"]
X_train8, X_test8, y_train8, y_test8 = train_test_split(X_8, y_8, test_size=0.2, random_state=42)
print("8.b Antrenați un nou model de regresie liniară folosind aceste două caracteristici.")
model_nou = LinearRegression()
model_nou.fit(X_train8, y_train8)

print("8.c Afișați coeficienții modelului pentru fiecare caracteristică.")
coef_bmi = model_nou.coef_[0]
coef_bp = model_nou.coef_[1]
print(coef_bmi)
print(coef_bp)
print("8.d Calculați scorul R² al modelului pe setul de testare.")
y_predictie = model_nou.predict(X_test8)
r2 = r2_score(y_test8, y_predictie)
print(r2)
