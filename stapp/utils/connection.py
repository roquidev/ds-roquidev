import pandas as pd
import logging


class Connection:
    def __init__(self):
        # Configure the logging module
        logging.basicConfig(level=logging.INFO)
        self.__logger = logging.getLogger(__name__)

    def read_data(self, path, file_name):
        """
        Read a file using pandas.

        Parameters:
        - path (str): Directory path where the file is located.
        - file_name (str): Name of the file to read.

        Returns:
        - DataFrame: Pandas DataFrame object or None if reading fails.
        """
        file_path = path.joinpath(file_name)

        allowed_formats = ["csv", "parquet", "avro", "xlsx"]

        for file_format in allowed_formats:
            try:
                if file_format == "csv":
                    return pd.read_csv(file_path)
                elif file_format == "parquet":
                    return pd.read_parquet(file_path)
                elif file_format == "avro":
                    return pd.read_avro(file_path)
                elif file_format == "xlsx":
                    return pd.read_excel(file_path)
            except (pd.errors.EmptyDataError, pd.errors.ParserError, pd.errors.UnsupportedFunctionCall, Exception) as e:
                self.__logger.warning(f"Unable to read as {file_format}. Error: {str(e)}")

        self.__logger.error("Unable to read the file. Make sure it is in a supported format.")
        return None
