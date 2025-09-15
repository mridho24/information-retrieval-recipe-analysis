from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np


resep_soto = "ayam bawang merah bawang putih kemiri jahe kunyit serai daun salam garam merica"
resep_rendang = "daging sapi santan kelapa bawang merah bawang putih cabai jahe lengkuas kunyit serai daun kunyit asam kandis"
resep_gado = "kacang tanah cabai bawang putih kencur gula merah asam jawa santan tahu tempe tauge kangkung garam"
resep_opor = "ayam santan bawang merah bawang putih kemiri ketumbar jintan merica serai lengkuas daun salam"

corpus = [resep_soto, resep_rendang, resep_gado, resep_opor]

print("=== KORPUS RESEP ===")
print("1. Soto:", resep_soto)
print("2. Rendang:", resep_rendang)
print("3. Gado-gado:", resep_gado)
print("4. Opor:", resep_opor)
print()


vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)

print("=== INFORMASI VECTORIZER ===")
print(f"Jumlah fitur (bahan unik): {len(vectorizer.get_feature_names_out())}")
print(f"Bahan-bahan: {list(vectorizer.get_feature_names_out())}")
print()


df = pd.DataFrame(X.toarray(), 
                  columns=vectorizer.get_feature_names_out(),
                  index=['Soto', 'Rendang', 'Gado-gado', 'Opor'])

print("=== TERM-DOCUMENT MATRIX ===")
print(df)
print()


print("=== ANALISIS KEMIRIPAN ===")


soto_vector = df.iloc[0]
similarities_with_soto = {}

for idx, resep_name in enumerate(['Rendang', 'Gado-gado', 'Opor']):
    other_vector = df.iloc[idx + 1]
   
    similarity = np.dot(soto_vector, other_vector)
    similarities_with_soto[resep_name] = similarity

print("Kemiripan dengan Soto (berdasarkan jumlah bahan yang sama):")
for resep, similarity in similarities_with_soto.items():
    print(f"  {resep}: {similarity} bahan sama")


most_similar = max(similarities_with_soto, key=similarities_with_soto.get)
print(f"\nResep paling mirip dengan Soto: {most_similar}")


soto_ingredients = set(df.columns[df.iloc[0] > 0])
most_similar_idx = list(df.index).index(most_similar)
similar_ingredients = set(df.columns[df.iloc[most_similar_idx] > 0])
common_ingredients = soto_ingredients.intersection(similar_ingredients)
print(f"Bahan yang sama: {', '.join(sorted(common_ingredients))}")
print()


print("=== BAHAN UNIK (hanya muncul di satu resep) ===")
unique_ingredients = []
for ingredient in df.columns:
    count = (df[ingredient] > 0).sum()
    if count == 1:
        resep_with_ingredient = df.index[df[ingredient] > 0].tolist()[0]
        unique_ingredients.append((ingredient, resep_with_ingredient))

print(f"Ditemukan {len(unique_ingredients)} bahan unik:")
for ingredient, resep in unique_ingredients:
    print(f"  {ingredient} → hanya di {resep}")
print()


print("=== BUMBU/BAHAN UMUM ===")
common_ingredients_count = {}
for ingredient in df.columns:
    count = (df[ingredient] > 0).sum()
    common_ingredients_count[ingredient] = count


sorted_ingredients = sorted(common_ingredients_count.items(), 
                          key=lambda x: x[1], reverse=True)

print("Frekuensi kemunculan bahan (dari yang paling sering):")
for ingredient, count in sorted_ingredients:
    print(f"  {ingredient}: muncul di {count}/4 resep")

print(f"\nBumbu paling umum: {sorted_ingredients[0][0]} (muncul di {sorted_ingredients[0][1]} resep)")
print()


print("=== BONUS: ANALISIS QUERY BARU ===")
query_resep = "ayam santan kunyit serai"
query_vec = vectorizer.transform([query_resep])

print(f"Query: {query_resep}")


query_df = pd.DataFrame(query_vec.toarray(), 
                       columns=vectorizer.get_feature_names_out(),
                       index=['Query'])

print("\nVektor query:")
query_ingredients = [col for col in query_df.columns if query_df[col].iloc[0] > 0]
print(f"Bahan dalam query: {', '.join(query_ingredients)}")


print("\nKemiripan query dengan setiap resep:")
similarities_with_query = {}
for idx, resep_name in enumerate(df.index):
    resep_vector = df.iloc[idx]
    query_vector = query_df.iloc[0]
    similarity = np.dot(resep_vector, query_vector)
    similarities_with_query[resep_name] = similarity
    
    
    resep_ingredients = set(df.columns[df.iloc[idx] > 0])
    query_ingredients_set = set(query_df.columns[query_df.iloc[0] > 0])
    common = resep_ingredients.intersection(query_ingredients_set)
    
    print(f"  {resep_name}: {similarity} bahan sama {sorted(common)}")


best_match = max(similarities_with_query, key=similarities_with_query.get)
print(f"\nResep yang paling mendekati query: {best_match}")
print(f"dengan {similarities_with_query[best_match]} bahan yang sama")


print("\n" + "="*25)
print("RINGKASAN ANALISIS")
print("="*25)
print(f"• Total bahan unik dalam dataset: {len(vectorizer.get_feature_names_out())}")
print(f"• Bahan yang hanya muncul sekali: {len(unique_ingredients)}")
print(f"• Bumbu paling umum: {sorted_ingredients[0][0]}")
print(f"• Resep paling mirip dengan Soto: {most_similar}")
print(f"• Query '{query_resep}' paling cocok dengan: {best_match}")