## Description:
While an input eurail system file is given, this project will find the shortest
path between any two destinations, and give an output file (.gv file) that can
draw a schematic of the entire timetable, highlighting the shortest route
between two cities in terms of least time travel.

## Dependencies:
Files I wrote:
project5.py
TripPlanner.py

## Other necessary files:
adaptable_heap_priority_queue.py
Empty.py
graph.py
heap_priority_queue.py
priority_queue_base.py
shortest_paths.py

## Requirements:
- Python 3

## Imported modules:
- argparse

## Needed Input files:
- timetable text
- optional itinerary filename (as an output file to draw
connected cities; the graph)

## Run as:
project5.py [-h] [--itinerary ITINERARY] timetable

## Operation:
In the User Interface (UI), to show the user, the stats would be printed out
like how many cities are there and how many rail routes are there
(total connections). After which, in the prompt, the user would be asked for
giving the origination and destination city for checking the path. If the
cities don't exist in the input file (such as eurail system), user would be
asked to input some other cities. While if the cities exists, the shortest
path (through some intermediary stops), and its travel time (least) would be
printed out. After which, user is asked if they want to continue looking for
other routes between another two cities. If yes, then the shortest path would
again be provided, while no would exit.

## Output:
To write an itinerary file of all the connected cities (graph) is an optional
argument, while if asked to make one, a new output file of whatever name user
gave would be written (.gv file). The format of which would be a simple
undirected, edge-weighted graph. Moreover, cities connected in the shortest
path is written in such a way that when that itinerary (.gv) file is used to
convert and draw a schematic drawing the shortest path (whole route) would be
highlighted among all other cities connections.

