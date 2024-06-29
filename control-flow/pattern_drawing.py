# Drawing Patterns with Nested Loops

pattern_size = int(input('Enter the size of the pattern: '))
count = 0
while (count < pattern_size):
    for i in range(1, pattern_size + 1):
        print("*", end="")
    print('')
    count += 1
