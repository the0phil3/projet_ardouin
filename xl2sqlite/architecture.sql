CREATE TABLE master (
        unittitle TEXT NOT NULL,
        function TEXT NOT NULL,
        ID TEXT PRIMARY KEY
        );
        
CREATE TABLE did (
        unittitle TEXT,
        dateD BLOB,
        dateF BLOB,
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
        sserie TEXT, 
        serie TEXT,
        ssserie INTEGER,
        atl INTEGER,
        mf INTEGER,
        ID TEXT NOT NULL,
        cID TEXT NOT NULL,
        aID BLOB NOT NULL,
        FOREIGN KEY(ID) REFERENCES master(ID),
        FOREIGN KEY(cID) REFERENCES scopecontent(cID)
        );
   
CREATE TABLE scopecontent (
        tome TEXT,
        page INTEGER,   
        ID TEXT NOT NULL,
        cID TEXT PRIMARY KEY,
        FOREIGN KEY(ID) REFERENCES master(ID)
        );
        
CREATE TABLE controlaccess (
        function TEXT NOT NULL,
        unittitle TEXT,
        contenu INTEGER,
        ID TEXT NOT NULL,
        cID TEXT NOT NULL,
        FOREIGN KEY(ID) REFERENCES master(ID),
        FOREIGN KEY(cID) REFERENCES scopecontent(cID)
        );

        

        
        
        
        
   