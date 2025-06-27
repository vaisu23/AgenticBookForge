import google.generativeai as genai

genai.configure(api_key="AIzaSyAnvLeMtyJLfQc6E3maGknL2SASrZv7wM8")


model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

def review_text(text)-> str:
    prompt = f"Edit the following passage for clarity, grammar, and style while keeping the original tone and meaning:\n\n{text}"


    response = model.generate_content(prompt)
    return response.text.strip()
print(" AI Reviewer ready")
