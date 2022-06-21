CREATE TABLE xml AS
SELECT controlaccess."function", did.*, controlaccess.contenu, scopecontent.tome, scopecontent.page
FROM did 
JOIN controlaccess 
ON did.cID = controlaccess.cID  
JOIN scopecontent 
ON did.cID = scopecontent.cID
ORDER by tome;