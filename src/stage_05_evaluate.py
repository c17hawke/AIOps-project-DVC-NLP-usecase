import argparse
import os
import joblib
import logging
from src.utils.common import read_yaml, save_json
import numpy as np
import sklearn.metrics as metrics
import math

STAGE = "stage 05 evaluate" ## <<< change stage name 

logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )


def main(config_path):
    ## read config files
    config = read_yaml(config_path)
    artifacts = config["artifacts"]
    featurized_data_dir_path = os.path.join(artifacts["ARTIFACTS_DIR"], artifacts["FEATURIZED_DATA"])
    featurized_test_data_path = os.path.join(featurized_data_dir_path, artifacts["FEATURIZED_TEST_DATA"])

    model_dir_path = os.path.join(artifacts["ARTIFACTS_DIR"], artifacts["MODEL_DIR"])
    model_path = os.path.join(model_dir_path, artifacts["MODEL_NAME"])

    model = joblib.load(model_path)
    matrix = joblib.load(featurized_test_data_path)

    labels = np.squeeze(matrix[:, 1].toarray())
    X = matrix[:,2:]

    prediction_by_class = model.predict_proba(X)
    predictions = prediction_by_class[:, 1]

    PRC_json_path = config["plots"]["PRC"]
    ROC_json_path = config["plots"]["ROC"]

    scores_json_path = config["metrics"]["SCORES"]

    avg_prec = metrics.average_precision_score(labels, predictions)
    roc_auc = metrics.roc_auc_score(labels, predictions)

    scores = {
        "avg_prec": avg_prec,
        "roc_auc": roc_auc
    }

    save_json(scores_json_path, scores)
    
    precision, recall, prc_threshold = metrics.precision_recall_curve(labels, predictions)
    nth_points = math.ceil(len(prc_threshold) / 1000)
    prc_points = list(zip(precision, recall, prc_threshold))[::nth_points]

    prc_data = {
        "prc": [
            {"precision": p, "recall": r, "threshold": t} 
            for p,r,t in prc_points
        ]
    }

    save_json(PRC_json_path, prc_data)

    fpr, tpr, roc_threshold = metrics.roc_curve(labels, predictions)

    roc_data = {
        "roc": [
            {"fpr": fp, "tpr": tp, "threshold": t}
            for fp, tp, t in zip(fpr, tpr, roc_threshold)
        ]
    } 

    save_json(ROC_json_path, roc_data)


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="configs/config.yaml")
    parsed_args = args.parse_args()

    try:
        logging.info("\n********************")
        logging.info(f">>>>> stage {STAGE} started <<<<<")
        main(config_path=parsed_args.config)
        logging.info(f">>>>> stage {STAGE} completed!<<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise e