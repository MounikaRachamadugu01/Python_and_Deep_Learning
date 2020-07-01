"""

Apply the following on the “input.txt” of Question 3 response file and show output:
a. Tokenization b. POS c. Stemming d. Lemmatization e. Trigram f. Named Entity Recognition

"""

import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk.util import ngrams
from nltk import ne_chunk

# reading input.txt file
text = open('input.txt', encoding="utf8").read()

# Tokenization
wtokens = word_tokenize(text)
stokens = sent_tokenize(text)
print("\n Word tokens:", wtokens)
print("\n Sentence tokens:", stokens)

# POS
pos = nltk.pos_tag(wtokens)
print("\n Parts of Speech:", pos)

# Stemming
pstem = PorterStemmer()
lstem = LancasterStemmer()
sstem = SnowballStemmer("english")
pstem_output = ' '.join([pstem.stem(w) for w in wtokens])
lstem_output = ' '.join([lstem.stem(w) for w in wtokens])
sstem_output = ' '.join([sstem.stem(w) for w in wtokens])
print("\n PorterStemmer Stemming:\n", pstem_output)
print("\n LancasterStemmer Stemming:\n", lstem_output)
print("\n SnowballStemmer Stemming:\n", sstem_output)

# Lemmatization
lemmatizer = WordNetLemmatizer()
lem_output = ' '.join([lemmatizer.lemmatize(w) for w in wtokens])
print("\n Lemmatization: \n", lem_output)

# Trigram
trigrams = ngrams(wtokens, 3)
print("\n Trigrams: ", list(trigrams))

# Named Entity Recognition
ner = ne_chunk(pos)
print("\nNamed Entity Recognition :", ner)