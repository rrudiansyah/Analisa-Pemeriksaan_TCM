import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

st.header('Bike Sharing Dashboard :sparkles:')

datetime_columns = ["Tgl Permohonan Lab", "Tgl Hasil dilaporkan", "tanggal"]

all_df = pd.read_csv("dashboard/all_data.csv")

for column in datetime_columns:
    all_df[column] = pd.to_datetime(all_df[column])
