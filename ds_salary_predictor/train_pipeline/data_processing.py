from typing import TYPE_CHECKING

import pandas as pd
import numpy as np

from ..logger import log

if TYPE_CHECKING:
    from os import PathLike
    from pandas import DataFrame


def process_csv(csv_path: 'str | PathLike'):
    "Reads CSV in format of original dataset, and returns arrays of features and targets."
    
    df = pd.read_csv(csv_path)
    df = clean_df(df)
    arr = df.to_numpy()
    
    log.info("Data Transformation complete!")
    return arr[:,:-1], arr[:,-1]


def clean_df(df: 'DataFrame'):
    "Clean the original dataframe"
    
    df = df[["Rating", "hourly","same_state", "python_yn", "R_yn", "spark", "aws", "excel", "avg_salary"]]
    df.apply(lambda x: np.float32(x))
    
    neg_rows = set()
    for col in df:
        for i, val in enumerate(df[col]):
            if val<0: neg_rows.add(i)
            
    df = df.drop(index=list(neg_rows))
    df = df.dropna()
    df = df.reset_index(drop=True)
    return df