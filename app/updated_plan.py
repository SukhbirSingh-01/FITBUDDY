from google import genai
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY"))

def update_workout_plan(original_plan: str, user_feedback: str) -> str:
    prompt = f"""
You are a professional fitness trainer assistant.

Here's the original 7-day workout plan:
{original_plan}

User Feedback:
"{user_feedback}"

Based on the feedback, revise the relevant parts of the workout plan. Keep the format and rest of the plan unchanged if not needed.
"""
    try:
        response = client.models.generate_content(
            model="gemini-1.5-pro",
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        return f"Error updating plan: {e}"
