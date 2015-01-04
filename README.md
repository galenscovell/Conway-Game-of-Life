Conway-Game-of-Life
===================

Cellular Automata simulation implementation using Python and pyGame.

Description:
<blockquote>The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970.</blockquote>

<blockquote>The "game" is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves or, for advanced players, by creating patterns with particular properties.</blockquote>

Requirements:
* Python 3.4
* PyGame 1.9.2a0

Usage: 
<blockquote><b>python base.py</b> [ -h ] [ -t ] [ -fps ] </blockquote>

+ Press [ spacebar ] at any time to create a new, blank grid.
+ Use the [ mouse and click ] on any open grid space to place a 'bit'.
+ Press [ enter ] to begin simulation for given amount of 'ticks'.

Arguments:
*  -h, --help 
<blockquote> Show this help message and exit </blockquote>
*  -t, --num_ticks 
<blockquote> Runtime length once simulation is begun. (Default: 1000) </blockquote>
* -fps, --framerate 
<blockquote> Framerate (Default: 10) </blockquote>

