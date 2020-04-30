DistanceChild = [[[1.0, 'Red', 'Blue'], [2.0, 'Red', 'Green'], [2.236, 'Red', 'Orange'], [2.828, 'Red', 'Violet']],
                 [[1.0, 'Orange', 'Green'], [1.0, 'Orange', 'Violet'], [1.414, 'Orange', 'Blue'], [2.236, 'Orange', 'Red']],
                 [[1.0, 'Blue', 'Green'], [1.0, 'Blue', 'Red'], [1.41, 'Blue', 'Orange'], [2.236, 'Blue', 'Violet']],
                 [[1.0, 'Green', 'Blue'], [1.0, 'Green', 'Orange'], [2.0, 'Green', 'Red'], [2.0, 'Green', 'Violet']],
                 [[1.0, 'Violet', 'Orange'], [2.0, 'Violet', 'Green'], [2.23, 'Violet', 'Blue'], [2.828, 'Violet', 'Red']]]
DistanceParent = []

def t1():
    Visited = [DistanceChild[0][0][1]]

    CurrentLocation = 0
    Destination = 0
    Loc_Des = DistanceChild[CurrentLocation][Destination]

    i = 0
    while len(DistanceParent) < (len(DistanceChild) - 1):

        DistanceParent.append(Loc_Des)
        for a, Groups in enumerate(DistanceChild):
            if DistanceParent[i][2] == Groups[0][1]:
                CurrentLocation = a
                Visited.append(DistanceChild[CurrentLocation][0][1])
                print(Visited)

        Destination = 0
        while True:
            if DistanceChild[CurrentLocation][Destination][2] not in Visited:
                Loc_Des = DistanceChild[CurrentLocation][Destination]
                break
            Destination += 1
            if Destination == (len(DistanceChild) - 1):
                break

        i += 1




t1()



def z():
    """
    Uses first option, deletes entire colour group.
    """
    DistanceParent.append(DistanceChild[0][0])
    Visited = [DistanceChild[0][0][1]]
    i = 0

    for a, colourGroups in enumerate(DistanceChild):
        for b, options in enumerate(colourGroups):
            for c, destinations in enumerate(options):
                if DistanceParent[i][2] == destinations and c == 1 and DistanceParent[i][1] != DistanceChild[a][b][2]\
                        and DistanceChild[a][b][2] not in Visited:
                    DistanceParent.append(DistanceChild[a][b])
                    i += 1
                    Visited.append(DistanceParent[i][1])
    print(Visited)
    print(DistanceParent)
    return DistanceParent

    """
        for i in range(len(DistanceChild)):
            xx = [x for x in range(i + 1)]
            for j in [x for x in range(len(LocationSequence) - 1) if x != xx]:
                for x in range(len(LocationSequence) - 1):
                    if DistanceChild[i][0][1] == DistanceChild[j][x][2]:
                        del DistanceChild[j][x]
                        break

        #######
        DistanceParent[0] = DistanceChild[0][0]

        for i in range(len(DistanceChild)):
            for j in range(len(DistanceChild) - 1):
                if DistanceChild[i][j][1] == DistanceChild[i][j][2]:
                    DistanceChild[0][j].remove()

        print(DistanceParent)
        """