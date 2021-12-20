# Define the Student class
class Student():
  
    # Initialize the object properties
    def __init__(self, ID, name, mark):
        # TODO: initialize the Student class object
        self.ID = ID
        self.name = name
        self.mark = mark
        

    # Print the object as an string
    def __str__(self):
        return ' - {}, {}, {}'.format(self.ID, self.name, self.mark)


    # Check if the mark of the input student is greater than the student object
    # The output is either True or False
    def is_greater_than(self, another_student):
	# TODO: compare every two Student objects based on their marks
        return self.mark > another_student.mark
	

# Sort the student_list
# The output is the sorted list of students
def sort_students(student_list):
    # TODO: sort the student list with ascending order
    for index in range(len(student_list)):
        small_index = index
	# finding the index of smallest element
        for i in range(index, len(student_list)):
            if student_list[index].is_greater_than(student_list[i]):
                small_index = i
	# swapping
        temp = student_list[index] 
        student_list[index] = student_list[small_index]
        student_list[small_index] = temp
    return student_list

	
if  __name__== "__main__":
    # Read the data
    students_file = open('student_list.txt', 'rt')
    students_data = students_file.readlines()
    student_list = []
    for student in students_data:
	
	# Create a student object
        fields = student.split(', ')
        ID = fields[0]
        name = fields[1]
        mark = fields[2]
        student_list.append(Student(ID, name, int(mark)))

	# Print the original data
        print('Original data:')
        for student in student_list:
            print(student)

	# Sort the students
        sorted_students = sort_students(student_list)

	# Print the sorted data
        print('Sorted data:')
        for student in sorted_students:
            print(student)
	