#pragma once

/*!
 * \file type.h
 * \brief Definition of useful types and aliases for the project.
 * \author Regnier Vassili
 * \version 1.0
 * \date 8 January 2025
 */

#include <map>
#include <string>
#include <vector>

/*!
 * \brief Line : alias for a line in the game grid matrix.
 */
typedef std::vector<char> Line;

/*!
 * \brief Matrix : alias for the game grid, a vector of Line.
 */
typedef std::vector<Line> Matrix;

/*!
 * \brief Position : represents a coordinate pair (row, column) in the grid.
 */
typedef std::pair<unsigned, unsigned> Position;

/*!
 * \brief Cell : represents a cell in the grid with a position and a character value.
 */
typedef std::pair<Position, char> Cell;

/*!
 * \brief SkinList : a map containing skin of every element to disaply in the game.
 *
 * Each skin consists of a name and a vector of strings representing color codes.
 */
const std::map<std::string, std::vector<std::string>> SkinList = {
    {"grass", {"GREEN_LIGHT", "GREEN_LIGHT", "GREEN_LIGHT", "GREEN_LIGHT", "GREEN_LIGHT",
               "GREEN_LIGHT", "GREEN_LIGHT", "GREEN_LIGHT", "GREEN_LIGHT", "GREEN_LIGHT",
               "GREEN_LIGHT", "GREEN_LIGHT", "GREEN_LIGHT", "GREEN_LIGHT", "GREEN_LIGHT",
               "GREEN_LIGHT", "GREEN_LIGHT", "GREEN_LIGHT", "GREEN_LIGHT", "GREEN_LIGHT"}},

    {"tree", {"GREEN_LIGHT", "GREEN_DARK", "GREEN_DARK", "GREEN_DARK", "GREEN_LIGHT",
              "GREEN_DARK", "GREEN_DARK", "GREEN_DARK", "GREEN_DARK", "GREEN_DARK",
              "GREEN_LIGHT", "GREEN_LIGHT", "BROWN_LIGHT", "GREEN_LIGHT", "GREEN_LIGHT",
              "GREEN_LIGHT", "GREEN_LIGHT", "BROWN_LIGHT", "GREEN_LIGHT", "GREEN_LIGHT"}},
    {"jump-pad", {"GREEN_LIGHT", "GRAY", "GRAY", "GRAY", "GREEN_LIGHT",
                  "GRAY", "WHITE", "WHITE", "WHITE", "GRAY",
                  "GRAY", "WHITE", "WHITE", "WHITE", "GRAY",
                  "GREEN_LIGHT", "GRAY", "GRAY", "GRAY", "GREEN_LIGHT"}},

    {"l", {"BLUE_CYAN", "BLUE_DARK", "BLUE_DARK", "BLUE_CYAN", "BLUE_LIGHT",
               "BLUE_LIGHT", "BLUE_LIGHT", "BLUE_DARK", "BLUE_DARK", "BLUE_CYAN",
               "BLUE_CYAN", "BLUE_LIGHT", "BLUE_CYAN", "BLUE_CYAN", "BLUE_CYAN",
               "BLUE_DARK", "BLUE_LIGHT", "BLUE_LIGHT", "BLUE_CYAN", "BLUE_DARK"}},

    {"wall", {"GREEN_LIGHT", "GRAY", "BLACK", "GRAY", "GREEN_LIGHT",
              "GRAY", "BLACK", "GRAY", "GRAY", "BLACK",
              "BLACK", "GRAY", "GRAY", "BLACK", "GRAY",
              "GREEN_LIGHT", "GRAY", "BLACK", "GRAY", "GREEN_LIGHT"}},

    {"purple-portal", {"GREEN_LIGHT", "PURPLE_DARK", "PURPLE_DARK", "PURPLE_DARK", "GREEN_LIGHT",
                    "PURPLE_DARK", "PURPLE_DARK", "PURPLE_LIGHT", "PURPLE_LIGHT", "PURPLE_DARK",
                    "PURPLE_DARK", "PURPLE_LIGHT", "PURPLE_LIGHT", "PURPLE_DARK", "PURPLE_DARK",
                    "GREEN_LIGHT", "PURPLE_DARK", "PURPLE_DARK", "PURPLE_DARK", "GREEN_LIGHT"}},

    {"red-portal", {"GREEN_LIGHT", "RED_LIGHT", "RED_LIGHT", "RED_LIGHT", "GREEN_LIGHT",
                    "RED_LIGHT", "RED_LIGHT", "RED_DARK", "RED_DARK", "RED_LIGHT",
                    "RED_LIGHT", "RED_DARK", "RED_DARK", "RED_LIGHT", "RED_LIGHT",
                    "GREEN_LIGHT", "RED_LIGHT", "RED_LIGHT", "RED_LIGHT", "GREEN_LIGHT"}},

    {"brown-portal", {"GREEN_LIGHT", "BROWN_DARK", "BROWN_DARK", "BROWN_DARK", "GREEN_LIGHT",
                      "BROWN_DARK", "BROWN_DARK", "BROWN_LIGHT", "BROWN_LIGHT", "BROWN_DARK",
                      "BROWN_DARK", "BROWN_LIGHT", "BROWN_LIGHT", "BROWN_DARK", "BROWN_DARK",
                      "GREEN_LIGHT", "BROWN_DARK", "BROWN_DARK", "BROWN_DARK", "GREEN_LIGHT"}},

    {"1-skin", {"GREEN_LIGHT", "GREEN_LIGHT", "BROWN_DARK", "GREEN_LIGHT", "GREEN_LIGHT",
                "GREEN_LIGHT", "BLACK", "BLACK", "BLACK", "GREEN_LIGHT",
                "GREEN_LIGHT", "GREEN_LIGHT", "BLACK", "GREEN_LIGHT", "GREEN_LIGHT",
                "GREEN_LIGHT", "BLACK", "GREEN_LIGHT", "BLACK", "GREEN_LIGHT"}},

    {"2-skin", {"GREEN_LIGHT", "GREEN_LIGHT", "WHITE", "GREEN_LIGHT", "GREEN_LIGHT",
                "GREEN_LIGHT", "BLACK", "BLACK", "BLACK", "GREEN_LIGHT",
                "GREEN_LIGHT", "GREEN_LIGHT", "BLACK", "GREEN_LIGHT", "GREEN_LIGHT",
                "GREEN_LIGHT", "BLACK", "GREEN_LIGHT", "BLACK", "GREEN_LIGHT"}},

    {"3-skin", {"GREEN_LIGHT", "GREEN_LIGHT", "PURPLE_LIGHT", "GREEN_LIGHT", "GREEN_LIGHT",
                "GREEN_LIGHT", "BLACK", "BLACK", "BLACK", "GREEN_LIGHT",
                "GREEN_LIGHT", "GREEN_LIGHT", "BLACK", "GREEN_LIGHT", "GREEN_LIGHT",
                "GREEN_LIGHT", "BLACK", "GREEN_LIGHT", "BLACK", "GREEN_LIGHT"}},

    {"4-skin", {"GREEN_LIGHT", "GREEN_LIGHT", "BLUE_LIGHT", "GREEN_LIGHT", "GREEN_LIGHT",
                "GREEN_LIGHT", "BLACK", "BLACK", "BLACK", "GREEN_LIGHT",
                "GREEN_LIGHT", "GREEN_LIGHT", "BLACK", "GREEN_LIGHT", "GREEN_LIGHT",
                "GREEN_LIGHT", "BLACK", "GREEN_LIGHT", "BLACK", "GREEN_LIGHT"}},

    {"5-skin",{"GREEN_LIGHT", "GREEN_LIGHT", "RED_LIGHT", "GREEN_LIGHT", "GREEN_LIGHT",
                "GREEN_LIGHT", "BLACK", "BLACK", "BLACK", "GREEN_LIGHT",
                "GREEN_LIGHT", "GREEN_LIGHT", "BLACK", "GREEN_LIGHT", "GREEN_LIGHT",
                "GREEN_LIGHT", "BLACK", "GREEN_LIGHT", "BLACK", "GREEN_LIGHT"}},
};

/*!
 * \brief Settings struct contains the keybindings for player movement.
 */
struct Settings {
    char KeyUp = 'z';           //!< Key for moving up
    char KeyDown = 'x';         //!< Key for moving down
    char KeyLeft = 'q';         //!< Key for moving left
    char KeyRight = 'd';        //!< Key for moving right
    char KeyUpLeft = 'a';       //!< Key for moving up-left
    char KeyDownLeft = 'w';     //!< Key for moving down-left
    char KeyUpRight = 'e';      //!< Key for moving up-right
    char KeyDownRight = 'c';    //!< Key for moving down-right
};

/*!
 * \brief Level struct contains the game level settings, including the player positions and terrain.
 */
struct Level {
    char tokenP1 = '1';                //!< Player 1 token
    char tokenP2 = '2';                //!< Player 2 token
    Position posPlayer1 {0, 0};        //!< Initial position of Player 1
    Position posPlayer2 {2, 2};        //!< Initial position of Player 2
    unsigned KMaxPartyNum = 50;        //!< Maximum number of turns
    char defaultCell = 'g';            //!< Default cell type
    std::size_t NbColumn = 3;          //!< Number of columns in the grid
    std::size_t NbRow = 3;             //!< Number of rows in the grid
    std::vector<Cell> terrainCases;    //!< List of terrain cells in the grid
};

/*!
 * \def BACK_GREEN_LIGHT
 * \brief Background color code for light green.
 */
#define BACK_GREEN_LIGHT "\033[48;5;46m"

/*!
 * \def BACK_GREEN_DARK
 * \brief Background color code for dark green.
 */
#define BACK_GREEN_DARK "\033[48;5;22m"

/*!
 * \def BACK_BROWN_LIGHT
 * \brief Background color code for light brown.
 */
#define BACK_BROWN_LIGHT "\033[48;5;137m"

/*!
 * \def BACK_BROWN_DARK
 * \brief Background color code for dark brown.
 */
#define BACK_BROWN_DARK "\033[48;5;94m"

/*!
 * \def BACK_BLACK
 * \brief Background color code for black.
 */
#define BACK_BLACK "\033[48;5;16m"

/*!
 * \def BACK_GRAY
 * \brief Background color code for gray.
 */
#define BACK_GRAY "\033[48;5;242m"

/*!
 * \def BACK_WHITE
 * \brief Background color code for white.
 */
#define BACK_WHITE "\033[48;5;15m"

/*!
 * \def BACK_BLUE_DARK
 * \brief Background color code for dark blue.
 */
#define BACK_BLUE_DARK "\033[48;5;20m"

/*!
 * \def BACK_BLUE_CYAN
 * \brief Background color code for cyan blue.
 */
#define BACK_BLUE_CYAN "\033[48;5;38m"

/*!
 * \def BACK_BLUE_LIGHT
 * \brief Background color code for light blue.
 */
#define BACK_BLUE_LIGHT "\033[48;5;117m"

/*!
 * \def BACK_PURPLE_DARK
 * \brief Background color code for dark purple.
 */
#define BACK_PURPLE_DARK "\033[48;5;134m"

/*!
 * \def BACK_PURPLE_LIGHT
 * \brief Background color code for light purple.
 */
#define BACK_PURPLE_LIGHT "\033[48;5;207m"

/*!
 * \def BACK_RED_DARK
 * \brief Background color code for dark red.
 */
#define BACK_RED_DARK "\033[48;5;52m"

/*!
 * \def BACK_RED_LIGHT
 * \brief Background color code for light red.
 */
#define BACK_RED_LIGHT "\033[48;5;196m"

/*!
 * \def BACK_RESET
 * \brief Reset background color.
 */
#define BACK_RESET "\033[0m"


