!pip install -U -q "google-generativeai>=0.8.2"
import google.generativeai as genai
import time

# === CONFIGURATION ===
API_KEY = ""  # Replace with your Google AI key
ITERATIONS = 9  # Number of times the question is improved

genai.configure(api_key=API_KEY)

# Function to improve the question
def improve_question(question, iterations):
    model = genai.GenerativeModel("gemini-2.0-flash-lite")
    current_question = question
    improvements = []
    
    for i in range(iterations):
        response = model.generate_content(f"Improve this question to make it clearer and more detailed, only provide the improved question: {current_question}")
        current_question = response.text.strip()
        improvements.append(current_question)
        print(f"Improvement {i+1}: {current_question}\n")
        time.sleep(1)  # To avoid abusing the API
    
    return current_question, improvements

# Function to get the final answer
def get_final_answer(final_question):
    model = genai.GenerativeModel("gemini-2.0-flash-lite")
    response = model.generate_content(final_question)
    return response.text.strip()

# === EXECUTION ===
user_question = input("Enter your question: ")
print("\nImproving the question...")
improved_question, improvements_made = improve_question(user_question, ITERATIONS)

print("\nFinal Improved Question:", improved_question)
print("\nGetting response from Gemini 2.0 Flash...")
final_answer = get_final_answer(improved_question)

print("\nFinal Answer:", final_answer)
