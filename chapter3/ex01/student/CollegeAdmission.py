# Task 1: Input statements
test_score = input("Enter student's test score: ")
class_rank = input("Enter student's class rank: ")

# Task 2: Convert input to integers
test_score = int(test_score)
class_rank = int(class_rank)

# Decision making based on test score and class rank
if test_score >= 90:
    if class_rank >= 25:
        print("Accept")
    else:
        print("Reject")
elif test_score >= 80:
    if class_rank >= 50:
        print("Accept")
    else:
        print("Reject")
elif test_score >= 70:
    if class_rank >= 75:
        print("Accept")
    else:
        print("Reject")
else:
    print("Reject")
