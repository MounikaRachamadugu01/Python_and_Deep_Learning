lbs_list = []
noOfStudents = int(input("Enter the number of students : "))
for i in range(noOfStudents):
    lbs = int(input("Enter the weight in lbs:"))
    lbs_list.append(lbs)

def lbsToKgs(lbs_list):
    kgs_list = []
    for i in lbs_list:
        kgs = round(i*0.454, 2)
        kgs_list.append(kgs)
    print("List of Weight in lbs", lbs_list)
    print("Corresponding List of Weight in Kilograms", kgs_list)

lbsToKgs(lbs_list)