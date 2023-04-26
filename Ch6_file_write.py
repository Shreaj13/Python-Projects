# This program writes three lines of data
# to a file.
def main():
    # Open a file named 
    outfile = open('friends.txt', 'w')

    # Write the names of three philosphers
    # to the file.
    outfile.write('Susan \n')
    outfile.write('Mary \n')
    outfile.write('Dang \n')
    

    # Close the file.
    outfile.close()

# Call the main function.
main()
