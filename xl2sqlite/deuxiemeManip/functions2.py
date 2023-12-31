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

def rename_columns(df, column_names):
    old_columns = df.columns
    for i, old_col in enumerate(old_columns):
        df = df.rename(columns={old_col: column_names[i]})
    return df

def Type_column(row): 
    if row['result'] == 0:
        return 'Personne'
    elif row['result'] == 1:
        return 'Bateau'
    elif row['result'] == 2:
        return 'Affaire'


def NomID(dataframe):
    person = dataframe['result'] == 0
    boat = dataframe['result'] == 1
    affaires = dataframe['result'] == 2
    if person.any:
        dataframe['ID'] = dataframe.groupby(['unittitle','function']).ngroup()
        dataframe['ID'] = "P" + dataframe['ID'].astype(str)
    
    elif boat.any():
        dataframe['ID'] = dataframe.groupby(['unittitle','function']).ngroup()
        dataframe['ID'] = "B" + dataframe['ID'].astype(str)
        
    elif affaires.any():
        dataframe['ID'] = dataframe.groupby(['unittitle','function']).ngroup()
        dataframe['ID'] = "A" + dataframe['ID'].astype(str)
    
    return dataframe

def ContenuID(dataframe):
    dataframe['cID'] = np.where(dataframe['contenu'].isnull(), "N" + dataframe.groupby(['unittitle', 'page', 'dateD', 'dateF']).ngroup().astype(str), "C" + dataframe.groupby(['unittitle', 'contenu', 'page', 'dateD', 'dateF']).ngroup().astype(str))
    
    return dataframe

def ArchivesID(dataframe):
    dataframe['atl'] = dataframe['atl'].astype(int)
    
    dataframe['aID'] = np.where(dataframe['ssserie'].isnull(), "MR" + dataframe['sserie'].astype(str) + dataframe['serie'].astype(str) + dataframe['atl'].round().astype(str), "MR" + dataframe['sserie'].astype(str) + dataframe['serie'].astype(str) + dataframe['ssserie'].astype(str) + dataframe['atl'].round().astype(str))
    
    return dataframe
 
def Master_concat(*dataframes):
    for dataframe in dataframes:
        dataframe = dataframe.drop(dataframe.columns.difference(['unittitle', 'function', 'ID']), 1, inplace=True)
        
    final = pd.concat([*dataframes])
    final = final.drop_duplicates(subset=['unittitle', 'function', 'ID'], keep='first')
    return final

def Contenu_concat(*dataframes):
    for dataframe in dataframes:
        dataframe = dataframe.drop(dataframe.columns.difference(['contenu','page', 'tome', 'ID', 'cID']), 1, inplace=True)
        
    final = pd.concat([*dataframes])
    final = final.drop_duplicates(subset=['cID'], keep='first')  
    return final
    
def Archive_concat(*dataframes):
    for dataframe in dataframes:
        dataframe = dataframe.drop(dataframe.columns.difference(['unittitle','dateD', 'dateF','f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10','f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f20',
       'f21', 'f22', 'f23', 'f24', 'f25', 'sserie', 'serie', 'ssserie', 'atl',
       'mf', 'ID', 'cID', 'aID']), 1, inplace=True)
        
    final = pd.concat([*dataframes])
    final = final.drop_duplicates(subset=['f1', 'f2', 'f3', 'f4',
       'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15',
       'f16', 'f17', 'f18', 'f19', 'f20', 'f21', 'f22', 'f23', 'f24', 'f25',
       'sserie', 'serie', 'ssserie', 'atl', 'mf', 'cID'], keep='first')
    return final

def Control_concat(*dataframes):
    for dataframe in dataframes:
        dataframe = dataframe.drop(dataframe.columns.difference(['function', 'geogname', 'ID', 'cID']), 1, inplace=True)
        
    final = pd.concat([*dataframes])
    return final


    
    
    
    
    
   

