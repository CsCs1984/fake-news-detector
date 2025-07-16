from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def train_sentiment_model(texts, labels):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(texts)
    
    model = MultinomialNB()
    model.fit(X, labels)
    
    return model, vectorizer
