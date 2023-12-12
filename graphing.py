#imports graphing library as plt
import matplotlib.pyplot as plt 

#uses open function to read the csv file and assign it to the data variable
data = open("./train.csv", "r").read()

#declares the dictionaries for tempo, duration, and genre
tempo = {}
duration = {}
genre = {}

#for loop that gets every line in the csv file without the first line
for line in data[slice(data.index("\n")+1, len(data))].split("\n"):
    #checks if there are quotes in the line and then removes any commas that are in the quotes
    if '"' in line:
        item = line.split('"')
        newline = ""
        for i in range(len(item)):
            if (i % 2) != 0:
                item[i] = item[i].replace(",", "")
            newline += item[i]
        line = newline
    #splits line by each comma and assigns array to values variable
    values = line.split(",")
    #checks if the popularity value as an integer if above 80
    if int(values[5]) > 80:
        #assigns the tvalue varable as the tempo value converted to a float so it can be rounded and then turned back into a string
        tvalue = str(round(float(values[18])))
        #assigns the dvalue variable as the duration converted to a float and then divided by 10000 to be rounded and then multiplied by 10 back into a string
        #it rounds the duration to the nearest 10 seconds
        dvalue = str(round(float(values[6])/10000)*10)
        #checks if the tvalue is not in the tempo dictionary to create it, else it will add one to the existing value
        if tvalue not in tempo.keys():
	        tempo[tvalue] = 1
        else:
            tempo[tvalue] += 1
        #same process is repeated for duration and genre

        if dvalue not in duration.keys():
	        duration[dvalue] = 1
        else:
            duration[dvalue] += 1
        
        if values[20] not in genre.keys():
	        genre[values[20]] = 1
        else:
            genre[values[20]] += 1

#assigns x and y as dictionaries
x = {}
y = {}

#assigns the t, d, and g variables as the keys of the tempo, duration, and genre dictionaries sorted from highest frequency to lowest
t = list(dict(sorted(tempo.items(), key=lambda item: item[1], reverse=True)).keys())
d = list(dict(sorted(duration.items(), key=lambda item: item[1], reverse=True)).keys())
g = list(dict(sorted(genre.items(), key=lambda item: item[1], reverse=True)).keys())

#for loop goes from 0 to the length of the tempo dictionary
for i in range(len(tempo)):
    #checks if it is the first iteration of the for loop to create the keys for x and y assigned as empty lists
    if i == 0:
        x["t"] = []
        y["t"] = []
    #checks if the frequency is greater than 1 to then append the key to the x list and the frequency to the y list
    if tempo[t[i]] > 1:
        x["t"].append(t[i])
        y["t"].append(tempo[t[i]])
#same process is repeated for the duration and genre

for i in range(len(duration)):
    if i == 0:
        x["d"] = []
        y["d"] = []
    if duration[d[i]] > 1:
        x["d"].append(d[i])
        y["d"].append(duration[d[i]])

for i in range(len(genre)):
    if i == 0:
        x["g"] = []
        y["g"] = []
    if genre[g[i]] > 1:
        x["g"].append(g[i])
        y["g"].append(genre[g[i]])

#assigns the new range as 100
#this variable is used to tell the graph the max amount values to display
newrange = 100

#uses graphing library to create a bar graph
#the first value is the x list split using the newrange value
#the second value is the y list split using the newrange value
#the third value is the x list split using the newrange value as the labels for the x axis
#the fourth value is the width of each item in the bar graph
#the fifth value is the colors red and blue in an array for the coloring of the bar graph
#the colors will alternate between eachother
plt.bar(x["t"][slice(0,newrange)], y["t"][slice(0,newrange)], tick_label = x["t"][slice(0,newrange)], width = 0.7, color = ['red', 'blue']) 
#rotates the labels in the x axis by 90 degrees
plt.xticks(rotation = 90)
#adds label to the x axis
plt.xlabel('Tempo (Beats Per Minute)') 
#adds label to the y axis 
plt.ylabel('Frequency') 
#adds a title to the entire graph
plt.title('Frequency of Songs with Similar Tempo (Above 80% Popularity)') 
#displays the graph
plt.show() 
#same process is repeated for duration and genre

plt.bar(x["d"][slice(0,newrange)], y["d"][slice(0,newrange)], tick_label = x["d"][slice(0,newrange)], width = 0.7, color = ['red', 'blue']) 
plt.xticks(rotation = 90)
plt.xlabel('Duration (Seconds)') 
plt.ylabel('Frequency') 
plt.title('Frequency of Songs with Similar Duration (Above 80% Popularity)') 
plt.show() 

plt.bar(x["g"][slice(0,newrange)], y["g"][slice(0,newrange)], tick_label = x["g"][slice(0,newrange)], width = 0.7, color = ['red', 'blue']) 
plt.xticks(rotation = 90)
plt.xlabel('Genre') 
plt.ylabel('Frequency') 
plt.title('Frequency of Songs with Similar Genre (Above 80% Popularity)') 
plt.show() 