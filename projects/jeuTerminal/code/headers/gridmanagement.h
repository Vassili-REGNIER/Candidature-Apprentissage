#pragma once

/*!
 * \file gridmanagement.h
 * \brief Defines useful functions for managing the game grid.
 * \author Regnier Vassili
 * \version 1.0
 * \date 8 january 2025
 */

#include "type.h"

/*!
 * \brief Clears the terminal screen.
 *
 * This function is used to clean the terminal by clearing its content.
 */
void clearScreen();

/*!
 * \brief Initializes the game matrix.
 *
 * This function sets up the game matrix from scratch based on the game's level
 *
 * \param[out] level The current level configuration to be initialized.
 * \param[out] Mat The matrix representing the game grid.
 */
void initGrid(Level& level, Matrix& Mat);

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
void displayGrid(Level& level, const Matrix& Mat, const Position& posPlayer1, const Position& posPlayer2);

/*!
 * \brief Prints a single pixel with a specified background color.
 *
 * This function prints a single pixel to the terminal using the provided background color code.
 *
 * \param[in] bgColor The color code for the background, example : BACK_GREEN_LIGHT.
 */
void printPixel(const std::string& bgColor);

/*!
 * \brief Displays a skin on the terminal.
 *
 * This function renders a visual representation of a terrain or element skin
 * using a vector of color codes.
 *
 * \param[in] skin A vector of strings where each string represents a background color code for a pixel.
 */
void displaySkin(std::vector<std::string> skin);

