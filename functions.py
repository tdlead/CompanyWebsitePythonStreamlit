import streamlit as st
import csv


# Calculate number of rows depending on data volume per 3 columns
def divide_rows_into_columns(total_rows):
    base_rows_per_column = total_rows // 3
    remainder = total_rows % 3

    column_1 = base_rows_per_column + (1 if remainder > 0 else 0)
    column_2 = base_rows_per_column + (1 if remainder > 1 else 0)
    column_3 = base_rows_per_column

    return column_1, column_2, column_3


# Streamlit functions

# column content
def print_column(team_content):
    for index, member in team_content.iterrows():
        st.header(f'{member['first name'].title()} {member['last name'].title()}')
        st.subheader(member['role'])
        st.image(f'images/{member['image']}')

