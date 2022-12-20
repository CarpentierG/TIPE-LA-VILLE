debug = False

import os
os.chdir("C:\\Users\\carpe\\OneDrive\\Desktop\\tipe")
#trouver un moyen d'affcher la matrice G_PGE sur un fichier (et mettres les stations en indice)

###Données PARIS

"""
Lignes_metro_Paris_centre :

Ligne_Metro_1 = {"château de vincennes","bérault","saint-mandé-tourelle","porte de vincennes", "nation", "reuilly-diderot","gare de lyon","bastille","saint-paul","hôtel de ville","châtelet","louvre-rivoli","palais-royal-musée du louvre","tuileries","concorde","champs-élysées-clemenceau","franklin d.roosevelt","george v","charles de gaulle-étoile","argentine","porte maillot", "les sablons","pont de neuilly","esplanade de la défense","la défense"}
Ligne_Metro_2 = {"porte dauphine","victor hugo","charles de gaulle-étoile","ternes","courcelles","monceau","villiers","rome","place de clichy", "blanche","pigalle","anvers","barbès-rochechouart","la chapelle","stalingrad","jaurès","colonel fabien","belleville","couronnes","ménilmontant","père lachaise","philippe auguste","alexandre dumas","avron","nation"}
Ligne_Metro_3 = {"pont de levallois bécon","anatole france","louise michel","porte de champeret","pereire","wagram","villiers","europe","saint-lazare","havre-caumartin","opéra","quatre-septembre","bourse","sentier","réaumur-sébastopol","arts et métiers","temple","république","parmentier","rue saint-maur","père lachaise","gambetta","porte de bagnolet","gallieni" }
Ligne_Metro_4 ={"porte de clignancourt","simplon","marcadet poissoniers","château rouge","barbès-rochechouart","gare du nord","gare de l'est","château d'eau","strasbourg saint-denis","réaumur-sébastopol","étienne marcel","les halles","châtelet","cité","saint-michel","odéon","saint-germain-des-près","saint-sulpice","saint-placide","montparnasse","montparnasse bienvenüe","vavin","raspail","denfert-rochereau","mouton-duvernet","alésia","porte d'orléans"}
Ligne_Metro_5 ={"bobigny pablo-picasso","bobigny-pantin raymond queneau","église de pantin","hoche","porte de pantin","ourcq","laumière","jaurès","stalingrad","gare du nord","gare de l'est","jacques bonsergent","république","oberkampf","richard-Lenoir","bréguet-sabin","bastille","quai de la rapée","gare d'austerlitz","saint-marcel","campo-formio","place d'italie"}
Ligne_Metro_6 = {"charles de gaulle-étoile","kléber","boissière","trocadéro","passy","bir-hakeim","dupleix","la motte-picquet grenelle","cambronne","sèvres-lecourbe","pasteur","montparnasse bienvenüe","edgar quinet","raspail","denfert-rochereau","saint-jacques","glacière","corvisart","place d'italie","nationale","chevaleret","quai de la gare","bercy","dugommier","daumesnil","bel-air","picpus","nation"}
Ligne_Metro_7a = {"la courneuve 8 mai 1945","fort d'aubervilliers","aubervilliers-pantin quatre chemins","porte de la vilette","corentin cariou","crimée","riquet","stalingrad","louis-blanc","château-landon","gare de l'est","poissonière","cadet","le peletier","chaussée d'antin - la fayette","opéra","pyramides","palais-royal-musée du louvre","pont neuf","châtelet","pont marie","sully-morland","jussieu","place monge","censier-daubenton","les gobelins","place d'italie","tolbiac","maison blanche","porte d'italie","porte de choisy","porte d'ivry", "pierre curie","mairie d'ivry"}
Ligne_Metro_7b = {"la courneuve 8 mai 1945","fort d'aubertvilliers","aubervilliers-pantin quatre chemins","porte de la vilette","corentin cariou","crimée","riquet","stalingrad","louis-blanc","château-landon","gare de l'est","poissonière","cadet","le peletier","chaussée d'antin - la fayette","opéra","pyramides","palais-royal-musée du louvre","pont neuf","châtelet","pont marie","sully-morland","jussieu","place monge","censier-daubenton","les gobelins","place d'italie","tolbiac","maison blanche","le kremlin-bicêtre", "villejuif léo lagrange","villejuif paul vaillant-couturier","villejuif louis-aragon"}
Ligne_Metro_8 ={"balard""lourmel","boucicaut","félix faure","commerce","la motte-picquet grenelle","école militaire","la tour-maubourg","invalides","concorde","madeleine","opéra","richelieu-drouot","grands boulevards","bonne nouvelle","strasbourg-saint-denis","république","filles de calvaire","saint-sébastien - froissart","chemin vert","bastille","ledru-rollin","faidherbe - chaligny","reuilly -  diderot","montgallet","daumesnil","michel bizot","porte dorée","porte de charenton","liberté","charenton - écoles","école vétérinaire de maisons-alfort","maisons-alfort - stade","maisons-alfort - les juilliottes","créteil - l'échat", "créteil - université","créteil - préfectures"}
Ligne_Metro_9 =
Ligne_Metro_10 =
Ligne_Metro_11 =
Ligne_Metro_12 =
Ligne_Metro_13 =
Ligne_Metro_14 =
"""

###Données ILE-DE-FRANCE : Lignes, Sites, Disciplines:

Sites = [ "Arena Porte de la Chapelle", "Grand Palais" , "La Concorde","Pont Alexandre III","Pont d'Iéna","Invalides","Hotel de Ville","Stade Tour Eiffel","Arena Champ de Mars","Stade Roland Garros","Arena Bercy","Parc des Princes","Arena Paris Sud 6","Arena Paris Sud 1","Arena Paris Sud  4","Stand de tir de la Courneuve","Site d'Esclalade du Bourget","Stade Yves-du-Manoir","Stade de France","Centre Aquatique","Arena la Défense","Château de Versailles","Colline d'Elancourt","Vélodrome National de Saint-Quentin-En-Yvelines","Stade BMX de Saint-Quentin-En-Yvelines","Golf National","Stade Nautique des Vaires-Sur-Marne"]

dictionnaire = {"Arena Porte de la Chapelle" : [ ["badminton", "gymnastique rythmique"],["para badminton", "para powerlifting"]] , "Grand Palais" : [["escrime", "taekwondo"],["para taekwondo","escrime fauteuil"]] , "La Concorde" : [["basketball 3x3", "bmx freestyle", "breaking", "skateboard"],""] , "Pont Alexandre III" :[["natation marathon", "triathlon", "cyclisme sur route"],""] , "Pont d’Iéna" : [["triathlon", "cyclisme sur route", "athlétisme", "natation marathon"],["para triathlon"]] , "Invalides" : [["tir à l’arc", "athlétisme", "cyclisme sur route"],["para tir à l’arc"]] , "Hotel de Ville" : [["athlétisme"],""] , "Stade Tour Eiffel" : [["volleyball de plage"],["cécifoot"]] , "Arena Champ de Mars" : [["judo", "lutte"],["para judo", "rugby fauteuil"]] , "Stade Roland Garros" : [["tennis", "boxe"],["volleyball assis", "tennis fauteuil"]] , "Arena Bercy" :[["basketball", "gymnastique artistique", "trampoline"],["basket fauteuil"]] , "Parc des Princes" : [["football"],""] , "Arena Paris Sud 6" : [["haltérophilie"],["goalball"]] , "Arena Paris Sud 1" : [["volleyball"],["boccia"]] , "Arena Paris Sud 4" : [["tennis de table"],["para tennis de table"]] , "Stand de tir de La Courneuve" : [["tir"],["para tir sportif"]] , "Site d’Escalade du Bourget" : [["escalade"],""] , "Stade Yves-du-Manoir": [["hockey"],""] , "Stade de France": [["athlétisme","rugby"],["para athlétisme"]] , "Centre Aquatique" : [["natation artistique","plongeon","water-polo"],""] , "Arena la Défense" : [["natation","water-polo"],["para natation"]] , "Château de Versailles" : [["sports équestres", "pentathlon moderne"], ["para équitation (para dressage)"]] , "Colline d’Elancourt" : [["vtt"],""] , "Vélodrome National de Saint-Quentin-En-Yvelines" : [["cyclisme sur piste", "pentathlon moderne"],["para cyclisme sur route"]] , "Stade BMX de Saint-Quentin-En-Yvelines" : [["bmx race"],""] , "Golf National" : [["golf"],""] , "Stade Nautique de Vaires-Sur-Marne" : [["canoë", "aviron"],["para canoë", "para aviron"]] }

##Lignes Paris Grand Express concernées (pour Paris métropole sans Paris ville)

Ligne_14 = ["aéroport d'orly","pont de rungis", "m.i.n. porte de thiais","chevilly trois-communes","villejuif institut gustave-roussy", "kremlin-bicêtre hôpital","maison-blanche paris xiiie","olympiades","bibliothèque françois mitterand","cour saint-émilion","bercy","gare de lyon", "châtelet", "pyramides", "madeleine",  "saint-lazare","pont cardinet","porte de clichy", "saint-ouen rer c", "mairie de saint-ouen","saint-denis-pleyel"]
Ligne_15_sud = ["pont de sèvres","issy rer","fort d'issy - vanves - clamart","châtillon - montrouge" ,"bagneux" ,"arceuil - cachan","villejuif institut gustave-roussy","villejuif louis-aragon","vitry centre","les ardoines","le vert de maisons","créteil l'échat","saint-maur - créteil","champigny centre","bry - villiers - champigny","noisy - champs"]
Ligne_15_est = ["saint-denis-pleyel","stade de france","mairie d'aubervilliers","fort d'aubervilliers","drancy - bobigny","bobigny pablo-picasso","pont de bondy","bondy","rosny bois-perrier","val de fontenay","nogent - le perreux","champigny centre"]
Ligne_15_ouest = ["pont de sèvres","saint-cloud","rueil - suresnes mont valérien","naterre la boule","nanterre la folie","la défense","bécon-les-bruyères","bois-colombes","les agnettes","les grésillons","saint-denis-pleyel"]
Ligne_16 = ["saint-denis-pleyel","la courneuve six routes","le bourget rer","le blanc-mesnil","aulnay","sevran - livry","clichy - montfermeil","chelles","noisy - champs"]
Ligne_17 = ["saint-denis-pleyel","la courneuve six-routes","le bourget rer","le bourget aéroport","triangle de gonesse","parc des expositions","aéroport charles-de-gaulle t2","aéroport charles-de-gaulle t4","le mesnil-amelot"]
Ligne_18 = ["aéroport d'orly","antonypole","massy opéra","massy-palaiseau","palaiseau","orsay - gif","cea saint-aubin","saint-quentin est","satory","versailles chantiers"]

dic_Lignes = {0:["Ligne_14",Ligne_14],1:["Ligne_15_sud",Ligne_15_sud],2:["Ligne_15_est",Ligne_15_est],3: ["Ligne_15_ouest",Ligne_15_ouest],4:["Ligne_16",Ligne_16],5:["Ligne_17",Ligne_17],6:["Ligne_18",Ligne_18]}

#Coût du trajet avec Paris Grand Express
Segment_Ligne_14 = [[3,3],[2,2],[3,3],[2,2],[3,3],[2,2],[3,3],[2,2],[3,3],[2,2],[4,4],[7,7],[4,4],[3,3],[3,3],[5,5],[2,2],[3,3],[2,2],[3,3]]
Segment_Ligne_15_sud = [[3,3],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[3,3],[3,3],[3,3],[4,4],[4,4],[3,3],[5,5]]
Segment_Ligne_15_est = [[2,2],[3,3],[3,3],[12,10],[14,12],[9,3],[3,3],[3,3],[6,7],[4,4],[3,3]]
Segment_Ligne_15_ouest = [[3,3],[3,3],[3,3],[3,3],[5,5],[6,6],[5,5],[5,5],[4,4],[4,4],[10,10]]
Segment_Ligne_16 = [[3,3],[3,3],[3,3],[3,3],[5,5],[4,4],[4,4],[4,4]]
Segment_Ligne_17 = [[3,3],[3,3],[3,3],[4,4],[4,4],[5,5],[3,3],[3,3]]
Segment_Ligne_18 = [[4,4],[3,3],[3,3],[5,5],[3,3],[3,3],[7,7],[4,4],[3,3]]

Segments_PGE = [Segment_Ligne_14, Segment_Ligne_15_sud, Segment_Ligne_15_est, Segment_Ligne_15_ouest, Segment_Ligne_16, Segment_Ligne_17, Segment_Ligne_18]

#Coût du trajet SANS PGE
Sgmnt_Ligne_14 = [[19,19],[15,15],[13,13],[16,16],[20,20],[14,14],[15,15],[2,2],[4,4],[4,4],[4,4],[7,7],[4,4],[3,3],[3,3],[13,13],[12,12],[11,11],[7,7],[12,12]]
Sgmnt_Ligne_15_sud = [[25,25],[13,13],[11,11],[23,23],[9,9],[20,20],[13,13],[12,12],[17,17],[27,27],[16,16],[20,20],[22,22],[27,27],[44,44]]
Sgmnt_Ligne_15_est = [[13,13],[14,14],[15,13],[12,10],[14,12],[9,9],[16,16],[11,9],[6,7],[4,4],[22,20]]
Sgmnt_Ligne_15_ouest = [[20,20],[31,31],[34,34],[23,23],[9,9],[10,10],[10,10],[12,12],[18,18],[24,24]]
Sgmnt_Ligne_16 = [[21,21],[21,21],[23,23],[25,25],[24,24],[45,45],[45,45],[25,25],[0,0]]
Sgmnt_Ligne_17 = [[21,21],[21,21],[16,16],[43,43],[33,33],[11,11],[8,8],[27,27]]
Sgmnt_Ligne_18 = [[28,28],[16,16],[20,20],[19,19],[14,14],[12,12],[24,24],[26,26],[15,15]]

Segments_sans_PGE = [Sgmnt_Ligne_14, Sgmnt_Ligne_15_sud, Sgmnt_Ligne_15_est, Sgmnt_Ligne_15_ouest, Sgmnt_Ligne_16, Sgmnt_Ligne_17, Sgmnt_Ligne_18]




###Partie 1 : premiers programmes
##récuperer les disciplines

def dis_j_olympiques():
#'''récupère tous les sites des jeux olympiques par lieux'''
    dis = []
    for sites in dictionnaire:
        dis.append(dictionnaire[sites][0])
    return dis

j_o = dis_j_olympiques()

def dis_j_paralympiques():
#''' récupère tous les sites des jeux paralympiques par lieux'''
    dis = []
    for sites in dictionnaire:
        dis.append(dictionnaire[sites][1])
    return dis

j_p = dis_j_paralympiques()

def listeliste_v_liste(L):
    l = []

    for liste in L:
        for i in range(len(liste)):
            if liste[i] not in l:
                l.append(liste[i])
    l.sort()
    return l

#liste des disciplines
dis_olympiques = listeliste_v_liste(j_o) #liste des disciplines olympiques
dis_paralympiques = listeliste_v_liste(j_p) #liste des disciplines paralypiques

## site, discipline : l'un pour trouver l'autre

def disciplines_du_site(Site): #récupère pour chaque site, les disciplines olympiques et paralympiques
    d_olym = []
    d_para = []

    for d in dictionnaire[Site][0]:
        d_olym.append(d)
    for d in dictionnaire[Site][1]:
        d_para.append(d)

    return d_olym, d_para

def sites_de_la_discipline(discipline): #pour chaque discipline, on récupère la liste des sites où elle peut se dérouler
    sites = []
    for lieu,disciplines in dictionnaire.items():
        for d in disciplines:
            if discipline in d:
                sites.append(lieu)
    return sites

###Partie 2 : calcul de trajet

#Partie 1

def f_Stations():
    L = []
    for indice_ligne, ligne in dic_Lignes.items():
        for station in dic_Lignes[indice_ligne][1]:
            if not (station in L):
                L.append(station)
    return L

Stations = f_Stations() #Toutes les stations du PGE
nb_stations = len(Stations)


def f_S1_Vers_S2(S1,S2):
#'''détermine si deux stations S1 et S2 sont voisines.'''
    for indice_ligne, ligne in dic_Lignes.items():
        L = ligne[1] #liste des stations de la ligne


        if (S1 in L) and (S2 in L):
            indice_S1_dans_L = L.index(S1)
            indice_S2_dans_L = L.index(S2)


            if indice_S2_dans_L == 1 + indice_S1_dans_L:
                return (True, indice_ligne, min(indice_S1_dans_L,indice_S2_dans_L))

    return (False,None,None)


import numpy as np

def f_graphe(Segment):
    H = nb_stations
    G = np.zeros((H,H),int)


    for i in range(H):
        for j in range(H): #demarrer de i à H?
            S1, S2 = Stations[i],Stations[j]

            condition, indice_ligne_dans_Lignes, indice_sta_S1_dans_ligne = f_S1_Vers_S2(S1,S2)

            if condition: #si les stations sont voisines, on récupère le cout du trajet entre les deux
                G[i,j],G[j,i] = Segment[indice_ligne_dans_Lignes][indice_sta_S1_dans_ligne][0],Segment[indice_ligne_dans_Lignes][indice_sta_S1_dans_ligne][1]
    return G

G_PGE = f_graphe(Segments_PGE)
G_sans_PGE = f_graphe(Segments_sans_PGE)

#Partie II

def f_voisins(S):
    Vois = []
    ind_S = Stations.index(S)
    for v in Stations:
        Iv = Stations.index(v)
        G = f_graphe()
        if G[Iv][ind_S]>0:
            Vois.append(Stations[Iv])
    return Vois

#Q5
from collections import deque

def parcours_largeur(S):

    s_visite = [S]
    while len(f)!=0:
        S = f.popleft()
        Voisins = f_voisins(S)
        for station in Voisins:
            if station not in s_visite:
                f.append(station)
                s_visite.append(station)
    return s_visite

def parcours_largeur2(S):

    Distances = [0]*len(Stations) #liste des distances de chaque station par rapport à la station de départ
    f = deque()
    f.append(S)
    s_visite = {S:0}

    while len(f)!=0:
        s = f.popleft()

        Voisins = f_voisins(s) #liste des voisins de la station de départ
        iS = Stations.index(s)

        for station in Voisins:
            if station not in s_visite:
                f.append(station)

                iV= Stations.index(station)
                Distances[iV]= Distances[iS]+1
                s_visite[station]=Distances[iV]

    return s_visite

s_visite = []
def parcours_profondeur(S):

    s_visite.append(S)
    Voisins = f_voisins(S)
    for station in Voisins:
        if station not in s_visite:
                parcours_profondeur(station)
    return s_visite

def parcours_profondeur_v2(S):
    return 'a'

#Partie III : Plus court chemin entre 2 stations

#PRENDRE EN COMPTE LES CHANGEMENTS DE LIGNE

def algo_dijkstra(sdeb,sfin,G):


    P=[0]*nb_stations
    Distances = [np.inf]*nb_stations #Initialisation des distances (à  + infini)

    s_min = sdeb
    iS = Stations.index(s_min)
    Distances[iS]=0 #Distance destination de départ= 0

    reste = Stations.copy() #on fait une copie de la liste des stations pour pouvoir la diminuer

    while s_min!=sfin and len(reste)>0 and Distances[iS]!=np.inf:
        s_min = reste[0]
        iS = Stations.index(s_min)
        Min = Distances[iS]

        for station in reste:

            if debug:
                print(reste)

            i= Stations.index(station)
            d= Distances[i]

            if d<Min:
                Min = d
                s_min = station
                iS = i

        reste.remove(s_min)

        Voisins = []
        for station in reste: # on ajoute toutes les stations voisines
            iB = Stations.index(station)

            d = G[iS,iB]
            if d>0:
                Voisins.append(station)

        for v in Voisins:
            iV = Stations.index(v)

            if Distances[iS]+G[iS,iV]<Distances[iV]:
                Distances[iV]=Distances[iS]+G[iS,iV]
                P[iV]=s_min

    i_Arr = Stations.index(sfin)
    Dst = Distances[i_Arr]

    if Dst == np.inf:
            print("Pas de chemin possible")
    else:
        arrivee = sfin
        Chemin = [arrivee]
        while arrivee != sdeb:
            i = Stations.index(arrivee)
            arrivee = P[i]
            Chemin = [arrivee]+Chemin

        return Chemin

def cout_trajet_optimal(sdeb,sfin,G):
    Chemin = algo_dijkstra(sdeb,sfin,G)
    cout_du_trajet = 0

    for indice_station in range(len(Chemin)-1):

        station = Chemin[indice_station]
        station_suivante = Chemin[indice_station + 1]

        indice_station_dans_Stations = Stations.index(station)
        indice_station_suivante_dans_Stations = Stations.index(station_suivante)

        cout_du_trajet += G[indice_station_dans_Stations,indice_station_suivante_dans_Stations]

    return cout_du_trajet


station_la_plus_proche_du_site = {"Arena Porte de la Chapelle" : "", "Grand Palais" : "", "La Concorde" : "" , "Pont Alexandre III" : "" , "Pont d’Iéna" : "" , "Invalides" : "" , "Hotel de Ville" : "" , "Stade Tour Eiffel" : "" , "Arena Champ de Mars" : "" , "Stade Roland Garros" : "" , "Arena Bercy" : "" , "Parc des Princes" : "" , "Arena Paris Sud 6" : "" , "Arena Paris Sud 1" : "", "Arena Paris Sud 4" : "" , "Stand de tir de La Courneuve" : "le bourget rer" , "Site d’Escalade du Bourget" : "le bourget rer" , "Stade Yves-du-Manoir": "bois-colombes" , "Stade de France" : "stade de france" , "Centre Aquatique" : "stade de france" , "Arena la Défense" : "nanterre la folie" , "Château de Versailles" : "versailles chantiers" , "Colline d’Elancourt" : "versailles chantiers" , "Vélodrome National de Saint-Quentin-En-Yvelines" : "versailles chantiers" , "Stade BMX de Saint-Quentin-En-Yvelines" : "versailles chantiers" , "Golf National" : "saint-quentin est", "Stade Nautique de Vaires-Sur-Marne" : "noisy - champs" }

### Algorithme du choix du plus court trajet.

def optimisation_demande_spectateur(sport, depart, G):

    liste_sites = sites_de_la_discipline(sport) #on récupère tous les sites où la discipline souhaitée se déroule

    site_le_plus_proche = liste_sites[0]
    station_la_plus_proche = station_la_plus_proche_du_site[ liste_sites[0]]
     #on récupère la station la plus proche du premier site de la liste

    print(station_la_plus_proche)

    trajet_le_plus_court = algo_dijkstra(depart, station_la_plus_proche, G) #on recupère le trajet jusqu'à cette station
    cout_minimal = cout_trajet_optimal(depart, station_la_plus_proche,G)
#on récupère le cout du trajet jusqu'à cette station

    for site in liste_sites[1:]:
        cout =  cout_trajet_optimal(depart,station_la_plus_proche_du_site[site],G)

        if cout <  cout_minimal :
            trajet_le_plus_court = algo_dijkstra(depart,station_la_plus_proche[site],G)
            cout_minimal = cout
            site_le_plus_proche = site
            station_la_plus_proche = station_la_plus_proche_du_site[site]


    return site_le_plus_proche, station_la_plus_proche, trajet_le_plus_court, cout_minimal
