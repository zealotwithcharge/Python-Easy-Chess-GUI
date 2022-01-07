# Python Easy Chess GUI
A Chess GUI based from Python using PySimpleGUI and Python-Chess modules. Users can also load a chess engine and play with it. This program is based on a [demo chess against ai](https://github.com/PySimpleGUI/PySimpleGUI/tree/master/Chess) from [PySimpleGUI](https://github.com/PySimpleGUI/PySimpleGUI).

![](https://i.imgur.com/DT0lOO2.png)

### A. Requirements
If you want to run from the python source the following are required or see the installation section below.
* Python 3.7 and up
* Python-chess v0.28.0 and up
* PySimpleGUI 4.4.1 and up
* Pyperclip
* Download this repo

Or you can just download the [executable file](https://github.com/fsmosca/Python-Easy-Chess-GUI/releases) along with other files such as book and images.

### B. Installation
1. If you want to run from the source code
* Python Easy Chess GUI<br>
Download the files including the Images, Engines and Book directories. You can use your favorite uci chess engine like stockfish by copying it into the engines dir.
* Python 3<br>
https://www.python.org/downloads/
* Python-Chess<br>
https://github.com/niklasf/python-chess<br>
pip install python-chess
* PySimpleGUI<br>
https://github.com/PySimpleGUI/PySimpleGUI<br>
pip install pysimplegui
* Pyperclip<br>
https://github.com/asweigart/pyperclip<br>
pip install pyperclip
2. If you want to run from the exe
* Download the exe file from the release link
### C. Features

This is an opening practice tool that lets you test yourself on different openings.
In Play Mode, the tool will show the name of the loaded opening in the top-right corner.
The tool waits until the correct move of the opening is played by the player.
If there are variations, the player can choose any of the variation moves.
The computer will choose a random variation and play the move.
When the opening line is finished, the tool will load another random opening.

Please note that most of the other features of the Python-Easy-Chess-GUI library are either disabled or should not be used.
This project is still a work in progress.


### D. How to

#### To prepare openings to practice
* Create PGN file of the opening to practice
* Add "white_" or "black_" to the front of the PGN file name. (EX. "white_london.pgn")
* Add all of the pgn files into the `/pgns` folder.
* 
#### To start the learner
* Execute learner.py [--color=white]<br>
Typical command line:<br>
`python learner.py --color white`
`python learner.py --color black`


#### To play as white
* Mode->Play
* Move the piece you want to move
* Press the square you want the piece to move to

#### To play as black
* If current mode is Neutral, Board->Flip, flip such that black pieces are at the bottom
* If current mode is Play, Mode->Neutral, then Board->Flip
* Mode->Play
* Engine->Go

#### To flip board
* If current mode is Neutral, Board->Flip
* If current mode is Play, Mode->Neutral, then Board->Flip


### E. Credits
* PySimpleGUI<br>
https://github.com/PySimpleGUI/PySimpleGUI
* Python-Chess<br>
https://github.com/niklasf/python-chess
* Pyperclip<br>
https://github.com/asweigart/pyperclip
* The Week in Chess<br>
https://theweekinchess.com/
* PyInstaller<br>
https://github.com/pyinstaller/pyinstaller
* pgn-extract<br>
https://www.cs.kent.ac.uk/people/staff/djb/pgn-extract/
