from random import shuffle

users = []
password = []
score = []
user_info = {}
u = open("users.txt", "r")
ui = open("userinfo", "r")
for line in u.readlines():
    data = line.split(" ")
    users.append(data[0])
    password.append(data[1])
    ud = ui.readline().split(",");
    score.append([ud[0], ud[1], ud[2]])
    user_info[data[0]] = [ud[3], ud[4], ud[5], ud[6]]
u.close()
ui.close()

q = open("questions.txt", "r")
o = open("options.txt", "r")
quesDSA = q.readline().split("*@")
    # "1. Which of the following data structures is used to implement a function call stack?\na) Queue\nb) Stack\nc) Linked List\nd) Tree",
    # "2. What is the time complexity of searching for an element in a balanced binary search tree (BST)?\na) O(1)\nb) O(log n)\nc) O(n)\nd) O(n^2)",
    # "3. In a singly linked list, how do you delete the last node?\na) Traverse the list to find the last node and remove it.\nb) Change the head pointer to the next node.\nc) Delete the last node by making the second last node's next pointer NULL.\nd) Simply delete the head node.",
    # "4. Which of the following sorting algorithms is considered the most efficient for large datasets when considering average time complexity?\na) Bubble Sort\nb) Quick Sort\nc) Insertion Sort\nd) Selection Sort",
    # "5. What is the space complexity of the Merge Sort algorithm?\na) O(1)\nb) O(n)\nc) O(log n)\nd) O(n log n)"
    

quesDBMS = q.readline().split("*@")
# "1. Which of the following is a property of the ACID test in database transactions?\na) Atomicity, Consistency, Isolation, Durability\nb) Accuracy, Consistency, Isolation, Durability\nc) Atomicity, Consistency, Integrity, Durability\nd) Atomicity, Clarity, Isolation, Durability",
#             "2. In a relational database, what is the purpose of a primary key?\na) To uniquely identify a record in a table\nb) To establish a foreign key relationship with another table\nc) To speed up query processing\nd) To store large binary data",
#             "3. Which of the following SQL statements is used to remove a table from a database?\na) DELETE\nb) DROP\nc) REMOVE\nd) TRUNCATE",
#             "4. What is the normalization process used for in a relational database?\na) To remove redundancy and improve data integrity\nb) To increase the performance of the database\nc) To encrypt the data for security\nd) To speed up data retrieval times",
#             "5. Which of the following is true about a 'foreign key' in a relational database?\na) It uniquely identifies records within its own table\nb) It establishes a link between two tables based on a common attribute\nc) It can have duplicate values within a table\nd) It must always be indexed for better performance"

quesPy = q.readline().split("*@")
    # "1. Which of the following is the correct way to declare a variable in Python?\na) int x = 10\nb) x = 10\nc) int x := 10\nd) declare x = 10",
    # "2. Which of the following data types is mutable in Python?\nA) tuple\nB) int\nC) str\nD) list",
    # "3. What will be the output of the following code?\n\nprint(type(5.0))\n\nA) <class 'int'>\nB) <class 'float'>\nC) <class 'str'>\nD) <class 'double'>",
    # "4. What does the following code snippet return?\n\nbool('False')\n\nA) True\nB) False\nC) None\nD) Error",
    # "5. Which of the following methods can be used to add an item to a list in Python?\nA) append()\nB) add()\nC) push()\nD) insert_last()"


ansDSA = {
    # 1: "b",
    # 2: "b",
    # 3: "c",
    # 4: "b",
    # 5: "b"
}
i = 1
for op in o.readline().split(" "):
    ansDSA[i] = op
    i += 1
ansDBMS = {
    # 1: "a",
    # 2: "a",
    # 3: "b",
    # 4: "a",
    # 5: "b"
}
i = 1
for op in o.readline().split(" "):
    ansDBMS[i] = op
    i += 1
ansPy = {
    # 1: "b",
    # 2: "d",
    # 3: "b",
    # 4: "a",
    # 5: "a"
}
i = 1
for op in o.readline().split(" "):
    ansPy[i] = op
    i += 1

def usernameValidate(string):
    for ch in string:
        if not (ch.isalnum() or ch == '_'):
            return False
    return True

def passwordValidate(string):
    for ch in string:
        if not(ch.isalnum() or ch in "@#$*_"):
            return False
    return True


def register():
    global users, password
    print("""
Rules for correct username and password ->
1) Your username and password must not contain any blank spaces, leading spaces and trailing spaces.
2) Your username and password must not exceed the limit of 20 characters.
3) Only small alphabets, capital alphabets, digits and _ are allowed characters in username.
4) Only small alphabets, capital alphabets, digits, @, #, $, *, _ are allowed characters in password.
A correct username would look like these: User_name123, userName99, 0_u1s23name80
A correct password would look like these: Ppass1$wor@d, pAssWord#9, 0_@1s23word$0

""")
    while True:
        username = input("Enter your username: ")
        
        if username == "-1":
            return False

        if len(username) > 20:
            print("Username is exceeding the limit of 20 characters. Pleaase try a shorter username.")
            continue

        isValid = usernameValidate(username)
        if not isValid:
            print("Invalid username, please try again.")
        else:
            if username in users:
                print("Username already exists. Please try another username.")
            else:
                while True:
                    pwd = input("Enter your password: ")
                    if pwd == "-1":
                        break

                    if len(pwd) > 20:
                        print("Password is exceeding the limit of 20 characters. Please check your password and remove blank spaces if there are any.")
                        continue

                    isValid = passwordValidate(pwd)
                    if not isValid:
                        print("Password is invalid.")
                    else:
                        print("Fill all the necessary information")
                        
                        name = input("Enter Full Name: ")
                        age = int(input("Enter Age: "))
                        college = input("Enter College: ")
                        rollno = int(input("Enter Roll Number: "))

                        # info = [name, age, college, rollno]
                        # users.append(username)
                        # password.append(pwd)
                        # user_info[username] = info
                        # score.append([None, None, None])
                        with open("users.txt", "a") as u:
                            u.write(f"{username} {password}\n")
                        with open("usersinfo.txt", "a") as ui:
                            ui.write(f"None,None,None,{name},{age},{college},{rollno}\n")

                        print("You are registerd successfully.")
                        return True
    return False


def login():
    global users, password
    while True:
        username = input("Enter your username: ")
        
        if username == "-1":
            return ""

        if len(username) > 20:
            print("Username is exceeding the limit of 20 characters. Pleaase try a shorter username.")
            continue

        isValid = usernameValidate(username)
        if not isValid:
            print("Invalid username, please try again.")

        else:
            if username not in users:
                print("Username is incorrect. Please try again.")
                continue
            while True:
                pwd = input("Enter your password: ")
                if pwd == "-1":
                    break
                
                if (len(pwd) > 20):
                    print("Password is too long.")

                else:
                    index = users.index(username)
                    if pwd == password[index]:
                        print("Login Successful.")
                        return username
                    else:
                        print("Password is incorrect.")
    return ""




def quiz(ques, ans):
    userAns = []
    score = 0
    shuffle(ques)

    for i in range(0, len(ques)):
        print(str(i + 1) + ". " + ques[i][3:])
        while True:
            inp = input("Enter Answer: ").lower()
            if inp == "-1":
                return score
            if inp in "abcd":
                userAns.append(inp)
                break
            else:
                print("Enter valid input.")
    
    
    for qn in ans: 
        if ans[int(ques[qn - 1][0])] == userAns[qn - 1]:
            score += 1
    print("Quiz Completed.")
    print("Thank you for taking the quiz.")
    return score

def result(user):
    global users
    sc = score[users.index(user)]
    info = user_info[user]
    print("\n*** REPORT ***")
    print("Username:", user)
    print("Full Name:", info[0])
    print("Age:", info[1])
    print("College:", info[2])
    print("Roll Number:", info[3])
    print("\nQuiz\t\t\tDSA\t\tDBMS\t\tPython")
    print("Score\t\t\t", end="")
    print(sc[0], "\t\t", end="") if (sc[0] != None) else print("Not attempted", "\t", end="")
    print(sc[1], "\t\t", end="") if (sc[1] != None) else print("Not attempted", "\t", end="")
    print(sc[2], "\t\t", end="") if (sc[2] != None) else print("Not attempted")
    
    print("Percentage\t\t", end="")
    print(str(sc[0]*20) + "%", "\t\t", end="") if (sc[0] != None) else print("Not attempted", "\t", end="")
    print(str(sc[1]*20) + "%", "\t\t", end="") if (sc[1] != None) else print("Not attempted", "\t", end="")
    print(str(sc[2]*20) + "%", "\t\t", end="") if (sc[2] != None) else print("Not attempted")
    print()


if __name__ == "__main__":
    print("WELCOME TO QUIZ APPLICATION")
    print("PLEASE SELECT ONE OF THE FOLLOWING OPTIONS")
    print("** press -1 anytime to exit or go back **")
    print("Enter digit corresponding to you desired option")
    print("1. REGISTER\n2. LOGIN\n3. ATTEMPT QUIZ\n4. VIEW RESULT")

    current_user = ""
    while True:
        inp = input("Enter your option: ")
        if inp == "-1":
            break
        elif inp == "1":
            register()
        elif inp == "2":
            current_user = login()
        elif inp == "3":
            if current_user == "":
                print("You must login first in order to attempt quiz.")
                continue

            sc = score[users.index(current_user)]
            print("Select Quiz Topic")
            print("a. DSA\nb. DBMS\nc. Python")
            while True:
                inp = input("Enter quiz topic: ").lower()
                if inp == "a":
                    print("DSA Quiz")
                    sc[0] = quiz(quesDSA, ansDSA)
                    
                elif inp == "b":
                    print("DBMS Quiz")
                    sc[1] = quiz(quesDBMS, ansDBMS)
                    
                elif inp == "c":
                    print("Python Quiz")
                    sc[2] = quiz(quesPy, ansPy)
                
                if inp in ("a", "b", "c", "-1"):
                    index = users.index(current_user)
                    with open("userinfo.txt", "r+") as ui:
                        dat = ui.readlines()
                        lin = dat[index].split(",")
                        lin[0] = sc[0]
                        lin[1] = sc[1]
                        lin[2] = sc[2]
                        dat[index] = ",".join(lin)
                        ui.writelines(dat)
                    break                
                else:
                    print("Invalid input!")
        elif inp == "4":
            if current_user == "":
                print("You must login first in order to view result.")
                continue
            result(current_user)
