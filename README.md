[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/_G_SdF8U)
# python-refresher

## Quick Start
Within the file directory, prompt
'''
./run.sh
'''
First displays the quantity of CO2 released by fires within the United States! Then purposely tries to retrieve a file that does not exist. Then purposely tries to turn strings into integers to demonstrate the programs ability to catch errors with custom messages.

## run.sh
run.sh runs print_fires.py to retrieve information about the CO2 released from fires in the United States year by year. Then purposely tries to retrieve a file that does not exist. Then purposely tries to turn strings into integers to demonstrate the programs ability to catch errors with custom messages.

## my_utils.py
my_utils.py is modified such that the get_column() function is properly implemented, such that a file may be opened, a column is read for a specific value, and another piece of information may be returned for all values registered. Can also return the mean, median, or standard deviation of requested data.

## print_fires.py
print_fires.py runs the aforementioned get_column() function from my_utils.py so that custom inputs may be queried and ran. It will also run custom errors depending on the error caught.

## Continuous Integration/Testing
Continuous integration and testing now implemented. PLEASE NOTE, pycodestyle WILL THROW A FIT. Because my code hygiene is horrifying. It just does that. The other tests are more important. It's super strict, alright? I can understand it just fine and I'm sure you can too. M'kay?