# class BankAccount:
#     def __init__(self, name, balance = 0):
#         self.name = name
#         self.__balance = balance
#         self.history = []        

#     def deposit(self, amount):
#         if amount < 0:
#             print("Invalid deposit amoumt")
#         else:
#             self.__balance += amount
#             self.history.append(f"Deposit : {amount}")
#             return f"Deposit succesfull, Amount deposited: {amount}"            

#     def withdraw(self, amount):
#         if amount < 0:
#             print("Invalid withdrawal amount")
#         elif amount > self.__balance:
#             print("Insufficient funds")
#         else:
#             self.__balance -= amount
#             self.history.append(f"Withdrawal : {amount}")
#             return f"Withdrawal succesfull, Amount withdrawn: {amount}"

#     def show_history(self):
#         print(f"---TRANSACTION HISTORY of {self.name}---")
#         for transaction in self.history:
#             print(transaction)

# a1 = BankAccount("Pradeep", 7019724730)
# print(a1.deposit(5000))
# print(a1.withdraw(750000))
# print(a1.show_history())

classroom = []

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        
    def grad(self):
        if self.marks >= 90:
            return f"Grade for {self.name} is 'A'"
        elif self.marks >= 60 and self.marks < 90:
            return f"Grade for {self.name} is 'B'"
        else:
            return f"Grade for {self.name} is 'C'"
        
# s1 = Student("Pradeep", 80, 85)
# s2 = Student("Suresh", 91, 91)
# s3 = Student("Ramesh", 92, 55)

# classroom.append(s1)
# classroom.append(s2)
# classroom.append(s3)

# target = 91

# for student in classroom:
#     if student.roll_no == target:
#         print(student.grad())