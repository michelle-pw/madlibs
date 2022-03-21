# A description of this project is in the readme.md file that I created
# users will be asked to enter the following as inputs. The inputs are then stored into the following variables:

adj1 = input("Adjective 1:")
adj2 = input("Adjective 2:")
adj3 = input("Adjective 3:")
adj4 = input("Adjective 4:")
noun1 = input("Noun 1:")
noun2 = input("Noun 2:")

# the inputs are then placed into the corresponding blanks.
madlib = f"Seattle is so {adj1}. Though the weather is {adj2} most of the time, it brings out the {adj3} of the city. \n\
There are many {adj4} bars and restaurants that accentuates the night life of this {adj1} city. \n\
It is also a major {noun1} hub with many {noun2}!"

# The madlib is printed for the user using the following command:
print(madlib)

# During my first attempt of running this script, Python closed before printing the madlib. I added this command
# to keep Python open:
input()
