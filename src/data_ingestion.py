import os
import pandas as pd
from src.logger import get_logger
from src.custom_exception import CustomException
from config.paths_config import *
from utils.common_functions import read_yaml


logger = get_logger(__name__)

class DataIngestion:

    def __init__(self, config):
        self.config = config["data_ingestion"]
        self.bucket_path = self.config['bucket_path']
        self.file_names = self.config['bucket_file_names']

        os.makedirs(RAW_DIR, exist_ok=True)

        logger.info("Data Ingestion started")

    def csv_file_loader(self):
        for file_name in self.file_names:
            file_path = os.path.join(self.bucket_path, file_name)
            data = pd.read_csv(file_path, nrows=5000000)
            data.to_csv(file_path)
            logger.info("Large file detected and just saved 5 million rows")


if __name__ == "__main__":
    logger.info("Starting Data Ingestion Process....")
    data_ingestion = DataIngestion(read_yaml(CONFIG_PATH))
    data_ingestion.csv_file_loader()