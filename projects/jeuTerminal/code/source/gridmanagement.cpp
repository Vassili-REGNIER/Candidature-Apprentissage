#include <iostream>
#include "../headers/gridmanagement.h"
#include "../headers/type.h"

using namespace std;

/*!
 * \brief Clears the terminal screen.
 *
 * This function is used to clean the terminal by clearing its content.
 */
void clearScreen()
{
    cout << "\033[H\033[2J";
}

/*!
 * \brief Initializes the game matrix.
 *
 * This function sets up the game matrix from scratch based on the game's level
 *
 * \param[out] level The current level configuration to be initialized.
 * \param[out] Mat The matrix representing the game grid.
 */
void initGrid(Level& level, Matrix& Mat)
{
    // Create a matrix filled with the level default cell
    Mat.resize (level.NbRow);
    const Line KLine (level.NbColumn, level.defaultCell);
    for (Line & ALine : Mat)
        ALine = KLine;

    // Replace the default cells with the cells of the map
    for (Cell c : level.terrainCases)
        Mat[c.first.first][c.first.second] = c.second;
}

/*!
 * \brief Displays the game grid on the terminal.
 *
 * This function renders the game grid based on the current state
 * of the matrix and player positions.
 *
 * \param[in] level The current level of the game.
 * \param[in] Mat The game matrix to be displayed.
 * \param[in] posPlayer1 The position of Player 1.
 * \param[in] posPlayer2 The position of Player 2.
 */
void displayGrid(Level& level, const Matrix& Mat, const Position& posPlayer1, const Position& posPlayer2)
{
    pair<string, vector<string>> skin_actual;
    for (unsigned i = 0; i < level.NbRow; ++i)
    {
        for (unsigned j = 0; j < 4; ++j)
        {
            for (unsigned k = 0; k < level.NbColumn; ++k)
            {
                char cell = Mat[i][k];
                if (posPlayer1.first == i && posPlayer1.second == k)
                {
                    cell = level.tokenP1;
                }
                else if (posPlayer2.first == i && posPlayer2.second == k)
                {
                    cell = level.tokenP2;
                }
                for (const auto& skin : SkinList)
                {
                    if (skin.first.at(0) == cell) {
                        skin_actual = skin;
                        break;
                    }
                }
                printPixel(skin_actual.second[5*j]);
                printPixel(skin_actual.second[5*j + 1]);
                printPixel(skin_actual.second[5*j + 2]);
                printPixel(skin_actual.second[5*j + 3]);
                printPixel(skin_actual.second[5*j + 4]);
            }
            cout << endl;
        }
    }
}

/*!
 * \brief Prints a single pixel with a specified background color.
 *
 * This function prints a single pixel to the terminal using the provided background color code.
 *
 * \param[in] bgColor The color code for the background, example : BACK_GREEN_LIGHT.
 */
void printPixel(const string& bgColor) {
    if (bgColor == "GREEN_LIGHT") {
        cout << BACK_GREEN_LIGHT << ' ' << BACK_RESET;
    } else if (bgColor == "GREEN_DARK") {
        cout << BACK_GREEN_DARK << ' ' << BACK_RESET;
    } else if (bgColor == "BROWN_LIGHT") {
        cout << BACK_BROWN_LIGHT << ' ' << BACK_RESET;
    } else if (bgColor == "BROWN_DARK") {
        cout << BACK_BROWN_DARK << ' ' << BACK_RESET;
    } else if (bgColor == "BLACK") {
        cout << BACK_BLACK << ' ' << BACK_RESET;
    } else if (bgColor == "GRAY") {
        cout << BACK_GRAY << ' ' << BACK_RESET;
    } else if (bgColor == "WHITE") {
        cout << BACK_WHITE << ' ' << BACK_RESET;
    } else if (bgColor == "BLUE_DARK") {
        cout << BACK_BLUE_DARK << ' ' << BACK_RESET;
    } else if (bgColor == "BLUE_CYAN") {
        cout << BACK_BLUE_CYAN << ' ' << BACK_RESET;
    } else if (bgColor == "BLUE_LIGHT") {
        cout << BACK_BLUE_LIGHT << ' ' << BACK_RESET;
    } else if (bgColor == "PURPLE_DARK") {
        cout << BACK_PURPLE_DARK << ' ' << BACK_RESET;
    } else if (bgColor == "PURPLE_LIGHT") {
        cout << BACK_PURPLE_LIGHT << ' ' << BACK_RESET;
    } else if (bgColor == "RED_DARK") {
        cout << BACK_RED_DARK << ' ' << BACK_RESET;
    } else if (bgColor == "RED_LIGHT") {
        cout << BACK_RED_LIGHT << ' ' << BACK_RESET;
    } else {
        cout << "Couleur inconnue : " << bgColor;
    }
}

/*!
 * \brief Displays a skin on the terminal.
 *
 * This function renders a visual representation of a terrain or element skin
 * using a vector of color codes.
 *
 * \param[in] skin A vector of strings where each string represents a background color code for a pixel.
 */
void displaySkin(vector<string> skin) {
    for (unsigned i = 0; i < 4; ++i)
    {
        cout << "      ";
        for (unsigned j = 0; j < 5; ++j)
        {
            printPixel(skin[i*5 + j]);
        }
        cout << endl;
    }
}
