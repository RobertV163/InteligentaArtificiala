import pandas as pd
data=pd.read_csv('data.csv')

print(" ")
print("Ex2")
print(" ")

jucatori_peste_40 = data[data['Age'] > 40].head(10)
print(jucatori_peste_40)

#pd.set_option('display.max_columns',None)
#pd.set_option('display.max_rows',None)
#print(data)
print(" ")
print("Ex3")
print(" ")

jucatori_ovr85_age25 = data[(data['Overall'] >= 85) & (data['Age'] < 25)].head
print(jucatori_ovr85_age25)

print(" ")
print("Ex4")
print(" ")

data_SM_desc=data.sort_values("Skill Moves",ascending=False).head(3)
print(data_SM_desc)

print(" ")
print("Ex5")
print(" ")

jucatori_contract2021 = data[data['Contract Valid Until'] == '2021']
print(jucatori_contract2021)

print(" ")
print("Ex6")
print(" ")

randuri, coloane = data.shape
print(f"Setul de date are {randuri} rânduri și {coloane} coloane.")

nr_jucatori_unici = data['Name'].nunique()
print(f"Avem {nr_jucatori_unici} jucători unici.")

print(" ")
print("Ex7")
print(" ")

