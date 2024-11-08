# ask user for a number and loop until they input a number more than zero
def num_check(question):
    error = "please enter a number that is more than zero\n"
    while True:

        try:
            response = float(input(question))

            if response > 0:
                return response
            else:
                print(error)
        except ValueError:
            print(error)


# main routine goes here
for item in range(0, 2):
    width = num_check("width: ")
    print(width)

for item in range(0, 2):
    height = num_check("height: ")
    print(height)
