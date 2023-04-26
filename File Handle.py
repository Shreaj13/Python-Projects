def main():
    infile = open('names.txt')
    count = 0
    for lines in infile:
        lines = lines.rstrip()
        count = count + 1
        print(lines)
    print('Line number is',count)




main()
