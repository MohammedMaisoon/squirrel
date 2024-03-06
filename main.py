import csv
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240305.csv")
count1 = len(data[data["Primary Fur Color"] == "Gray"])
print(count1)
count2 = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(count2)
count3 = len(data[data["Primary Fur Color"] == "Black"])
print(count3)
print(data["Primary Fur Color"])


data_dict = {
    "Fur Color": [ "Gray" ,"Cinnamon","Black"],
    "Count":[count1,count2,count3]
}
pan=pandas.DataFrame(data_dict)
pan.to_csv("squirrel_count.csv")