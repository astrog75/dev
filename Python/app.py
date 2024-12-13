# To do
# 2. Ajouter la fonction "apercu" des données
# 3. Améliorer le rendu graphique
# 4. Affiner la détection du type de données
# 5. Pour les données numériques : générer un boxplot
# 6. Pour les données categoriques : générer un bar-plot

import streamlit as st
import pandas as pd
import re
import altair as alt
import plotly.express as px

# ---------- presentation ----------
st.title("Data Explorer")
st.write("This app displays a customizable dashboard for your data (see sideboard)")
st.write("Please upload a csv file")

# ---------- load data ----------
data_csv = st.file_uploader("Upload a file", type = "csv")
data = pd.read_csv(data_csv, delimiter=';')


def basic_infos(data):
    if data is not None:
        n_rows,n_columns = data.shape
        st.write(f"Your file contains {n_rows:,} rows and {n_columns:,} columns")
        st.dataframe(data)

def compute_missing_values(data):
    if data is not None:
        n_rows,n_columns = data.shape
        
        missing_rate = round(data.isna().sum()/n_rows*100,1)
        missing_rate_df = pd.DataFrame({"Feature name":data.columns, "Missing rate in percent":missing_rate})
        
        st.write("Ratio of missing values for each column :")
        
        st.altair_chart(alt.Chart(missing_rate_df).mark_bar().encode(
            x=alt.X("Feature name", axis=alt.Axis(labelAngle=-45)),
            y="Missing rate in percent"))
    else:
        st.write("No data were provided")

# Trying to infer data types of every column
def infer_types(data):
    
    # The type is either numeric, datetime, string, boolean, category of mixed (if dtype is object)
    # Detects date of either format : YYYY/MM/DD, YY/MM/DD, YYYY-MM-DD, YY-MM-DD,
    # DD/MM/YYYY, DD/MM/YY, MM/DD/YYYY or MM/DD/YY
    # The detection is done in two steps : first check if a column contains only data on 
    # the above format, and then check if it corresponds to a valid date
    # regex = r'\d{2,4}[-/]\d{2}[-/]\d{2}'
    
    # WARNING : The 2nd step (validate if the matched string is indeed a valid date
    # For example : 45/12/78 is a match for the beneath regex but it doesnt correspond to a valid date)
    
    # The main point of this function is to detect if a feature is temporal
    # A feature is temporal is it contains a date, a time or both
    
    # We're looking for the first non NaN cell
    def isfloat(num):
        try:
            float(num)
            return True
        except ValueError:
            return False

    temporal = {}
    pattern = re.compile(r'\d{2,4}[-/]\d{2}[-/]\d{2}')
    
    for col in data.columns:
        temporal[col] = False
        for d in data[col]:
            if d is not None and not isfloat(str(d)):
                st.write(d)
                if re.search(pattern, d):
                    temporal[col] = True
    
    st.write(temporal)
    
    dtypes = ["numeric", "object"]
    
    counter = {}
    for t in dtypes:
        counter[t] = 0
    
    for col in data.columns:
        if data[col].dtype in ["int64","float64"]:
            counter["numeric"] += 1
        else:
            counter["object"] += 1
            
    df_counter = pd.DataFrame({"dtype":dtypes, "values":counter.values()})
    
    st.write(df_counter)
            
    st.altair_chart(alt.Chart(df_counter).mark_arc().encode(
        theta="values",
        color="dtype"))

def display_data(column):
    if data[col].dtype in ["int64","float64"]:
        st.plotly_chart(px.box(data, y=col))
        st.write(data[col].describe().T) # Transpose doesnt work
    else:
        data_counts = data[col].value_counts()
        df = pd.DataFrame({"col1":data_counts.index, "col2":data_counts})
        st.altair_chart(alt.Chart(df).mark_bar().encode(
            x=alt.X("col1"),
            y="col2"))


# ---------- sidebar ----------
with st.sidebar:
    st.title("Data Explorer") 
    state = st.sidebar.toggle(label="Display rate of missing values in data")
    
    selected = st.multiselect("Select a column of interest", data.columns)


# ---------- main page  ----------
if data is not None:
    basic_infos(data)
    infer_types(data)
    
    if state:
        compute_missing_values(data)
    
    for col in selected:
        display_data(col)
        








