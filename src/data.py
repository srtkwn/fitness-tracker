# Handles data storage and retrievel

import hashlib as hb
import json as j
import os

class Userdata():
    def __init__(self,username):
        self.username = username
        self.water_intake = 0
        self.water_log = []
        self.food_log = {
            "Breakfast": [],
            "Lunch": [],
            "Dinner": [],
            "Snacks": []
        }

    def log_food(self,meal_type,item,calories,protein,carbs,fats):
        food_entry = {
            "Name" : item,
            "Calories" : calories,
            "Protein" : protein,
            "Carbohydrates" : carbs,
            "Fats" : fats
        }
        if meal_type in self.food_log:
            self.food_log[meal_type].append(food_entry)
            print(f"{item} logged successfully under {meal_type}!")
        else:
            print("Invalid meal type. Please choose anyone of the above.")
        
    def remove_food(self,item):
        found = False
        for meal in self.food_log:
            for i in self.food_log[meal]:
                if i['Name'].lower() == item.lower():
                    self.food_log[meal].remove(i)
                    found = True
                    print(f"{item} remove from {meal} successfully!")
                    break
            if found:
                break
        if not found:
            print("Food not found in the log.")

    def add_water(self,amount):
        self.water_log.append(amount)
        print(f"{amount}ml logged successfully.")
        self.water_intake += amount

    def remove_water(self,amount):
        if amount in self.water_log:
            self.water_log.remove(amount)
            print(f"{amount}ml removed successfully.")
            self.water_intake -= amount

        else:
            print("Not much water logged in there.")
        if not self.water_log:
            self.water_intake = 0

    def view_food_log(self):
        print('-------FOOD LOG-------\n')
        if not self.food_log:
            print('No food items logged yet.')
        else:
            for meal, foods in self.food_log.items():
                print(f"\n--- {meal.upper()} ---")
                for food in foods:
                    print(f"""Name: {food['Name']}
                      Calories: {food['Calories']} kcal
                      Protein: {food['Protein']}g
                      Carbs: {food['Carbohydrates']}g
                      Fats: {food['Fats']}g""")

    def view_water_log(self):
        print("-------WATER LOG-------\n")
        if not self.water_log:
            print("No water logged yet.")
        else:
            print("Water Intake History:")
            for amount in self.water_log:
                print(f"- {amount}ml")
            print(f"\nTotal intake: {self.water_intake}ml")
    
    def save_logs(self):
        data = {
            "food_log": self.food_log,
            "water_log": self.water_log,
            "water_intake": self.water_intake
        }
        with open(f"data_{self.username}.json", "w") as file:
            j.dump(data, file, indent=4)
    
    def load_logs(self):
        filename = f"data_{self.username}.json"
        if os.path.exists(filename):
            with open(filename, "r") as file:
                data = j.load(file)
                self.food_log = data.get("food_log", [])
                self.water_log = data.get("water_log", [])
                self.water_intake = data.get("water_intake", 0)


class UserAuth():
    def __init__(self):
        self.users = {} 
        self.load_users()

    def signup(self,username,password):
        if username in self.users:
            print("Username already exists! Choose another username:")
            return False
        hashed_pass = self.hash_pass(password)
        self.users[username] = hashed_pass
        self.save_users()
        print("Signup Successfull!")
        return True
    
    def login(self,username,password):
        if username not in self.users:
            print("Username does not exist! Write your username correctly.")
            return False
        if self.verify_pass(self.users[username], password):
            print(f"Welcome {username}!")
            return True
        else:
            print("Incorrect Password! Try again.")
            return False
        
    def verify_pass(self,stored_hash,entered_password):
        return stored_hash == self.hash_pass(entered_password)
    
    def hash_pass(self,password):
        return hb.sha256(password.encode()).hexdigest()
    
    def change_pass(self,username,old_password,new_password):
        if username in self.users and self.verify_pass(self.users[username], old_password):
            self.users[username] = self.hash_pass(new_password)
            self.save_users()
            print("Password Changed successfully!")
        else:
            print("Old password is incorrect.")

    def delete_acc(self,username,password):
        if username in self.users and self.verify_pass(self.users[username], password):
            while True:
                answer = str(input("Are you sure you want to delete your account?\nAll the progress will be lost.\nType Yes or No: "))
                if answer.lower() == 'yes':
                    del self.users[username]
                    self.save_users()
                    print("Account Deleted Successfully!")
                    print("\nReturning to the Main Menu")
                    return
                elif answer.lower() == "no":
                    print("\n----Returning to the Welcome Page----")
                    return
                else:
                    print("Invalid Input.")
                    return
        else:
            print("Invalid Username and Password.")

    def save_users(self):
        with open("users.json", "w") as file:
            j.dump(self.users, file, indent=4)

    def load_users(self):
        if os.path.exists("users.json"):
            with open("users.json", "r") as file:
                self.users = j.load(file)
        else:
            self.users = {}







        
             