from flask import Flask, request
import sys

import pip
from maintanance.entity import maintanance_predictor
from maintanance.utils.util import read_yaml_file, write_yaml_file
from matplotlib.style import context
from maintanance.logger import logging
from maintanance.exception import maintananceException
import os, sys
import json
from maintanance.config.configuration import configuration
from maintanance.constant import CONFIG_DIR,get_current_time_stamp
from maintanance.pipeline.pipeline import Pipeline
from maintanance.entity.maintanance_predictor import MaintanancePredictor, MaintananceData
from flask import send_file, abort, render_template


ROOT_DIR = os.getcwd()
LOG_FOLDER_NAME = "Maintanance_logging"
PIPELINE_FOLDER_NAME = "maintanance"
SAVED_MODELS_DIR_NAME = "saved_models"
MODEL_CONFIG_FILE_PATH = os.path.join(ROOT_DIR, CONFIG_DIR, "model.yaml")
LOG_DIR = os.path.join(ROOT_DIR, LOG_FOLDER_NAME)
PIPELINE_DIR = os.path.join(ROOT_DIR, PIPELINE_FOLDER_NAME)
MODEL_DIR = os.path.join(ROOT_DIR, SAVED_MODELS_DIR_NAME)


from maintanance.logger import get_log_dataframe

MAINTANANCE_DATA_KEY = "maintanance_data"
MAINTANANCE_LABEL_VALUE_KEY = "maintanance_label_value"

app = Flask(__name__)


@app.route('/artifact', defaults={'req_path': 'maintanance'})
@app.route('/artifact/<path:req_path>')
def render_artifact_dir(req_path):
    os.makedirs("maintanance", exist_ok=True)
    # Joining the base and the requested path
    print(f"req_path: {req_path}")
    abs_path = os.path.join(req_path)
    print(abs_path)
    # Return 404 if path doesn't exist
    if not os.path.exists(abs_path):
        return abort(404)

    # Check if path is a file and serve
    if os.path.isfile(abs_path):
        if ".html" in abs_path:
            with open(abs_path, "r", encoding="utf-8") as file:
                content = ''
                for line in file.readlines():
                    content = f"{content}{line}"
                return content
        return send_file(abs_path)

    # Show directory contents
    files = {os.path.join(abs_path, file_name): file_name for file_name in os.listdir(abs_path) if
             "artifact" in os.path.join(abs_path, file_name)}

    result = {
        "files": files,
        "parent_folder": os.path.dirname(abs_path),
        "parent_label": abs_path
    }
    return render_template('files.html', result=result)


@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return str(e)


@app.route('/view_experiment_hist', methods=['GET', 'POST'])
def view_experiment_history():
    experiment_df = Pipeline.get_experiments_status()
    context = {
        "experiment": experiment_df.to_html(classes='table table-striped col-12')
    }
    return render_template('experiment_history.html', context=context)


@app.route('/train', methods=['GET', 'POST'])
def train():
    message = ""
    pipeline = Pipeline(config=configuration(current_time_stamp=get_current_time_stamp()))
    if not Pipeline.experiment.running_status:
        message = "Training started."
        pipeline.start()
    else:
        message = "Training is already in progress."
    context = {
        "experiment": pipeline.get_experiments_status().to_html(classes='table table-striped col-12'),
        "message": message
    }
    return render_template('train.html', context=context)


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    context = {
        MAINTANANCE_DATA_KEY: None,
        MAINTANANCE_LABEL_VALUE_KEY: None
    }

    if request.method == 'POST':
                
        Cycle = int(request.form['Cycle'])
        OpSet1 = float(request.form['OpSet1'])
        OpSet2 = float(request.form['OpSet2'])
        OpSet3 = float(request.form['OpSet3'])
        SensorMeasure1 = float(request.form['SensorMeasure1'])
        SensorMeasure2 = float(request.form['SensorMeasure2'])
        SensorMeasure3 = float(request.form['SensorMeasure3'])
        SensorMeasure4 = float(request.form['SensorMeasure4'])
        SensorMeasure5 = float(request.form['SensorMeasure5'])
        SensorMeasure6 = float(request.form['SensorMeasure6'])
        SensorMeasure7 = float(request.form['SensorMeasure7'])
        SensorMeasure8 = float(request.form['SensorMeasure8'])
        SensorMeasure9 = float(request.form['SensorMeasure9'])
        SensorMeasure10 = float(request.form['SensorMeasure10'])
        SensorMeasure11 = float(request.form['SensorMeasure11'])
        SensorMeasure12 = float(request.form['SensorMeasure12'])
        SensorMeasure13 = float(request.form['SensorMeasure13'])
        SensorMeasure14 = float(request.form['SensorMeasure14'])
        SensorMeasure15 = float(request.form['SensorMeasure15'])
        SensorMeasure16 = float(request.form['SensorMeasure16'])
        SensorMeasure17 = int(request.form['SensorMeasure17'])
        SensorMeasure18 = int(request.form['SensorMeasure18'])
        SensorMeasure19 = float(request.form['SensorMeasure19'])
        SensorMeasure20 = float(request.form['SensorMeasure20'])
        SensorMeasure21 = float(request.form['SensorMeasure21'])
        Life_Ratio = float(request.form['Life_Ratio'])



        maintanance_data = MaintananceData( Cycle=Cycle,
                                            OpSet1=OpSet1,
                                            OpSet2=OpSet2,
                                            OpSet3=OpSet3,
                                            SensorMeasure1=SensorMeasure1,
                                            SensorMeasure2=SensorMeasure2,
                                            SensorMeasure3=SensorMeasure3,
                                            SensorMeasure4=SensorMeasure4,
                                            SensorMeasure5=SensorMeasure5,
                                            SensorMeasure6=SensorMeasure6,
                                            SensorMeasure7=SensorMeasure7,
                                            SensorMeasure8=SensorMeasure8,
                                            SensorMeasure9=SensorMeasure9,
                                            SensorMeasure10=SensorMeasure10,
                                            SensorMeasure11=SensorMeasure11,
                                            SensorMeasure12=SensorMeasure12,
                                            SensorMeasure13=SensorMeasure13,
                                            SensorMeasure14=SensorMeasure14,
                                            SensorMeasure15=SensorMeasure15,
                                            SensorMeasure16=SensorMeasure16,
                                            SensorMeasure17=SensorMeasure17,
                                            SensorMeasure18=SensorMeasure18,
                                            SensorMeasure19=SensorMeasure19,
                                            SensorMeasure20=SensorMeasure20,
                                            SensorMeasure21=SensorMeasure21,
                                            Life_Ratio=Life_Ratio)
        maintanance_df = maintanance_data.get_maintanance_input_data_frame()
        maintanance_predictor = MaintanancePredictor(model_dir=MODEL_DIR)
        maintanance_lable_value = maintanance_predictor.predict(X=maintanance_df)
        context = {
            MAINTANANCE_DATA_KEY: maintanance_data.get_maintanance_data_as_dict(),
            MAINTANANCE_LABEL_VALUE_KEY: maintanance_lable_value,
        }
        return render_template('predict.html', context=context)
    return render_template("predict.html", context=context)


@app.route('/saved_models', defaults={'req_path': 'saved_models'})
@app.route('/saved_models/<path:req_path>')
def saved_models_dir(req_path):
    os.makedirs("saved_models", exist_ok=True)
    # Joining the base and the requested path
    print(f"req_path: {req_path}")
    abs_path = os.path.join(req_path)
    print(abs_path)
    # Return 404 if path doesn't exist
    if not os.path.exists(abs_path):
        return abort(404)

    # Check if path is a file and serve
    if os.path.isfile(abs_path):
        return send_file(abs_path)

    # Show directory contents
    files = {os.path.join(abs_path, file): file for file in os.listdir(abs_path)}

    result = {
        "files": files,
        "parent_folder": os.path.dirname(abs_path),
        "parent_label": abs_path
    }
    return render_template('saved_models_files.html', result=result)


@app.route("/update_model_config", methods=['GET', 'POST'])
def update_model_config():
    try:
        if request.method == 'POST':
            model_config = request.form['new_model_config']
            model_config = model_config.replace("'", '"')
            print(model_config)
            model_config = json.loads(model_config)

            write_yaml_file(file_path=MODEL_CONFIG_FILE_PATH, data=model_config)

        model_config = read_yaml_file(file_path=MODEL_CONFIG_FILE_PATH)
        return render_template('update_model.html', result={"model_config": model_config})

    except  Exception as e:
        logging.exception(e)
        return str(e)


@app.route(f'/Maintanance_logging', defaults={'req_path': f'{LOG_FOLDER_NAME}'})
@app.route(f'/{LOG_FOLDER_NAME}/<path:req_path>')
def render_log_dir(req_path):
    os.makedirs(LOG_FOLDER_NAME, exist_ok=True)
    # Joining the base and the requested path
    logging.info(f"req_path: {req_path}")
    abs_path = os.path.join(req_path)
    print(abs_path)
    # Return 404 if path doesn't exist
    if not os.path.exists(abs_path):
        return abort(404)

    # Check if path is a file and serve
    if os.path.isfile(abs_path):
        log_df = get_log_dataframe(abs_path)
        context = {"log": log_df.to_html(classes="table-striped", index=False)}
        return render_template('log.html', context=context)

    # Show directory contents
    files = {os.path.join(abs_path, file): file for file in os.listdir(abs_path)}

    result = {
        "files": files,
        "parent_folder": os.path.dirname(abs_path),
        "parent_label": abs_path
    }
    return render_template('log_files.html', result=result)


if __name__ == "__main__":
    app.run()
