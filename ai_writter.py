import google.generativeai as genai

genai.configure(api_key="AIzaSyAnvLeMtyJLfQc6E3maGknL2SASrZv7wM8")

model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

def rewrite_text(text)-> str:
    prompt = f"Rewrite the following passage in a modern, engaging tone while preserving the original meaning:\n\n{text}"


    response = model.generate_content(prompt)
    return response.text.strip()
print(" AI Writer ready")
