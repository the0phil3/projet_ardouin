CREATE TABLE tome1 AS
SELECT controlaccess."function", did.*, scopecontent.contenu, scopecontent.tome, scopecontent.page
FROM did 
JOIN controlaccess 
ON did.cID = controlaccess.cID  
JOIN scopecontent 
ON did.cID = scopecontent.cID
WHERE tome = '1'
ORDER by page;

CREATE TABLE tome2 AS
SELECT controlaccess."function", did.*, scopecontent.contenu, scopecontent.tome, scopecontent.page
FROM did 
JOIN controlaccess 
ON did.cID = controlaccess.cID  
JOIN scopecontent 
ON did.cID = scopecontent.cID
WHERE tome = '2'
ORDER by page;

CREATE TABLE tome3 AS
SELECT controlaccess."function", did.*, scopecontent.contenu, scopecontent.tome, scopecontent.page
FROM did 
JOIN controlaccess 
ON did.cID = controlaccess.cID  
JOIN scopecontent 
ON did.cID = scopecontent.cID
WHERE tome = '3'
ORDER by page;

CREATE TABLE tome4 AS
SELECT controlaccess."function", did.*, scopecontent.contenu, scopecontent.tome, scopecontent.page
FROM did 
JOIN controlaccess 
ON did.cID = controlaccess.cID  
JOIN scopecontent 
ON did.cID = scopecontent.cID
WHERE tome = '4'
ORDER by page;

CREATE TABLE tome5 AS
SELECT controlaccess."function", did.*, scopecontent.contenu, scopecontent.tome, scopecontent.page
FROM did 
JOIN controlaccess 
ON did.cID = controlaccess.cID  
JOIN scopecontent 
ON did.cID = scopecontent.cID
WHERE tome = '5'
ORDER by page;

CREATE TABLE tome6 AS
SELECT controlaccess."function", did.*, scopecontent.contenu, scopecontent.tome, scopecontent.page
FROM did 
JOIN controlaccess 
ON did.cID = controlaccess.cID  
JOIN scopecontent 
ON did.cID = scopecontent.cID
WHERE tome = '6'
ORDER by page;

CREATE TABLE tome7 AS
SELECT controlaccess."function", did.*, scopecontent.contenu, scopecontent.tome, scopecontent.page
FROM did 
JOIN controlaccess 
ON did.cID = controlaccess.cID  
JOIN scopecontent 
ON did.cID = scopecontent.cID
WHERE tome = '7'
ORDER by page;

CREATE TABLE tome8 AS
SELECT controlaccess."function", did.*, scopecontent.contenu, scopecontent.tome, scopecontent.page
FROM did 
JOIN controlaccess 
ON did.cID = controlaccess.cID  
JOIN scopecontent 
ON did.cID = scopecontent.cID
WHERE tome = '8'
ORDER by page;

CREATE TABLE tome9 AS
SELECT controlaccess."function", did.*, scopecontent.contenu, scopecontent.tome, scopecontent.page
FROM did 
JOIN controlaccess 
ON did.cID = controlaccess.cID  
JOIN scopecontent 
ON did.cID = scopecontent.cID
WHERE tome = '9'
ORDER by page;