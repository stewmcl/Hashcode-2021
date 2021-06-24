import sys

class Street():
    def __init__(self,vars):
        self.start_i = vars.split(" ")[0]
        self.end_i = vars.split(" ")[1]
        self.name = vars.split(" ")[2]
        self.time = vars.split(" ")[3]
        self.queue = []

class Car:
    def __init__(self,strs, maxt):
        self.streets = strs
        self.max_t = maxt
        self.cur_srtlen = 0
        self.inters = len(strs) - 1

class Intersec:
    def __init__(self):
        self.strs_in = []
