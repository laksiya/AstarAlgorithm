# Sample code from https://www.redblobgames.com/pathfinding/a-star/
# Copyright 2014 Red Blob Games <redblobgames@gmail.com>
#
# Feel free to use this code in your own projects, including commercial projects
# License: Apache v2.0 <http://www.apache.org/licenses/LICENSE-2.0.html>

import collections

#TOOLS FOR DRAWING GRID
#draw_graph uses draw_tile draws correct tile based on graph, id, width
#and other given info about style(cost, came_from, path, start, goal
#wall)

def draw_tile(graph, id, style, width):
    r = "."
    if 'number' in style and id in style['number']: r = "%d" % style['number'][id]
    if 'point_to' in style and style['point_to'].get(id, None) is not None:
        (x1, y1) = id
        (x2, y2) = style['point_to'][id]
        if x2 == x1 + 1: r = ">"
        if x2 == x1 - 1: r = "<"
        if y2 == y1 + 1: r = "v"
        if y2 == y1 - 1: r = "^"
    if 'weight' in style and id in style['weight']:
        r = "%s" % style['weight'][id]
    if 'start' in style and id == style['start']: r = "A"
    if 'goal' in style and id == style['goal']: r = "B"
    if 'path' in style and id in style['path']: r = "@"
    if id in graph.walls: r = "#" * width
    return r

def draw_grid(graph, width=2, **style):
    for y in range(graph.height):
        for x in range(graph.width):
            print("%%-%ds" % width % draw_tile(graph, (x, y), style, width), end="")
        print()

#Finds the most efficient path from goal to start, returns list
def find_path(graph, came_from, goal, start):
    path=[]
    next=goal
    print(" start:",start)
    print(" goal: ",next)
    print(path)
    print(came_from[next])
    cnt = 0
    while not came_from[next]==start:
        cnt+=1
        path.append(came_from[next])
        next = came_from[next]
    print("count:",cnt)
    return path

#Defining the grid
class SquareGrid:
    def __init__(self):
        self.width = 0
        self.height = 0
        self.start=None
        self.goal= None
        self.walls = []


    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, id):
        return id not in self.walls

    def neighbors(self, id):
        (x, y) = id
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        if (x + y) % 2 == 0: results.reverse() # aesthetics
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results

    def cost(current, next):
        return 1

#Loads board from text file
    def read_board(self, fileName):
        x = 0
        y = -1
        print("x=", x)
        print("y=", y)

        with open(fileName, 'r') as f:
            for line in f:
                print("current line: ", line)
                print("length of line:", len(line))
                if len(line)>= self.width-1:
                    print("Line is valid")
                    y += 1
                    for j in line.rstrip():
                        print("Now processing", j, "in location x,y= ", x, ",", y)
                        if j == '#' in line:
                            self.walls.append((x, y))
                            print("-Added to wall")
                        if j == 'A' in line:
                            self.start = (x, y)
                            print("-Added as start")
                        if j == 'B' in line:
                            self.goal = (x, y)
                            print("-Added as goal")

                        x += 1
                    x=0
        self.height = y+1
        return self


#Defining a subclass of SquareGrid
#that includes different cell cost
class GridWithWeights(SquareGrid):
    def __init__(self):
        super().__init__()
        self.weights = {'s': 1, 'g': 1, 'r': 1, 'g': 5, 'f': 10, 'm': 50, 'w':100}
        self.type = {}

    def cost(self, from_node, to_node):
        return self.weights.get(self.type[to_node], 1)
    def read_board(self, fileName):
        x = 0
        y = -1
        print("x=", x)
        print("y=", y)

        with open(fileName, 'r') as fh:
            lines = fh.read().splitlines()
            for line in lines:
                print(line)
            self.width = len(lines[0])
            print("self.width=", self.width)


        with open(fileName, 'r') as f:
            for line in f:
                print("current line: ", line)
                print("length of line:", len(line))
                if len(line)>= self.width-1:
                    print("Line is valid")
                    y += 1
                    for j in line.rstrip():
                        print("Now processing", j, "in location x,y= ", x, ",", y)
                        if j == '#' in line:
                            self.walls.append((x, y))
                            print("-Added to wall")
                        if j == 'A' in line:
                            self.start = (x, y)
                            self.type[(x, y)] = 's'
                            print("-Added as start")
                        if j == 'B' in line:
                            self.goal = (x, y)
                            self.type[(x, y)] = 'g'
                            print("-Added as goal")
                        if j == 'f' in line:
                            self.type[(x,y)] = 'f'
                            print("-Added as a f cell")
                        if j == 'g' in line:
                            self.type[(x,y)] = 'g'
                            print("-Added as a g cell")
                        if j == 'r' in line:
                            self.type[(x,y)] = 'r'
                            print("-Added as a r cell")
                        if j == 'm' in line:
                            self.type[(x,y)] = 'm'
                            print("-Added as a m cell")
                        if j == 'w' in line:
                            self.type[(x,y)] = 'w'
                            print("-Added as a w cell")

                        x += 1

                    x=0
        self.height = y+1
        return self

import heapq

#PriorityQueue priorities the cells
#with input from cost_so_far and heurestic
class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


#heuristic calculates the Manhattan
#distance between a and b
def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

#a_star_search takes a graph, start and goal
#and return came_from and cost_so_far
def a_star_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    print()
    while not frontier.empty():
        current = frontier.get()

        print()
        if current == goal:
            break

        for next in graph.neighbors(current):
            cnt=0
            print("CURRENT frontier: ", current)
            print("NEXT: ",next)
            print(" cost_so_far[current]= ", cost_so_far[current])
            print(" graph.cost(current, next)= ", graph.cost(current, next))
            new_cost = cost_so_far[current] + graph.cost(current, next)
            print(" new_cost= ", new_cost)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cnt += 1
                print("IN LOOP ",cnt)
                cost_so_far[next] = new_cost
                print(" cost_so_far[next]=", cost_so_far[next])
                priority = new_cost + heuristic(goal, next)
                print(" heuristic(goal, next)", heuristic(goal, next))
                print(" priority=", priority)
                frontier.put(next, priority)
                came_from[next] = current
                print()

    return came_from, cost_so_far


g = GridWithWeights()
g.read_board("board-2-1.txt")
print("boardstart:", g.start)
print("boardgoal", g.goal)
print("width:", g.width)
print("height:", g.height)
print("boardwalls:")
for x in range(len(g.walls)):
    print(g.walls[x])

print("goal= ", g.goal)
came_from, cost_so_far = a_star_search(g, start=g.start, goal=g.goal)

print("came_from:",came_from)
found_path=find_path(g, came_from,  goal=g.goal, start=g.start)


print(found_path)

draw_grid(g, width=3, point_to=came_from, start=g.start, goal=g.goal)
print()
draw_grid(g, width=3, start=g.start, goal=g.goal, path=found_path,weight= g.type)
print()

