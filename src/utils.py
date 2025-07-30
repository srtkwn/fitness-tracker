#Helper functions

# food_info.py

import requests

# Replace with your actual App ID and Key
APP_ID = "c66e2b03"
APP_KEY = "437c69cafea6f0e328f1cedb93c8c6cc"

def get_nutrition(food_name):
    url = "https://trackapi.nutritionix.com/v2/natural/nutrients"
    headers = {
        "x-app-id": APP_ID,
        "x-app-key": APP_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "query": food_name
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        if result["foods"]:
            food = result["foods"][0]
            return {
                "Calories": round(food["nf_calories"], 2),
                "Protein": round(food["nf_protein"], 2),
                "Carbohydrates": round(food["nf_total_carbohydrate"], 2),
                "Fats": round(food["nf_total_fat"], 2)
            }
    else:
        print("Error:", response.status_code, response.text)
        return None