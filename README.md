# movie_reviews_classification

Project for kaggle competition [Bag of Words Meets Bags of Popcorn](https://www.kaggle.com/c/word2vec-nlp-tutorial/overview)

## Reproduce experiments

### 1. Install dependencies

```bash
pip install -r reuqirements.txt
pip install -e .
```

### 2. Reproduce datasets

```bash
dvc repro split
```

### 3. Train model

```bash
python -m deeppavlov train models/$MODEL_NAME
```

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
