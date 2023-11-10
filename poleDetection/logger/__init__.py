import logging
import os
from datetime import datetime
from from_root import from_root


# LOG_FILE = f"{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log"
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"    # format for log file
log_path = os.path.join(from_root(), "log", LOG_FILE)   # define log path
# log_path = os.path.join(from_root(), 'log', LOG_FILE)
os.makedirs(log_path, exist_ok=True)    # create directory if it does not exist
# os.makedirs(log_path, exist_ok=True)
LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)    # path to store log file

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format = "[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)



# lOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

# logging.basicConfig(
#     filename=lOG_FILE_PATH,
#     format= "[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
#     level= logging.INFO
# )