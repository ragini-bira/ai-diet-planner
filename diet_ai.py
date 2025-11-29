from openai import OpenAI

client = OpenAI(api_key="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")

def get_diet_recommendation(age, gender, weight, height, goal):
    prompt = f"""
    Create a detailed DAILY Indian diet plan.

    User Details:
    - Age: {age}
    - Gender: {gender}
    - Weight: {weight} kg
    - Height: {height} cm
    - Goal: {goal}

    Requirements:
    - Breakfast, Lunch, Dinner, 2 Snacks
    - Daily calories
    - Indian food only
    - No food repeated more than 2 times/week
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


def get_weekly_diet_plan(age, gender, weight, height, goal):
    prompt = f"""
    Create a WEEKLY 7-day Indian diet plan.

    - Include all meals
    - Snacks
    - Calories
    - Day-wise format
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
