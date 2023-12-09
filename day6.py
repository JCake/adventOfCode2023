import math
timeIndex = 0;
distanceIndex = 1;
sampleInput = [[7, 9], [15, 40], [30, 200]];
realInput = [[44,277],[89,1136],[96,1890],[91,1768]];
multiple = 1;
for race in realInput:
    time = race[timeIndex];
    speed = math.floor(time/2); # for max
    movingTime = math.ceil(time/2); # for max
    waysToBeat = 1 if speed == movingTime else 2; #assumes max is > record
    speed -= 1;
    movingTime += 1;
    while(speed * movingTime > race[distanceIndex]):
          waysToBeat += 2
          speed -= 1
          movingTime += 1
    multiple *= waysToBeat
print(multiple)

singleTimeStr = '';
singleDistStr = '';
for race in realInput:
    singleTimeStr += str(race[timeIndex])
    singleDistStr += str(race[distanceIndex])
speed = math.floor(int(singleTimeStr)/2); # for max
movingTime = math.ceil(int(singleTimeStr)/2); # for max
waysToBeat = 1 if speed == movingTime else 2; #assumes max is > record
speed -= 1;
movingTime += 1;
while(speed * movingTime > int(singleDistStr)):
      waysToBeat += 2
      speed -= 1
      movingTime += 1
print(waysToBeat)
    
          
        
    