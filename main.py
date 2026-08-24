
class GeneralManager:
    
    def __init__(self,chefs,waiters,casheirs):
        self.chefs = chefs
        self.next_chef = 4
        self.waiters = waiters
        self.next_waiter = 4
        self.casheirs = casheirs
        self.next_casheirs = 3
        self.id = 0

    def add_employee(self, employee_name, position, salary):
        if position == "chef":
            self.id = self.next_chef
            self.chefs[self.id] = {
                "name": employee_name, "position": position, "salary":salary
            }
        elif position == "waiter" or position == "waitress":
            self.id = self.next_waiter
            self.waiters[self.id] = {
                "name": employee_name, "position": position, "salary":salary
            }
        else:
            self.id = self.next_chef
            self.chefs[self.id] = {
                "name": employee_name, "position": position, "salary":salary
            }
        print("Added successfuly")

    def remove_employee(self, employee_id, position):
        if position == "chef":
            if employee_id in self.chefs:
                del self.chefs[employee_id]
                print("Removed successfuly")
            else:
                print("Can't found ID ")
        elif position == "waiter" or position == "waitress":
            if employee_id in self.waiters:
                del self.waiters[employee_id]
                print("Removed successfuly")
            else:
                print("Can't found ID ")
        if position == "casheir":
            if employee_id in self.casheirs:
                del self.casheirs[employee_id]
                print("Removed successfuly")
            else:
                print("Can't found ID ")

    def update_employee(self,employee_id,employee_name,position,salary):
        if position == "chef":
            if employee_id in self.chefs:
                self.chefs[self.id] = {
                    "name": employee_name, "position": position, "salary":salary
                    }
            else:
                print("Can't found ID ")    
        elif position == "waiter" or position == "waitress":
            if employee_id in self.waiters:
                self.chefs[self.id] = {
                    "name": employee_name, "position": position, "salary":salary
                    }
            else:
                print("Can't found ID ")
        else:
            if employee_id in self.casheirs:
                self.chefs[self.id] = {
                    "name": employee_name, "position": position, "salary":salary
                }
            else:
                print("Can't found ID ")      

    def display_employee(self):
        print(self.chefs)
        print(self.waiters)
        print(self.casheirs)

chefs = {
        1: {
            "name": "Ahmed Mohamed", "position": "chef", "salary": 5000
        },
        2: {
            "name": "Tamer Adel", "position": "chef", "salary": 5000
        },
        3: {
            "name": "Mohamed Hany", "position": "Head chef", "salary": 8000
        }
    }
waiters = {
    1: {
        "name": "Mona Ahmed", "position": "waiteress", "salary": 4500
       },
    2: {
        "name": "Ali Khaled", "position": "waiter", "salary": 4500
        },
    3: {
        "name": "Mohamed Moamen", "position": "Head waiter", "salary": 6500
        }
}
casheirs = {
    1: {
        "name": "Layla Walid", "position": "cashier", "salary": 2000
        },
    2: {
        "name": "Ibrahim Mohsen", "position": "cashier", "salary": 2000
        }
}
employee = GeneralManager(chefs,waiters,casheirs)
employee.add_employee("Hassan Hassan","Chef",5000)
employee.display_employee()
employee.remove_employee(4,"chef")
employee.display_employee()
employee.update_employee(1,"LailaWalyd","casheir",2000)
