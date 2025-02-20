#pragma once

/*!
 * \file game.h
 * \brief Defines every useful functions for the game.
 * \author Regnier Vassili
 * \version 1.0
 * \date 8 january 2025
 */

#include "type.h"

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
void moveToken(Settings& settings, Level& level, Matrix& Mat, const char& Move,
               Position& posPlayer1, Position& posPlayer2, bool& Player1Turn);

/*!
 * \brief Explains the rules of the game to the players.
 *
 * This function provides an overview of the game rules, explaining the purpose of different elements
 * like grass, trees, trampolines, walls, water, and portals. It also displays the skins associated
 * with each game element.
 */
void explainRules();

/*!
 * \brief Asks the player to select a level.
 *
 * This function repeatedly asks the player to choose a level (from 1 to 5) until a valid input is provided.
 * It ensures the input is a valid integer within the range.
 *
 * \return int The level selected by the player (between 1 and 5).
 */
int selectLevel();

/*!
 * \brief Retrieves the file path of a level based on its number.
 *
 * This function returns the file path corresponding to the selected level. The paths are predefined
 * and correspond to the level numbers 1 through 5.
 *
 * \param[in] level The level number chosen by the player.
 * \return string The file path of the level.
 */
std::string getPathLevel(int level);

/*!
 * \brief Main function for starting the game loop.
 *
 * This function serves as the entry point to the game and handles
 * the main gameplay loop.
 *
 * \return int Returns 0 if the game runs successfully.
 */
int game();
