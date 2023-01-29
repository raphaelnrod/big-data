import pandas as pd

ratings = pd.read_csv('ratings.csv')
ratings.head()

ratings.shape

ratings.columns = ['user', 'movieId', 'nota', 'momento']
ratings.head()

ratings['nota'].unique()

ratings['nota'].value_counts()

print(f'Media: {ratings.nota.mean()}')
print(f'Mediana: {ratings.nota.median()}')

ratings.nota.plot(kind="hist")

ratings.nota.describe()

import seaborn as sns
print(sns.__version__)

sns.boxplot(ratings.nota)

filmes = pd.read_csv("movies.csv")
filmes.head()

ratings.query("movieId==1").nota.mean()

medias_por_filme = ratings.groupby('movieId').mean().nota
medias_por_filme.head()

sns.boxplot(medias_por_filme)

sns.distplot(medias_por_filme)

tmdb = pd.read_csv("tmdb_5000_movies.csv")

tmdb.head()

contagem_de_lingua = tmdb.original_language.value_counts().to_frame().reset_index()
contagem_de_lingua.columns = ['original_language', 'total']
contagem_de_lingua.head()

sns.barplot(x="original_language", y="total", data = contagem_de_lingua)

sns.catplot(x="original_language", kind="count", data = tmdb)

total_por_lingua = tmdb.original_language.value_counts()
total_geral = total_por_lingua.sum()
total_de_ingles = total_por_lingua.loc['en']
total_do_resto = total_geral - total_de_ingles

dados = {
    'lingua': ['ingles', 'outros'],
    'total': [total_de_ingles, total_do_resto]
}
dados = pd.DataFrame(dados)
sns.barplot(x="lingua", y="total",data = dados)

outras_linguas = tmdb.query("original_language != 'en'")
total_outras_linguas = outras_linguas.original_language.value_counts()
sns.catplot(data=outras_linguas,
    x="original_language", 
    kind="count", 
    aspect=3, 
    order = total_outras_linguas.index,
    palette = "GnBu_d")

notas_toy_story = ratings.query("movieId == 1")
notas_jumanji = ratings.query("movieId == 2")
print(f"Media ToyStory {round(notas_toy_story.nota.mean(), 2)}")
print(f"Media Jumanji {round(notas_jumanji.nota.mean(), 2)}")

np.array([2.5] * 10)

