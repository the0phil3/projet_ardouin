CREATE TABLE master (
        nom TEXT NOT NULL,
        type TEXT NOT NULL,
        ID TEXT NOT NULL,
        PRIMARY KEY(ID),
        FOREIGN KEY(nom) REFERENCES name(nom),
        FOREIGN KEY(type) REFERENCES category(type)
        );
   