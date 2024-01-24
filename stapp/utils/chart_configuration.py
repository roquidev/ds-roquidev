# Import external modules
import streamlit as st
import pandas as pd
from typing import Tuple
import plotly.express as px
import plotly.graph_objects as go

# Import internal modules


class ChartConfiguration:
    def __init__(self) -> None:
        self.__fig = go.Figure()
        
        pass

    def plot_line_chartr(self, df: pd.DataFrame, title: str, subtitle: str, title_position: Tuple):
        # Crear la figura
        fig = px.line(df, x="Date", y=["Adj Close"])
        # Personalizar el aspecto de la gráfica
        fig.update_layout(
            title={
                "text": title,
                "x": title_position[0],
                "y": title_position[1],
                "font": dict(size=16)
                },
            xaxis_title="Fecha (Años)",
            yaxis_title="Precio de cierre ajustado ($)",
            plot_bgcolor="white",
            height=500,
        )
