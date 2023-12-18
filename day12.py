import re;
input1 = '''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1'''
input2 = '''???.??????? 1,4
?????...#?? 5,1
????#.???? 2,2,2
????.??#?.?.????# 3,4,1,1
#??.#.??????##? 1,1,7
??###?##.??????#??#. 8,1,2,2
.?##????.#??? 3,4
.?#.#?#???.?#?? 2,1,2,1,3
??..????#. 2,2
?#??#??.???##??. 5,5
?#?#??????#?? 4,1,1
??.??????# 1,6
##??.??????# 2,1,3,2
????????##?.#????.? 9,5
.???#?#?###??#..??? 13,2
??...????##??? 1,6
??????#.???#????. 1,1,2,4,1
#.#??.??.#??#.?? 1,2,2,4,2
?.??.?????????# 2,2,3,1
??.?..#.??????? 1,1,1,1,3
?#?#?#??#????#? 2,1,4,1,2
??#?..#..# 2,1,1
?#?#?#????????? 5,7
???.????#?? 1,3
.??????#?#.#. 1,1,5,1
??#?????.??????..?? 7,1,3,1
??#??#?.???#?? 5,1
?#??????????#?# 1,4,7
?.?#?.????? 3,1,2
??#.?#.??#?. 1,1,1,2
???.?##.?? 2,3,1
?#...??????.??.?.# 2,2,2,1,1,1
.?#??#???##????#?#.. 11,3
#?#?.??.??????????? 1,1,1,9
?.?.?#?.??#??? 1,1,2,2
??..?????#????? 1,6,2
?.??.??.?????#? 1,7
?#.?.????#???.?# 2,1,2,1,1
???.????..??#? 2,3,2
???#???#?? 4,2
.##.?#??#?#??#? 2,4,1,3
..?#??#?.??. 5,2
???.??.??#???#?#?? 2,2,1,3,3
.#??##???#.????#..?? 1,3,1,1,3,1
?????.#?.#???? 2,2,1,1
.?#.?????#?? 1,6
.??#?.???#??.?? 2,1
?#????##??.???? 2,1,4,2
?#????.???..?.?????. 1,3,1,3
#.?.????.?..??. 1,1,2,1,2
.??#.??#?#?? 1,5
##????##???##??? 2,1,2,4
???#??..#??#??#. 5,7
..?.?.????? 1,1,1
..#????.?#?? 1,1,1,3
?#????.?###?????? 2,2,4,2,1
??#.?.?#.#?##?###? 2,1,8
??.#??.??.???? 1,3,4
#???#???#??. 5,2
?.#?.??????? 2,1
.????#??????#?#??? 1,5,1,1,1,1
?#??.?#??#????.?#? 1,1,8,1
#..???..?#????###.? 1,2,9
????#?#???? 4,5
?????###??#???#?. 4,7
???.#??#?? 1,1,4
????#?????# 1,7
?????????#???#?#.?? 2,1,5,1,2
?????????.??.? 2,3,2
????.??... 1,1,1
?????..????.????. 1,3
???.??????????.#.? 1,10,1,1
?#.????????#????#? 1,10,1
.??????.?#??#.#? 6,1,1,2
???.?????? 1,3,1
?.#???????.??? 1,5,1
.????#?#?##??? 1,8
????#????#.?? 1,1,3
#????.????#?#??? 1,1,2,4,1
????#?.??#???.? 3,5
.??#???.?????? 4,1
#??#?..?..?.?.? 1,3,1,1,1
?..????#??????##?.. 5,4
?##??????##?#??#? 4,9,1
??#?.#??#??????? 3,2,3,2
???.#??#???#????#. 1,2,2,1,1,1
???????#?#??#.? 3,6
??.????#?#?.??? 2,7,1,1
.??##.??????? 3,2,2
?.???.??#? 1,1,1
#??##?#?.?#????? 1,3,2,2,1
??#????#???? 1,4
??..?.#??.??????#? 1,1,1,1,2,4
.???????#.????#?? 1,2,1,1,3
??????#??.?# 6,1
????#?????#???????? 4,1,2,1,3
##????????? 2,2,2
.?##?.???? 3,1
????#??.?????#?? 5,3
????????#???? 1,1,8
???#.????????#? 2,7
????????##.? 2,2
?#..?.?????#???? 1,1,3,3,1
?????????###??. 2,1,7
?????##???##?#?#?? 1,4,8
??????????#? 1,1,1,1
.?????#??? 1,1,1
.?????????? 2,1,2
.???..#????.?? 3,1,1,1
?#????#??????? 1,5,2,1
??????????##?? 4,2,5
#.???????????? 1,7,3
??#??#??.?#????# 5,6
.?#????.#?????????# 3,2,3,2
.#..??#?#????..?? 1,9,2
??.???#??#?.?? 4,2
??##??????#?.?# 4,2,2,2
.???????.?#?#???#? 2,2,2,1,3
.??#?#?#??#?.????#? 10,5
.#??#???#??##?. 5,5
??#?#???.? 2,3
..??#??????##??#??? 3,8,1
?.??.#.???##.##???# 1,2,1,4,4,1
.#?.???????#. 2,4
.????##???????? 1,5,1
????...#??.?. 1,1,2,1
??????#?#????? 1,8
?#.?.?.#???### 1,1,1,7
#?#?.??#?#??##?? 1,1,1,9
.?.#??#???.?..##? 6,2
???????????# 1,3,3
???##?.##???.?.? 5,3,1,1,1
??.???##.?##???? 1,2,2,2,1
??.#???????????.# 1,1,1,6,1
..?##?##??????#? 7,5
?#???????? 1,1,1
?#?.?#???? 1,4
??#?????#?#?.#?? 8,1,3
?.???.?#?###? 1,1,1,3
?#?#????##????????? 3,5,2
##?????#?##?????.?? 3,7,2,1
????#.#???# 1,1,5
.????#???????? 1,3,4
?#?#.?#?#? 2,1,4
?.?.?#??#?#? 1,2,3
?#?##??#?##??????? 12,2
.??#.????#? 1,1,3
#????.?###????? 2,1,8
?#?.?????? 1,1,1
???#????#? 3,1,3
???#??..?#??.?.??? 6,4,2
#???????#?.??#????? 5,1,2,3,2
.#??#??##???? 4,4,1
.?????????? 4,2,2
?.?#?????????.??? 1,9,1,1
?#?.##?##??##?# 1,11
???##???????????? 5,2,2,4
????????????##???. 2,2,6,1
.#??###???. 6,1
?.?#.??##????? 1,1,3,1
#??.??.?????????. 1,1,1,1,6
.???#?#????? 1,4
?.#..#?..?# 1,2,1
????????#????.?? 1,3,2,2,1
?#?#???.???.#??? 6,3,2
.????.??#?#?..?? 3,5
#???#??#?#??#??. 5,1,1,1,1
???.?.??#??????#?? 1,1,1,3,7
?????#?#??.#??. 6,3
?#?##???#???????? 10,2
?????#????#?##??.?? 1,3,7,1
...??????. 1,1
#.??????#. 1,1,1
??.?#?????.??#?????? 1,3,2,2,3
????#?????#??? 1,8,1
???.?##??#????? 2,7,2
?.??????#?#? 1,1,1,4
????.??#???#??#?.#?# 2,1,9,3
#???.???#???#????# 4,6,2
??..##?#???? 1,2,1,1
.???#???.?#? 3,2
?#????#??.?#???#???? 4,1,7,1
#?.???#????#??#??? 1,15
???????.???#????. 4,1,4,1
??#????#???..??.? 4,3,2,1
.??..???????? 1,1,2,1
?????#???????????? 1,3,3,3
?#?.???.?#???#??.?# 1,2,6,1,2
??#??#???## 2,2,3
??#?##???#?? 1,3,3
????????#??.????? 1,8,2
???.??.?????.? 1,3
?##?.?#?##?? 3,5,1
???????.??#??# 5,4,1
???#??.???? 1,3,4
.?????..?????.? 4,1
??##??#?#??.? 6,1,1,1
.???????#???##??#? 5,2,8
????###??##???? 1,10
?#?.?#???????#?.?#. 1,2,3,1,1
##?.#??.?.???##??? 3,1,1,1,2,1
?..#???????##????? 5,4
??#?#???#?..????. 1,3,3,4
??#??.?#??? 2,5
.??#????#??#? 1,1,5,2
????????#.???#? 3,1,2,1,1
?#??.#?#???. 1,3,1
????????##??. 1,2,3
#????#??????. 3,2,1,1
?#.??.????#..# 1,1,3,1
#??#??#??#??????#?? 4,6,2,2
??.??#?.#?## 1,3,4
????.#???? 3,4
???????.???? 1,2
?.#???..?.#?#..?. 1,2,1,3,1
?.?????.??#.?? 1,1,2,2
.????#??#.??? 8,1
??#???#???##??.??#?? 2,2,4,2,1
.??????????.?#???#? 2,5,6
??.????##??????? 1,12
??????#?.?##??. 1,5,4
????.?????. 1,1,1
??????.?..??##? 1,1,1,1,4
#??##?????.?? 1,3,1,1
.##..?##??.??### 2,4,5
#???????.???? 1,1,1,2
?????.????? 2,1,1
#.??.?#.?.? 1,2
?.???????..###?????? 1,1,3,4,1,1
?..??.##?.??? 1,2,2,1
??#????..?????# 3,1,3
??#?.????#?.???. 1,1,1,1,3
??#.???.#????#### 2,1,1,6
??#???.?.?????#? 5,1,1,1,1
?#???#.????? 6,1,1
?#??.??.??? 4,1,1
??????#???????? 6,2,1
??.#??.???#?? 1,4
#??.?#???.#?. 2,4,2
??##???#.??? 1,2,3,2
?.??????????# 1,5,1,1
?#?????#?. 1,1,3
????.?##??? 1,4,1
.??#..???##?##??##?? 2,10
??##????#???. 4,3
.??#???##?? 2,3
#???.#?#?????.?..#? 1,1,7,1,1
?##??#??????..? 3,2,1,1,1
?????.?#?#? 5,2,1
???.????#?? 2,3
????.#???.???? 1,3,1
?#???.???? 1,1,2
?#..??.??#?.. 1,3
??.??###?????? 1,8,1
#????#???. 6,1
#.??##????.?#???# 1,6,1,1,1
????#?????..#? 7,1
???.??#??????# 1,1,4,4
#???#.?...??.? 5,1,1
???.?????#??#???. 1,10
???????##??##?.?.? 2,4,2,1
#.#.??????.?#?#? 1,1,4,1,4
?.??##????. 1,2,2
?#?##.????.?..?? 5,1,1,2
..???#????# 4,3
.?.??????#??#?#?#.? 7,6
??#???#?##?.??? 4,5,1
.#?.????#??#.?? 1,1,6,1
??#??#?????. 3,1,1
?.#?.#?????????? 1,1,6
#..?????.?.?#??.?? 1,1,2,1,3,1
.?????.#??????..# 4,1,2,2,1
.##.???????? 2,1,1,2
??##?#??#?.#??.?? 7,1,3,2
???#???????#????. 4,5,1
????.???##???.????# 1,1,1,3,2,1
??.?##.?..???? 2,1
#???.??????#???#?? 1,1,7,3
#???#??.?? 5,1
#??.#??.#.#????#??? 1,1,1,1,1,7
?????????.???????? 1,1,2,1,1,2
??##??#??????? 7,1,1
##??.???.????. 4,1,1
?#????.?????... 4,2,1
????.????.????#?.? 1,5
???????#???.???? 4,3,1,2
??.??.?.?? 1,1,1
??????.?#???#?? 3,1,2
??.#?.??#????? 1,1,3,2
??#.??..???#.??? 1,2,1,1,1
??#???.?.? 4,1
?.???...?#? 1,3
??#?#??#?#? 3,1,1
???.#?#??.?..##??? 1,1,5,1,2,1
?.#??????###? 1,1,4,3
?###??.??????#??? 6,1,2,1,1
??#??#??.???#?.??? 8,3,1
.???????????#?? 2,1,4,1
?#???..?##?? 2,3
?????????#??.#? 1,1,5,1
???#???#??#?????#?#. 4,12
??#?????????????? 6,4,1
#???##????.?#.?? 1,5,1,2,1
?#?#?#?#?.?.??? 9,1
?.#?#???????#? 5,1,3
.????????#? 3,1,1
.????????### 3,1,3
??.???.???#???#? 1,1,2,3
???#.?####???.??? 3,4,1,1
.??#..??????.??? 2,4,1
??#?##???#? 4,2
?#.?#?#?????????# 1,5,6
??#?????.????? 3,2,2
?????#?.???.?????? 5,2,2,1
.?#???#????# 6,3
#.????.??#??.? 1,4,1,1
?#???..?#???..?? 5,2,1,1
??????#??.#?. 7,2
??????..??. 3,2
??#???.????#?. 2,1,2
#.??#?#?????#? 1,7,2
.??.#?.?#?. 1,2,2
?#??????#?.???#?# 3,1,2,1,3
.??..?????? 2,4
??????????.####?#?.? 2,5,6
.??????????#.#?.?# 1,8,1,1
??????#??##?#?##?? 1,2,11
###????#?.?.# 5,2,1
??#..??.??? 2,1,1
#??.#??#?##???#?#. 1,1,1,9,1
#????#.??. 3,2,1
????.????.???# 1,3,2,1
#.?#???##?#.. 1,4,4
..#???#.?? 1,1,1
???.?#?#??.#?#?.? 1,4,4
?#???##???##??????# 7,10
.?#???#???. 2,2
??????????#?????#??# 1,1,6,1,1,2
?????????#..## 1,1,3,2
???.?????????. 2,2
?#?.????###?#? 1,1,4,1
#..???#??????????# 1,1,1,3,2,1
?#.????##?? 1,1,2
?#?.?.??#? 3,1,1
.?????????. 1,4
?????.#???? 2,2,1
#??#?.?.????.?. 5,1,1,1,1
#.?#???.?? 1,3,1
??#????#???##???? 1,1,8,1
.?.?????#?? 1,1,3
#?#?##.?.??????.. 6,1,1,1,1
#??.???.?#???? 1,1,1,5
?#.?????#.?#.???##.? 2,6,1,3
?????.??????#.?#? 1,6,2
.????##????? 6,1
???#?.?#??#??# 4,2,4
??????.??#??.. 1,1,1,3
?????????????#????? 1,11,3
..?.?????.?? 2,1,1
#.?#?????.??????# 1,1,2,2,2
#??.???..???## 3,1,1,2
?????#?????.#???.# 5,1,1,1,1,1
?#?#??.?.???# 2,1,1,4
##.#?#?.####????. 2,1,2,7
?#????###???#??.?#?. 15,3
.??##??.???##. 4,5
?#?.????.?##?#? 1,3,4
.??????.??. 3,1
.?#???.?#???? 2,3,2
.???????.?.. 1,2
#?#.???.??#??? 3,2,2,1
???.?????#?????#?? 6,1
?.?##??????.??. 6,1
###?##??????#???. 3,2,7
????#????.??#????. 8,3,1
?#????.??.???? 4,2,1,1
?.?????#??#??#???#? 4,1,9
?.???????##?#?. 4,4
??#???????#???#?.? 1,9,1,1,1
?.#????#????? 1,1,6
???#?????.??## 6,3
?.??.#????? 1,1,4
.???#???.??.???.?? 4,1,1,1,1,1
.?????...??...?? 1,1
.??#??#??????????? 4,8
???..???###? 2,6
.#???.????#???.?? 4,2
??..??.#??#??#? 1,7
??#?#.??.?.???##?#. 1,1,1,1,1,7
#?????????.?#??? 8,1,1,1
????????????#??? 2,8,1,1
##?#?##??? 2,6
????.??.##??????#? 1,1,1,2,5
??????#?????? 2,3,1
.??#..##????#?#??.? 3,10
???.#?#?????#? 1,3,1,2
?????#?#??..?#??? 2,5,3
?.?.???#??? 1,4
??##???????#??? 7,1,1
??#..??#.?? 1,2
?????#?..??????## 5,7
?#??.??##?##? 1,7
????..#????.##???. 3,1,1,5
???.????#?.?.??#.?? 1,2,3,1,1,2
???##????..??#????. 1,6,7
???#?????##?.????? 1,1,5,4
.?#???..????#. 1,5
????????##??.#. 2,1,4,1
??.#?????..??#####? 1,7
???#?.??.????.?# 2,1,3,1
?????.???# 2,1,4
??#?#????##..#??#?? 5,3,1,2
?#?????##????? 10,1
??#??#???.?.#??#?? 6,1,1,1,3
#?.??##????#### 1,6,4
???#?#??????##? 6,4
?#??????..# 6,1,1
????.???#?? 1,1,5
.#??#.??.??.??# 4,1,2,3
???#.?.#?..?#???.?? 1,1,1,2,2,1
???.?##??#.?. 2,4,1,1
#.???.???#?#.? 1,1,5
????..#???#?#?? 2,1,9
?.?????.???.? 1,1
#??#?#.?#?.????# 6,1,3
???.??##?.??.??.?#? 1,1,4,1,1,3
?????###?##.???????? 1,8,1,1,1
??##??????#.? 4,3,1
???#.#??#.?.#?# 4,1,1,3
?#?#???#?? 5,2
????#?#????????#?? 3,5,1
??.#.??###.????? 1,1,4,1,1
..???##???????#?.??? 12,1
###??#.?#.????#?#?#? 6,1,2,3,1
.???#???????#? 1,1,1,3
?#..??.??#???#.??#? 1,7,3
?.##..#?#?## 1,2,6
??.???..?.#???? 1,2
?.??..??#?...? 1,3
.???#????#?.?.??.?? 5,1,2
..?##?????#?? 3,2,3
?#?#???#?#?? 4,4,1
??.??#??#..???#?# 6,4
#???.??#?#?#.#????? 2,1,1,5,1,3
?#????.#?.?? 2,3,1,2
?##?#????. 6,1
..??.#??#???.?? 2,1,4,1
???#.??.????? 3,1,3
.#????????#?#??# 5,1,7
..???????????.#? 1,4,2,1
??#.#???????????.? 1,1,5,6
?.#???.???. 3,2
#.#..?????#??#??? 1,1,10
?#?##?.?####?#????# 4,4,1,1,2
?..???????? 1,1
?.##?####?.???#..??? 7,1,1,1
?#???..??? 2,2
?.??.#???#?#..??? 1,3,1,1,2
??.????#?.?#?.? 2,1,1,1,1
?.#?????#.?# 7,1
.#?????#?##?#? 2,4,1
.???#???????????#.? 1,5,1,3
???#?#?#??.?. 7,1,1
?##?.#???#??#?.? 3,6,2,1
????#???????..??#? 1,1,1,6,4
??###??.?##???#.?? 3,7,2
???..????.? 1,3
????.?#?.#? 1,2,1
?.#.#.??##?##??.?? 1,1,1,1,7,1
.?###.?????? 4,1,1
?#??##.????.??????? 1,3,2,1,1,4
.????##???? 1,4
.#?##?.#????.???#? 4,2,1,4
.?#????.??#..# 4,1,3,1
???????????### 1,3,2,4
###???#????#?? 4,1,1,1
??##????????#?#?? 3,7
#?#?#####?#????.??. 14,2
???..??????.?#?#???? 2,5
????###?.##? 5,2
?????.?#???#????#.? 1,10
#.???.???#????????? 1,2,1,6,3
??#.??###???.???. 2,4
??#???????.??? 4,2,1
#?..#???##?##?? 2,6,4
????#?.??.?#.??. 2,1,1,2,1
##????#?????.?.???. 8,1,3
??#??.?????.? 3,4
#??#?????????.??? 1,3,3,3,2
????.????##? 4,6
.????##?#?#??.??? 7,1,2
?.#?.????.???##? 1,1,1,1,4
??.#???#???.?#??#? 5,1,4
??#?##???????????? 10,1,1
#???????.?### 2,3,4
.??.#?????#?#.#??# 1,1,3,1,1,4
.##?#???#.????.#??#? 8,1,4
.??.??#??#.???###?. 1,6,7
?.??#?#?.??? 1,1,3,1
???#??#??? 1,5,1
.??..#???#? 1,3
???#?###?#?#.?#??# 12,2,1
????#.?##??? 5,4
.##?.??.###?.#??# 2,1,3,1,1
??.??##??#????.#.? 1,7,1,1,1,1
?#??#.??.#??????.#?? 5,1,1,1,1,1
..??###.???####?.??? 5,6
????#?#?#.??# 6,1,1,1
??#?#??.#?#.? 3,3
??##?#????. 3,1,2
.??#??.#.???????.. 5,1,2
.#???????#? 1,1
##???????##??? 2,10
????.#????#?????.? 2,1,2,1,4
???##?????#????#? 1,2,1,4,3
?.#?.????#???#?. 1,1,1,4,1
.????.?????? 2,2
??.#?##?????? 2,6,1
.?#?.#??????#??# 2,5,4
?#??.??????????## 1,1,8
????????#?# 1,8
#???#.????# 3,1,3
???????..??#?#???. 1,6
??.???.#.?????#???.. 1,1,1,3,4
???#?##???#????#.#. 9,2,1
...???????? 4,1
???#?#???#??#?.??? 10,1,2
.##?.??.?. 3,1
???????#??? 1,3
???##????.? 7,1
??#?????##?#??.. 2,4,1
???.????#???? 1,6
??#???#.??#?? 7,1,1
?????##.??.??? 7,1,1
?#??.?#??.. 2,2
??#?#?????#??.#? 1,1,1,4,2
??#???##??##????.?? 2,9,1,1
???##??????????.#.?? 6,1,3,1,1,1
#????#????????? 1,1,8,1
??#?.??#.??? 1,3,1,1
?##??#.??? 3,1
?..#??????? 1,3
..??##..?#?###.? 4,6
??#????????.???? 6,1,2,1,1
?.?????.??? 1,3
?#?#.#???#.#? 3,5,2
.?.????#??. 1,1,2
???.???.??#?. 2,1
????#??????#????#? 1,1,1,5,1,1
#??????#???#.???? 12,2
.????????????#??.?. 6,2,3,1
???.??###??.?????#? 3,6,2,1
?.?#??#??. 1,1
#??#?#????## 4,1,4
?.??#?????#?????. 4,6
??#????.#? 1,2,1
?.??##.?##???#?? 1,3,4,1
?#??????#???#?.# 1,1,3,1,1
???#.??????.??? 1,1,1,1,2
.????.#???? 2,4
##??#?..?##.????...? 6,3,1,2,1
?.#??#???..##??? 1,2,4,5
???#?????.???#??#? 1,3,2,4,2
.?.#???#???.??.# 1,6,1,1,1
#???#????..##?????? 9,2,4
.#?.???????.#??###?. 2,5,6
?.?###????? 1,4,1
????#?##?????#.? 1,6,4,1
??.??.????##?.? 1,1,2,3
????###?..????? 6,3
.?????..??#???... 3,4,1
.?.#?##?##????????? 7,1,4
?.?###???#??.??.? 1,8,1,1,1
?#?#?##?#???.?.????? 9,2,1,1,1
?..??#????.????.?# 1,3,3,3,1
????##?.??#?..??? 6,3,1
.??.?##?.##?.? 1,4,3,1
??##???#??#???.?? 1,3,6,1
#??#???.??.? 7,1,1
?..??.?.???.. 2,3
??????#?????#. 2,4,1,1
???.??????.#.?? 1,1,2,1,1
?.?#?.????? 1,2
.#.?#??#???????? 1,4,2,1
??..???#.?. 1,1,2
?.??#???.????? 1,6,1,2
??#.???#???#??? 2,8
?##..?#.#???????# 3,1,3,5
??.??#?#?? 2,4,1
.#??.?..??? 3,1
.#?#?.???????? 3,2,1,1
.??????#?#??# 4,1,1,1
???#?????.??#??? 3,1,6
?.#?.?#.??? 1,2,1
.?#??##??# 1,5
?..????#?? 1,3
?????????#?#.????##? 3,2,1,1,1,4
..#..???#?##? 1,1,4
???##??.??#?##????# 1,3,1,4,1
????#??#?####?????? 2,10,1
??.??.##..??. 1,1,2,1
??.???.???##?#?##.?. 1,1,1,10,1
???.????????? 2,1,2
.?##?.?#?????#??.? 3,8
#??#???.?.?#.? 4,2,2,1
??####?##????#?? 9,4
?????#??.??...?.?..? 2,1
???????.?#?? 2,1,2
??.#???????.??#..?# 2,3,3,2,2
?..???????????? 1,1,3,2
?##????.?.?#.?#???? 5,1,1,1,1,1
.????.?????????.?. 4,1,4
????????#???? 1,1,4
#?##?#.??.?#???????# 6,1,1,1,1,1
??#???##?#???# 1,1,7,1
.??#???????? 3,1
?????#?###??##? 2,9
?.#?#???##??#????# 1,1,1,1,6,2
????#?..?##.??? 2,2,3,1
???.???.??.? 3,1
#?#.#?###??.????##? 1,1,5,1,2,3
???????#?#??? 10,1
.?????????. 1,1
..#.?##????## 1,5,3
???#?????.?? 1,2,1,2
????.??#??# 1,6
????.??##??????. 4,6,2
??.????#.?.?#?#??? 5,5
?.???#.??? 1,1,2
#.?.?#..?###???#??? 1,1,2,5,1,1
.??##..#?.?#?. 4,2,1
???.?#?.??.?. 3,1
?#???#?.?#?. 3,1,2
?.????#??? 4,2
????.??#?..???#?. 3,3,1,2
..?##??..?#?????#?#. 4,10
??#?.?#??# 3,1,1
#?.???.#?#???##?? 1,1,3,5
?#???##?#??.???#?. 8,4
?#?.?#?.???.?# 1,3,1,2
???.??.??????.#.?? 1,1,3,1,1,1
.??#??????#?.?? 6,2
?????????. 3,2
????#??.????#? 2,2,1,1
??#????#???.??? 4,2,1
##?????#??? 4,1,1
.#??.??#.#.? 2,2,1
?.?##????? 1,5,1
#???#??#???????. 2,4,4,1
?#?.???##????#??? 1,9
##?.#??.??#..?#????. 3,3,1,1,5
?#.???#####???#??#?? 1,8,1,1,4
???#..????.#????? 3,1,6
?.?????##?? 1,2,2
???#?#????..#????. 4,2,4
..??????.?????#.?? 3,1,1,1,1,1
##??#??????????#??.# 2,1,10,1
?.#?##???.??? 1,5,1,2
?.?#.??????????#??#. 1,2,10,1
???.?#?##.??.?#?#??? 3,5,2,1,3
??..#.???# 2,1,4
??.????##?#?#???? 1,6,2
?.?.???#????.??.? 1,4,1,1,1
.#??.#??.#?.?? 1,3,1,1
.?##?#???.?.. 3,1,1,1
?#????????#??#??? 1,1,10,1
?.??#??..#. 1,2,1
.?#????##??? 4,2
..#.???.?#????????# 1,2,11
?##??#?.????.?#??. 6,2,3
????..?..??#??.#?# 1,1,1,1,1,3
????#?.#.? 3,1
.??#??.??.. 3,1
.#??#???#???. 5,4
?.?..#??.? 1,1,1
??#..???#?.. 2,4
##???????#????##?.? 3,2,4,3
???#????.#????.?? 4,3
?????####?????????#? 14,1
?????#.??#??# 3,1,5
.?.?#???#??##??? 6,4
#???#??.?..??##?#??? 7,1,9
?????#???????#??? 3,2,1,6
???###?#????#??#.?# 5,9,2
???#??.?#??#?#???# 4,7,2
..??..?.#??????# 2,1,1,5
.????????#??? 1,3,1,1
????.??#?#???? 2,4,1
.???????????. 2,3
??????#??? 4,1,1
?????.??.??.?#? 1,1,1,1,2
.#???#???.????.?.? 8,2
.??#.??????..??????? 1,1,1,4,2,3
??????.???? 3,2,1
#?.#?????.?????? 1,1,1,2,2
??#.??#..##??? 2,2,3,1
?#???.???? 4,4
???.?????.#?? 2,3,1
??#?.#?#??##?#??#. 1,12
?.#?##??.??????. 1,1,4,1,4
.?.??#??????##??.# 1,12,1
..#??????.#??.??? 3,2
???????.?????#???.?. 1,3,7,1
?#?.?????#?.?.? 1,1,1,2,1
#?????#???.?????? 8,1,1,1
????????#???#??# 1,1,1,2,6
??????#???.?#????### 4,1,9
??#?????#?????#?#? 3,10
.??##???.?? 4,1
????#???#? 1,2,3
??#?.?#????? 2,6
#?#?#?..?.#???? 5,1,1,2
??.?????#??????#??# 2,1,5,1,4
.##??.??..???#.? 2,2,4
??#???.#.?? 4,1,1
.#??#???.?#..?.??.?# 5,1,2,1,2,1
?#?????##?#????.?. 4,7,1
##????#???#???. 4,1,3
?.??????#??.?????.? 7,5
?????#.???.? 1,1,2,1
.#????#?#??##?#. 1,2,4,4
?.??.????##? 1,1,1,3
?#.#??.?#??? 2,1,2,1
.????#??????###??. 8,5
.??????.?#? 1,1,2
?#????????? 4,1
???#.???#.##??##??# 1,2,1,1,9
#??..?????? 3,3
?##???.#?#?????## 5,6,3
?????#??#.??##???. 1,2,2,4,2
.???#?????#???##?? 5,1,1,3,1
..?.?.?#??#????#.? 1,1,2,3,1,1
?????#????? 2,3,1
??#??????.???..? 1,2,1,2,1
?????.?..?##?#????? 1,3,1,7,1
?#?.??.?#?#??#.?? 3,1,4,2,1
????.??#?#?#? 1,1,6
.?#???#??.#.? 2,2,1
????.#?????. 2,2,1
?.#??..??????#??? 2,10
?#?.??#?.?.?? 3,3,1
.??#?#??#?#?##?????# 1,12,3
.?...?#?#??#. 4,1
.?#???????#?.?#??#? 2,1,3,2,2
.?.???.????? 1,1,3
???#???..# 3,1,1
????.?????#?? 3,1,2
#.??##?????????#? 1,5,3,1
??#??????????? 4,5,1
??????....##???#? 1,1,1,3,2
??.????##?????. 1,10
????#?????#?? 1,4,1
?????##?#? 1,2,1
?#.#?#?.?#.?..#?### 1,3,1,1,5
??.#??.???#?#?#?#??? 1,1,11,1
??#?#????#?#? 1,1,2,4
??##?.???? 2,2
?.???#?????.????#?# 1,1,5,1,2,3
##???#???#?? 4,6
??#??.???????..? 1,3,2,1,1
??.?##.###??????...? 1,3,5,1,1
.???.?##??# 1,4,1
??????.#.??##?##?#? 2,1,1,1,9
?????????##????.?? 11,1
#??#?##????#?#? 1,11
.??#?.??.?? 4,1
?#????.??.???# 3,2
.?.???.??? 1,2,1
??##??#??#??#?#??#. 1,2,2,1,4,1
???.??#?#??# 1,1,4
?.#???#??##.??..???. 1,6,2,1,1,1
???#?????. 3,3
?.????.?.#? 4,1
???.#?.?#??..#?? 1,2,2,3
??#??????##. 1,6,2
??##?#??##? 5,3
????????.?#? 3,3,3
.??????????.?##??? 8,4
??.??.??##???##?. 2,2,9
#?#???..?###?.???#? 5,3,3
?????..?#??#?##?#??? 1,1,2,9
.???#??..? 1,3
??.##???#???.??? 1,8,1,1
?.????.?#? 2,2
???#???#????##?? 1,12
????.?#?##?.????##?? 2,2,3,1,6
??#?.?.??????.?? 1,4
????..??.???? 1,1,1,2
?.#??????# 1,1,2
???#????.?.#?? 1,4,1,2
???#???#??? 5,1,1
??#?????#?????. 9,2
???##?#??#????????? 7,1,7
??##??..????#??#? 3,1,8
#?????#??#???.?#???. 2,2,5,4
?#?#????### 1,8
?..?#????.???.? 1,1,2,1,1
??????#?.?..? 1,3
.?#.???#??#?????.#. 2,10,1
.?.?#?.??#?..?#. 1,2,3,2
?#?.??.??#??.??#? 1,1,3,1,3
.#??????#?#???#.???# 2,3,4,1,2,1
????????.??? 2,2,3
??????..##???.???. 2,3,3,3
#.?.??.??.?? 1,2,1,1
#????#.???## 1,3,5
#??####?.?#??##???? 2,4,9
?#??????.?#?? 2,3,1
....?????.?.???#??. 1,3
????.?#???. 1,2
??#.#??###?##?#?? 2,13
.?.????????. 1,7
?????.????. 1,1
?..?#?#??.??.? 4,2
.??#?????#?#?#?????. 1,2,6,1,1,1
?#..#??.?#.?????? 1,2,2,5
?.???.??##?.#? 2,1,2,1
??#?#.???. 4,2
?#?????###?#? 1,3,3,2
???#.#.#.#??????## 1,1,1,1,4,3
.?#..????..???##?? 1,3,6
??.#.?#?.##? 1,1,2,3
##?#??.???#..?. 6,1,1,1
???????.?? 3,1
???#???????? 1,1,1,1
.????#????.??#?????. 4,7
????????##.?.?????. 9,4
?###?.#??? 4,1,1
??##?#???# 6,2
.?##????????#.? 2,4
????.????#??#?? 2,1,8
????##??#?#?.?.??#.? 12,1,1,1
?????..??##? 5,1,2
????????#? 1,1,3
?????#?..???.??? 2,2
.#?????#??#??#?# 5,1,1,1,1
?#?.??.?#???# 1,1,2,1
.??#?#?#?????# 5,1,2,1
.?#??.??????..??? 3,2,2
???##?.#?#.???. 5,3,1,1
#?#?????????.. 4,1,2
???..???.??#??# 1,1,1,1,2
??????#??##???.??? 11,1,1,1
...???#?????##?#?#? 1,1,2,6
.#?###??.?.??.?.?##? 7,1,2
.????#?#??.? 6,1
.??.??.??. 2,1
?????.#??????.? 2,5
.?????.??? 1,1,2
??#???.##.??? 6,2,2
???#??..?##??##? 5,3,4
?#???#??#? 1,5
#?#?????#?.?? 1,1,4,1
???.?#????? 1,7
???????.?. 2,3
?####??#??????????# 11,1,1,1
.?#?#???????#??? 3,1,4
???#?????????#?.... 8,1
????????#?????#????? 2,2,11,1
.##???#.?????#?# 3,1,4,1,1
??#???#??#. 1,3,1
????????#.?###? 3,1,1,4
?#.??.???#???????#? 1,2,1,5,2
.??..#???#??#?##???. 1,14
?##??#?#?.?..? 6,1,1
?..#??.#.?# 1,1,1
?.#???????#??? 1,6,1,1
??#?.#?????? 1,7
??.#??????. 1,1
#??.??##.??? 1,1,4,2
??????????.? 1,3,1,1
#?????#???. 5,4
.?##?#??.?##.?? 3,1,1,3,1
.???#.???#?? 1,1,1,1
..###.??????.? 3,2,1,1
?.??.?#????#.??#?#?? 1,1,1,4,1,3
????#??????????? 3,1,2,1,4
.?.??????? 3,1
?###???#.?.?? 5,1,1,1
??###???.?.?#???. 4,3
??..????.?.?# 1,1,1,1
#??.??..?. 3,1
???#?#??#??????? 8,2
#?????#.?????? 5,1,2,1
??.?#??#???#???#.#? 2,13,1
???#?#?#?.###??????? 4,1,8
???..?.???#..?.#?? 2,4,1
???.???#.. 3,3
????#?#.????#?..??? 1,4,1,3,2
?.?###.???# 3,3
?#?#.?.?#???#??. 2,1,1,2,5
???##???#?#.? 5,3
#?##???#..???###.??? 8,1,3,1,1
??.??#????#??.? 1,1,4
#??#???..???. 4,3
??#???????#??#?#. 1,12
???#??#??#?? 1,2,1,4
####.???#??#????? 4,1,1,4
?????##??????? 9,1
?.??????????#?#?? 3,10
??..??#?#?##.??? 1,1,6,1
?#?#??#?##?#?..?#?? 6,5,4
??.??.??#?#? 1,1,6
??#???#.??##??#.?#.? 1,1,2,6,1,1
?#???#???? 1,6
???.###?????#??#??? 1,9,4
#?.????#??????###?. 1,1,3,1,4
???.??###.?.#?????. 2,5,1,1,2
##??##?.?#???? 6,1,3
???#??????. 4,1
????#?####?#?.????#? 13,1,3
??#.?????? 1,4
?#?###??#.?#???????? 6,2,5,1,1
????.???#??????? 1,2,6,1,1
#???##?????###??.?.. 8,5,1,1
???#????#.?????.#?? 1,4,1,5,1,1
??...?#??? 2,1,1
?????????? 2,2,1
.?.??#??..??#???# 1,4,5
?#?.????????? 3,2,3,1
?????.?#####??#?. 5,8
?#?.???#??#?.??? 1,1,2,2,1
.???..?#?#?##?# 2,8
?#????????#?????.#?? 2,1,8,1,1,1
???#????.##???.? 2,2
?.??.?.????????? 1,7
?????#??#.???# 1,4,2,1
?#???????.?.? 1,1
????##??..??...????? 7,3
???.?????????#...?? 3,1
?#?#??#?????#?#? 9,3
??????????. 3,5
??#??.#??# 4,1,1
???????.?# 2,1
???????###?..?#?? 2,6,4
??#?????##?. 4,4
.??#???????. 3,1,1
?.?..???#??#? 1,1,3,2
????...????#??#???? 1,7
???????????#????#?? 2,1,11,1
.????????.? 3,1
?.??#???.???????.??? 1,5,2,1,3
?#????..????? 2,1,4
??????#??? 1,1,1
?.?.??.??#?. 1,1
????????#??? 4,3
?####?????#????????? 5,1,1,1,6
???.?.?#???#??#? 1,1,7,2
.????##.???????#. 4,6
.????????##? 5,3
?????.???#??? 4,3
???#?#??..#????.?.? 8,1,2,1
.????#?.??##? 2,2
??????.#???????##? 1,1,1,7
?#??#?#??.??#??? 1,1,2,1,3
.?#????.?? 1,1,1
?.#??#????????##??? 1,16
##?????????????#..? 8,1,1,1
?.#?#??????##.?#?? 11,1
#?????#.#?#??? 1,3,4
??????????. 1,1,1
#.????.?#.??.?.? 1,3,1,1,1
?#???#??...? 3,3
???????#????? 3,1,1,3
?##?#??.???? 6,3
?.??#?.??????.#??? 1,3,5,4
??#?.???.#??#? 2,2,5
?#???#???#.? 1,5
???##?#???????? 7,5
#.????.?????? 1,2,1,1
???#..???##??#?.#? 1,1,1,2,2,1
#?##???..??????#?# 4,1,1,6
?#??.#?.?#???.? 1,1,1,4,1
????..????###? 4,2,4
.?#??##??#??? 1,5,1
.#.?.?##????? 1,1,2,1
??.?.????#?????? 1,1,10
???##?#??????.#???.? 5,2,1,4,1
??..???#.????.# 1,4,1,1,1
???##??????.???. 2,2,2
#???.?????#? 4,1,2
##?#?.?##? 4,2
????#??????? 4,1
?.?.???.?? 1,1,1
??.????...??. 1,2,1,1
???????.?# 2,2,1
?????????. 3,3
?#?#??#?#?????.??. 6,5,2
#???????#???#?##???? 2,6,6,1
.?#?#.#.??#?????## 3,1,2,2,2
..?##?????##?.??#. 10,2
?..?#???????????? 1,6,2,1
?#?#???.???.?#??#??. 2,4,1,6
???.??????.????...?. 3,3
???#?.???????#??? 1,1,1,3,5
??###??##.?????????. 7,6
.????????.?? 4,1,1
#????.?#?##??#?. 5,8
?#??????#?..? 4,1,1,1
??#?#????.?##????? 1,5,5,1'''
lines = re.split("\n+", input2);
def gt0(num):
    return num > 0;
def isSpring(char):
    return char == '#';
def countSprings(s):
    return len(list(filter(isSpring, list(s))));
def countSpringsInGroups(s):
    workingSections = re.split("\.+",s);
    return list(filter(gt0, [int(len(x)) for x in workingSections]))
def endsWithSpring(s):
    return len(s) > 0 and s[-1] == '#';
totalPossibleCount = 0;
for line in lines:
    springsAndCounts = line.split(' ')
    springs = f'{springsAndCounts[0]}?{springsAndCounts[0]}?{springsAndCounts[0]}?{springsAndCounts[0]}?{springsAndCounts[0]}'
    countsStr = f'{springsAndCounts[1]},{springsAndCounts[1]},{springsAndCounts[1]},{springsAndCounts[1]},{springsAndCounts[1]}'
    targetCounts = [int(x) for x in countsStr.split(',')]
    targetTotal = sum(targetCounts);
    unknowns = [];
    for index in range(0,len(springs)):
        if springs[index] == '?':
            unknowns.append(index)
    untilFirstUnknown = springs.split('?')[0];
    groupCounts = countSpringsInGroups(untilFirstUnknown);
    onWorkingSpring = endsWithSpring(untilFirstUnknown);
    options = [{'s':springs,'c':groupCounts,'onWorkingSpring': onWorkingSpring}];
    while len(unknowns) > 0:
        nextIndex = unknowns[0]
        newOptions = [];
        for option in options:
            os = option['s'];
            oc = option['c'];
            oOnWorking = option['onWorkingSpring']
            nextSetUntilUnknown = os[nextIndex+1:].split('?')[0];
            nextGroupCounts = countSpringsInGroups(nextSetUntilUnknown);
            withNotWorkingNext = list(oc) + nextGroupCounts;
            onWorkingNext = False if len(nextSetUntilUnknown) == 0 else endsWithSpring(nextSetUntilUnknown);
            if len(unknowns) == 1:
                if (withNotWorkingNext == targetCounts):
                   newOptions.append({'s':f'{os[:nextIndex]}.{os[nextIndex+1:]}','c': withNotWorkingNext, 'onWorkingSpring': onWorkingNext}); 
            elif not onWorkingNext:
                if (withNotWorkingNext == targetCounts[:len(withNotWorkingNext)]):
                    newOptions.append({'s':f'{os[:nextIndex]}.{os[nextIndex+1:]}','c': withNotWorkingNext, 'onWorkingSpring': onWorkingNext});
            else:
                lenMinus1 = len(withNotWorkingNext) - 1;
                if(len(withNotWorkingNext) <= len(targetCounts) and withNotWorkingNext[:-1] == targetCounts[:lenMinus1] and withNotWorkingNext[-1] <= targetCounts[lenMinus1]):
                    newOptions.append({'s':f'{os[:nextIndex]}.{os[nextIndex+1:]}','c': withNotWorkingNext, 'onWorkingSpring': onWorkingNext});
                                  
            updatedCounts = list(oc);
            if oOnWorking:
                updatedCounts[-1] = updatedCounts[-1] + 1;
            else:
                updatedCounts.append(1);
            if len(nextGroupCounts) > 0:
                if nextSetUntilUnknown[0] == '#':
                    updatedCounts[-1] = updatedCounts[-1] + nextGroupCounts[0];
                    updatedCounts = updatedCounts + nextGroupCounts[1:]
                else:
                    updatedCounts = updatedCounts + nextGroupCounts
            onWorkingNext = True if len(nextSetUntilUnknown) == 0 else endsWithSpring(nextSetUntilUnknown);
            if len(unknowns) == 1:
                if (updatedCounts == targetCounts):
                    newOptions.append({'s':f'{os[:nextIndex]}#{os[nextIndex+1:]}','c':updatedCounts,'onWorkingSpring': onWorkingNext});
            elif not onWorkingNext:
                if (updatedCounts == targetCounts[:len(updatedCounts)]):
                    newOptions.append({'s':f'{os[:nextIndex]}#{os[nextIndex+1:]}','c':updatedCounts,'onWorkingSpring': onWorkingNext});
            else:                   
                lenMinus1 = len(updatedCounts) - 1;
                if(len(updatedCounts) <= len(targetCounts) and updatedCounts[:-1] == targetCounts[:lenMinus1] and updatedCounts[-1] <= targetCounts[lenMinus1]):               
                    newOptions.append({'s':f'{os[:nextIndex]}#{os[nextIndex+1:]}','c':updatedCounts,'onWorkingSpring': onWorkingNext});
        options = newOptions;
        unknowns = unknowns[1:]
    possibleCount = len(options);
# Don't need to recount anymore:
#     for option in options:
#         workingSections = re.split("\.+",option['s']);
#         workingCounts = list(filter(gt0, [int(len(x)) for x in workingSections]))
#         if workingCounts == targetCounts:
#             possibleCount += 1;
    print(possibleCount);
    totalPossibleCount += possibleCount;
print(totalPossibleCount);
        
        
        