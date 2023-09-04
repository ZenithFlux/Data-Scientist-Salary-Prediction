import joblib as jl

from ds_salary_predictor.config import Config


model = jl.load(Config.model_path)
pred = model.predict([[3.5, 0, 1, 1, 0, 0, 0, 0]])

if isinstance(pred[0], float):
    print("Model inference test passed!")
else:
    raise Exception("Test Failed!")