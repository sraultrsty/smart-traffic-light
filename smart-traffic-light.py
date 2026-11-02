# PYTHON PROGRAM <Smart Traffic Light>
# an Automated Traffic Controller for a standard 4-way intersection (North, South, East, West)

# DECLARATIONS
# phases    : array of strings
# cross     : integer

#ALGORITHM
import time

phases = ["South <-> North: ",  #1
          "West <-> East: ",    #2
          "East -> North: ",    #3
          "South -> East: ",    #4
          "West -> South: ",    #5
          "North -> West: "]    #6

# Traffic light function
def light_order():
    print("(A red light for the roads are not mentioned)")
    #Green light
    print("\033[32mGreen light (10s)\033[33m")
    time.sleep(10)

    #Yellow light
    print("\033[33mYellow light (5s)\033[31m")
    time.sleep(5)

    #Red light
    print("\033[31mRed Light\033[0m")

# Pedestrian cross light function
def cross_light():
    cross = int(input("Is there anyone who wants to cross (1=yes, 0=no)? "))
    if cross == 1:
        # 5s warning buffer
        print("\033[33mYellow light\033[0m for road, \033[31mRed light\033[0m for Pedestrian (5s buffer)")
        time.sleep(5)

        print("\033[31mRed light\033[0m for road, \033[32mGreen light\033[0m for Pedestrian (10s)")
        time.sleep(10)

        print("\033[32mGreen light\033[0m for road, \033[31mRed light\033[0m for Pedestrian")
        time.sleep(1.5)

# Road order
while True:
    for direction in phases:
         print(f"\n{direction}")
         cross_light()
         light_order()