import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

data = pd.read_csv(r"D:\Coding\Codes\Industrial Training\Mall claster\Mall_Customers.csv")
print(data.head())
print(data.corr(numeric_only=True))


plt.figure(figsize = (10, 6))
sns.set(style = 'whitegrid')
sns.distplot(data['Annual Income (k$)'])
plt.title("Distribution of Annual Income (k$)")
plt.xlabel("Range of Annual Income (k$)")
plt.ylabel('Count')

plt.figure(figsize = (10, 6))
sns.set(style = 'whitegrid')
sns.histplot(data['Age'], kde=True)
plt.title("Distribution of Age")
plt.xlabel("Range of Age")
plt.ylabel('Count')

plt.figure(figsize = (10, 6))
sns.set(style = 'whitegrid')
sns.distplot(data['Spending Score (1-100)'])
plt.title("Distribution of Spending Score (1-100)")
plt.xlabel("Range of Spending Score (1-100)")
plt.ylabel('Count')

genders = data.Gender.value_counts()
sns.set_style("darkgrid")
plt.figure(figsize=(10, 4))
sns.barplot(x = genders.index, y = genders.values)
plt.show()

data.columns

df = data[['CustomerID', 'Gender', 'Age', 'Annual Income (k$)',
       'Spending Score (1-100)']]

X = df[['Annual Income (k$)','Spending Score (1-100)']]

X.head()

plt.figure(figsize = (10, 6))
sns.scatterplot(x = 'Annual Income (k$)', y = 'Spending Score (1-100)', data= X, s = 60)
plt.title('Annual Income (k$) vs Spending Score (1-100)')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.show()

from sklearn.cluster import KMeans

wcss = []
for i in range(1, 11):
    km = KMeans(n_clusters=i)
    km.fit(X)
    wcss.append(km.inertia_)

    plt.figure(figsize = (12, 6))
plt.plot(range(1, 11), wcss)
plt.plot(range(1, 11), wcss, linewidth = 2, color="red", marker = "8")
plt.xlabel("K Value")
plt.xticks(np.arange(1, 11, 1))
plt.ylabel('WCSS')
plt.show()

km1 = KMeans(
    n_clusters=5,
    init="k-means++",
    n_init=10,
    random_state=42
)
km1.fit(X)
y=km1.predict(X)
df["label"] = y
df.head()

plt.figure(figsize = (10, 6))
sns.scatterplot(x = 'Annual Income (k$)', y = 'Spending Score (1-100)', hue = "label",
               palette=['red', 'green', 'orange', 'brown', 'dodgerblue'], legend = 'full', data = df, s = 60)

plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.title("Spending Score (1-100) vs Annual Income (k$)")
plt.show()

cust1=df[df["label"]==1]
print('Number of customer in 1st group=', len(cust1))
print('They are -', cust1["CustomerID"].values)
print("--------------------------------------------")
cust2=df[df["label"]==2]
print('Number of customer in 2nd group=', len(cust2))
print('They are -', cust2["CustomerID"].values)
print("--------------------------------------------")
cust3=df[df["label"]==0]
print('Number of customer in 3rd group=', len(cust3))
print('They are -', cust3["CustomerID"].values)
print("--------------------------------------------")
cust4=df[df["label"]==3]
print('Number of customer in 4th group=', len(cust4))
print('They are -', cust4["CustomerID"].values)
print("--------------------------------------------")
cust5=df[df["label"]==4]
print('Number of customer in 5th group=', len(cust5))
print('They are -', cust5["CustomerID"].values)
print("--------------------------------------------")

data.columns

df2 = data[['CustomerID', 'Gender', 'Age', 'Annual Income (k$)',
       'Spending Score (1-100)']]
df2.head()
X2 = df2[['Age', 'Annual Income (k$)','Spending Score (1-100)']]

wcss = []
for i in range(1, 11):
    km = KMeans(n_clusters=i, init="k-means++")
    km.fit(X2)
    wcss.append(km.inertia_)

    plt.figure(figsize = (12, 6))
plt.plot(range(1, 11), wcss)
plt.plot(range(1, 11), wcss, linewidth = 2, color="red", marker = "8")
plt.xlabel("K Value")
plt.xticks(np.arange(1, 11, 1))
plt.ylabel('WCSS')
plt.show()

km2  = KMeans(n_clusters=5)
km2.fit(X2)
y2=km2.predict(X2)
df2["label"] = y2
df2.head()

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize = (20, 10))
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(df2.Age[df2.label == 0], df2['Annual Income (k$)'][df2.label==0], df2['Spending Score (1-100)'][df2.label==0], c = 'purple', s = 60)
ax.scatter(df2.Age[df2.label == 1], df2['Annual Income (k$)'][df2.label==1], df2['Spending Score (1-100)'][df2.label==1], c = 'red', s = 60)
ax.scatter(df2.Age[df2.label == 2], df2['Annual Income (k$)'][df2.label==2], df2['Spending Score (1-100)'][df2.label==2], c = 'orange', s = 60)
ax.scatter(df2.Age[df2.label == 3], df2['Annual Income (k$)'][df2.label==3], df2['Spending Score (1-100)'][df2.label==3], c = 'green', s = 60)
ax.scatter(df2.Age[df2.label == 4], df2['Annual Income (k$)'][df2.label==4], df2['Spending Score (1-100)'][df2.label==4], c = 'yellow', s = 60)

ax.view_init(35, 185)
plt.xlabel("Age")
plt.ylabel('Annual Income (k$)')
ax.set_zlabel('Spending Score (1-100)')
plt.show()

cust1=df2[df2["label"]==0]
print('Number of customer in 1st group=', len(cust1))
print('They are -', cust1["CustomerID"].values)
print("--------------------------------------------")
cust2=df2[df2["label"]==1]
print('Number of customer in 2nd group=', len(cust2))
print('They are -', cust2["CustomerID"].values)
print("--------------------------------------------")
cust3=df2[df2["label"]==2]
print('Number of customer in 3rd group=', len(cust3))
print('They are -', cust3["CustomerID"].values)
print("--------------------------------------------")
cust4=df2[df2["label"]==3]
print('Number of customer in 4th group=', len(cust4))
print('They are -', cust4["CustomerID"].values)
print("--------------------------------------------")
cust5=df2[df2["label"]==4]
print('Number of customer in 5th group=', len(cust5))
print('They are -', cust5["CustomerID"].values)
print("--------------------------------------------")

joblib.dump(
    km1,
    r"D:\Coding\Codes\Industrial Training\Mall claster\mall_customer_model.pkl"
)

print("Saved!")