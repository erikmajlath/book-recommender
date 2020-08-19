import streamlit as st
import numpy as np
import pandas as pd

"""
# Book Recommender
"""

book_weights = np.load('../data/book_embedding_weights.npy')
book2id = np.load('../data/book_2_id.npy', allow_pickle=True).item()
id2book = np.load('../data/id_2_book.npy', allow_pickle=True).item()
lens = np.linalg.norm(book_weights, axis=1)
normalized = (book_weights.T / lens).T

def neighbors(book, count):
  dists = np.dot(normalized, normalized[book2id[book]])
  closest = np.argsort(dists)[-count:]
  return [(id2book[c], dists[c]) for c in reversed(closest)]



books = np.load('../data/reduced-books.npy', allow_pickle=True)
df = pd.DataFrame(data=books, columns=['isbn', 'title'])
book_filter = ''
book_filter = st.text_input('Please start typing name of the book')
book_filter = book_filter.strip()

if book_filter == '' or len(book_filter) < 3:
  st.stop()

selected_book = st.selectbox(
  'Select book to see recommendations',
  df[df['title'].str.contains(book_filter, case=False)].iloc[:5].values,
  format_func=lambda x: x[1]
)[0]

count = st.slider('How many recommendations would you like?', 0, 40, 10)

results = neighbors(selected_book, count)

def book2title(book):
  book_filter = books[:, 0] == book
  filtered = books[book_filter, 1]

  if len(filtered) == 0:
    return 'Error occured'

  return filtered[0]

"""
## Recommendations
"""

for book, dist in results[1:]:
  st.write(book2title(book), dist)







