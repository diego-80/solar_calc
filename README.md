# solar_calc
A simple sunrise/sunset calculator in Python 2.7

This program reads latitude, longitude, a date (yyyymmdd), and an optional time zone relative to UTC and prints out the corresponding sunrise and sunset times. It is structured so that reading from the command line and printing the output are entirely separate from the actual calculation, so that it can easily be repurposed to talk to other programs/methods (rather than a human).

NOTE: This program only works for days/locations with distinct sunrise and sunset times; i.e., it does not work for areas in the Arctic or Antarctic circles when those areas have one or more days of constant sunlight.
