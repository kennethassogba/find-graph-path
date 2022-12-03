# Some algorithms for solving graph path finding problems

This project comes from the python course of my master [Mathematical Engineering](https://m2ingmath.math.upmc.fr/impe/). The objective is to find the shortest path between two points of a cartesian grid, which we will represent as a graph.

The code includes :
- 3 folders (input, Tests, docs) which contain what their name says
- 2 modules (main.py, cleaning.py)
- our reports in english and french
- 1 script for visualisation (fig.py)

## main.py
This script allows the user to test our algorithm.

## cleaning.py
The Cleaning class defines the main storage point for room to clean.

## fig.py
fig.py allow us to have smooth visualisation of our graph.
#### Prerequisite
[Matplotlib](https://matplotlib.org/) : `python3 -m pip install -U matplotlib`

[NetworkX](https://networkx.github.io/) `python3 -m pip install -U networkx`
#### Get stared:
Uncomment the graph you want to draw and launch `python3 fig.py`
> We want to create animation to visualise the cleaning steps of the room but have no enough time to develop that

## python_aspir_en.pdf
Our report in English. The French version is **python_aspir_fr**.pdf

## input
The eight cases tests use as input file.

## docs
Here, we use Pycco to generate decent looking code documentation. It produce HTML pages that displays our comments alongside with code. Comments are passed through Markdown, while code is passed through Pygments for syntax highlighting.
> To improve: comments presentation

## Tests
### Test_AspiR
python3 -m unittest Tests/Test_AspiR.py
> Ran 8 tests in 164.246s OK
### Test_Robot.py
python3 -m unittest Tests/Test_Robot.py
> Ran 2 tests in 0.001s OK
### Test_Room.py
python3 -m unittest Tests/Test_Room.py
> Ran 1 test in 0.000s OK


> Kenneth Assogba & Alexis Squarcioni.

> March 2020
