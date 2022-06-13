import xlrd, sqlite3, pandas as pd, numpy as np
from datetime import datetime, timedelta
from sqlite3 import OperationalError

def Xlopen(sheetname):
    sheetname = pd.read_excel('~/dev/projet_ardouin/Ardouin La Totale.xls', sheetname, header=0)
    
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
    dataframe.dateD = pd.to_datetime(dataframe.dateD, format='%Y')
    dataframe.dateF = pd.to_datetime(dataframe.dateF, format='%Y')
    dataframe.dateF = dataframe.dateF.apply(lambda x: datetime(x.year, 12, 31))
        
    return dataframe

def Type_column(dataframe, categorie):
    if categorie == "personnes":
        dataframe["type"] = "P"
    if categorie == "bateaux":
        dataframe["type"] = "B"
    if categorie == "affaires":
        dataframe["type"] = "A"
    return dataframe

def AddID(dataframe):
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

def Clean_concat(*dataframes):
    unwantedcol = ['masque', 'page','contenu', 'tome', 'f1', 'f2', 'f3', 'f4',
       'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15',
       'f16', 'f17', 'f18', 'f19', 'f20', 'f21', 'f22', 'f23', 'f24', 'f25',
       'sserie', 'serie', 'ssserie', 'atl', 'mf', 'dateD', 'dateF']
    for dataframe in dataframes:
        dataframe = dataframe.drop(unwantedcol, inplace=True, axis=1)
        
    master = pd.concat([*dataframes])
    master = master.drop_duplicates(subset=['nom', 'type'], keep='first')
    
    return master
    
    
    
    
    
   

