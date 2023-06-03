import random

def create_meal_plan():
    # List of meals
    meals = [
        "Spaghetti Bolognese",
        "Chicken Stir-Fry",
        "Vegetable Curry",
        "Grilled Salmon with Quinoa",
        "Mushroom Risotto",
        "Beef Tacos",
        "Pasta Primavera",
        "Honey Glazed Chicken",
        "Greek Salad with Grilled Chicken",
        "Teriyaki Salmon with Steamed Vegetables"
    ]

    # Create a meal plan for each day of the week
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    meal_plan = {}
    for day in days_of_week:
        meal = random.choice(meals)
        meal_plan[day] = meal

    return meal_plan

# Generate a meal plan
plan = create_meal_plan()

# Print the meal plan for each day
for day, meal in plan.items():
    print(f"{day}: {meal}")
