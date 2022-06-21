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
                               'Intitulé / analyse\nNom lieu\nNom personne\nAffaires diverses':'unittitle', 
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

def Totalclean(dataframe):
    dataframe.columns = [x.replace('Folio ','f') for x in dataframe.columns]
    dataframe.rename(columns = {'Masque de saisie':'masque', 'Page Ardouin':'page', 
                               'Intitulé / analyse\nNom lieu\nNom personne\nAffaires diverses':'unittitle', 
                               'Présentation du contenu':'contenu',
                               'N° de TOME':'tome', 'Sous-série':'sserie',
                               'Série':'serie', 'Sous-sous-série':'ssserie',
                               'Article':'atl', 'Microfilm MI':'mf',
                               'Date':'dateD',},inplace=True)
    
    dataframe['dateF'] = dataframe['dateD']
    
    return dataframe

def Type_column(dataframe, categorie):
    if categorie == "personnes":
        dataframe["function"] = "Personne"
    if categorie == "bateaux":
        dataframe["function"] = "Bateau"
    if categorie == "affaires":
        dataframe["function"] = "Affaire"
    return dataframe

def NomID(dataframe):
    person = dataframe['function'] == "Personne"
    boat = dataframe['function'] == "Bateau"
    affaires = dataframe['function'] == "Affaire"
    if person.any():
        dataframe['ID'] = dataframe.groupby(['unittitle','function']).ngroup()
        dataframe['ID'] = "P" + dataframe['ID'].astype(str)
    
    if boat.any():
        dataframe['ID'] = dataframe.groupby(['unittitle','function']).ngroup()
        dataframe['ID'] = "B" + dataframe['ID'].astype(str)
        
    if affaires.any():
        dataframe['ID'] = dataframe.groupby(['unittitle','function']).ngroup()
        dataframe['ID'] = "A" + dataframe['ID'].astype(str)
    
    return dataframe

def ContenuID(dataframe):
    dataframe['cID'] = np.where(dataframe['contenu'].isnull(), "N" + dataframe.groupby(['unittitle', 'page', 'dateD', 'dateF']).ngroup().astype(str), "C" + dataframe.groupby(['unittitle', 'contenu', 'page', 'dateD', 'dateF']).ngroup().astype(str))
    
    return dataframe

def ArchivesID(dataframe):
    dataframe['aID'] = np.where(dataframe['ssserie'].isnull(), "MR" + dataframe['sserie'].astype(str) + dataframe['serie'].astype(str) + dataframe['atl'].astype(str), "MR" + dataframe['sserie'].astype(str) + dataframe['serie'].astype(str) + dataframe['ssserie'].astype(str) + dataframe['atl'].astype(str))
    
    return dataframe
 
def Master_concat(*dataframes):
    for dataframe in dataframes:
        dataframe = dataframe.drop(dataframe.columns.difference(['unittitle', 'function', 'ID']), 1, inplace=True)
        
    final = pd.concat([*dataframes])
    final = final.drop_duplicates(subset=['unittitle', 'function', 'ID'], keep='first')
    return final

def Contenu_concat(*dataframes):
    for dataframe in dataframes:
        dataframe = dataframe.drop(dataframe.columns.difference(['page', 'tome', 'ID', 'cID']), 1, inplace=True)
        
    final = pd.concat([*dataframes])
    final = final.drop_duplicates(subset=['cID'], keep='first')  
    return final
    
def Archive_concat(*dataframes):
    for dataframe in dataframes:
        dataframe = dataframe.drop(dataframe.columns.difference(['unittitle','dateD', 'dateF','f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10','f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f20',
       'f21', 'f22', 'f23', 'f24', 'f25', 'sserie', 'serie', 'ssserie', 'atl',
       'mf', 'ID', 'cID']), 1, inplace=True)
        
    final = pd.concat([*dataframes])
    final = final.drop_duplicates(subset=['f1', 'f2', 'f3', 'f4',
       'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15',
       'f16', 'f17', 'f18', 'f19', 'f20', 'f21', 'f22', 'f23', 'f24', 'f25',
       'sserie', 'serie', 'ssserie', 'atl', 'mf'], keep='first')
    return final

def Control_concat(*dataframes):
    for dataframe in dataframes:
        dataframe = dataframe.drop(dataframe.columns.difference(['function', 'unittitle', 'contenu', 'ID', 'cID']), 1, inplace=True)
        
    final = pd.concat([*dataframes])
    return final


    
    
    
    
    
   

