import pandas as pd
import numpy as np 
import warnings
warnings.filterwarnings('ignore')

from perdido.geoparser import Geoparser
from perdido.geocoder import Geocoder

import cython


import spacy
from spacy import displacy

from display_xml import XML

def parse_sample(df,option):
    geoparser = Geoparser(version=f"{option}")
    df['parsed_contenu'] = df['contenu'].apply(geoparser)
    return df
    
def parse_sample_fast(df):
    geoparser = Geoparser(version="Standard")
    df['parsed_contenu'] = df['contenu'].map(geoparser)
    return df

def print_entities_df(df):
    count = 0 
    for row in df.itertuples():
        if row.parsed_contenu is None:
            print(f'Row {count} is NaN')
            
        else:
            print(f'List of entities in row {count} : ')
            for ent in row.parsed_contenu.named_entities:
                    print(ent.text, ent.tag)
                    
        count = count +1