local function myGreatFunction()
    local result = nil

    if result == nil then
        local result1 = true
        print(result1)
    else
        local result2 = false
        print(result2)
        -- print(result1) / Would give an error because it can only be accessed in the codeblock it was created
    end
end

myGreatFunction()

-- print(mySecondVariable) / Would give an error because the variable is defined after
local mySecondVariable = "Random thing"