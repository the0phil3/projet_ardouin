# essai2recherche

Ce dossier contient les microfilmes numerisées et photos des support d'archives que j'ai consulté lors d'un essai de recherche où j'ai comparé ma base de données, l'information sur internet et les fiches excel pour trouver la première entrée sur M. Petit (mf 7, SHD MR 1 E 44, folii 256, 323) (ID = 'P1049' , cID = 'C2162') qui parle de son refus de voyager au Mississippi (1701). 


## Explication de la comparaison des méthodes de recherches 

**ma base de données**  --> Pour trouver Petit dans ma base, j'ai fais une requête `sql` très simple : 

` SELECT contents.contenu, contents.page, contents.dateD, archives.*
FROM contents JOIN archives
USING (cID)
WHERE contents.ID = 'P1049'
ORDER by dateD `

Cette requête ma donnée toutes les descriptions de contenu où apparaissent Petit et les cotes respectives. 

**l'information sur internet** --> Sur le site du [SHD](https://www.servicehistorique.sga.defense.gouv.fr/ark/970665) la démarche est plus compliquée et il faut fouiller parmi le grand nombre de sorties car c'est impossible de chercher pour le contenu. D'autant plus que le nom Petit apparait dans plusieurs fonds du SHD de Rochefort. J'ai réussi à le trouver grâce à sa cote qui est afficher à côté du nom. 

**les fiches excel de Ardouin La Totale.xls** --> Pour la fiche excel c'est très simple mais on ne peut fouiller efficacement que si on connait déjà le tome des tables ardouin concerné. 





