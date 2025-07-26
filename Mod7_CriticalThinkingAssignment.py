# Course Number dictionary
course_info = {'CSC101': [3004, 'Haynes', '8:00 a.m.'], 
               'CSC102': [4501, 'Alvarado', '9:00 a.m.'], 
               'CSC103': [6755, 'Rich', '10:00 a.m.'], 
               'NET110': [1244, 'Burke', '11:00 a.m.'],
               'COM241': [1411, 'Lee', '1:00 p.m.']
}

# Defining the function for accessing the dictionary
def course_information(course):
    try:
        print("Room number, instructor, and meeting time:")
        print(f'{course}:', course_info[course_name])
        return course_info[course_name]
    
    # Most likely error is typing in a class that is not in the dictionary resulting in a KeyError
    except KeyError:
        print(f"Not Applicable: {course} is not a valid course number.")
        return

# Allowing the user to input the course name
course_name = input('Input the name of the course: ')

# Initiate the function
course_information(course_name)


