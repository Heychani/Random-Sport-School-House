import random

student1 = input("Please enter first student: ")
student2 = input("Please enter second student: ")
student3 = input("Please enter third student: ")

sports_house = ['blue', 'red', 'white']

student1_house = sports_house[random.randint(0, 2)]
student2_house = sports_house[random.randint(0, 2)]
student3_house = sports_house[random.randint(0, 2)]

print("SCHOOL HOUSE ASSIGNMENT")
print("***************************")
print(f"{student1}", f"Assigned to the {student1_house} house with student number {student1_house}{random.randint(1000, 9000)}")
print(f"{student2}", f"Assigned to the {student2_house} house with student number {student2_house}{random.randint(1000, 9000)}")
print(f"{student3}", f"Assigned to the {student3_house} house with student number {student3_house}{random.randint(1000, 9000)}")