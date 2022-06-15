import xlrd, sqlite3, pandas as pd, numpy as np, os
from datetime import datetime, timedelta
from sqlite3 import OperationalError
from collections import Counter

def ExecuteSQL(data_base_name,filename):
    db_run = sqlite3.connect(data_base_name)
    c = db_run.cursor()
    # Open and read the file as a single buffer
    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()

    # all SQL commands (split on ';')
    sqlCommands = sqlFile.split(';')

    # Execute every command from the input file
    for command in sqlCommands:
        # This will skip and report errors
        # For example, if the tables do not yet exist, this will skip over
        # the DROP TABLE commands
        try:
            c.execute(command)
        except OperationalError as msg:
            print("Command skipped: ", msg)
    db_run.close()
            
def FillTables(data_base_name, *dataframes, titles):
    #Please note that titles must be a list for this function to work
    db_run = sqlite3.connect(data_base_name)
    c = db_run.cursor()
    for dataframe, title in zip(dataframes, titles):
        dataframe.to_sql(title, db_run, if_exists='append', index=False)
    db_run.close()