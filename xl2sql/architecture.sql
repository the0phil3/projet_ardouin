CREATE TABLE master (
        nom TEXT NOT NULL,
        type TEXT NOT NULL,
        ID TEXT NOT NULL,
        PRIMARY KEY(ID),
        FOREIGN KEY(nom) REFERENCES name(nom),
        FOREIGN KEY(type) REFERENCES category(type)
        );
   
CREATE TABLE personnes (
        masque TEXT,
        page INTEGER,
        nom TEXT NOT NULL,
        contenu TEXT,
        tome INTEGER,
        f1 TEXT,
        f2 TEXT,
        f3 TEXT,
        masque TEXT,
        masque TEXT,
        masque TEXT,
        masque TEXT,
    
    
    
    
    
    
    
        type TEXT NOT NULL,
        ID TEXT NOT NULL,
        PRIMARY KEY(ID),
        FOREIGN KEY(nom) REFERENCES name(nom),
        FOREIGN KEY(type) REFERENCES category(type)
        );
   

'masque', 'page', 'nom', 'contenu', 'tome', 'f1', 'f2', 'f3', 'f4',
       'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15',
       'f16', 'f17', 'f18', 'f19', 'f20', 'f21', 'f22', 'f23', 'f24', 'f25',
       'sserie', 'serie', 'ssserie', 'atl', 'mf', 'dateD', 'dateF', 'type',
       'ID'