#Entry point of the app

from data import Userdata
from data import UserAuth
from utils import get_nutrition



def main():
    auth = UserAuth()

    print("Welcome to Fitness Tracker!")
    while True:
        choice = input("\n1. Login\n2. Signup\n3. Delete Account\n4. Exit\nEnter your choice: ")

        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")

            if auth.login(username, password):
                break
        elif choice == "2":
            username = input("Choose a Username: ")
            password = input("Choose a Password: ")

            if auth.signup(username, password):
                break

        elif choice == "3":
            username = input("Enter your Username: ")
            password = input("Enter your Password: ")
            auth.delete_acc(username, password)
        elif choice == "4":
            print("Exiting... Goodbye!")
            return
        else:
            print("Invalid choice. Try again.")

    # Logged in successfully
    user = Userdata(username)
    user.load_logs()

    while True:
        print("\n--- Main Menu ---")
        print("1. Log Food")
        print("2. View Food Log")
        print("3. Remove Food")
        print("4. Add Water")
        print("5. View Water Log")
        print("6. Remove Water")
        print("7. Logout")

        action = input("Enter your choice: ")

        if action == "1":
            print("\nLog Food Under:")
            print("1. Breakfast")
            print("2. Lunch")
            print("3. Dinner")
            print("4. Snacks")

            meal_choice = input("Enter the meal type: ")
            meal = {
                "1" : "Breakfast",
                "2" : "Lunch",
                "3" : "Dinner",
                "4" : "Snacks"
            }
            if meal_choice not in meal:
                print("Invalid meal type. Returning to main menu.")
                continue
            meal_type = meal[meal_choice]
            food_name = input("Enter food item (e.g., '1 cup rice'): ")
            nutrients = get_nutrition(food_name)

            if nutrients:
                user.log_food(
                    meal_type=meal_type,
                    item=food_name,
                    calories=nutrients["Calories"],
                    protein=nutrients["Protein"],
                    carbs=nutrients["Carbohydrates"],
                    fats=nutrients["Fats"]
                )
                user.save_logs()
            else:
                print("Could not retrieve food data. Try a different item.")
        
        elif action == "2":
            user.view_food_log()

        elif action == "3":
            item = input("Enter the food item to remove: ")
            user.remove_food(item)
            user.save_logs()

        elif action == "4":
            try:
                amount = int(input("Enter water amount in ml: "))
                user.add_water(amount)
                user.save_logs()
            except ValueError:
                print("Please enter a valid number.")

        elif action == "5":
            user.view_water_log()

        elif action == "6":
            try:
                amount = int(input("Enter the amount of water (in ml) to remove: "))
                user.remove_water(amount)
                user.save_logs()
            except ValueError:
                print("Pleae Enter a Valid number.")

        elif action == "7":
            print("Logging out...")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()