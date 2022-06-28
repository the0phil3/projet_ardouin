# projet_ardouin 

## L'organisation du dépot 

**sources** --> l'intégralité des tables ardouin en pdf (numérisées), en excel et en `xml` 

**xl2sqlite** --> le traitement en `python` avec `pandas` et `sqlite3` des fiches excel (personnes, bateaux et affaires) du 2ème tome des tables ardouin pour les transformer en base de données relationnelles qui sera après transformée en `xml ead`

**sqlite2xml** --> le dossier pour le traitement de la base en `xml ead` avec les fiches xml extraites de la base de données sql `final.db` par DBeaver


## Description 
Dans le cadre de mon stage de master d'humanités numériques, je participe à un travail de harmonisation, de fluidification et de remaniement du projet des [tables ardouin](https://www.servicehistorique.sga.defense.gouv.fr/ressources/les-tables-ardouin) porté par le SHD de Rochefort.  

Les tables ardouin sont un index fait par le docteur Ardouin, un ancien officier de Marine devenu archiviste pour le Service historique de la Marine au début du 20ème siecle. Les index manuscrits qu'il a écrit référencent des noms de personnes, des noms de bateaux et diverse noms propres qui varient des lieux jusqu'aux événements. Ces references font appel aux côtes des archives de la correspondance entre le ministère de la marine et l'intendance de l'arsenal de Rochefort aux 17ème et 18ème siècles.

## Attentes
J'espère pouvoir effectuer ces améliorations ou au moins établir une méthodologie pour y arriver : 
- La création d’une base de données relationnelle qui pourrait permettre un encodage en XML plus complexe 
- La normalisation des noms (l’information dans `<unittitle>`)
- La continuation de la base avec l’index des fiches Descubes
- Faire la liaison entre l’entrée dans l’index et le microfilm numérisé
- La reconnaissance des entités nommées par apprentissage machine
 