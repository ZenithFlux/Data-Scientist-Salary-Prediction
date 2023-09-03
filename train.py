from ds_salary_predictor.train_pipeline import trainpipe
from ds_salary_predictor.config import Config

DATASET_PATH = "dataset/salary_data_cleaned.csv"


if __name__ == "__main__":
    _, report_df = trainpipe(DATASET_PATH)

    report_df.to_csv(Config.report_path, index=False)

    print("\n", report_df)