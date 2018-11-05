solution = "SSNWES"
moves = 0
lives = 3
amountsolved = 0

print("Welcome to the magic maze game!")

while True:

    for letter in solution:
        direction = input("Enter one of the following directions: N,  W, S,  E ")
        moves += 1
        if moves % 10 == 0:
            lives-=1
            print("you lost a life, you have", lives, "life left")
        if direction != letter:
            print("Incorrect direction")
            amountsolved = 0
            break

        amountsolved += 1

    if amountsolved == 6:
        print("Congratulations you escaped the magic maze")
        break

    if lives == 0:
        print("GAME OVER")
        break

