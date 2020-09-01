"""Splits dataset in 2 subsamples
"""
from argparse import ArgumentParser
from pathlib import Path

import pandas as pd
import yaml
from sklearn.model_selection import train_test_split

from movie_reviews_classification.utils.types import MovieReviews

SRC_DIR = Path(__file__).resolve().parents[2]


def get_params():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path, help='Input data')
    parser.add_argument('output', type=Path, help='Output directory')
    parser.add_argument('--column', '-c', type=str, help='Column to split')
    args = parser.parse_args()

    with open(SRC_DIR / 'params.yaml') as fd:
        params = yaml.safe_load(fd)
    return args, params['data']


def main():
    cli_args, dvc_params = get_params()
    filename: Path = cli_args.input
    filename = '.'.join(filename.name.split('.')[:-1])

    data: MovieReviews = pd.read_table(cli_args.input)
    train, valid, _, _ = train_test_split(
        data, data[cli_args.column],
        stratify=data[cli_args.column],
        random_state=17,
        test_size=dvc_params['test_size']
    )
    print('Train size:', train.shape[0])
    print('Valid size:', valid.shape[0])
    train.to_csv(cli_args.output / f'{filename}.train.csv', index=False)
    valid.to_csv(cli_args.output / f'{filename}.valid.csv', index=False)


if __name__ == "__main__":
    main()
