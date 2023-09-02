from ds_salary_predictor.train_pipeline import trainpipe
from ds_salary_predictor.config import Config

_, report_df = trainpipe("dataset/salary_data_cleaned.csv")

report_df.to_csv(Config.report_path, index=False)

print("\n", report_df)