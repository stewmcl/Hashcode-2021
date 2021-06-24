import os
import sys
from classes import *

points = 0

def read_file():
    #file1 = open('datasets\\a.txt', 'r')
    final_list = []
    with open('datasets\\a.txt') as f:
        lines = f.readlines()
    for item in lines:
        final_list.append(item.replace("\n", ""))
    return final_list

def get_intersects(list_structs_streets, no_intersections):
    strts = []
    for item in list_structs_streets:
        if item.end_i == i:
            strts.append(item.name)
    inter = Intersec(srts)
    return inter

def set_street(final_list, i):
    Str = Street(final_list[i])
    return Str

def set_car(final_list, i):
    list_of_streets = []
    list2 = []
    max_t = 0
    no = int(final_list[i].split(" ", 1)[0])
    list_of_streets = final_list[i].split(" ", 1)[1]
    for x in range(no):
        list2.append(list_of_streets.split(" ")[x])

    for item in list2:
        max_t += item.time
    car1 = Car(list2, max_t)
    return car1

def answer(sim_t, list_structs_cars, list_structs_streets):
    for item in list_structs_cars:
        start_street = item.streets[0]
        for x in list_structs_streets:
            if x.name == start_street:
                x.queue.append(item)
                
    for i in range(0, sim_t):
        cars_at_intersection = []
        for item in list_structs_cars:
            if item.cur_srtlen == 0:
                cars_at_intersection.append(item)
            elif item.cur_srtlen != 0:
                item.cur_srtlen -= 1



def dest_reached():
    points += 1000

def main():
    file_text = read_file()
    no_streets = file_text[0].split(" ")[2]
    no_cars = file_text[0].split(" ")[3]
    no_intersections = file_text[0].split(" ")[1]
    list_structs_streets = []
    list_structs_cars = []
    sim_t = file_text[0].split(" ")[0]
    point_amt = file_text[0].split(" ")[4]

    #Str1 = set_street(file_text)

    for i in range(int(no_streets)):
        list_structs_streets.append(set_street(file_text, (i+1)))

    for i in range(int(no_cars)):
        list_structs_cars.append(set_car(file_text, (i+int(no_streets)+1)))

    for i in range(int(no_intersections)):
        list_structs_intersects.append(set_intersect(list_structs_streets, i))

    answer(sim_t, list_structs_cars, list_structs_streets, no_intersections)

    print(list_structs_streets[1].name)
    print(list_structs_cars[1].streets)
    print("TESTING")
    for item in list_structs_streets:
        print(item.queue)


if __name__ == "__main__":
    main()
