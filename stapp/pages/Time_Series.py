import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd


# Internasl modules
from utils.connection import Connection
from utils.constants import Constants

connection = Connection()
constants = Constants()

# Load dataset
index_2018_df = connection.read_data(constants.DATA_PATH, str(constants.INDEX_2018_CSV_FILE_PATH))   # noqa: E501

# Overview of datset
st.write("Este es una vista general de los campos del dataset:")
st.table(index_2018_df.head(3))

# Two columns
col1, col2 = st.columns(spec=[0.7, 0.3], gap="small")

# 
col1.write("Descripcion de las características principales del dataset:")
col1.table(index_2018_df.describe())


# Missing values
col2.write("Valores nulos")
col2.table(pd.DataFrame({
    "campos": index_2018_df.isna().sum().index,
    "cantidad_nulos": index_2018_df.isna().sum().values
    }))

st.subheader("Graficos de Series de tiempo")

# Time series plot

