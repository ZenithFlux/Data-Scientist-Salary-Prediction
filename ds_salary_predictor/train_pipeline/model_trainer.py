from typing import TYPE_CHECKING

from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
from xgboost import XGBRegressor
from sklearn.model_selection import GridSearchCV
import pandas as pd

from ..logger import log

if TYPE_CHECKING:
    from numpy import ndarray


models = {"LR": {"model": LinearRegression(),
                 "params": {}},
         "SVR": {"model": SVR(),
                 "params": {
                     "C": [0.01, 0.1, 1],
                     "gamma": ["scale", "auto"]
                 }},
         "Random Forest": {
             "model": RandomForestRegressor(random_state=350),
             "params":{
                 "n_estimators": [10, 50, 100, 500]
             }},
         "MLP": {
             "model": MLPRegressor(random_state=651),
             "params": {
                 "hidden_layer_sizes": [
                     [100],
                     [100, 10],
                     [1000, 100, 10]
                 ],
                 "learning_rate_init": [0.0001, 0.001, 0.01, 0.1],
                 "early_stopping": [True, False]
             }
         },
         "XGBoost": {"model": XGBRegressor(random_state=600),
                     "params": {
                         "learning_rate": [0.01, 0.3, 1]
                     }}}
        

        
def search_and_train(X: 'ndarray', Y: 'ndarray'):
    "Returns best model trained and a dataframe of model performance report"
    
    best_score = None
    best_model = None
    report = {"Model": [], "best_params": [], "RMSE": [], "R2": []}
    
    log.info("Training started!")
    for name, m in models.items():
        gscv = GridSearchCV(m["model"], m["params"], 
                            scoring=("neg_root_mean_squared_error", "r2"),
                            refit="neg_root_mean_squared_error",
                            verbose=1)
        gscv.fit(X, Y)
        
        mean_test_rmse = gscv.cv_results_["mean_test_neg_root_mean_squared_error"][gscv.best_index_]
        assert mean_test_rmse == gscv.best_score_, \
            f"Best Scores are different: {mean_test_rmse} and {gscv.best_score_}"
        
        report["Model"].append(name)
        report["best_params"].append(gscv.best_params_)
        report["RMSE"].append(-gscv.best_score_)
        report["R2"].append(gscv.cv_results_["mean_test_r2"][gscv.best_index_])
        
        if best_score is None or gscv.best_score_ > best_score:
            best_score = gscv.best_score_
            best_model = gscv.best_estimator_
    
    log.debug(f"Best Score: {-best_score}")
    log.info("Training finished!")
    return best_model, pd.DataFrame(report)