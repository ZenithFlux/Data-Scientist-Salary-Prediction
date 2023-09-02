from typing import TYPE_CHECKING

import pandas as pd
import numpy as np

from ..logger import log

if TYPE_CHECKING:
    from os import PathLike


def process_csv(csv_path: 'str | PathLike'):
    "Reads CSV in format of original dataset, and returns arrays of features and targets."
