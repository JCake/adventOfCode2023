import re;
input1 = '''...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....'''
input2 = '''...#...............................................#............................#........#.............................................#....
.................................#............#...........................#.........................#....................#..................
.......................#........................................#...........................................................................
..........#...........................................................................#.....................................................
...................#.........#............#.....................................................#...........................................
...........................................................................................................#......#.............#...........
.......#......#..........#..................................................................................................................
..........................................................#............#....................................................................
.#...............................................#...........................#......................#..................................#....
..............................................................#.....................#................................#.....#................
.......................#.......#.....#...................................................................#.................................#
..................#.........................................................................................................................
.............#........................................#.............#.............................#...........................#.............
............................................................................................#.......................................#.......
............................#..................................................#.................................#..........................
.........#...........#...............................................................................#......................................
................................#......#..........#......................................................................#..................
...........................................................................................................#................................
.................#....................................................................#...........#.......................................#.
..........................................................................#.....#.....................................#.....................
..............................................................#.............................................................................
....................................................................#..................................#.............................#......
..#..........................................#..............................................................................................
........................................................................................#..................#......#.........................
.........#.......#......#..........................#.........................................#..............................................
...........................................................................#........................#.......................................
.....#......................................................#.....................#...................................................#.....
..............................#...........#...........#...........#.........................................................................
#................................................#......................#.................................#.................................
........#..........................................................................................................#........................
..............#...........#..........#...................#..................................................................................
....................#..........................................................................#............................................
.........................................................................................#..............#....................#......#.......
...#......................................#..................#..............................................................................
..................................#................................#........................................#............#..................
.......................#............................................................#...........................................#.........#.
...............................................................................#................#...........................................
...............................#............................................................................................................
................#.......................#.................................................#.................................................
.........#..................................................#..........#.............................................................#......
.....................#.............................#........................................................................................
...............................................................................................#.......#.....................#..............
..................................#................................................................................#....................#...
.#.....#.....#.............................#....................................#.....#.....................#...............................
......................................#....................................#.....................................................#..........
.........................#..................................................................................................................
...................................................#........................................................................................
..............................#..............................................................#......#..................#....................
....................#...................#..........................#..........#...........................#....................#............
......................................................................................#.....................................................
..#.....#...........................#.....................#.................................................................................
............................................................................................................................................
............................................................................................................................................
................#.......................................................................................#...............................#...
.......................#.....................................................#.......#......................................................
............................................................................................................................................
.....#......................#.....#...........#................................................#..................#.........................
................................................................................#............................#..............................
.......................................................................#........................................................#...........
..........#...........................................#...............................#................................................#....
.......................................#...................................#.........................#...................#..................
....................#............................#.........#......#...........................#....................................#........
............................................................................................................................................
..#.....................................................................................#......................#............................
................................#........................................#....................................................#.............
............#..............................................................................................................................#
...............................................................#.......................................#...........#........................
......#...............#....................#........................#........#...............................#..............................
.............................#...............................................................#..............................................
............................................................................................................................................
.........................................................................................................#..................................
..#.............................#.......................#.............................#...........................................#.........
..............#..................................#..............................................#.............#..............#..............
..........................................................................#...........................................#.....................
..................#........................................#................................#.........................................#.....
............................#.......................................................................#.......................................
........................................#..........#...........#............................................................................
...........#................................................................................................................................
.........................#........................................................#..........................................#..............
................................................................................................#......#............#................#......
#.....................................#.....#..........................#....................................................................
.....#.......#.................#.....................#......................................#...................................#...........
............................................................................................................................................
.........#..........................................................#................#...............#......#............#.................#
............................#...............................#..................#......................................................#.....
................................................................................................#............................#..............
#......................#..........#.........................................................................................................
..................#................................#...............................#....................#.......#...........................
.......#..............................#.....#.............................................................................#.................
............#.......................................................#........#..................................................#...........
..............................................................................................#....................#......................#.
............................#...........................................................#..................#................................
#............................................................................................................................#..............
......#................#............#.................#..............................................#.............................#........
................#.............................................................#......#......................................................
................................#..............#..............#.........#...................................................................
.......................................#...............................................................................#................#...
...........#.............................................#..............................#...................................................
....................................................#.......................................................................#...............
.....#.................#..........................................#...........................................#.............................
#..............................#..................................................................#.........................................
...........................................#.............................................................#..........................#.......
.................................................#........#....................#............................................................
.............#..........................................................................#..........................#...........#............
............................................................................................................................................
..................#..............................................#.................................#.....................#..................
...................................................#....................#......................................#.......................#....
........................#.....................#.............................................................................................
...#...........................................................................#.....#.....#........................#..............#........
.............................................................#..............................................................................
..........#..................#.......................#.........................................#........#...................................
...........................................................................#..................................................#.............
.......................#.........#.........#..........................................................................#.....................
...............................................................................................................#............................
...#............#........................................#.....................#.............#........#.....................................
........................................................................................#..............................................#....
..........#..............#.....#.....................................#.............#........................................................
............................................................................................................................................
...................................................#........#...............#..............#...............#...........#....................
.....................#......................................................................................................................
.......................................#...............................................................#..........#.........................
.....#...........#..................................................................................................................#.......
.....................................................................................#......................................#...............
.............#..............................................................................................................................
........................................................................#.......#..............#................................#...........
.....................#..........#.......................#...................................................................................
.....................................................................................................................#...............#......
...........#...............#.............#..................................................#.......#......................#...............#
.................................................................#........#...............................#.................................
#............................................#..............................................................................................
......................................................................................#.....................................................
.........................................................#.....................................#..................................#.........
...................................................................#..............#...........................#........#....................
......#..........................................#..................................................#.......................................
..........................................................................................................#.................................
....................#..............#..........................#................................................................#............
...............................................................................#........#...........................................#.......
..........................................#......................................................#..........................................
........................#........................................#......#..........................................#........................
...........#.....................#...............#.......#.................................................#...............#...........#....''';
strGrid = input2;
rows = re.split("\n+", strGrid);
nonExpandedGrid = [list(row) for row in re.split("\n+", strGrid)];
print(nonExpandedGrid);
expandedRows = [];
allDots = re.compile("^\\.+$");
rowsToExpand = [];
for rowI in range(0,len(rows)):
    row = rows[rowI];
    if allDots.match(row):
        rowsToExpand.append(rowI);
colsToExpand = [];
for colI in range(0,len(rows[0])):
    col = ''.join(row[colI] for row in rows);
    if allDots.match(col):
        colsToExpand.append(colI);
galaxyCoords = [];
for rowI in range(0,len(nonExpandedGrid)):
    for colI in range(0,len(nonExpandedGrid[0])):
        if nonExpandedGrid[rowI][colI] == '#':
            galaxyCoords.append([rowI,colI])
print(galaxyCoords);

shortestPathSum = 0;
for galaxyIndex, galaxy in enumerate(galaxyCoords):
    for otherGalaxyIndex in range(galaxyIndex + 1, len(galaxyCoords)):
        otherGalaxy = galaxyCoords[otherGalaxyIndex];
        shortestPathSum += (abs(galaxy[0] - otherGalaxy[0])) + (abs(galaxy[1] - otherGalaxy[1]));
        for rowIndex in range(min(galaxy[0],otherGalaxy[0]), max(galaxy[0],otherGalaxy[0])):
            if rowIndex in rowsToExpand:
                shortestPathSum += (1000000-1); # part 1 is simply + 1
        for colIndex in range(min(galaxy[1],otherGalaxy[1]), max(galaxy[1],otherGalaxy[1])):
            if colIndex in colsToExpand:
                shortestPathSum += (1000000-1); # part 1 is simply + 1
print(shortestPathSum);
        
        
    
