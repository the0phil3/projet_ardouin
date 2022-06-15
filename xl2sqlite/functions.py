import xlrd, sqlite3, pandas as pd, numpy as np, os
from datetime import datetime, timedelta
from sqlite3 import OperationalError
from collections import Counter


def Xlopen(sheetname):
    sheetname = pd.read_excel('~/dev/projet_ardouin/sources_excel/Ardouin La Totale.xls', sheetname, header=0)
    
    return sheetname

def Xlclean(dataframe):
    dataframe.columns = [x.replace('Folio ','f') for x in dataframe.columns]
    dataframe.rename(columns = {'Masque de saisie':'masque', 'Page Ardouin':'page', 
                               'Intitulé / analyse\nNom lieu\nNom personne\nAffaires diverses':'nom', 
                               'Présentation du contenu':'contenu',
                               'Ancienne cote\nN° de TOME':'tome', 'Sous-série':'sserie',
                               'Série':'serie', 'Sous-sous-série':'ssserie',
                               'Article':'atl', 'Microfilm MI':'mf',
                               'Date début':'dateD', 'Date fin':'dateF',},inplace=True)
    #dataframe.dateD = pd.to_datetime(dataframe.dateD, format='%Y%m%d')
    #dataframe.dateF = pd.to_datetime(dataframe.dateF, format='%Y%m%d')
    #dataframe.dateD = dataframe.dateD.apply(lambda x: datetime(x.year, 1, 2))
    #dataframe.dateF = dataframe.dateF.apply(lambda x: datetime(1+x.year, 1, 1))
        
    return dataframe

def Type_column(dataframe, categorie):
    if categorie == "personnes":
        dataframe["type"] = "P"
    if categorie == "bateaux":
        dataframe["type"] = "B"
    if categorie == "affaires":
        dataframe["type"] = "A"
    return dataframe

def NomID(dataframe):
    person = dataframe['type'] == "P"
    boat = dataframe['type'] == "B"
    affaires = dataframe['type'] == "A"
    if person.any():
        dataframe['ID'] = dataframe.groupby(['nom','type']).ngroup()
        dataframe['ID'] = dataframe['type'] + dataframe['ID'].astype(str)
    
    if boat.any():
        dataframe['ID'] = dataframe.groupby(['nom','type']).ngroup()
        dataframe['ID'] = dataframe['type'] + dataframe['ID'].astype(str)
        
    if affaires.any():
        dataframe['ID'] = dataframe.groupby(['nom','type']).ngroup()
        dataframe['ID'] = dataframe['type'] + dataframe['ID'].astype(str)
    
    return dataframe

def ContenuID(dataframe):
    dataframe['cID'] = np.where(dataframe['contenu'].isnull(), "N" + dataframe.groupby(['nom', 'page', 'dateD', 'dateF']).ngroup().astype(str), "C" + dataframe.groupby(['nom', 'contenu', 'page', 'dateD', 'dateF']).ngroup().astype(str))
    
    return dataframe

def Master_concat(*dataframes):
    for dataframe in dataframes:
        dataframe = dataframe.drop(dataframe.columns.difference(['nom', 'type', 'ID']), 1, inplace=True)
        
    final = pd.concat([*dataframes])
    final = final.drop_duplicates(subset=['nom', 'type', 'ID'], keep='first')
    return final

def Contenu_concat(*dataframes):
    for dataframe in dataframes:
        dataframe = dataframe.drop(dataframe.columns.difference(['page', 'nom', 'contenu', 'dateD', 'dateF', 'ID', 'cID']), 1, inplace=True)
        
    final = pd.concat([*dataframes])
    final = final.drop_duplicates(subset=['cID'], keep='first')  
    return final
    
def Archive_concat(*dataframes):
    unwantedcol = ['contenu','masque', 'type', 'nom', 'page','dateD', 'dateF']
    for dataframe in dataframes:
        dataframe = dataframe.drop(dataframe.columns.difference(['tome', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10','f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f20',
       'f21', 'f22', 'f23', 'f24', 'f25', 'sserie', 'serie', 'ssserie', 'atl',
       'mf', 'ID', 'cID']), 1, inplace=True)
        
    final = pd.concat([*dataframes])
    final = final.drop_duplicates(subset=['tome', 'f1', 'f2', 'f3', 'f4',
       'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15',
       'f16', 'f17', 'f18', 'f19', 'f20', 'f21', 'f22', 'f23', 'f24', 'f25',
       'sserie', 'serie', 'ssserie', 'atl', 'mf'], keep='first')
    return final


    
    
    
    
    
   

