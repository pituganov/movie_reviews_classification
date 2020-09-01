"""Module for datasets desctiption"""
from typing import Union
from collections import namedtuple

import pandas as pd

MovieReviews = Union[pd.DataFrame, namedtuple("MovieReviews", ['id', 'sentiment', 'review'])]
