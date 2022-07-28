import logging
from datetime import datetime
import os
LOG_DIR="Maintanance_logging"   # log directory name

CURRENT_TIME_STAMP=f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"  # assigning current time stamp for loging

LOG_FILE_NAME=f"log_{CURRENT_TIME_STAMP}.log"  # initializing the log file name with time stamp

os.makedirs(LOG_DIR,exist_ok=True) # creating the directory for log file

LOG_FILE_PATH =os.path.join(LOG_DIR,LOG_FILE_NAME) # assigning the file path to save the file

logging.basicConfig(filename=LOG_FILE_PATH,
filemode="w",
format='[%(asctime)s]^;%(levelname)s^;%(lineno)d^;%(filename)s^;%(funcName)s()^;%(message)s',
level=logging.INFO
)     # creating custom logging
