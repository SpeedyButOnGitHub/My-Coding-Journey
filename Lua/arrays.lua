local myArray = {10, 20, 30}

for i = 1, #myArray do
    print(myArray[i])
end

table.insert(myArray, 40)

for i = 1, #myArray do
    print(myArray[i])
end

table.remove(myArray, 4)

for i = 1, #myArray do
    print(myArray[i])
end