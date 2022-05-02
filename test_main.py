from main import Student, Tutor

def test_student():
    s = Student("Bob", "Smith")
    assert s.first_name == "Bob"
    assert s.last_name == "Smith"

def test_get_name_and_email():
    s = Student("test-student", "test-email")
    assert s.get_name_and_email() == "test-email"

def test_get_github_username():
    s = Student("test-student", "test-email")
    assert s.get_github_username() == "test-student"

def test_change_email():
    s = Student("test-student", "test-email")
    s.change_email("new-email")
    assert s.get_name_and_email() == "new-email"

def test_is_active_student():
    s = Student("test-student", "test-email")
    assert s.is_active_student() == True

def test_get_tutor():
    s = Student("test-student", "test-email")
    assert s.get_tutor() == None

def test_get_tutor_email():
    s = Tutor("test-tutor", "test-email")
    assert s.get_name_and_email() == "test-email"

def test_get_github_username():
    s = Tutor("test-student", "test-email")
    assert s.get_github_username() == "test-student"

def test_change_email():
    s = Tutor("test-student", "test-email")
    s.change_email("new-email")
    assert s.get_name_and_email() == "new-email"

def test_assign_student():
    s = Tutor("test-student", "test-email")
    s.assign_student(t)
    assert s.get_tutor() == t

def test_get_tutor_email():
    s = Student("test-student", "test-email")
    assert s.get_tutor_email() == "No tutor assigned"