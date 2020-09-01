from typing import List

import click
from dotenv import load_dotenv, find_dotenv
import mlflow.sklearn
import sklearn


def load_model(model_path: str):
    model = mlflow.sklearn.load_model(model_path)
    return model


def predict(model: sklearn.base.BaseEstimator, X: List[float]) -> str:
    y_pred = model.predict([X])[0]
    classes = ['Iris-Setosa', 'Iris-Versicolour', 'Iris-Virginica']
    return classes[y_pred - 1]


@click.command()
@click.argument('model_path', type=str)
@click.argument('sepal_length', type=float)
@click.argument('sepal_width', type=float)
@click.argument('petal_length', type=float)
@click.argument('petal_width', type=float)
def main(model_path, **X):
    model = load_model(model_path)
    pred = predict(model, list(X.values()))
    print(pred)


if __name__ == '__main__':
    load_dotenv(find_dotenv())
    main()