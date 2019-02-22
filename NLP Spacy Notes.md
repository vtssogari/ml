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

English with 3 different sizes *use large size for production usage
```
python -m spacy download en_core_web_sm 
python -m spacy download en_core_web_md
python -m spacy download en_core_web_lg
```
