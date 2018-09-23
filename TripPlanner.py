# TripPlanner.py
# Rutu Patel
# rpatel53@stu.parkland.edu
# CSC 220, Spring 2017

from graph import Graph
from shortest_paths import *

class TripPlanner:
    def __init__(self, timetable, itinerary=None):
        self.__myGraph = Graph()
        self.__cities = dict()
        self.__shortestPath = list()
        self.__timetable = timetable
        self.__listOfEdges = list()
        self.__itinerary = itinerary

    def load_data(self):
        print("File loading...")
        with open(self.__timetable, 'r') as infile:
            lines = infile.readlines()
            for line in lines:
                source, destination, time = line.split(',')
                hour, minutes = time.split(':')
                minutes = int(minutes) + 60 * int(hour)
                if source not in self.__cities:
                    sourceVertex = self.__myGraph.insert_vertex(source)
                    self.__cities[source] = sourceVertex
                if destination not in self.__cities:
                    destinationVertex = self.__myGraph.insert_vertex(
                        destination)
                    self.__cities[destination] = destinationVertex
                self.__myGraph.insert_edge(self.__cities[source],
                                           self.__cities[destination], minutes)
            print("There are", len(self.__cities), "cities with",
                  self.__myGraph.edge_count(), "connections.")

    def User_Interface(self):
        while True:
            origination = input("Please enter the origination: ")
            destination = input("Please enter the destination: ")
            origination = origination.strip().capitalize()
            destination = destination.strip().capitalize()

            if origination not in self.__cities:
                print(origination + " not in the eurail system.")

            elif destination not in self.__cities:
                print(destination + " not in the eurail system.")

            else:
                originationVertex = self.__cities[origination]
                destinationVertex = self.__cities[destination]
                cloud = shortest_path_lengths(self.__myGraph, originationVertex)

                if cloud[destinationVertex] != float('inf'):
                    path = shortest_path_tree(self.__myGraph, originationVertex,
                                              cloud)
                    currentVertex = destinationVertex
                    self.__shortestPath = [currentVertex.element()]
                    travelTime = cloud[destinationVertex]

                    while True:
                        currentEdge = path[currentVertex]
                        currentVertex = currentEdge.opposite(currentVertex)
                        self.__shortestPath.append(currentVertex.element())
                        self.__listOfEdges.append(currentEdge)

                        if currentVertex is originationVertex:
                            self.__shortestPath.reverse()
                            print("...")
                            print("The shortest travel time is by going through"
                                  " these intermediary stops:")
                            for city in self.__shortestPath:
                                print(city)
                            print("The whole journey takes", travelTime // 60,
                                  "hours","and", travelTime % 60, "minutes.")
                            break
                else:
                    print("There is no path between " + origination + " and "
                          + destination)

                if not input(
                        "Do you want to continue and look for another "
                        "route?").startswith('y'):
                    if self.__itinerary is not None:
                        self.writeFile()
                    break

    def writeFile(self):
        with open(self.__itinerary + ".gv", 'w') as outfile:
            outfile.write("graph {")
            for edge in self.__myGraph.edges():
                endpoints = edge.endpoints()
                outfile.write(endpoints[0].element() + " -- " +
                              endpoints[1].element())
                hr, min = edge.element() // 60, edge.element() % 60
                outfile.write('[label="' + str(hr) + ":" + str(min) + '"')
                if edge in self.__listOfEdges:
                    outfile.write(", style = bold , color = red")
                outfile.write("]")
                outfile.write("\n")
            outfile.write("}")

if __name__ == '__main__':
    print('TripPlanner class file does not contain tests.')
    print("This module is not made to run directly.")