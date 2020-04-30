import math
import itertools

Reference = { "Red":0, "Blue":1, "Green":2, "Yellow":3, "Purple":4, "Orange":5, "Pink":6, "Brown":7, "Violet":8}


class Location:
    def __init__(self, colour: str, x_cord: int, y_cord: int):
        self.colour = colour
        self.x = x_cord
        self.y = y_cord

    def __repr__(self):
        return "{}:<{},{}>".format(self.colour, self.x, self.y)


def Plot_Locations(Turtle, Square_Length, colour, Square):
    """
    Function to create 2x2 Grid, as well as Locations
    with names, colours, and coordinates at each cross/vertex

    """
    if Square:
        Turtle.speed(0)
        Turtle.hideturtle()
        Turtle.penup()
        Turtle.goto(-Square_Length, -Square_Length)
        Turtle.width(10)

        x, y = -Square_Length, -Square_Length

        for i in range(3):
            for j in range(3):
                colour[(i * 3) + j].append(x)
                colour[(i * 3) + j].append(y)

                Turtle.pencolor(colour[(i*3)+j][0])
                Turtle.goto(x, y)
                Turtle.dot()

                Turtle.goto(x, y + (Square_Length / 25))
                Turtle.write(colour[(i*3)+j][0], font=("Arial", 10, "normal"))

                x += Square_Length

            x = -Square_Length
            y += Square_Length
    else:
        quit()


def Input(colours):

    LocationSequence = []
    print("Which Locations would you like to visit?\nEnter (x) when finished selecting locations.\n")

    while 1:
        LocationInput = input().title()

        if LocationInput == "X":
            print("Location Selections Completed.")
            break
        elif any(LocationInput in colour for colour in colours):
            for colour in colours:
                if colour[0] == LocationInput:
                    LocationSequence.append((LocationInput, colour[1], colour[2]))
            print(LocationInput, " was Selected")
        else:
            print("Invalid Request")
    return LocationSequence


def Calculations(Locations):

    all_possible_paths = [[Locations[0]] + list(L)
                          for L in list(itertools.permutations(Locations[1:]))]

    for a, path in enumerate(all_possible_paths):
        distance = []
        for colour in range(len(path)-1):
            distances = math.sqrt((path[colour + 1].x - path[colour].x)**2 +
                                  (path[colour + 1].y - path[colour].y)**2)
            distance.append(distances)
        distance = sum(distance)

        all_possible_paths[a].insert(0, distance)

    all_possible_paths.sort(key=lambda x: x[0])

    return all_possible_paths[0][1:]


def Path(Turtle, Sequence):
    Turtle.penup()
    Turtle.goto(Sequence[0].x, Sequence[0].y)
    Turtle.showturtle()
    Turtle.width(5)
    Turtle.pencolor("grey")
    Turtle.pendown()

    for Location_ in Sequence[1:]:
        Turtle.goto(Location_.x, Location_.y)

    while True:
        Turtle.goto(Sequence[-1].x, Sequence[-1].y)
