
import streamlit as st

import os

import dropbox

import pandas as pd


# Get the access token from the environment variable
#ACCESS_TOKEN = os.environ['DROPBOX_ACCESS_TOKEN']

ACCESS_TOKEN = os.environ.get('DROPBOX_ACCESS_TOKEN')

# Initialize Dropbox client
dbx = dropbox.Dropbox(ACCESS_TOKEN)


# Specify the name of the file and folder you want to access
file_name = "Pourashava_v4.xlsx"
folder_name = "/Dashboard"

# Get the metadata for the specified file
metadata = dbx.files_get_metadata(folder_name + "/" + file_name)

# Download the file content as a binary string
file_binary = dbx.files_download(folder_name + "/" + file_name)[1].content

# Display the contents of the file in Streamlit
#st.write(file_binary)

# Read the binary string into a Pandas DataFrame
df = pd.read_excel(file_binary)

# Display the contents of the DataFrame in Streamlit
#st.write(df)

# define the app title and subtitle
#st.title("Urban Governance Improvement Action Plan (UGIAP) for IUGIP")
st.markdown("<h1 style='font-size: 25px;'>Urban Governance Improvement Action Plan (UGIAP) for IUGIP</h1>", unsafe_allow_html=True)

st.markdown("<h2 style='font-size: 20px;'>Overall Performance of the Pourashavas - Top 10 Pourashavas</h2>", unsafe_allow_html=True)

# Sort the DataFrame by Total Score in descending order
df_sorted = df.sort_values('Total Score', ascending=False)

# Reset the index of the sorted DataFrame
# Reset the index and start from 1
df_sorted = df_sorted.reset_index(drop=False).head(10)
df_sorted.index += 1



# Display the Pourashavas and Total Score columns in a Streamlit table
st.table(df_sorted[['Pourashava', 'Total Score']])

st.markdown("<h2 style='font-size: 20px;'>Area: Citizen Awareness and Participation</h2>", unsafe_allow_html=True)
st.markdown("<h2 style='font-size: 16px;'>Sub-Area: Formation and Working of Town Level Consultation Committee (TLCC)</h2>", unsafe_allow_html=True)

# Create a pivot table that summarizes the data by Pourashava and TLCC Total Score
pivot_table = pd.pivot_table(df, values='TLCC Total Score', index='Pourashava', aggfunc=sum)

# Create a bar chart to display the data from the pivot table
st.bar_chart(pivot_table)

