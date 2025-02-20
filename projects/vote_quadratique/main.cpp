/**
 *  @date : 7 novembre 2024
 *  @author : Vassili Régnier
 *  @Brief : Implémentation du vote quadratique
**/
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

/**
 * @brief Lit une string
 * @author Alain Casali
 * @return la chaine lue sauf si :
 * (1) on une boulette sur l'entrée
 * (2) on trouve un commentaire sur l'entrée
 * le commentaire est matérialisé par la chaine "//"
**/
string litUneString (){
    string uneChaine;
    while (true){
        getline (cin, uneChaine);
        if ((!cin) || (uneChaine.substr(0,2) != "//")) break;
    }
    return uneChaine;
}

/**
 * @brief Lit un entier
 * @author Alain Casali
 * @return l'entier lue sauf si :
 * (1) on une boulette sur l'entrée
 * (2) on trouve un commentaire sur l'entrée
 * le commentaire est matérialisé par la chaine "//"
**/
int litUnEntier (){
    string uneChaine;
    while (true){
        getline (cin, uneChaine);
        if ((!cin) || (uneChaine.substr(0,2) != "//")) break;
    }
    return stoi(uneChaine);
}

struct electeur {
    string nom;
    string prenom;
    vector<unsigned> vote;
};

struct candidat {
    string nom;
    string prenom;
    float score = 0;
};

/**
 * @brief Récupère les données de votes adaptées au vote quadratique.
 * @author Vassili Régnier
 *
 * @param[out] points_max       Nombre maximum de points que chaque électeur peut attribuer.
 * @param[out] nombre_candidats Nombre total de candidats dans le vote.
 * @param[out] nombre_electeurs Nombre total d'électeurs participant au vote.
 * @param[out] candidats        Vecteur contenant les candidats (objets de la structure candidat).
 * @param[out] electeurs        Vecteur contenant les électeur (objets de la structure electeurs).
**/
void recupererDonneesVote(unsigned& points_max,
                          unsigned& nombre_candidats,
                          unsigned& nombre_electeurs,
                          vector<candidat>& candidats,
                          vector<electeur>& electeurs) {
    // Lit les paramètres de base du vote
    points_max = litUnEntier();
    nombre_candidats = litUnEntier();
    nombre_electeurs = litUnEntier();

    // Réserve de l'espace en fonction du nombre de candidats
    candidats.resize(nombre_candidats);

    // Lit les informations des candidats
    for (unsigned i = 0; i < nombre_candidats; ++i) {
        candidats[i].nom = litUneString();
        candidats[i].prenom = litUneString();
    }

    // Réserve de l'espace en fonction du nombre d'élécteurs
    electeurs.resize(nombre_electeurs);

    // Lit les informations des élécteurs
    for (unsigned i = 0; i < nombre_electeurs; ++i) {
        electeurs[i].nom = litUneString();
        electeurs[i].prenom = litUneString();
        for (unsigned j = 0; j < nombre_candidats; ++j) {
            electeurs[i].vote.push_back(litUnEntier());   // electeurs[i].vote[j] correspond au vote de l'élécteur i pour le candidat j
        }
    }
}

/**
 * @brief Calcule le candidat gagnant selon un système de vote quadratique.
 * @author Vassili Régnier
 * @return Une string : le nom du candidat ayant le score le plus élevé.
**/
candidat vote_quadratique() {
    // Déclare et récupère les données de l'élection
    unsigned nombre_candidats;
    unsigned nombre_electeurs;
    unsigned points_max;
    vector<candidat> candidats;
    vector<electeur> electeurs;
    recupererDonneesVote(points_max, nombre_candidats, nombre_electeurs, candidats, electeurs);

    // Calcul le score de chaque candidats
    for (unsigned i = 0; i < nombre_candidats; ++i) {
        for (unsigned j = 0; j < nombre_electeurs; ++j) {
            candidats[i].score += sqrt(electeurs[j].vote[i]); // On ajoute la racine carré des points attribués (principe du vote quadratique)
        }
    }

    // Détermine le candidat avec le meilleur score
    float plusDeScore = candidats[0].score;
    unsigned indicePlusDeScore = 0;
    for (unsigned i = 1; i < nombre_candidats; ++i) {
        if (candidats[i].score > plusDeScore) {
            plusDeScore = candidats[i].score;
            indicePlusDeScore = i;
        }
    }


    // Renvoie le candidat avec le plus de score
    return candidats[indicePlusDeScore];
}

int main() {
    // Détermine puis affiche le gagnant de l'élection selon le vote quadratique
    candidat gagnant = vote_quadratique();
    cout << "Le gagnant est :" << endl << gagnant.nom << gagnant.prenom;
    return 0;
}
