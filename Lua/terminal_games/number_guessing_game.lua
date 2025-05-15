math.randomseed(os.time() + math.floor(os.clock() * 1000))
math.random(); math.random(); math.random()

print("Number Guessing Game!")
print(("*"):rep(21))

local n = math.random(1, 100)
local tries = 0

while true do
    io.write("Guess a number between 1 and 100: ")
    local line = io.read()

    local guess = tonumber(line)

    if guess == nil then
        print("Please enter a valid number.")
    elseif guess < n then
        print("Too low! Try again.\n")
        tries = tries + 1
    elseif guess > n then
        print("Too high! Try again.\n")
        tries = tries + 1
    else
        print("\nCongratulations! You guessed the number!")
        print("It took you " .. tries .. " tries.")
        break
    end
end
