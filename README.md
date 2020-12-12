[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=341490&assignment_repo_type=GroupAssignmentRepo)
# Group-Assignment

Group Member - Birkan Ak, Ugurcan Demir, Nilgun Ilayda Akalin, Kerem Atasoy

HOW TO RUN = python <FILE NAME> # Python Version -- 3.8.5

==========   PROXY PATTERN - Patient and Doctor Appointment System   =============

Our real word problem is making patient appointment between patient and doctor but as we all know doctors are not dealing with that kind of stuffs and mostly, they have assistant who deals with that issues.
We decided to select proxy pattern to our real-world problem because of some reasons. One of the reasons is coming from definition of Proxy pattern. Which is, the proxy design pattern allows us to represent another class through a Proxy class we created. In this way, the Proxy class can perform all the operations or transactions it wants without interfering with the main class. So, in our example Doctor Assistant represents the proxy. Doctor assistant allows patient to create appointment without interfering with doctor directly.

Firstly, we created doctor class which includes functions like is_Available, get_Name, get_Expertise, set_date for appointment adjustment and specifications. Also, Doctor class represents the Actual Subject in proxy concept. 

In the second part we created our most important class as a Doctor Assistant to handle our problem with real world concept. Doctor Class represents the Proxy.

Thirdly, we created our patient class to represent the client object. Patient class basically assigns the doctor assistant to DoctorAssistant and checks the availability of Doctor.

==========  COMMAND PATTERN - Coffee Shop   ==============

Command pattern is a behavioral design pattern that turns a request from client into a stand-alone object that contains all information about the request. This transformation lets you parameterize methods with different requests, delay or queue a request’s execution
Many people love to spend time with their friends. People generally prefer coffee shops to meet. For example, let's say you want to order coffee for your beloved friends. You entered a nice coffee shop and the waiter came to take the order. The waiter wrote the orders on paper and delivered them to the barista. Barista started to prepare the coffees after receiving the order receipt. Then the waiter notified you when the orders were ready, and you started drinking your coffee with your friends in a pleasant way.
In this scenario, the barista is a receiver class which has some necessary methods to make the wanted thing. We have command interface which is abstract command class to execute the order. After creating command interface, we specified concrete command classes according to the receiver to get order properly. The waiter in this Coffeeshop is invoker class which is get the order from customer and give this order to barista (receiver class). Customer is client class which request the thing he or she wanted.



========== TEMPLATE PATTERN - School System  =================

COMMENT == We've worked with this pattern before. We wanted to share this as an extra. 

One of the problems is that the daily working style of people in the same institution is the same. 
For example, a university has students, teachers and deans and many other officers. Due to the Coronavirus, many events take place online. Template Method, on the other hand, allows us to use functions effectively without changing the structure of the algorithm. That's why we used the template method to show what the student, teacher and dean did in one day.

First, we created a person class which includes templates.

After that, we created template method we created concrete classes which are Teacher, Student, and Dean.

