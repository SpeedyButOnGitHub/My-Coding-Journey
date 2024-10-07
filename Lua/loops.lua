local number = 1

for i = 1, 5, 1 do
    print(number)
    number = number + 1
end

local number2 = 6

while number2 < 11 do
    print(number2)
    number2 = number2 + 1
end

for i = 1, 5, 1 do
    print("A")

    for x = 1, 5, 1 do
        print("B")
    end
end

for i = 1, 100000 do
    print("meow")
    if i == 50 then
        print("No more meowing")
        break
    end
end
