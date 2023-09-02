from typing import TYPE_CHECKING
import os

import joblib as jl

from .data_processing import process_csv
from .model_trainer import search_and_train
from ..config import Config

if TYPE_CHECKING:
    from os import PathLike

def trainpipe(data_csv_path: 'str | PathLike', model_savepath: 'str | PathLike'=Config.model_path):
    X, Y = process_csv(data_csv_path)
    model, report_df = search_and_train(X, Y)
    
    model_savepath = str(model_savepath)
    os.makedirs(os.path.dirname(model_savepath), exist_ok=True)
    jl.dump(model, model_savepath)
    return model, report_df