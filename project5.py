# project5.py
# Rutu Patel
# rpatel53@stu.parkland.edu
# CSC 220, Spring 2017

import argparse
from TripPlanner import TripPlanner

if __name__ == '__main__':
    # First create the parser object.
    # description will be printed when some calls the program
    # with the -h or --help args.
    parser = argparse.ArgumentParser(description='Project 5 Driver file.')

    # Add a required input timetable file name.
    parser.add_argument('timetable',
                        help='The name of the eurail timetable file.')

    # Add an optional itinerary argument.
    parser.add_argument('--itinerary',dest= 'itinerary' ,
                        help='The name of the optional itinerary .gv file.')

    args = parser.parse_args()
    if args.itinerary:
        myTrip = TripPlanner(args.timetable, args.itinerary)
    else:
        myTrip = TripPlanner(args.timetable)

    myTrip.load_data()
    myTrip.User_Interface()

