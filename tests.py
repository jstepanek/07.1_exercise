#Jack Stepanek, 3/19/22

import pytest
import System

# login - System.py
# Pass Number 1
def test_login(grading_system):
    name = 'calyam'
    password = '#yeet'
    grading_system.login(name, password)
    assert grading_system.usr.name == name
    assert grading_system.usr.password == password
    
#2. check_password - System.py
# Pass Number 2
def test_check_password(grading_system):
    name = 'calyam'
    password = '#yeet'
    assert grading_system.check_password(name, password) == True

#3. change_grade - Staff.py
# Fail Number 1 - TypeError in Staff.py for change_grade func
# Additionally, it sets it to zero as opposed to inputted grade
def test_change_grade(grading_system):
    name = 'saab'
    password = 'boomr345'
    grading_system.login(name, password)
    username = 'akend3'
    course = 'comp_sci'
    assignment = 'assignment1'
    grade = 98 
    grading_system.usr.change_grade(name, course, assignment, grade)
    assert grading_system.users[username]['courses'][course][assignment]['grade'] == grade

#4. create_assignment - Staff.py
#Pass Number Three
def test_create_assignment(grading_system):
    name = 'goggins'
    password = 'augurrox'
    grading_system.login(name, password)
    course = 'databases'
    assignment = 'final_exam'
    due_date = '12/31/99'
    #need to get total num of assignments BEFORE insertion to verify the change occured
    num_assignments = len(grading_system.courses[course]['assignments'])
    grading_system.usr.create_assignment(assignment, due_date, course)
    assert len(grading_system.courses[course]['assignments']) == num_assignments + 1

#5. add_student - Professor.py
#   Fail Number Two - Another TypeError in System.py, this time for add_student func
def test_add_student(grading_system):
    name = 'goggins'
    password = 'augurrox'
    username = 'akend3'
    course = 'databases'    
    grading_system.login(name, password)
    total_courses  = len(grading_system.users[username]['courses'])
    grading_system.usr.add_student(username, course)    
    assert len(grading_system.users[username]['courses']) == total_courses + 1

#6. drop_student - Professor.py
#   Pass Number Four
def test_drop_student(grading_system):
    name = 'goggins'
    password = 'augurrox'
    username = 'akend3'
    course = 'databases'
    grading_system.login(name, password)
    total_courses = len(grading_system.users[username]['courses'])
    grading_system.usr.drop_student(username, course)
    assert len(grading_system.users[username]['courses']) == total_courses - 1

#7. submit_assignent - Student.py
#   Pass Number Five
def test_submit_assignment(grading_system):
    username = 'akend3'
    password = '123454321'
    course = 'comp_sci'
    assignment = 'assignment1'
    submission = 'blah blah blah'
    submission_date = '2/01/20'
    grading_system.login(username, password)
    grading_system.usr.submit_assignment(course, assignment, submission, submission_date)
    assert grading_system.users[username]['courses'][course][assignment]['submission'] == submission
    assert grading_system.users[username]['courses'][course][assignment]['ontime'] == True
    assert grading_system.users[username]['courses'][course][assignment]['submission_date'] == submission_date

#8. check_ontime - Student.py
#   Fail Number Three
#   The check_ontime function in Student.py only returns True
#   Therefore, even though the given input should fail, it returns True
#   This proves that this test results in a Fail
def test_check_ontime(grading_system):
    username = 'akend3'
    password = '123454321'
    submission_date = '2/01/99'
    due_date = '2/01/20'
    grading_system.login(username, password)
    assert grading_system.usr.check_ontime(submission_date, due_date) == False

#9. check_grades - Student.py
#   Fail Number Four
#   This test yields a KeyError function from check_grades in Student.py
def test_check_grades(grading_system):
    username = 'hdjsr7'
    password = 'pass1234'
    course = 'cloud_computing'
    grading_system.login(username, password)
    assert grading_system.usr.check_grades(course) == [['assignment1', 100], ['assignment2', 100]]

#10. view_assignments - Student.py
#    Fail Number Five
#    In view_assignments from Student.py, its hardcoded to retrieve info about 'comp_sci'
#    Since this asks for info about cloud_computing and receives comp_sci info, it results in a test failure
def test_view_assignments(grading_system):
    username = 'hdjsr7'
    password = 'pass1234'
    course = 'cloud_computing'
    grading_system.login(username, password)
    assert grading_system.usr.view_assignments(course) == [['assignment1', '1/3/20'], ['assignment2', '2/3/20']]


#11. invalid_assignment - Staff.py
#    Fail Number Six
#    This attempts to create an assignment which already exists
#    The assertion checks for an increase in assignments, and since no new assignment was created, it returns an AssertionError
def test_invalid_assignment(grading_system):
    name = 'goggins'
    password = 'augurrox'
    course = 'databases'
    assignment = 'assignment1'
    due_date = '5/13/22'
    grading_system.login(name, password)
    total_assignments = len(grading_system.courses[course]['assignments'])
    grading_system.usr.create_assignment(assignment, due_date, course)
    assert len(grading_system.courses[course]['assignments']) == total_assignments + 1

#12. invalid_drop_student - Staff.py
#    Fail Number Seven
#    This attempts to drop a student from a class they're not enrolled in
#    This returns a KeyError from drop_student in Staff.py
def test_invalid_drop_student(grading_system):
    name = 'goggins'
    password = 'augurrox'
    username = 'akend3'
    course = 'cloud_computing'
    grading_system.login(name, password)
    enrolled_courses = len(grading_system.users[username]['courses'])
    grading_system.usr.drop_student(username, course)
    assert len(grading_system.users[username]['courses']) == enrolled_courses - 1

#13. invalid_course_check - Student.py
#    Fail Number Eight
#    This attempts to check grades for a course which doesn't exist
#    This results in a KeyError as 'algorithms' doesn't exist
def test_invalid_course_check(grading_system):
    name = 'akend3'
    password = '123454321'
    course = 'algorithms'
    grading_system.login(name, password)
    assert grading_system.usr.check_grades(course) == [['assignment1', 100], ['assignment2', 100]]

#14. invalid_student_check - Student.py
#    Fail Number Nine
#    This attempts to check grades for a student which doesn't exist
#    This results in a KeyError as 'test_user' doesn't exist
def test_invalid_student_check(grading_system):
    name = 'test_user'
    password = 'test_pass'
    course = 'databases'
    grading_system.login(name, password)
    assert grading_system.usr.check_grades(course) == [['assignment1', 100], ['assignment2', 100]]

#15. invalid_prof_grade_check - Staff.py
#    Fail Number Ten
#    This attempts for a professor to check grades in an invalid class
#    This results in an error as the course being accessed doesn't exist
def test_invalid_prof_grade_check(grading_system):
    name = 'goggins'
    password = 'augurrox'
    username = 'akend3'
    course = 'test_course'
    grading_system.login(name, password)
    assert grading_system.usr.check_grades(course) == [['assignment1', 100], ['assignment2', 100]]

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
