"""this code will take an employee's information and print out their salary,bonus, vacation hourse and retirement fund"""


class employee:
    def __init__(self,name,surename,year) -> None:
        self.name = name
        self.surename = surename
        self.year = year
        pass

    def get_salary(self):
        #between 45k to 100k
        while True:
            self.salary = int(input("enter annual salary: "))
            if 45000 <= self.salary <= 100000:
                return self.salary

            print("invalid amount")


    def bonus(self):
        #must be between 10 to 20 percent,any thing else must be asked agai
        while True:
            self.range = int(input("enter bonus range (will be calculated in percent): "))
            if 10 <= self.range <= 20:
                return self.range

            print("invalid amount")

    def contribution(self):

        while True:
            self.fund = int(input("what percentage of your salary would like to contribute? "))
            if 0 <= self.fund <= 10:
                return self.fund

            print("invalid amount")

    def cla_vac(self,year):
        self.vacation = 104 * year
        if 1 <= year <= 4:
            self.vacation = self.vacation + (self.vacation * (year/10))
        else:
            self.vacation = self.vacation + (self.vacation/2)

def calculate(percentage,salary):
    if 0 <= percentage <= 5:
        return (salary * (percentage / 100) + (salary * percentage / 200))
    return (salary * (percentage / 100)) + (salary/40)

emp1 = employee("harry","potter",3)
salary = emp1.get_salary()
bonus = emp1.bonus()
vacation = emp1.cla_vac(emp1.year)
fund = calculate(emp1.contribution(),salary)

print(f"information: {emp1.name} {emp1.surename}".center(100,'-'))
print(f"{"salary:":<25}{emp1.salary:>30,.2f}")
print(f"{"bonus:":<25}{emp1.range:>30,.2f}")
print(f"{"vacation hours:":<25}{emp1.vacation:>30,.2f}")
print(f"{"total retirement fund:":<25}{fund:>30,.2f}")
