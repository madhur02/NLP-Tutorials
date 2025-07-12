import numpy as np
from sklearn.metrics.pairwise import pairwise_distances


def dist1(a, b):
    return np.linalg.norm(a - b)
def dist2(a, b):
    return 1 - a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b))

# pick a distance type
dist, metric = dist2, 'cosine'
## faster
def find_analogies(w1, w2, w3):
  for w in (w1, w2, w3):
    if w not in word2vec:
      print("%s not in dictionary" % w)
      return

  king = word2vec[w1]
  man = word2vec[w2]
  woman = word2vec[w3]
  v0 = king - man + woman

  distances = pairwise_distances(v0.reshape(1, D), embedding, metric=metric).reshape(V)
  idxs = distances.argsort()[:4]
  for idx in idxs:
    word = idx2word[idx]
    if word not in (w1, w2, w3): 
      best_word = word
      break

  print(w1, "-", w2, "=", best_word, "-", w3)


def nearest_neighbors(w, n=5):
  if w not in word2vec:
    print("%s not in dictionary:" % w)
    return

  v = word2vec[w]
  distances = pairwise_distances(v.reshape(1, D), embedding, metric=metric).reshape(V)
  idxs = distances.argsort()[1:n+1]
  print("neighbors of: %s" % w)
  for idx in idxs:
    print("\t%s" % idx2word[idx])

word2vec = {}
embedding = []
idx2word = []
with open(r'glove.6B.300d.txt', encoding='utf-8') as f:
  # is just a space-separated text file in the format:
  # word vec[0] vec[1] vec[2] ...
  for line in f:
    
    #print("This is the first line:::", line)
    values = line.split()
    #print("Value after split() method:::", values)
    word = values[0]
    #print("picking forst word value[0]:::", word)
    vec = np.asarray(values[1:], dtype='float32')
    
    word2vec[word] = vec
    embedding.append(vec)
    idx2word.append(word)
print('Found %s word vectors.' % len(word2vec))
embedding = np.array(embedding)
V, D = embedding.shape
