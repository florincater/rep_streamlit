import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("Application de visualisation des donnees CSV ")

# 1. Telecharger le fichier CSV
uploaded_file = st.file_uploader("Telecharger un fichier CSV", type=["csv"])

if uploaded_file is not None:
    # Lire CSV
    df = pd.read_csv(uploaded_file)
    
    # 2. Afficher les donnees
    st.subheader("Donnees brutes")
    st.dataframe(df)

    # 3. Selectionner la colonne a visualiser
    column = st.selectbox("Selectionner une colonne a visualiser", df.columns)

    # 4. Choisir le type de graph
    plot_type = st.radio("Selectionner le type de graph", ["Line Chart", "Bar Chart", "Histogram"])

    # 5. Generer le graph
    st.subheader(f"Plot of {column}")
    fig, ax = plt.subplots()

    if plot_type == "Line Chart":
        ax.plot(df[column])
    elif plot_type == "Bar Chart":
        ax.bar(df.index, df[column])
    elif plot_type == "Histogram":
        ax.hist(df[column], bins=20)

    ax.set_title(column)
    st.pyplot(fig)

else:
    st.warning("SVP telecharger un fichier csv pour commencer.")