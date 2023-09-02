from typing import TYPE_CHECKING

import pandas as pd
import numpy as np

from ..logger import log

if TYPE_CHECKING:
    from os import PathLike


def process_csv(csv_path: 'str | PathLike'):
    "Reads CSV in format of original dataset, and returns arrays of features and targets."
    
    df = pd.read_csv(csv_path)
    df = df[["Rating", "hourly", "employer_provided",
             "same_state", "python_yn", "R_yn", "spark", "aws", "excel", "avg_salary"]]
    df.apply(lambda x: np.float32(x))
    
    neg_rows = set()
    for col in df:
        for i, val in enumerate(df[col]):
            if val<0: neg_rows.add(i)
            
    df = df.drop(index=list(neg_rows))
    df = df.dropna()
    df = df.reset_index(drop=True)
    arr = df.to_numpy()
    
    log.info("Data Transformation complete!")
    return arr[:,:-1], arr[:,-1] 