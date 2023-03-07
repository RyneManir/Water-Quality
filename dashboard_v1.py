


import streamlit as st

import dropbox

import pandas as pd

# Authenticate with Dropbox using your access token
access_token = "sl.BaEF8_yvuNsbXWbg7_XWLyMJWlmv2m86vPKpQaUyyuQRdxLDDPEORy2DUf4be07i5bnTuepy2I2pFb2nLwmeGXVGGqI_NrU73zJkc5YLffv-4creJ7hy57WmhpzjnTi-meOkags"
dbx = dropbox.Dropbox(access_token)

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
st.write(df)


