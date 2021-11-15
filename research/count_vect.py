from sklearn.feature_extraction.text import CountVectorizer


examples = [
    "apple ball cat",
    "ball cat dog",
]

# vectorizer = CountVectorizer()
# X = vectorizer.fit_transform(examples)

# print(vectorizer.get_feature_names_out())
# print(X.toarray())


max_features = 3
ngrams = 2

vectorizer = CountVectorizer(max_features=max_features, ngram_range=(1, ngrams))

X = vectorizer.fit_transform(examples)

print(vectorizer.get_feature_names_out())
print(X.toarray())
