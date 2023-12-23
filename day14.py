import re;
input1 = '''O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....'''
input2 = '''#....O#O.......O.......#O.......#...#O#.O...O...O..O#..#.O......OOO.OOO...#O.O.........OO.#..O....O.
##.#O..........OO.#.#..#...O..O.O##....O.....#....O.#....O....O.#..OOO..#..O.OO..##.#O#OO..##OO..#..
#.O.#O.O.O.......#.....##.##......#.###..###........OO...#..OO.....O....O......OOO.OOO.......OO.O#.O
O#.....#......#..##O#O.#..#O#.O.O.#...O....O.#......#....#.....O.#........O....O...O..O#...O...#O...
O#..#.OO.O#..#O##.#.#..O...OO..#..O#...#.....O.#.OO#...O.OO.O.O.....#...#.O..##...O.#.O.....O.##..O#
..OOO...#O#...O...OO.#...#OO.....#O..#.#.#OO...O.O#.......#..O..O..##..O#.O.....#O..OO#......O.O.O.O
..O.......O.....##OO#OO.#..#...O.O...O...O...#OOOO.O.O..#..O....O....OO#O.O.OOOO...#OO#.OO.O.#...#.#
#..O.......O.O...O.....#.O...O.#.....##.#...#.#.O...O...#.O.....O....#........#.O.#.#O#......O#..O.O
..#.#OO..#..OO.#..O.O.OO....OOOO...OO#..O..O...OO.O..O.O...#..#.....#.......O...O.......##O#....#.O#
.O.O#..O..O.#OO..O...#.O..O##O..##OO.OO.O.OO.O#...O...O........#.O..#......O#O#.O........OO..O......
.O#...........O..#...O.O......#O..###O....#O...OO...........#OO....O..OO..O..O.#O..O......#.O.O..#..
O..O#....OO....#.##.O#....OO.......O.......O....##.O.O....O#...#.O.O###...#....#..#...#...#OO....O##
###.O..#O..#O.#.#......##...OO...#.....OO.#O#..#...#..##O..#...O#....#O#...O..O...O...O..O.O..O..#.O
OOO.#.#..O..O#.O....#...O.OO###.#........OO.#.O#.#.....O..O..O#...O.O.O#.#O......O.#OOO#.#O.#O.O..OO
...##O#..O.#O......OO.#..OO....OOOO#...O...O.#....#..O...........OOO#.O.OO..O..O...O.#..O..OO##.O#..
.#.....#..#.....#..#OOO.O#O..O#O#..O.....OO..O##.O.OOO...#O....#O...O#...#O..O#O##....#.....O.O..O.#
OO............O....O##..OO.#..O.O.....#O...#.##O.#.O.OO#....#...O..O.#.##...........##....O.OO..O...
.##O#OO......O#...OO#...##O.O.......O....OOO..O..#.#...OOO.#..#.#..O..O#..O.....#.#.OO...O.....O##.O
O..#OOO#.O...O.......O#....O.O...O......O.......OO....##......OO#.....##...O#.............O#.....O#.
..O..##OO..O...#..OO..#...#.O.O..#..O...O.###..O.......#.O....O.##....OO.#..O.......#.O.O...O.O.####
.....O..OOO##..#.........O......O..O.#O##O#..O#O......##..O.O..#.......#.O##.#..#.#....O.OO.O.#O....
##....O..#.....#O.O...O#O#O.#.....O#.O.#..#O..O...O.#.#.....O.......#O...............#O......OO#..#.
..#O....#.......O..#O..#.OO..O...##.O.....O.#....#O..O.#O.O#O...O...O........#..OOO#..#....OO.##..O.
.#O#OO....OO.O...O..#..#O.O..#...#..#O.O....O#..OO.....O.#....#O..#....O.....#O.#......OO#O.........
.O..#.O#..O#.O..#.#.......#O......O.....O.#O...#O.#.#..OO.O..#..O............#OO#..#..O..#O..O.O.#..
..#..O.......#O##O.......O.O#O....OOO..OOO..O.#..OO..#O..O#......#.###O.O.#O.#.....#..O.##.OO.#.....
.O.#...O...O...O#..O.##O...#.OO......OOO.OO..#...#...OO#..O.#...OO#....###..O.#..#.....#....O.O.....
....O.OO..O#........#.#.#O..#.O....O...###.....O.O.#O#....O...O...##.#O#..O.#......OO.#####..#...#O.
O...#OO..##O##.......O#.O#...OOO.....O.O..#..OO......O#.##....#......O##......#OO#.#.........OOOO..#
O.O..##..O..#.#O.....#.OO.O...OO..#...O...###.....O..#....#.....#..O.O..#O.O#OO....#..OO.OO#....OO..
.OOO#..#.O.........O..O...O........OO#....#..#..##....O.....#......O....O#.O.O.OO..##...O.#....#....
....O...##O...#...OO.#O....O..O.O.O....#...O#O#..##.O.......O#.#..OO.#...#....O.....O..O#O#..#.O....
..#....O.O....#..O.OO.......O#..OO......O.O...OO.......O..#..O....OO#..O.O......#.......#...#....#.O
.....O#.........#...O.O..O.O#..O....OO..O.....O....O..#O..O.O....#...#.OO..O.#.#..O.#O...#..O..#....
#....#..##...O#OO....#..#.#O...............#.O........O..#.##............#.O#...#..##...O.....#..#.O
#.OO...O...O##...#O#..O....O.O..OO..O.OO.#OO.O..O...O#........#O.O....#.#.OO.....O....#..#O..O.#.###
......O....#...........#...#.........O.O....#..#...#..#.O#....#.O.#.O..#...O..#.......O.#..O#...#...
.#O.OO#.#...#.O.#..OO....O.......O#OO.O...........#.OO..#...##.O.#....O....##O....#..#...O#..O.O..O.
.#..##...#.O#O.O..O.......O..#...OO#......##.#O.#.O#O...##..#.O...#O.....O....O.....#......O..#.....
#O.O.O.OO.....O#..#....O.O#.O.OO.O#..O.#O.....O#.O#.O.O.........O...#...O.O..#O.#.#O#......#OO...##.
....#O....#.#.#O.O.OO.O.#..O.O...#...#...O....O........O#O.......#OO.#.........#....OO...O..O.......
.#.O#O..#.O.#...O#O.#......#.....O.O.O.#OOOO..##OOO.O.O....O..O#OO......OOO..O.##...O.O.#.....O.O#O.
##..........O...O.#...#O............#O.O......O..O#.....O......O..##.O.#O#.#......#..#....O...#..O..
..#..#..O#..#..O#O.........O##......##O.O....##.OOO#..#........O#OO..#.#.O.OO.#.OO#O.#.O..#.......##
.OO....O..OO...O.#..O....#O......##O.OOO..#.#O...#......O..#.#.....O#...OO.#...#O###...O...#........
O...O..OO..#.....OOO.#..O.##....#.O..O.OOO..#...O.#O..........#...O##....O.O..O...O...O.O.#O..O#.O#.
OO.O#O.##O.#.#..O.O.#.#..#...O..O..#...OO.OOO..O.O...OOO.#..O..O..OO.O##O#.#O...O...#...O.#O.#......
..OO.#.##.............#..#O.......O.O.#O..O.OOOO....OO..O..........#O.#..O.##.........#.....O.......
.O..O.##O#...O.#.O.#.......##.#...#....O#..O..OO............###.....#.O.O......##.#..O...........O.#
.##...#OO.O.O#.....O..O.OO##O.#..O..O...OO..#..O.O..O.O.O....O..............O#.###OO.#.#.#O#....#...
..O#...#.....O.OOO.....#O..O.#.#.....##....##O#..............O...O..#O##.#..O.....O..#...O.#O...O..O
O..OO.O....##O##O#......O..#O.O........O##O...#...O..O.....O.##..#....OO#O..O..#.....##..OO....O..O.
OO#.#OO.....O###....#O..O...#...#O..#O.#.O#.O.....O#O.O..O....O....##.....#....O.....#O...##....O.#.
#.#..#O#..O.#.#OO..##...#...#..OO.#..O....O..#...OO....OO..#..#....#....#O#.O...OO...#O..........O..
O..O.O.....O.....#.........O....O#......OO#..O..#.#.O##..#O.#..#...#..O.O......#.O..O..#.O......OO..
.#.......#..#.O.....O.#O#.#.#.....#O####.......O.#O........###..##...##..O..##...O.OO..#..O.O......#
.#.O.#.........#O.O.O...O..OO...O..O.O..O....O#..........O...O.O#.OO#..OOO.O..#O.O.O#O..O#.#..#OO..O
#.#.#...#.#.....#..#........O..#..#..###..O..O...O.O#..##.OOO.O...O.#O...O.......OOO#....#.#...O.#..
...#.O...O#O..O...#..O..O..O#.#...#..#....O.O..O...OO.#..O.OO.##O..OOOOO..#......#..OO##...OOO..O..O
.O...O..O.#O.....OO...#OO#..O#.....O..#.O.#.O#.O.##.O.OOO#OO..#..OO#OOO.O....O.....O#O.O..O..O##.O##
O.O.............O.......OOO#.....#.......#....#.O..##.#...#...OO......#..#..O.O...O.#.O.O..##O#..#..
O...#...##.O.#.##.O#.#..............O.O.#......###...OO......O.#..#.#O.......O#.#.O..O.OO#..O.....O.
OO#.....#.....#.#.#O.O#..#.#...........#...##.....#....O#...#....O#..#O.#O......O#.#.#.O..#.O##...#.
..#....O..##..#.###.OO.#......O..................##O#O....#OO#......O..O...##.##O....OO..#..#OO##.##
...#........O.#...O.##.#..#O..O......#....O##.#..OO..O#..#O......O.....#..O..#.OO.O.#..OO....O..#.#O
.O#..O......O.#OOO.....#.O...OO#.#.........#...O...O.#...##O.........#O#.O.#.#O.#..#.##.....O...OO..
.....OOOO..O.O####..#.O....#..OO......O.O.......OO#OO#O.OO..O##....#.........OO...#....O.O..O..#....
#O...#..#...O.OO#..##O...O.#......O..O##.#...#....OO..#...#..O....#.O...O##.#O#....#...#...O.O...#.O
..#.OOO.....O#......##.....#..O#O...#..#...........O#O.OO...#....#.........O....#..O.#...#..#..#.#O.
...OO.#..O...O..#.#O.##O.#..O.O.#O....O.....#..#O#.O....O.OO#.O..#..#...#...O...##.#.....O......O#O.
.###O....#......O.O..O...#...O..#......O.........O..O...##....#.#...#..........O##O...#..O..O.OO##..
..O.#O.O#...#..O#...O..#O..#.OO.....#.O.....##.O##.##...O..#...#O.O...#......#O...O...OO.#....O#..O.
...O.O...O.O.O.O#O.###..#.##O......O.O.O#..O...#.#O.O...##..##O.OOOO...#...O....O.##O#O.....#O#..O#O
....OOO#.....O..O.......#O#...........#.....#.#.#.....O..OO#.....O.OO..#...####.O.#O#.....#..#....OO
O##..OO..O#.#..O...#.....OOO......O.....O.....O#OO....O...O....O.#...#...OO...#..#....#.......O#.O.#
..#OOOOO.O#..#....##O.O#.....O.O.......O#......O#..#......#.O##.#...#O...O........O......O.O..O.....
..OO........O..O#..O.O.#..O.O#.O#...O.......##..O#......#O.O.#.#......O..#..#O.O.#.#.O#......##O.O..
.#......#..#...O..OOOO#.O#..........O.....#...OOO...O...O.#O..O..O...O..O...#.O....#O#......OO..OO..
...OO....O#O#OO...O.OOO.#...O.....#.O..O.O....#.O.#.O.#.#O.....O..#.##...OO#..#.O....#O.#.O.#O.O.#..
..#..#..O......#.#O.O...#.OO.....OOO...###.....O...O#..##.O...##O#..#.O.#.....O..#..O.O.OOOO..O...##
.#....O.O.O..O.O........O.#O..#OO#.##..O#..#.....OO#..O.#O..O..#.......O..#.....##....O..O.O#.......
....O...#OOO..##O...#OO...O...O......##......O....O..O..O....OO..#O..#....#..OO##.O.#.#.#...#.OO#...
.OO#..#...O.......O..#....OO..O#.....OO.##...##...#O......O.....#........#.##.O.....O..O..O..O.....O
.O..O#...#..O.OO...O....##.O..##...O..##O.#....O#.O....O...O.#O....#O......OO#..........O....##OO.#.
..OO..##.#.O.O....O....#O...O#......##......O.O.O#......O.#O......##.O.......O....OO#O.O..##O.O...O.
#.O....#..##........O#O.OO.#.#..OOO.#.O...#.##...#.O#....#.......#..O#O....O.O...O..O....OO.O#....O.
..#....OO..........O##.##..O..#..O.......#.........##OO....#.O...O.O##.......OO...#O#....O..##..OO..
#O.##O#....#.OOO.......O..#.O.O..O.#.OOOO#.#.#...##.O.OO......O..OO#.#...#.O##O.O........O.#...O.#..
#....O.OO#.#....O.#...O....#..O...#..O.OO..O..#..#..O#.#..OOO.O.O..#.O.#.#.......#.O#..O.##....OO...
..#.....#.O...O.O...O...O.#.#.O...OO#.#.#.....O#O.OOO.O.#......O.O.....O.#..O....O.O.OOOO#...O#.##.#
..O.O#O..OO......O......OO.#.#.....OO#...O..O......OOO..#..O...O#.##..O...#.......#.#.O....#..##.O.O
...O..#O..O#O...#..#...##.#....O.#...#.OOO.#O.......O...O....#...O...##...O..O..#..#...O#O..#...#.O.
..#..##.O#O...OO##..#..OO.#......O......O....#.#.O..O.......OO.#O.......#O...#.O.O.#....##O#O..OO...
.OO...O..O...#.OOO..OO.O...#O.......#.#.....OO..O..#.OO###.O.#O........#O.O#.O...............O.....#
....#O..#..#....O.##O.O#.O...#O..O#..#....O#.O...O....O......##...##O...#.#...#..#.O..O..#..#..O.O#O
.....#..O#...O.#.#.#......#O.O..#.#....O....##.O##O..O.#O..O.O.....#O....#..#.#..O.#O#......OOO#...O
.#..O...##.O.....##.#....#O.O.##..#.......O.....#.#..O##........#.O..........#.#O.#..#......#O#..#O.
OO.#...O...O#.......OO.OOO#.O#....#.OO...O..OO....OO#O.O#....O..O....O..O.O..O....O........O.O.#....
.O...#.......O..#OO.....#O.O...#O.#O..#.#.....#....O....#.....O..#O.#.O......O.O.OOOO.....O...#....#
.#OO.....#.#O..O........O.#O..O..#......O.O....OO.#..OO#..O#.#O.#O.O...#......O#O....#.#O...#...#.OO'''
rows = [list(row) for row in (re.split('\n', input2))]

rockCount = 0;
for row in rows:
    for col in row:
        if col == 'O':
            rockCount += 1;
print(rockCount);

minSum = 0;
for rowIndex in reversed(range(0,len(rows))):
    for colIndex in range(0,len(rows[0])):
        if not rows[rowIndex][colIndex] == '#':
            if not rows[rowIndex-1][colIndex] == '#':
                minSum += (len(rows) - rowIndex);
                rockCount -= 1;
        if rockCount == 0:
            print(minSum);
            break;
    if rockCount == 0:
        break;

minActualSum = 9999999;
for cycle in range(0,1000): #1000000000
    rowsMap = {};
    flattenedRows = [];
    for row in rows:
        flattenedRows.append("".join(row))
    flattenedGrid = "".join(flattenedRows)
    if flattenedGrid in rowsMap:
        print (rowsMap[flattenedGrid])
    else:
        rowsMap[flattenedGrid] = cycle
    # North:
    for rowIndex in range(1,len(rows)):
        row = rows[rowIndex];
        for colIndex in range(0,len(row)):
            if row[colIndex] == 'O':
                newRowIndex = rowIndex;
                for upperRowIndex in reversed(range(0,rowIndex)):
                    if(rows[upperRowIndex][colIndex] == '.'):
                        newRowIndex = upperRowIndex;
                    else:
                        break;
                if not newRowIndex == rowIndex:
                    rows[newRowIndex][colIndex] = 'O';
                    rows[rowIndex][colIndex] = '.';
    # West:
    for colIndex in range(1,len(rows[0])):
        for rowIndex in range(0,len(rows)):
            if rows[rowIndex][colIndex] == 'O':
                newColIndex = colIndex;
                for leftColIndex in reversed(range(0,colIndex)):
                    if(rows[rowIndex][leftColIndex] == '.'):
                        newColIndex = leftColIndex;
                    else:
                        break;
                if not newColIndex == colIndex:
                    rows[rowIndex][newColIndex] = 'O';
                    rows[rowIndex][colIndex] = '.';
    # South:
    for rowIndex in reversed(range(0,len(rows)-1)):
        row = rows[rowIndex];
        for colIndex in range(0,len(row)):
            if row[colIndex] == 'O':
                newRowIndex = rowIndex;
                for lowerRowIndex in range(rowIndex + 1, len(rows)):
                    if(rows[lowerRowIndex][colIndex] == '.'):
                        newRowIndex = lowerRowIndex;
                    else:
                        break;
                if not newRowIndex == rowIndex:
                    rows[newRowIndex][colIndex] = 'O';
                    rows[rowIndex][colIndex] = '.';
    # East:
    for colIndex in reversed(range(0,len(rows[0])-1)):
        for rowIndex in range(0,len(rows)):
            if rows[rowIndex][colIndex] == 'O':
                newColIndex = colIndex;
                for rightColIndex in range(colIndex+1,len(rows[0])):
                    if(rows[rowIndex][rightColIndex] == '.'):
                        newColIndex = rightColIndex;
                    else:
                        break;
                if not newColIndex == colIndex:
                    rows[rowIndex][newColIndex] = 'O';
                    rows[rowIndex][colIndex] = '.';
    sum = 0;
    for rowIndex in range(0,len(rows)):
        for spot in rows[rowIndex]:
            if spot == 'O':
                sum += (len(rows) - rowIndex);
    if sum < minActualSum:
        minActualSum = sum;
print(minActualSum);

# Part 1:
# 109665

# 101199 (001r)
# 101046 (005r)
# 101242 (010r)
# 101102 (020r)
# 100902 (030r)
# 100473 (040r)
#  99866 (050r)
#  96645 (100r)
#  96079 (200r)
#  96061 (300r)
#  96063 (400r)
#  96064 (800r)
#  96079 1600r
#  24898 -- min possible

# Guess of 96063 is TOO HIGH
# Guess of 60480 (halfway between this and min) is TOO LOW
# Guess of 78271 (halfway between previous two) is TOO LOW

# 96061 was the minimum over 1000 iterations and this happened to be correct
                
    
