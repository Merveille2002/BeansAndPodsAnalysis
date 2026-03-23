import streamlit as st
from matplotlib import pyplot as plt
from pandas import read_csv
import pandas as pd
import seaborn as sns

st.sidebar.title("Beans and Pod")
menu=st.sidebar.selectbox("Navigation",['Accueil','Données','Peek at the data','Statistique','Analyse','Corrélation','Recommandation'])

st.markdown(
    """
    <h1 style='text-align:center; color:#6F4E37;'>
    ☕ Beans & Pods Analyse de Donnée
    </h1>
    """,
    unsafe_allow_html=True
    )

chemin='BeansDataSet.csv'
    
col = ['Channel','Region','Robusta','Arabica','Espresso','Lungo','Latte','Cappuccino']


ligne = [f"Transaction_{x}" for x in range(1,441)]

data = read_csv(chemin, names=col, header=0)

data.index = ligne


if menu == "Accueil":
    
    st.image("coffee.jpg")

    st.markdown(
    """
    ### Objectif du projet

    Cette application analyse les données de ventes de Beans & Pods
    afin d’identifier les tendances importantes et aider l’entreprise
    à améliorer ses stratégies marketing.

    ### Dataset
    - 440 transactions
    - ventes de café et capsules
    - ventes en magasin et en ligne
    - ventes dans les region du Nord, Centre et Sud
    """
    )
    
elif menu=='Données':
        st.header('Affichage des données')
        st.dataframe(data)
        
elif menu == 'Peek at the data':
    
    st.header("Aperçu des données")
    st.subheader("Dimensions du dataset")
    st.write("Nombre de transactions :", data.shape[0])
    st.write("Nombre de variables :", data.shape[1])

    st.subheader("Les 5 premières lignes")
    st.dataframe(data.head())

    st.subheader("Les 5 dernières lignes")
    st.dataframe(data.tail())

    st.subheader("Types de données")
    st.write(data.dtypes)

    st.subheader("Distribution des canaux de vente (Store / Online)")

    count_channel = data['Channel'].value_counts()
    st.write(count_channel)

    fig, ax = plt.subplots()
    data['Channel'].value_counts().plot(kind='bar', ax=ax)
    ax.set_xlabel("Canal de vente")
    ax.set_ylabel("Nombre de transactions")
    st.pyplot(fig)

    st.subheader("Distribution des régions")

    fig, ax = plt.subplots()
    data['Region'].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=ax)
    ax.set_ylabel("")
    st.pyplot(fig)
    
    st.subheader("Distribution des ventes par produit")

    produits = data[['Robusta','Arabica','Espresso','Lungo','Latte','Cappuccino']].sum()

    st.write(produits)
    
    fig, ax = plt.subplots()
    produits.plot(kind='pie', autopct='%1.1f%%', ax=ax)

    ax.set_ylabel("")
    st.pyplot(fig)
    
    
elif menu=='Statistique':  
    st.header('Statistiques Descriptives')
    st.write(data.describe())
    
    st.header("Statistique produit")

    produits = data[['Robusta','Arabica','Espresso','Lungo','Latte','Cappuccino']]

    st.subheader("Moyenne")
    st.write(produits.mean())

    st.subheader("Minimum")
    st.write(produits.min())

    st.subheader("Maximum")
    st.write(produits.max())

    st.subheader("Écart type")
    st.write(produits.std())
    
elif menu=='Analyse': 
    
    st.subheader("Ventes totales par produit")

    produits = data[['Robusta','Arabica','Espresso','Lungo','Latte','Cappuccino']].sum()

    st.bar_chart(produits)
    
    st.subheader("Ventes totales par région")

    region = data.groupby("Region")[['Robusta','Arabica','Espresso','Lungo','Latte','Cappuccino']].sum()

    st.bar_chart(region)
        
    st.subheader("Ventes total selon le canal")

    channel_product = data.groupby("Channel")[['Robusta','Arabica','Espresso','Lungo','Latte','Cappuccino']].sum()

    st.bar_chart(channel_product)
    
    
    
    
elif menu == "Corrélation":

    st.header("Corrélation entre les produits")
    fig,ax=plt.subplots(figsize=(15,15))
    sns.heatmap(data.corr(method='pearson',numeric_only=True),annot=True,fmt='2f',cmap='coolwarm',ax=ax)
    st.pyplot(fig)
    


elif menu == "Recommandation":

    st.header("Rapport d'analyse & Recommandations Marketing")

    st.write("""
    En somme la Région du Sud génère le plus de vente, le plus de vente est obtenu grace au vente en store ,
    le centre et le nord ont un faible taux de revenu,le cappuccino,le latte et lungo sont les moins vendu a l'inverse 
    du Robusta qui est le plus vendu.L’analyse de corrélation montre que les produits de type capsules (Espresso, Latte, Cappuccino
    et Lungo) présentent des corrélations positives entre eux. Cela indique que ces produits sont souvent achetés ensemble ou par les mêmes types de clients.

    En revanche, les produits en grains (Robusta et Arabica) présentent une corrélation plus faible avec les capsules, ce qui suggère des comportements d’achat différents.
    voici mes Recommandations :
    
             
    1. Mettre davantage l'accent sur le café Robusta car il génère le plus de ventes.

    2. Investir dans la région Sud qui représente la majorité des ventes.

    3. Promouvoir davantage les capsules Espresso sur la boutique en ligne.

    4. Créer des packs promotionnels combinant Espresso,Lungo,Latte et Cappuccino.Une forte corrélation a été observée entre Espresso et Latte,
    ce qui suggère qu'ils sont souvent achetés ensemble.Certains produits comme Lungo et Latte étant faiblement corrélés,
    il est préférable de ne pas les combiner dans les promotions similaires.
    Les produits Robusta et Arabica étant peu corrélés avec les capsules,il est conseillé de développer des stratégies marketing distinctes.

    5. Mettre  l'accent sur les promotions dans le centre et le nord pour augmenter les ventes.
    
    6. Beans and Pods pourrait recueillir les avis des clients sur les differents service offert, collecter
    le nombre de  clients qui participe aux promotions en prenant leur nom,age, leur frequence cela permettrait de connaitre les 
    différentes cibles de chaque service.

   
    """)
   