# This program append three lines of data
# to a file.
def main():
    # Open a file named philosophers.txt.
    outfile = open('members.txt', 'a')

    # Write the names of three philosphers
    # to the file.
    outfile.write('Susan \n')
    outfile.write('Jeson \n')
    outfile.write('Sung \n')

    # Close the file.
    outfile.close()

# Call the main function.
main()
