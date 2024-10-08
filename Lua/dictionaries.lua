local menu = {
    ["Cheeseburger"] = 6,
    ["Coca cola"] = 2,
    ["French fries"] = 2,
    ["Chicken nuggets"] = 2,
}

menu["Cheeseburger"] = 5

print("$"..menu["Cheeseburger"])

local menu2 = {
    Cheeseburger = 6,
    Coca_Cola = 2
}

print("$"..menu2.Cheeseburger)

for menuItem, price in pairs(menu) do
    print(menuItem..": ".. "$"..price)
end