#include <string>
#include <fstream>
#include "../headers/params.h"

using namespace std;

/*!
 * \brief Initializes the basic game settings.
 *
 * \param[out] settings The settings object to be initialized.
 */
void initSettings(Settings& settings)
{
    // Set basic settings
    settings.KeyUp = 'z';
    settings.KeyDown = 'x';
    settings.KeyLeft = 'q';
    settings.KeyRight = 'd';
    settings.KeyUpLeft = 'a';
    settings.KeyUpRight = 'e';
    settings.KeyDownLeft = 'w';
    settings.KeyDownRight = 'c';
}

/*!
 * \brief Initializes a level with default values.
 *
 * \param[out] level The level object to be initialized.
 */
void initLevel(Level& level)
{
    // Set basic values
    level.tokenP1 = '1';
    level.tokenP2 = '2';
    Position posP1 (0, 0), posP2 (2, 2);
    level.posPlayer1 = posP1;
    level.posPlayer2 = posP2;
    level.NbColumn = 3;
    level.NbRow = 3;
}

/*!
 * \brief Loads the game settings from a specified file path.
 *
 * \param[out] settings The settings object to be updated.
 * \param[in] path The file path of the settings file.
 */
void loadSettings(Settings& settings, const string& path)
{
    ifstream file(path);

    // Load basic settings if unable to read the settings file
    if (!file.is_open()) {
        initSettings(settings);
        return;
    }

    // Go through all the lines of the file
    string line, key, value;
    while (getline(file, line)) {

        // Isolate values
        splitString(line, key, value, ':');
        remove_space(key);
        remove_space(value);

        // Assigns the value to the corresponding attribute
        if (key == "KeyUp") settings.KeyUp = value.at(0);
        else if (key == "KeyDown") settings.KeyDown = value.at(0);
        else if (key == "KeyDownLeft") settings.KeyDownLeft = value.at(0);
        else if (key == "KeyLeft") settings.KeyLeft = value.at(0);
        else if (key == "KeyUpLeft") settings.KeyUpLeft = value.at(0);
        else if (key == "KeyDownRight") settings.KeyDownRight = value.at(0);
        else if (key == "KeyRight") settings.KeyRight = value.at(0);
        else if (key == "KeyUpRight") settings.KeyUpRight = value.at(0);
    }
}

/*!
 * \brief Loads a level from a specified file path.
 *
 * \param[out] level The level object to be updated.
 * \param[in] path The file path of the level file.
 */
void loadLevel(Level& level, const string& path)
{
    ifstream file(path);

    // Load basic map if unable to read the map file
    if (!file.is_open())
    {
        initLevel(level);
        return;
    }

    // Go through all the lines of the file
    string line, key, value;
    while (getline(file, line))
    {
        // Isolate values
        splitString(line, key, value, ':');
        remove_space(key);
        remove_space(value);

        // Assigns the value to the corresponding attribute
        if (key == "cell") addTerrainCell(level, value);
        else if (key == "defaultCell") level.defaultCell = value.at(0);
        else if (key == "TokenP1") level.tokenP1 = value.at(0);
        else if (key == "TokenP2") level.tokenP2 = value.at(0);
        else if (key == "PosPlayer1") level.posPlayer1 = readPos(value);
        else if (key == "PosPlayer2") level.posPlayer2 = readPos(value);
        else if (key == "KMaxPartyNum") level.KMaxPartyNum = stoul(value);
        else if (key == "NbColumn") level.NbColumn = stoull(value);
        else if (key == "NbRow") level.NbRow = stoull(value);
    }
}

/*!
 * \brief Splits a string into two parts based on a separator.
 *
 * \param[in] input The input string to be split.
 * \param[out] part1 The first part of the split string.
 * \param[out] part2 The second part of the split string.
 * \param[out] sep The separator character used in the split.
 */
void splitString(const string& input, string& part1, string& part2, char sep)
{
    // Determinate the position of the separator character
    size_t pos = input.find(sep);

    // Slice the string if the separator character is found
    if (pos != string::npos)
    {
        part1 = input.substr(0, pos);
        part2 = input.substr(pos + 1);
    }
    // Fill the string in the first part otherwise
    else
    {
        part1 = input;
        part2 = "";
    }
}

/*!
 * \brief Adds a terrain cell to the level based on a value.
 *
 * \param[in, out] level The level object where the cell will be added.
 * \param[in] value The value defining the terrain cell.
 */
void addTerrainCell(Level& level, const string& value)
{
    // Isolate values from the string
    string temp, pos1, pos2, type;
    splitString(value, type, temp, ',');
    splitString(temp, pos1, pos2, ',');
    char type_c = type[0];

    // Remove every spaces caracter
    remove_space(pos1);
    remove_space(pos2);

    // Add the cell to the terrain cases list
    Position cell_pos = {stoul(pos1), stoul(pos2)};
    Cell c = {cell_pos, type_c};
    level.terrainCases.push_back(c);
}

/*!
 * \brief Reads a position from a string.
 *
 * \param[in] StringPos The string containing the position information.
 * \return Position The position found from the string.
 */
Position readPos(const string& StringPos)
{
    // Isolate values
    string posX, posY;
    splitString(StringPos, posX, posY, ',');
    remove_space(posX);
    remove_space(posY);

    // Return the position
    Position pos = {stoul(posX), stoul(posY)};
    return pos;
}

/*!
 * \brief Removes leading and trailing spaces from a string.
 *
 * This function modifies the input string by removing any spaces
 * before the first non-space character and after the last non-space character.
 *
 * \param[in, out] str The string to be modified. The spaces at the beginning
 *                     and end of the string will be removed.
 */
void remove_space(string& str)
{
    // Remove spaces before the first non-space character
    str.erase(0, str.find_first_not_of(' '));

    // Remove spaces after the last non-space character
    str.erase(str.find_last_not_of(' ') + 1);
}

