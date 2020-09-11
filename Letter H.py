c = 'H'
# top cone
for row in range(3):
    for col in range(5):
        if row == 2 or ((row == 1) and (0 < col < 4)) or ((row == 0) and (1 < col < 3)):
            print(c, end="")

        else:
            print(end=" ")
    print()

# body
for row in range(10):
    for col in range(18):
        if (row < 10 and col <= 4) or (2 < row < 6 and 4 < col < 13) or (row < 10 and col > 12):

            print(c, end="")

        else:
            print(end=" ")

    print()
# bottom cone
for row in range(3):
    for col in range(18):
        if((row == 2) and (14 < col < 16) or (row == 1) and (13 < col < 17)) or ((row == 0) and (12 < col < 18)):
            print(c, end="")

        else:
            print(end=" ")
    print()
