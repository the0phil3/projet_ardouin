import pandas as pd
import xlrd
import sqlite3

def xlopen(sheetname):
    sheetname = pd.read_excel('~/dev/projet_ardouin/Ardouin La Totale.xls', sheetname, header=0)
    
    return sheetname.head()

def xlclean(dataframe):
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
    
    return dataframe.head()

