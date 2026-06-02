from   sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import numpy as np

iris = load_iris()
X=iris.data
Y=iris.target
# print(iris.data)
print("Ex1. Explorarea setului de date")
print("Ex1.2Afișați:")

print("numărul de exemple și dimensiunea caracteristicilor")
print(X.shape[0])

print("denumirile coloanelor (atributelor)")
print(iris.feature_names)

print("numele claselor")
print(iris.target_names)

print("Ex2  Împărțirea setului în date de antrenament și testare")
print("Ex2.1:Utilizați train_test_split() pentru a împărți datele: 80% antrenare, 20% testare.")
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

print("Ex2.2:Afișați forma (shape) pentru fiecare subset.")
print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)

print("Ex3 3. Preprocesarea datelor")
print("Ex3.1: Standardizați caracteristicile cu StandardScaler pentru a asigura comparabilitatea distanțelor")
scaler=StandardScaler()
X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.transform(X_test)

print("Ex3.2:Comparați primele 3 exemple înainte și după scalare.")
print(X_train[:3])
print(X_train_scaled[:3])

print("Ex4 Construirea și antrenarea modelului KNN")
print("Ex4.1. Inițializați un model KNeighborsClassifier cu k = 3")
knn = KNeighborsClassifier(n_neighbors=3)

print("Ex4.2. Antrenați modelul pe datele de antrenament și afișați acuratețea obținută pe setul de testare")
knn.fit(X_train_scaled, Y_train)
acuratete = knn.score(X_test_scaled, Y_test)
print(f"Acuratețea modelului KNN pe setul de testare este: {acuratete:.4f}")

print("5. Explorarea impactului valorii k")
print("Ex5.1:Antrenați și evaluați modelul KNN pentru k în intervalul 1 – 15.")
valori_k = list(range(1, 16))
acurateti = []

for k in valori_k:
    knn_temp = KNeighborsClassifier(n_neighbors=k)
    knn_temp.fit(X_train_scaled, Y_train)
    scor = knn_temp.score(X_test_scaled, Y_test)
    acurateti.append(scor)
    print(f"Pentru k = {k:2d}, acuratețea este: {scor:.4f}")
print("Ex5.2Afișați un grafic cu acuratețea în funcție de valoarea lui k.")
plt.figure(figsize=(10, 6))
plt.plot(valori_k, acurateti, marker='o', linestyle='-', color='b', markersize=8)
plt.title('Impactul valorii lui k asupra acurateții modelului KNN')
plt.xlabel('Valoarea lui k (Numărul de vecini)')
plt.ylabel('Acuratețe pe setul de testare')
plt.xticks(valori_k)  # Afișează toate numerele de la 1 la 15 pe axa X
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

print("Ex5.3: Comentați care valoare pare a fi optimă și de ce.")
max_acuratete = max(acurateti)
k_optimi = [valori_k[i] for i, acc in enumerate(acurateti) if acc == max_acuratete]
print(f"\nAcuratețea maximă obținută este {max_acuratete:.4f} pentru k = {k_optimi}.")

print("6. Evaluarea modelului")
print("Ex6.1. Afișați matricea de confuzie utilizând confusion_matrix")
Y_pred=knn.predict(X_test_scaled)
matrice=confusion_matrix(Y_test,Y_pred)
print(matrice)

print("6.2. Generați un raport complet de clasificare cu classification_report, incluzând precizia, recall-ul și scorul F1.")
repost=classification_report(Y_pred,Y_test)
print(repost)
print("6.3. Interpretați rezultatele obținute: care clasă este cel mai bine prezisă?")

print("7. Vizualizarea datelor")
print("7.1. Utilizați doar 2 caracteristici (ex: lungime și lățime petală) și afișați un grafic scatter colorat în funcție de clasă.")

lungime= X[:, 2]
latime= X[:, 3]

plt.figure(figsize=(8, 6))
grafic = plt.scatter(lungime, latime, c=Y, cmap='autumn', edgecolors='blue')
plt.title("grafic petala")
plt.xlabel("Lungime petală (cm)")
plt.ylabel("Lățime petală (cm)")
plt.legend(handles=grafic.legend_elements()[0], labels=list(iris.target_names))
plt.show()
print("7.2. Simulați o predicție pentru o floare nouă, dată de utilizator, utilizând input() și modelul KNN.")

print("Introduceți dimensiunile florii:")
lungime_s = float(input("Lungime sepală (cm): "))
latime_s  = float(input("Lațime sepală (cm): "))
lungime_p = float(input("Lungime petală (cm): "))
latime_p  = float(input("Lațime petală (cm): "))

floare = [[lungime_s, latime_s, lungime_p, latime_p]]
date_scalate = scaler.transform(floare)
clasa_prezisa= knn.predict(date_scalate)[0]
nume_clasa_prezisa = iris.target_names[clasa_prezisa]
print(nume_clasa_prezisa)







