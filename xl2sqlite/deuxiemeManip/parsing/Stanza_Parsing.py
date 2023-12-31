import pandas as pd
import numpy as np 

from display_xml import XML

import stanza

import cython

from perdido.geocoder import Geocoder
geocoder = Geocoder()

stanza_parser = stanza.Pipeline(lang='fr', processors='tokenize,ner')

def parse_content_loc(df):
    df['lieu'] = df['contenu'].apply(lambda x: [ent.text for ent in stanza_parser(x).ents if ent.type == "LOC"])
    return df

def parse_content_pers(df):
    df['persname'] = df['contenu'].apply(lambda x: [ent.text for ent in stanza_parser(x).ents if ent.type == "PER"])
    return df

def geocode_loc(df):
    geocoder = Geocoder()
    df = df[df['lieu'].apply(lambda x : len(x)!=0)].copy()
    df['geoJson'] = df['lieu'].apply(lambda x: geocoder(x).geojson)
    return df

def print_entities_df(df):
    count = 0 
    for row in df.itertuples():
        print(f'List of places in row {count} : ')
        for item in row.geo:
            print(item)
                    
        count = count +1
