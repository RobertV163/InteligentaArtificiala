from   sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, classification_report

iris = load_iris()
X=iris.data
Y=iris.target
# print(iris.data)
print("Ex1")
print("Ex1.2")
print("numărul de exemple și dimensiunea caracteristicilor")
print(X.shape[0])

print("denumirile coloanelor (atributelor)")
print(iris.feature_names)

print("numele claselor")
print(iris.target_names)

print("Ex2")
print("Ex2.1")
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

print("Ex2.2")
print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)

print("Ex3")
print("Ex3.1")
scaler=StandardScaler()
X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.transform(X_test)

print("Ex3.2")
print(X_train[:3])
print(X_train_scaled[:3])


print("Ex4.1")

print("Ex4.2")

print("Ex5.1")
print("Ex5.2")
print("Ex5.3")

print("Ex6.1")
Y_pred=knn.predict(X_test_scaled)
matrice=confusion_matrix(Y_test,Y_proces)
print(matrice)


repost=classification_report(Y_pred,Y_test)
print(repost)