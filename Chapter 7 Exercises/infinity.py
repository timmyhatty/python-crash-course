# 7-7: Infinite Loop

# This program purposely creates an infinite loop

x = 0
while x < 5:
    print(x)
    # To stop this infinite loop, add a statement to make sure x eventually becomes greater than 5
    # Like: x += 1