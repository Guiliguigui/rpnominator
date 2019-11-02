def trouverNomRP(univers,prenom,nom,data):
    lettrePrenom = prenom[data[univers]['numLettrePrenom']].upper()
    lettreNom=nom[data[univers]['numLettreNom']].upper()
    PrenomRP = data[univers]['Prenom'][lettrePrenom]
    NomRP =data[univers]['Nom'][lettreNom]
    nomCompletRP="%s %s"%(PrenomRP,NomRP)
    return nomCompletRP