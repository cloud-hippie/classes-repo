# Classes

Classes in Python are a way to group together variables and functions. They are also known as modules.

## When to use classes?

Let's think about the following scenario: you want to build an app to help schools manage their students. You want to keep track of students' names, ages, and grades. You want to be able to add new students, remove students, and update students' grades.

To organzie our data, we can create a student class that will help us group together all of the data we need.

```python
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
```
In the above example:
    * `self` is a reference to the current instance of the class.
    * `name` is a variable that stores the student's name.
    * `age` is a variable that stores the student's age.
    * `grade` is a variable that stores the student's grade.

Every student in our app will be an instance of the `Student` class.

We want to be able to have a visual on our app that shows the students' names, ages, and grades.

We can create getter methods to access the data.

```python
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_grade(self):
        return self.grade
```

These are also called accessor methods. They allow us to access the data in our class. They are useful for when we want to display the data in a way that is easy to read.

It's also a great way to get facts about our data, in this case, our Students.

We know we want our app to be able to show if a student is passing or failing. This functionality will be used in a lot of places in our app. It would be much easier to have a method that returns a boolean value. We can create a method to check if a student is passing or failing.

```python
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_grade(self):
        return self.grade
    
    def is_passing(self):
        if self.grade >= 70:
            return True
        else:
            return False
```

Now, Developers can use this method to check if a student is passing or failing rather than writing the if statement in the code every time they need to check if a student is passing or failing.

## Setter methods

We want to be able to add grades to our students. We can create a setter method to add grades to our students.

```python
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_name(self):
        return self.name
    
    def get_grade(self):
        return self.grade
    
    def is_passing(self):
        if self.grade >= 70:
            return True
        else:
            return False
    
    def set_grade(self, grade):
        self.grade = grade
```

Now, the grade can be set by the developer. This is useful for when we want to update a student's grade.

## __init__.py

The `__init__.py` file is a special Python file that is used to initialize the class. It is used to define the class and to define the variables and methods that are part of the class. We use the same method when we create our classes.

They allow you to create a namespace for your code. This namespace is a dictionary that contains all the variables and functions you want to use in your code.


## Inheritance

Another power of classes is inheritance.

Let's take the student application example. We have students in our application, but each of these students needs a teacher and a class to teach. We can create a teacher class and a class class.

```python
class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
    
    def get_name(self):
        return self.name
    
    def get_subject(self):
        return self.subject
class Class:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
```

Each student has a teacher and a class. We can create a student class that inherits from the teacher and class classes.

```python
class Student(Teacher, Class):
    def __init__(self, name, age, grade, teacher, class_name):
        Teacher.__init__(self, teacher.name, teacher.subject)
        Class.__init__(self, class_name)
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_grade(self):
        return self.grade
    
    def is_passing(self):
        if self.grade >= 70:
            return True
        else:
            return False
    
    def set_grade(self, grade):
        self.grade = grade
```

So now, when we create a student, we can pass in a teacher and a class. We can also access the teacher's name and subject. We can also access the class's name.

```python
student = Student("John", 15, 80, Teacher("Mrs. Smith", "Math"), "1st Grade")
```


## Assignment

Let's build this app and help schools manage their students!

Create a class called Student that has the following attributes: `name`, `email`, `github`, `cohort`, `start_date`, and `current_project`.

The constructor should accept all of these parameters as arguments, and assign each one to the appropriate attribute.

The Student class should have the following methods:
- `get_name_and_email()` - returns a string containing the student's full name and email address
- `get_github_username()` - returns a string containing just the student's github username
- `change_email(new_address)` - change the student's email address to the new address
- `is_active_student()` - returns True if the student start_date is less than 60 datys from now.
- `get_tutor()` - returns the student's current tutor. If the student is not assigned, return None.

Create a class called Tutor that has the following attributes: `name`, `email`, `github`, `calendar_link`, `students` and `current_project`.
 

The constructor should accept all of these parameters as arguments, and assign each one to the appropriate attribute.

The Tutor class should have the following methods:
- `get_name_and_email()` - returns a string containing the tutor's full nameand email address
- `get_github_username()` - returns a string containing just the tutor's Github username
- `change_email(new_address)` - change the tutor's email address to the new address
- `assign_student(student)` - assign the given student to the tutors `students` list.

Add a method to to the Student class called get_tutor_email that returns the email address of the student's tutor. If they do not have a tutor assigned, it should return "No tutor assigned".

## Bonus: Refactor the two classes above into a single class called User.

The User class should have the following attributes: `name`, `email`, `github`, `cohort`, `start_date`, `current_project`, `tutor`, and `class`.