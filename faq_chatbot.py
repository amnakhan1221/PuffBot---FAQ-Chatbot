import string
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# FAQ dataset
faqs = {
    "What is your return policy?": "You can return any product within 30 days of purchase.",
    "Do you offer free shipping?": "Yes, we offer free shipping on orders above $50.",
    "How can I track my order?": "Once your order is shipped, we will send you a tracking link via email.",
    "What payment methods are accepted?": "We accept credit cards, debit cards, PayPal, and online banking.",
    "Do you have customer support?": "Yes, our customer support is available 24/7 via chat or email."
}

def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text

faq_questions = list(faqs.keys())
faq_answers = list(faqs.values())

processed_questions = [preprocess(q) for q in faq_questions]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(processed_questions)

def get_response(user_input):
    processed_input = preprocess(user_input)
    user_vec = vectorizer.transform([processed_input])
    similarity = cosine_similarity(user_vec, X)
    idx = np.argmax(similarity)
    score = similarity[0][idx]
    # lower threshold to match similar questions
    if score > 0.1:
        return faq_answers[idx]
    else:
        return "Sorry, I don’t have an answer for that."
