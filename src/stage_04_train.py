import argparse
import os
from tqdm import tqdm
import logging
from src.utils.common import read_yaml, create_directories
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier

STAGE = "stage 04 training"  

logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )


def main(config_path, params_path):
    ## read config files
    config = read_yaml(config_path)
    params = read_yaml(params_path)

    artifacts = config["artifacts"]
    featurized_data_dir_path = os.path.join(artifacts["ARTIFACTS_DIR"], artifacts["FEATURIZED_DATA"])
    featurized_train_data_path = os.path.join(featurized_data_dir_path, artifacts["FEATURIZED_TRAIN_DATA"])
 
    model_dir_path = os.path.join(artifacts["ARTIFACTS_DIR"], artifacts["MODEL_DIR"])
    create_directories([model_dir_path])

    model_path = os.path.join(model_dir_path, artifacts["MODEL_NAME"])

    matrix = joblib.load(featurized_train_data_path)
    labels = np.squeeze(matrix[:, 1].toarray())
    X = matrix[:, 2:]

    logging.info(f"input matrix size: {matrix.shape}")
    logging.info(f"X matrix size: {X.shape}")
    logging.info(f"y matrix size or label size: {labels.shape}")

    seed = params["train"]["seed"]
    n_est = params["train"]["n_est"]
    min_split = params["train"]["min_split"]

    model = RandomForestClassifier(
        n_estimators=n_est, min_samples_split=min_split, n_jobs=2, random_state=seed
    )

    model.fit(X, labels)

    joblib.dump(model, model_path)
    logging.info(f"model is trained and saved at: {model_path}")

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="configs/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")
    parsed_args = args.parse_args()

    try:
        logging.info("\n********************")
        logging.info(f">>>>> stage {STAGE} started <<<<<")
        main(config_path=parsed_args.config, params_path=parsed_args.params)
        logging.info(f">>>>> stage {STAGE} completed!<<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise e