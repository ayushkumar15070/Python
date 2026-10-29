car = {
    "Brand" : "Ford",
    "Model" : "Mustang",
    "Year" : 2015
}

car["Model"] = "Endavour"
print(car)

car.update({"Year" : 2001})
print(car)

car["Color"] = "Blue"
print(car)

newcar = {

}

name = input("Enter the car name: ") 
model = input("Enter the model name: ")
year = int(input("Enter the year of the car: "))
color = input("Enter the color of the car: ")
brand = input("Enter your brand title: ")

newcar.update(
   {
      brand : name, 
      "Model": model, 
      "year" : year, 
      "color": color
    }
)
print(newcar)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict.pop("model")
print(thisdict)

thisdict.popitem()
print(thisdict)

del thisdict["brand"]
print(thisdict)



newdictionary = {
    "Actor": "Robert Downey Jr.",
    "Cricketer": "Virat Kohli",
    "Footballer": "Christiano Ronaldo"
}

for i in newdictionary:
    print(newdictionary[i])

for i in newdictionary.values():
    print(i)

for i in newdictionary.keys():
    print(i)

another = newdictionary.copy()
print(another)

anotherone = dict(newdictionary)
print(anotherone)

Cars = {
   "Car1" : {
       "Brand" : "BMW",
       "Model" : "M8"
   },
   "Car2" : {
       "Brand" : "Mercedes",
       "Model" : "Benz"
   },
   "Car3" : {
       "Brand" : "TATA",
       "Model" : "Harrier"
   }
}


print(Cars["Car1"]["Brand"])
print(Cars["Car1"], Cars["Car2"], Cars["Car3"])

for x, obj in Cars.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])