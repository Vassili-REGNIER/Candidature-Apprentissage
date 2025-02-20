#pragma once

/*!
 * \file params.h
 * \brief Defines the parameters, level and associated functions.
 * \author Regnier Vassili
 * \version 1.0
 * \date 8 January 2025
 */

#include "type.h"
#include <string>

/*!
 * \brief Initializes the basic game settings.
 *
 * \param[out] settings The settings object to be initialized.
 */
void initSettings(Settings& settings);

/*!
 * \brief Initializes a level with default values.
 *
 * \param[out] level The level object to be initialized.
 */
void initLevel(Level& level);

/*!
 * \brief Loads the game settings from a specified file path.
 *
 * \param[out] settings The settings object to be updated.
 * \param[in] path The file path of the settings file.
 */
void loadSettings(Settings& settings, const std::string& path);

/*!
 * \brief Loads a level from a specified file path.
 *
 * \param[out] level The level object to be updated.
 * \param[in] path The file path of the level file.
 */
void loadLevel(Level& level, const std::string& path);

/*!
 * \brief Splits a string into two parts based on a separator.
 *
 * \param[in] input The input string to be split.
 * \param[out] part1 The first part of the split string.
 * \param[out] part2 The second part of the split string.
 * \param[out] sep The separator character used in the split.
 */
void splitString(const std::string& input, std::string& part1, std::string& part2, char sep);

/*!
 * \brief Adds a terrain cell to the level based on a value.
 *
 * \param[in, out] level The level object where the cell will be added.
 * \param[in] value The value defining the terrain cell.
 */
void addTerrainCell(Level& level, const std::string& value);

/*!
 * \brief Reads a position from a string.
 *
 * \param[in] StringPos The string containing the position information.
 * \return Position The position found from the string.
 */
Position readPos(const std::string& StringPos);

/*!
 * \brief Removes leading and trailing spaces from a string.
 *
 * This function modifies the input string by removing any spaces
 * before the first non-space character and after the last non-space character.
 *
 * \param[in, out] str The string to be modified. The spaces at the beginning
 *                     and end of the string will be removed.
 */
void remove_space(std::string& str);
