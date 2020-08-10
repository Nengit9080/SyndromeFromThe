import PIL
from random import randrange
import numpy as np
from PIL import Image, ImageFont, ImageDraw
import facebook
import urllib.request, json
import re

#graph connection
graph = facebook.GraphAPI(access_token='token', version="3.1")

starLocations = []
connections = []
userIds = []

#read connections
f = open("connections.txt", "r")
connectionsString = f.read()
if len(connectionsString) > 2:
    connectionsString = connectionsString[2:-2].split('], [')
    for x in range(len(connectionsString)):
        connections.append(connectionsString[x].split(', '))
    for x in range(len(connections)):
        if connections[x][0] != "'end'":
            for y in range(len(connections[x])):
                connections[x][y] = int(connections[x][y])
else:
    connections = []

#read stars
f = open("stars.txt", "r")
starLocationsString = f.read()
#starts new thread
if len(starLocationsString) == 0:
    img = Image.new('RGB', (1280, 1024))
    for x in range(100):
        a = randrange(3, 1277)
        b = randrange(3, 1021)
        d = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", 16)
        d.text((a+5, b),str(x),(255,255,255),font=font)
        randStar = randrange(5)
        starLocations.append([x, a, b, randStar])
        if randStar == 0:
            img.putpixel((a, b), (255, 255, 255))
            img.putpixel((a+1, b), (255, 255, 255))
            img.putpixel((a, b+1), (255, 255, 255))
            img.putpixel((a+1, b+1), (255, 255, 255))
        if randStar == 1:
            img.putpixel((a, b), (255, 255, 255))
            img.putpixel((a-1, b), (255, 255, 255))
            img.putpixel((a+1, b), (255, 255, 255))
            img.putpixel((a, b-1), (255, 255, 255))
            img.putpixel((a, b+1), (255, 255, 255))
            img.putpixel((a, b-2), (255, 255, 255))
            img.putpixel((a, b+2), (255, 255, 255))
            img.putpixel((a, b-3), (255, 255, 255))
            img.putpixel((a, b+3), (255, 255, 255))
        if randStar == 2:
            img.putpixel((a, b), (255, 255, 255))
            img.putpixel((a, b+1), (255, 255, 255))
            img.putpixel((a, b-1), (255, 255, 255))
            img.putpixel((a+1, b), (255, 255, 255))
            img.putpixel((a-1, b), (255, 255, 255))
        if randStar == 3:
            img.putpixel((a, b), (255, 255, 255))
            img.putpixel((a-1, b), (255, 255, 255))
            img.putpixel((a+1, b), (255, 255, 255))
            img.putpixel((a, b+1), (255, 255, 255))
            img.putpixel((a-1, b+1), (255, 255, 255))
            img.putpixel((a+1, b+1), (255, 255, 255))
            img.putpixel((a, b-1), (255, 255, 255))
            img.putpixel((a-2, b), (255, 255, 255))
            img.putpixel((a+2, b), (255, 255, 255))
            img.putpixel((a-1, b+2), (255, 255, 255))
            img.putpixel((a+1, b+2), (255, 255, 255))
        if randStar == 4:
            img.putpixel((a, b), (255, 255, 255))
            img.putpixel((a-1, b), (255, 255, 255))
            img.putpixel((a+1, b), (255, 255, 255))
            img.putpixel((a, b+1), (255, 255, 255))
            img.putpixel((a-1, b+1), (255, 255, 255))
            img.putpixel((a+1, b+1), (255, 255, 255))
            img.putpixel((a, b-1), (255, 255, 255))
            img.putpixel((a-1, b-1), (255, 255, 255))
            img.putpixel((a+1, b-1), (255, 255, 255))
            img.putpixel((a+2, b), (255, 255, 255))
            img.putpixel((a-2, b), (255, 255, 255))
            img.putpixel((a, b+2), (255, 255, 255))
            img.putpixel((a, b-2), (255, 255, 255))
        
    f = open("stars.txt", "w")
    f.write(str(starLocations))
    f.close()
    img.save("image.png", "PNG")
    f = open("connections.txt", "w")
    f.write("[]")
    f.close()

    graph.put_photo(
        parent_object=588423595117226,
        connection_name="feed",
        image=open("image.png", 'rb')
    )

else:
    #get info from stars.txt
    starLocationsString = starLocationsString[2:-2].split('], [')
    for x in range(len(starLocationsString)):
        starLocations.append(starLocationsString[x].split(', '))
    for x in range(len(starLocations)):
        for y in range(len(starLocations[x])):
            starLocations[x][y] = int(starLocations[x][y])

    #get previous comments
    with urllib.request.urlopen("https://graph.facebook.com/v8.0/token") as url:
        data = json.loads(url.read().decode())
    id = data['data'][0]['id']

    with urllib.request.urlopen("https://graph.facebook.com/v8.0/"+id+"/comments?access_token=token") as url:
        data = json.loads(url.read().decode())


    img = Image.new('RGB', (1280, 1024))
    d = ImageDraw.Draw(img)
    endCount = 0
    for x in starLocations:
        a = x[1]
        b = x[2]
        randStar = x[3]
        if randStar == 0:
            img.putpixel((a, b), (255, 255, 255))
            img.putpixel((a+1, b), (255, 255, 255))
            img.putpixel((a, b+1), (255, 255, 255))
            img.putpixel((a+1, b+1), (255, 255, 255))
        if randStar == 1:
            img.putpixel((a, b), (255, 255, 255))
            img.putpixel((a-1, b), (255, 255, 255))
            img.putpixel((a+1, b), (255, 255, 255))
            img.putpixel((a, b-1), (255, 255, 255))
            img.putpixel((a, b+1), (255, 255, 255))
            img.putpixel((a, b-2), (255, 255, 255))
            img.putpixel((a, b+2), (255, 255, 255))
            img.putpixel((a, b-3), (255, 255, 255))
            img.putpixel((a, b+3), (255, 255, 255))
        if randStar == 2:
            img.putpixel((a, b), (255, 255, 255))
            img.putpixel((a, b+1), (255, 255, 255))
            img.putpixel((a, b-1), (255, 255, 255))
            img.putpixel((a+1, b), (255, 255, 255))
            img.putpixel((a-1, b), (255, 255, 255))
        if randStar == 3:
            img.putpixel((a, b), (255, 255, 255))
            img.putpixel((a-1, b), (255, 255, 255))
            img.putpixel((a+1, b), (255, 255, 255))
            img.putpixel((a, b+1), (255, 255, 255))
            img.putpixel((a-1, b+1), (255, 255, 255))
            img.putpixel((a+1, b+1), (255, 255, 255))
            img.putpixel((a, b-1), (255, 255, 255))
            img.putpixel((a-2, b), (255, 255, 255))
            img.putpixel((a+2, b), (255, 255, 255))
            img.putpixel((a-1, b+2), (255, 255, 255))
            img.putpixel((a+1, b+2), (255, 255, 255))
        if randStar == 4:
            img.putpixel((a, b), (255, 255, 255))
            img.putpixel((a-1, b), (255, 255, 255))
            img.putpixel((a+1, b), (255, 255, 255))
            img.putpixel((a, b+1), (255, 255, 255))
            img.putpixel((a-1, b+1), (255, 255, 255))
            img.putpixel((a+1, b+1), (255, 255, 255))
            img.putpixel((a, b-1), (255, 255, 255))
            img.putpixel((a-1, b-1), (255, 255, 255))
            img.putpixel((a+1, b-1), (255, 255, 255))
            img.putpixel((a+2, b), (255, 255, 255))
            img.putpixel((a-2, b), (255, 255, 255))
            img.putpixel((a, b+2), (255, 255, 255))
            img.putpixel((a, b-2), (255, 255, 255))

    if len(connections) == 0 or connections[len(connections) -1][0] != "end":
        for x in range(len(connections)):
            d.line([(starLocations[connections[x][0]][1],starLocations[connections[x][0]][2]), (starLocations[connections[x][1]][1],starLocations[connections[x][1]][2])], fill=(255, 255, 255), width = 1)
        added = 0
        for x in range(len(data['data'])):
            y = re.search("^Connect [0-9][0-9]?, [0-9][0-9]?$", data['data'][x]['message'])
            z = re.search("^End", data['data'][x]['message'])
            if y and added <= 5:
                coordinates = data['data'][x]['message'][7:].split(', ')
                coordinates[0] = int(coordinates[0])
                coordinates[1] = int(coordinates[1])
                added = added + 1
                d.line([(starLocations[coordinates[0]][1],starLocations[coordinates[0]][2]), (starLocations[coordinates[1]][1],starLocations[coordinates[1]][2])], fill=(255, 255, 255), width = 1)
                connections.append([coordinates[0], coordinates[1]])
            if z and data['data']['from']['id'] not in userIds:
                if endCount == 0:
                    ending = (data['data'][x]['message'])[4:23]
                endCount = endCount + 1
                userIds.append(data['data']['from']['id'])
        if endCount >= 3 and len(connections) > 4:
            connections.append(["end", ending])
            font = ImageFont.truetype("arial.ttf", 48)
            d.text((640, 20),(str(connections[len(connections)-1][1])[4:24]) ,(255,255,255),font=font)
            f = open("stars.txt", "w")
            f.write("")
            f.close()
            connections = []
        else:
            for x in starLocations:
                a = x[1]
                b = x[2]
                font = ImageFont.truetype("arial.ttf", 16)
                d.text((a+5, b),str(x[0]),(255,255,255),font=font)


        added = added + 1
        f = open("connections.txt", "w")
        f.write(str(connections))
        f.close() 

img.save("image.png", "PNG")

img.show() 
graph.put_photo(
    parent_object="object",
    connection_name="feed",
    image=open("image.png", 'rb')
)



