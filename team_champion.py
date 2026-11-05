team_blue = input("team blue score").split(",")
team_red = input("team red score").split(",")
team_green = input("team green score").split(",")
point_blue = 0
point_red = 0
point_green = 0
for point in team_blue:
    if (point == "w"):
        point_blue += 3
    elif (point == "d"):
        point_blue += 1
#point for team blue

for point in team_red:
    if (point == "w"):
        point_red += 3
    elif (point == "d"):
        point_red += 1
#point for team red

for point in team_green:
    if (point == "w"):
        point_green += 3
    elif (point == "d"):
        point_green += 1
#point for team green
   
if(point_blue > point_red and point_blue > point_green):
    print ("team_blue champion")
if(point_red > point_blue and point_red > point_green):
    print ("team_red champion")
if(point_green > point_red and point_green > point_blue):
    print ("team_green champion")
print(point_blue,"blue team points")
print(point_red,"red team points")
print(point_green, "green team points")