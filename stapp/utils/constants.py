from pyprojroot import here


class Constants:
    pass
    # ROOT PATH
    ROOT_PATH = here()
    # STREAMLIT ROOT PATH
    STREAMLIT_ROOT_PATH = ROOT_PATH.joinpath("stapp")
    # API ROOT PATH
    API_ROOT_PATH = ROOT_PATH.joinpath("stapp", "api")
    # DATA PATH
    DATA_PATH = ROOT_PATH.joinpath("stapp", "data")
    # FILE URLs
    INDEX_2018_CSV_FILE_PATH = "Index2018.csv"
