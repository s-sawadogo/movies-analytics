import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
import os
#from utils import load_parquet_data
import utils

# Définition du dossier de sortie
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"

st.title("🎬 Analyse Générale des Films et Évaluations")
# Fonction cache pour charger les fichiers parquet
@st.cache_data
def load_parquet_data(file_name):
    file_path = OUTPUT_DIR / file_name
    return pd.read_parquet(file_path)

# Chargement des données
genre_df = load_parquet_data("genre_df.parquet")
st.write(genre_df)

