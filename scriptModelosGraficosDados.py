import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder

# Carregar o arquivo CSV
df = pd.read_csv('./Ecommerce_DBS.csv')

# Limpar os nomes das colunas
df.columns = df.columns.str.strip().str.replace(' ', '_').str.replace('�', '')

# Exibir as primeiras linhas do dataframe
print(df.head())

# Verificar se há valores nulos
print(df.isnull().sum())

# Distribuição de gênero
sns.countplot(data=df, x='Gender')
plt.title('Distribuição de Gênero')
plt.show()

# Distribuição de idade
sns.histplot(data=df, x='Customer_Age', bins=20)
plt.title('Distribuição de Idade dos Clientes')
plt.show()

# Distribuição de canais de venda
sns.countplot(data=df, x='Source')
plt.title('Distribuição dos Canais de Venda')
plt.show()

# Distribuição das categorias de produtos
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='Product_Category')
plt.title('Distribuição das Categorias de Produtos')
plt.xticks(rotation=45)
plt.show()

# Relação entre gênero e categoria de produto
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='Product_Category', hue='Gender')
plt.title('Distribuição das Categorias de Produtos por Gênero')
plt.xticks(rotation=45)
plt.show()

# Relação entre idade e categoria de produto
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='Product_Category', y='Customer_Age')
plt.title('Distribuição das Idades por Categoria de Produto')
plt.xticks(rotation=45)
plt.show()

# Relação entre canal de venda e categoria de produto
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='Product_Category', hue='Source')
plt.title('Distribuição das Categorias de Produtos por Canal de Venda')
plt.xticks(rotation=45)
plt.show()

####MODELO####
# Codificar variáveis categóricas
labelencoder = LabelEncoder()
df['Gender'] = labelencoder.fit_transform(df['Gender'])
df['Source'] = labelencoder.fit_transform(df['Source'])
df['Product_Category'] = labelencoder.fit_transform(df['Product_Category'])

# Definir variáveis independentes e dependentes
X = df[['Gender', 'Customer_Age', 'Source']]
y = df['Product_Category']

# Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Construir o modelo de árvore de decisão
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Prever no conjunto de teste
y_pred = clf.predict(X_test)

# Avaliar o modelo
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Mostrar a importância das características
feature_importances = pd.Series(clf.feature_importances_, index=X.columns)
feature_importances.plot(kind='barh')
plt.title('Importância das Características')
plt.show()
