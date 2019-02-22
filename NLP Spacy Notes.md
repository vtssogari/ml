# NLP using Spacy Notest

## installation

CPU only installation
```
conda install -c conda-forge spacy
```
or
```
pip install -U spacy
```

GPU
```
pip install -U spacy[cuda92]
```

```
import spacy

spacy.prefer_gpu()
nlp = spacy.load('en_core_web_sm')
```

## download the language model 

English with 3 different sizes 
Use large size for production usage
```
python -m spacy download en_core_web_sm 
python -m spacy download en_core_web_md
python -m spacy download en_core_web_lg
```

## Customizing Word Vectors 

https://spacy.io/usage/vectors-similarity

Converting word vectors for use in spaCyV2.0.10
Custom word vectors can be trained using a number of open-source libraries, such as Gensim, Fast Text, or Tomas Mikolov's original word2vec implementation.

```
wget https://s3-us-west-1.amazonaws.com/fasttext-vectors/word-vectors-v2/cc.la.300.vec.gz
python -m spacy init-model en /tmp/la_vectors_wiki_lg --vectors-loc cc.la.300.vec.gz
```

PubMed and PMC word vectors 

http://bio.nlplab.org
http://evexdb.org/pmresources/vec-space-models/

## Train the Named Entity Recognizer 

https://spacy.io/usage/training#ner

## visualize

```
print(spacy.displacy.render(doc, style="ent", jupyter=True, page="true"))
```




