import streamlit as st
import pandas as pd
import functions

st.set_page_config(layout="wide")

title = "The Best Company"
st.title(title)

about = """
A company profile is your brand's professional introduction to your audience. It's meant to inform visitors and prospects on your products, services, and current positioning in the market. A well crafted company profile is a way to make yourself stand out from the competition and offer how you're unique.
"""

st.write(about)

st.subheader("Our team")

team_content = pd.read_csv('data.csv', header=0)
total_rows = team_content.shape[0] - 1

rows_1, rows_2, rows_3 = functions.divide_rows_into_columns(total_rows)

col1, col2, col3 = st.columns(3)

with col1:
    team_content_col1 = team_content.iloc[0:rows_1]
    functions.print_column(team_content_col1)
with col2:
    team_content_col2 = team_content.iloc[rows_1 : (rows_1 + rows_2)]
    functions.print_column(team_content_col2)

with col3:
    team_content_col3 = team_content.iloc[(rows_1 + rows_2) : (rows_1 + rows_2 + rows_3)]
    functions.print_column(team_content_col3)
