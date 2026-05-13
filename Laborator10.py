import pandas as pd
data=pd.read_csv('StudentsPerformance.csv')

print(" ")
print("Ex1:Încărcați setul de date într-un DataFrame Pandas")
print(" ")

print(data.head)

print(" ")
print("Ex1:Afișați primele 5 înregistrări")
print(" ")

print(data.head())

print(" ")
print("Ex1:Încărcați setul de date într-un DataFrame Pandas")
print(" ")

print(data.info())

print(" ")
print("Ex1:Analizați structura dataset-ului (tipuri de date, număr de valori non-null)")
print(" ")

data.info()

print(" ")
print("Ex1:Calculați statistici descriptive pentru variabilele numerice")
print(" ")

print(data.describe())

print(" ")
print("Ex1:Identificați eventualele valori lipsă")
print(" ")

print(data.isnull().sum())

print(" ")
print("Ex2_Identificarea tipurilor de variabile")
print("Ex2_Determinați:variabilele categorice si variabilele numerice;Enumerați fiecare categorie identificată")

numerice = data.select_dtypes(include=['number']).columns
categorice = data.select_dtypes(include=['object', 'string']).columns
print(" ")
print("Variabile categorice:", categorice.tolist())
print(" ")
print("Variabile numerice:", numerice.tolist())

print(" ")
print("Exe3_3. Curățarea datelor")
print("Exe3_3. Verificați existența valorilor lipsă;")
print("Dacă există:")
print("înlocuiți valorile numerice lipsă cu mediana")
print("înlocuiți valorile categorice lipsă cu „Unknown”")
print("Verificați din nou dataset-ul pentru a confirma eliminarea valorilor lipsă")
print(" ")

# 1. Identificăm coloanele pe tipuri (am stabilit deja listele 'numerice' și 'categorice')
numerice = data.select_dtypes(include=['number']).columns
categorice = data.select_dtypes(include=['object', 'string']).columns

for col in numerice:
    mediana = data[col].median()
    data[col] = data[col].fillna(mediana)

for col in categorice:
    data[col] = data[col].fillna("Unknown")

print("--- Verificare finală valori lipsă ---")
print(data.isnull().sum())



