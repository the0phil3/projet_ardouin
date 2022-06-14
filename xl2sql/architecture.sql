CREATE TABLE master (
        nom TEXT NOT NULL,
        type TEXT NOT NULL,
        ID TEXT PRIMARY KEY
        );
   
CREATE TABLE contents (
        nom TEXT,
        page INTEGER,
        contenu TEXT,
        dateD DATE,
        dateF DATE,    
        ID TEXT NOT NULL,
        cID TEXT PRIMARY KEY,
        FOREIGN KEY(nom) REFERENCES nom(nom),
        FOREIGN KEY(ID) REFERENCES ID(ID)
        );
        
CREATE TABLE archives (
        tome TEXT,
        f1 INTEGER, 
        f2 INTEGER,
        f3 INTEGER,
        f4 INTEGER,
        f5 INTEGER,
        f6 INTEGER,
        f7 INTEGER,
        f8 INTEGER,
        f9 INTEGER,
        f10 INTEGER,
        f11 INTEGER,
        f12 INTEGER,
        f13 INTEGER,
        f14 INTEGER,
        f15 INTEGER,
        f16 INTEGER,
        f17 INTEGER,
        f18 INTEGER,
        f19 INTEGER,
        f20 INTEGER,
        f21 INTEGER,
        f22 INTEGER,
        f23 INTEGER,
        f24 INTEGER,
        f25 INTEGER,
        sserie INTEGER, 
        serie TEXT,
        ssserie TEXT,
        atl INTEGER,
        mf INTEGER,
        ID TEXT NOT NULL,
        cID TEXT NOT NULL,
        FOREIGN KEY(ID) REFERENCES ID(ID),
        FOREIGN KEY(cID) REFERENCES contenuID(cID)
        );
        
        
        
        
   