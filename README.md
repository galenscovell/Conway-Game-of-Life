<img src='http://galenscovell.github.io/css/pics/cgol.png' width=500px />

Conway's Game of Life
===================

Cellular automata simulation implemented with Python.

<b>Description:</b>
<blockquote>The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970.</blockquote>

<blockquote>The 'game' is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves or, for advanced players, by creating patterns with particular properties.</blockquote>

<b>Requirements:</b>
* Python 3.4
* PyGame 1.9.2a0
  <blockquote>Use the unofficial pygame build for Python 3.4 from here: http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame</blockquote>

<b>Installing Unofficial pygame for Python 3.4:</b>
* Save .whl file from above to somewhere you'll remember
* Open a terminal
* <blockquote>pip install wheel</blockquote>
* Navigate to the previous directory with .whl file
* <blockquote>pip install package_name.whl</blockquote>

<b>Usage:</b>
<blockquote><b>python base.py</b> [ -h ] [ -t ] [ -fps ] </blockquote>

+ Press [Spacebar] at any time to create a new, blank canvas.
+ Use the mouse and [Left-Click] on any open grid space to place a 'bit'.
+ If clicked space is occupied, the bit will be erased.
+ Press [Enter] to begin simulation for given amount of 'ticks'.

Arguments:
*  -h, --help 
<blockquote> Show this help message and exit </blockquote>
*  -t, --num_ticks 
<blockquote> Runtime length once simulation is begun. (Default: 1000) </blockquote>
* -fps, --framerate 
<blockquote> Framerate (Default: 10) </blockquote>

