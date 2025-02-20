#include <iostream>
#include <string>

#include "../headers/game.h"
#include "../headers/type.h"
#include "../headers/params.h"
#include "../headers/gridmanagement.h"

using namespace std;

/*!
 * \brief Moves the token of the player based on the user's input.
 *
 * This function updates the matrix and the player's position.
 *
 * \param[in, out] settings    Game settings.
 * \param[in, out] level       Current level of the game.
 * \param[in, out] Mat         The game matrix.
 * \param[in]      Move        The key pressed by the user to determine the move.
 * \param[in, out] posPlayer1  Position of Player 1.
 * \param[in, out] posPlayer2  Position of Player 2e.
 * \param[in, out] Player1Turn Boolean indicating if it is Player 1's turn.
 */
void moveToken(Settings& settings, Level& level, Matrix& Mat, const char& Move, Position& posPlayer1, Position& posPlayer2, bool& Player1Turn)
{
    Position Pos = (Player1Turn ? posPlayer1 : posPlayer2);

    // Determines the position where the player wants to go
    unsigned x (Pos.first), y (Pos.second);
    if (settings.KeyUpLeft == Move) {
        if (x > 0 && y > 0) {
            --x;
            --y;
        }
    }
    else if (settings.KeyUp == Move) {
        if (x > 0) {
            --x;
        }
    }
    else if (settings.KeyUpRight == Move) {
        if (x > 0 && y < level.NbColumn - 1) {
            --x;
            ++y;
        }
    }
    else if (settings.KeyLeft == Move) {
        if (y > 0) {
            --y;
        }
    }
    else if (settings.KeyRight == Move) {
        if (y < level.NbColumn - 1) {
            ++y;
        }
    } 
    else if (settings.KeyDownLeft == Move) {
        if ((x < level.NbRow - 1) && y > 0) {
            ++x;
            --y;
        }
    } 
    else if (settings.KeyDown == Move) {
        if (x < level.NbRow - 1) {
            ++x;
        }
    }
    else if (settings.KeyDownRight == Move) {
        if (x < level.NbRow - 1 && y < level.NbColumn - 1) {
            ++x;
            ++y;
        }
    }

    // The player want to go in a forbidden position
    if (Mat[x][y] == 'w' || Mat[x][y] == 't' || Mat[x][y] == 'l' ) {
        return;
    }
    // The player want to go on grass
    else if (Mat[x][y] == 'g') {
        if (Player1Turn) posPlayer1 = {x, y};
        else posPlayer2 = {x, y};
    }
    // The player want to go on a jump pad
    else if (Mat[x][y] == 'j') {
        if (Player1Turn) posPlayer1 = {x, y};
        else posPlayer2 = {x, y};
        moveToken (settings, level, Mat, Move, posPlayer1, posPlayer2, Player1Turn);
    }
    // The player want to go on a purple portal
    else if (Mat[x][y] == 'b' || Mat[x][y] == 'p' || Mat[x][y] == 'r') {
        // Find the coordinates of the other purple portal
        for (size_t row = 0; row < level.NbRow; ++row) {
            for (size_t col = 0; col < level.NbColumn; ++col) {
                if (Mat[row][col] == Mat[x][y] && (row != x || col != y)) {
                    if (Player1Turn) posPlayer1 = {row, col};
                    else posPlayer2 = {row, col};
                }
            }
        }
    }
}

/*!
 * \brief Explains the rules of the game to the players.
 *
 * This function provides an overview of the game rules, explaining the purpose of different elements
 * like grass, trees, trampolines, walls, water, and portals. It also displays the skins associated
 * with each game element.
 */
void explainRules() {
    cout << "Règle du jeu : Le premier joueur qui attrape l'autre à gagné." << endl;
    cout << "Voici les différents éléments que vous rencontrerez :" << endl;
    cout << " - Le bloc d'herbe : Vous pouvez vous déplacer dessus." << endl;
    for (const auto& skin : SkinList)
    {
        if (skin.first.at(0) == 'g') {
            displaySkin(skin.second);
            break;
        }
    }
    cout << " - L'arbre : Vous ne pouvez pas vous déplacer dessus." << endl;
    for (const auto& skin : SkinList)
    {
        if (skin.first.at(0) == 't') {
            displaySkin(skin.second);
            break;
        }
    }
    cout << " - Le trampoline : Si vous avancez dessus, il vous fera avancer jusqu'à la case après lui." << endl;
    for (const auto& skin : SkinList)
    {
        if (skin.first.at(0) == 'j') {
            displaySkin(skin.second);
            break;
        }
    }
    cout << " - De l'eau : Vous ne pouvez pas vous déplacer dessus." << endl;
    for (const auto& skin : SkinList)
    {
        if (skin.first.at(0) == 'l') {
            displaySkin(skin.second);
            break;
        }
    }
    cout << " - Le mur : Vous ne pouvez pas vous déplacer dessus." << endl;
    for (const auto& skin : SkinList)
    {
        if (skin.first.at(0) == 'w') {
            displaySkin(skin.second);
            break;
        }
    }
    cout << " - Le portail : Si vous rentrez dedans, il vous téléportera à l'autre portail de la même couleur." << endl;
    for (const auto& skin : SkinList)
    {
        if (skin.first.at(0) == 'p') {
            displaySkin(skin.second);
            break;
        }
    }

    cout << " - Votre personnage : C'est vous dans la vraie vie." << endl;
    for (const auto& skin : SkinList)
    {
        if (skin.first.at(0) == '1') {
            displaySkin(skin.second);
            break;
        }
    }
}

/*!
 * \brief Asks the player to select a level.
 *
 * This function repeatedly asks the player to choose a level (from 1 to 5) until a valid input is provided.
 * It ensures the input is a valid integer within the range.
 *
 * \return int The level selected by the player (between 1 and 5).
 */
int selectLevel() {
    int level = 0;
    string input;
    cout << "Choisissez un niveau parmi les 5 niveaux disponibles (1 à 5) : \n>>> ";
    while (true) {
        getline(cin, input);
        input.resize(1);
        if (isdigit(input[0])) {
            level = stoi(input);
            // Check if the input is valid (integer) and in the range 1 to 5
            if (level < 1 || level > 5) {
                cout << "Entrée invalide, veuillez choisir un niveau entre 1 et 5 : \n>>> ";
            } else {
                // Valid input
                return level;
            }
        }
    }
}

/*!
 * \brief Retrieves the file path of a level based on its number.
 *
 * This function returns the file path corresponding to the selected level. The paths are predefined
 * and correspond to the level numbers 1 through 5.
 *
 * \param[in] level The level number chosen by the player.
 * \return string The file path of the level.
 */
string getPathLevel(int level) {
    // Sur linux
    // return "/amuhome/r24030678/Documents/sae-cpp/v9/v9/jeu/levels/l1.yaml";
    switch (level) {
    case 1:
        return "../../levels/l1.yaml";
        break;
    case 2:
        return "../../levels/l2.yaml";
        break;
    case 3:
        return "../../levels/l3.yaml";
        break;
    case 4:
        return "../../levels/l4.yaml";
        break;
    case 5:
        return "../../levels/l5.yaml";
        break;
    default:
        return "";
        break;
    }
}

/*!
 * \brief Main function for starting the game loop.
 *
 * This function serves as the entry point to the game and handles
 * the main gameplay loop.
 *
 * \return int Returns 0 if the game runs successfully.
 */
int game()
{
    // Initializes settings and level
    Settings settings;
    initSettings(settings);
    Level level;
    initLevel(level);

    // Explain rules and ask game level
    int levelNumber;
    explainRules();
    levelNumber = selectLevel();
    string level_path = getPathLevel(levelNumber);

    // Sur windows
    string config_path = "../../settings/settings.yaml";

    // Load settings and level
    loadSettings(settings, config_path);
    loadLevel(level, level_path);

    // Initializes all game variables then dispalys grid
    Position posPlayer1 = level.posPlayer1;
    Position posPlayer2 = level.posPlayer2;
    unsigned partyNum (1);
    Matrix Mat;
    bool player1Turn (true);
    bool victory (false);
    initGrid(level, Mat);
    displayGrid(level, Mat, posPlayer1, posPlayer2);

    string entry;
    char move;
    while (partyNum <= level.KMaxPartyNum && !victory)
    {
        // Request then retrieve the move safely
        cout << "Tour numero : " << partyNum << ", Joueur " << (player1Turn ? '1' : '2') << ", entrez un déplacement :\n>>>";
        getline(cin, entry);
        move = tolower(entry[0]);

        // Move token then update the display
        moveToken (settings, level, Mat, move, posPlayer1, posPlayer2, player1Turn);
        clearScreen();
        displayGrid (level, Mat, posPlayer1, posPlayer2);

        // Check if a player has won then move on to the next round
        if (posPlayer1 == posPlayer2) victory = true;
        ++partyNum;
        player1Turn = !player1Turn;
    }

    // If the game ended but there no one won, then there is no winner
    if (!victory)
    {
        cout << "Aucun vainqueur" << endl;
        return 0;
    }

    // Else, display the winner
    cout << "Félicitations Joueur " << (player1Turn ? '2' : '1') << " vous avez gagné :)" << endl;
    return 0;
}
