SELECT controlaccess.* , did.*
FROM controlaccess JOIN did 
on controlaccess.subject = did.cID 