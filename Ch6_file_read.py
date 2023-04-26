# This program reads and displays the contents
# of the philosophers.txt file.
def main():
    # Open a file named .txt.
    infile = open('text.txt', 'r')

    # Read the file's contents.
    file_contents = infile.read()
    #x = infile.read()


    # Close the file.
    infile.close()

    # Print the data that was read into
    # memory.
    print(file_contents)

# Call the main function.
main()
