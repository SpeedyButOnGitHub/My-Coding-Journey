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

local myArray = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

for i = 1, #myArray do
    if myArray[i] == 5 then
        print("5 has been found.")
    end
end