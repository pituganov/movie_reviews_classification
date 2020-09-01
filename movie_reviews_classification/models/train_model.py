import mlflow
import mlflow.sklearn
import pandas as pd
from dotenv import find_dotenv, load_dotenv
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split

load_dotenv(find_dotenv())

if __name__ == '__main__':
    mlflow.set_experiment('Experiment')
    mlflow.start_run()

    X = pd.read_csv('data/raw/X.csv')
    y = pd.read_csv('data/raw/y.csv').values.ravel()

    X_train, X_test, y_train, y_test = train_test_split(X,
                                                        y,
                                                        shuffle=True,
                                                        test_size=0.3)

    clf = RandomForestClassifier(n_estimators=100)
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)

    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')

    mlflow.log_param('n_estimators', clf.n_estimators)
    mlflow.log_metric('precision', precision)
    mlflow.log_metric('recall', recall)
    mlflow.log_metric('f1', f1)

    mlflow.sklearn.log_model(clf, 'model')

    mlflow.end_run()
