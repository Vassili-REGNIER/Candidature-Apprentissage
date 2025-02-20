/*!
 * \file   main.cpp
 * \author Regnier Vassili
 * \version 1.0
 * \date   8 January 2025
 * \brief  Main point of the game project.
 *         Starts the game.
 */

#include <iostream>
#include "code/headers/game.h"

using namespace std;

/*!
 * \brief Main function of the game.
 *
 * Try to launch the game. In case of an exception, an error message is
 * displayed, and the program returns 1. If the parameters file cannot be loaded, it returns 2.
 *
 * \return Returns 0 if everything is OK, 1 if an exception occurs.
 */
int main()
{
    try
    {
        return game ();
    }
    catch (...)
    {
        cerr << "Something went wrong :(" << endl;
        return 1;
    }
}
