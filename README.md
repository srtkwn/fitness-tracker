<!-- Project information -->
Fitness Tracker App
This is a command-line Python application that allows users to track their daily food and water intake. It includes a login/signup system and uses the Edamam API to fetch real-time nutrition data.

⸻

Key Features:
	•	User login and signup
	•	Add/remove food entries by meal type (breakfast, lunch, snacks, dinner)
	•	Track daily water intake
	•	Daily logs reset automatically and are saved by date
	•	Delete account option
	•	Data stored locally in a JSON file
  • No UI implemented as of now - runs entirely in the terminal

⸻

Project Files:
	•	main.py – Main menu and program flow
	•	data.py – Handles data storage, user info, and logs and tracks the data
	•	utils.py – Connects to nutritionx API for food data
	•	auth.json – Stores all user data and logs
	•	requirements.txt – Contains the required Python modules

⸻

How to Run:
	1.	Install required packages: pip install -r requirements.txt
	2.	Add your nutritionx API credentials in utils.py
	3.	Run the program: python main.py