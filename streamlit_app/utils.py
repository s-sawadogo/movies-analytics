import streamlit as st
from pathlib import Path
import pandas as pd

# Définition du dossier de sortie
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"

# Fonction cache pour charger les fichiers parquet
@st.cache_data
def load_parquet_data(file_name):
     file_path = OUTPUT_DIR / file_name
     return pd.read_parquet(file_path)

# === Configuration et chargement des fichiers ===
output_dir = Path(__file__).resolve().parents[1] / "output"

movie_stats = pd.read_parquet(output_dir / "top_movies_by_ratings.parquet")
genre_df = pd.read_parquet(output_dir / "genre_df.parquet")
tags_df = pd.read_parquet(output_dir / "user_tag_stats.parquet")
ratings_df = pd.read_parquet(output_dir / "ratings.parquet")
