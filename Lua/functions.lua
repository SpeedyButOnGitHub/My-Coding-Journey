local function addition(number1, number2)
    local result = number1 + number2
    return result
end

local function multiplication(number1, number2)
    local result = number1 * number2
    return result
end

local function subtraction(number1, number2)
    local result = number1 - number2
    return result
end

local function division(number1, number2)
    local result = number1 /  number2
    return result 
end

local additionresult = addition(3, 5)
local multiresult = multiplication(7, 8)
local subtresult = subtraction(7, 9)
local divresult = division(5, 7)

print("Addition result: "..additionresult)
print("Multiplication result: "..multiresult)
print("Subtraction result: "..subtresult)
print("Dividation result: "..divresult)

