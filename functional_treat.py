
def input_data():
    """
    create 1D list and 2D list
    """
    global data
    global matrix
    data = []
    matrix = []

    while True:
        print("\n1.Add 1D list\n2.Add 2D list\n0.Exit\n")

        c = int(input("Enter your choice:"))
        if c == 1:
            data = list(int(i) for i in input("Enter 1D array (sperated by comma)").split(","))
            print("\n1D list creat Successfully........\n")

        elif c == 2:
            rows = int(input("Enter number of row:"))
            col = int(input("Enter number of Column:"))
            for i in range(rows):
                row =[]
                for j in range(col):
                    val = int(input(f"Enter element[{i+1}][{j+1}] : "))
                    row.append(val)
                matrix.append(row)
            print("\n2D list creat Successfully........\n")
        elif c == 0:
            break
        else:
            print("\nplease enter currect input(1 and 2)....\n")


def display_summary():
    """
    Display  Display Data Summary using Built-in Functions
    """
    while True:
        print("\n1.Print Data Summary (using built-in function)\n2.Print 2D List\n0.Exit\n")
        c = int(input("Enter your choice(1 and 2):"))
        if c == 1:

            print("Total element :",len(data))
            print("Maximun element :",max(data))
            print("minimum element :",min(data))
            print("Sum of all element:",sum(data))
            average = sum(data)/len(data)
            print("Average value :",average)

        elif c == 2:

            print("\n2D list display in Grid structure....")

            if not matrix:
                print("2D List Not Found")
            for i in matrix:
                print(i)
        elif c == 0:
            break
        else:
            print("\nplease enter currect input..(1 and 2).....\n")

    
def fact(n):
    """
    calculate the factorial of given number using recursion.
    """
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)
    
def filter_data(n):
    """
    Filters elements greather than or equal to n from the data list.
    """
    f =filter( lambda x : x >= n, data)
    l1 = list(f)
    print(l1)

def sort_data():
    """
    sort 1D list using sort() and 
    sort 2D list using sorted()
    """
    
    while True:
        print("\n1.Sort 1D list\n2.Sort 2D list\n0.Exit\n")
        c = int(input("Enter your choice:"))

        if c == 1:
            while True:
                print("\n1.Ascending\n2.Descending\n0.Exit\n")
                ch = int(input("Enter your choice"))
                if ch == 1:
                    data.sort()
                    print("\nSort 1D list in Ascending :",data)

                elif ch == 2:
                    data.sort(reverse=True)
                    print("\nSort 1D list in Descending :",data)
                elif ch == 0:
                    break
                else:
                    print("\nPlease Enter Currect Input(1 and 2)........\n")
        elif c == 2:
            while True:
                print("\n1.Ascending\n2.Descending\n0.Exit\n")
                ch = int(input("Enter your choice"))

                if ch == 1:
                    asc_order = sorted(matrix)

                    print("\nAscending order...")
                    for i in asc_order:
                        print(i)

                elif ch == 2:
                    desc_order = sorted(matrix,reverse=True)

                    print("\nDescending Order...")
                    for i in desc_order:
                        print(i)
                elif ch == 0:
                    break
                else:
                    print("\nplease Enter Currect Input(1 and 2)..........\n")
        elif c == 0:
            break
        else:
            print("Please Enter Currect Input(1 and 2)...")
        

def dataset():
    """
    return the multiple values
    """
    return min(data),max(data),sum(data),sum(data)/len(data)

def show_data(*args):
    """
    diplay data using *args
    """
    print("values ",args)

def show_data_summary(**kwargs):
    """
    Display data using **kwargs
    """
    
    for key , value in kwargs.items():
        print(f"{key}:{value}")

while True:
    print("\n1. Input Data")
    print("2. Display Data Summary (Built-in Functions) and 2D List")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program\n")

    choice = int(input("Enter Your choice:"))

    if choice == 1:
        print(input_data.__doc__)
        input_data()

    elif choice == 2:
        print(display_summary.__doc__)
        display_summary()

    elif choice == 3:
        print(fact.__doc__)
        num = int(input("Enter number:"))
        f = fact(num)
        print(f" factorial of {num} is {f}")


    elif choice == 4:
        print(filter_data.__doc__)
        num = int(input("Enter number:"))
        print(f"Filtered Data (value >={num})")
        filter_data(num)


    elif choice == 5:
        print(sort_data.__doc__)
        sort_data()

    elif choice == 6:
        print(dataset.__doc__)
        if not data:
            print("data not found")
        s = dataset()
        print(show_data.__doc__)
        show_data(s)
        print(show_data_summary.__doc__)
        show_data_summary(Minimum=s[0],Maximun=s[1],Sum=s[2],Aveage=s[3])

    elif choice == 7:
        break
    else:
        print("invalid choice")
