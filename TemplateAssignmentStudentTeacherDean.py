from abc import ABC, abstractmethod



#abstract class
class Person(ABC):

# This is the template method.
# The template method defines the skeleton of an algorithm.
  def weekdays(self, id):
    self.id = id
    self.start_day()
    self.zoom_event()
    self.eat_lunch()
    self.check_email()
    self.main_task()
    self.do_hobby()
    self.end_day()
# One of the methods from template
  def start_day(self):
    print(f'{self.id}: Starting the day!')
# One of the methods from template
  def end_day(self):
    print(f'Finally done with the day!\n')
# One of the methods from template
  @abstractmethod
  def zoom_event(self):
    pass
# One of the methods from template
  @abstractmethod
  def eat_lunch(self):
    pass
# One of the methods from template
  @abstractmethod
  def check_email(self):
    print("Looking my email from my laptop")
# One of the methods from template
  @abstractmethod
  def main_task(self):
    pass
# One of the methods from template
  @abstractmethod
  def do_hobby(self):
    pass
# We have 3 different classes  with one person template, each of our classes use same methods with different outputs.
# This is the one of our classes who use our template


#concrete class
class Teacher(Person):
# One of the abstractmethods from template but with different output
  def zoom_event(self):
    print(f'Starting the zoom lecture and taking attendance.')
# One of the abstractmethods from template but with different output
  def eat_lunch(self):
    print(f'Eating home-made vegetables.')
# One of the abstractmethods from template but with different output
  def check_email(self):
     print(f'Sending notifications to students about the assignment.')
# One of the abstractmethods from template but with different output
  def main_task(self):
    print(f'Assigning homework to the students.')
# One of the abstractmethods from template but with different output
  def do_hobby(self):
    print(f'Reading a novel.')


# This is the one of our classes who use our  Person template
#concrete class
class Student(Person):
# One of the abstractmethods from template but with different output
  def zoom_event(self):
    print(f'Attending to the zoom lecture the teacher created.')
# One of the abstractmethods from template but with different output
  def eat_lunch(self):
    print(f'Eating a sandwich.')
# One of the abstractmethods from template but with different output
  def check_email(self):
    print(f'Asking the teacher about questions for the assignment.')
# One of the abstractmethods from template but with different output
  def main_task(self):
    print(f'Working on the assignment to complete before the deadline just like us right now.')
# One of the abstractmethods from template but with different output
  def do_hobby(self):
    print(f'Watching favourite show on Netflix and chilling.')

#concrete class
# This is the one of our classes who use our  Person template
class Dean(Person):
# One of the abstractmethods from template but with different output
  def zoom_event(self):
    print(f'Attending to the meeting with other deans.')
# One of the abstractmethods from template but with different output
  def eat_lunch(self):
    print(f'Eating a delicious juicy New York Steak.')
# One of the abstractmethods from template but with different output
  def check_email(self):
    print(f'Arranging meetings with teachers through e-mails.')
# One of the abstractmethods from template but with different output
  def main_task(self):
    print(f'Signing formal documents.')
# One of the abstractmethods from template but with different output
  def do_hobby(self):
    print(f'Playing golf with other rich deans.')


# Main function creates student, teacher, dean from related classes. Also, they assigns with weekdays.
def main():
  student = Student()
  teacher = Teacher()
  dean = Dean()
  student.weekdays('Student')
  teacher.weekdays('Teacher')
  dean.weekdays('Dean')

if __name__ == "__main__":
    main()
