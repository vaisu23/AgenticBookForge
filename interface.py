import threading
import webbrowser
from flask import Flask, request, render_template_string
import time
import os

app = Flask(__name__)

edited_text = None
reviewed_text_path = "output/reviewed_text.txt"
final_output_path = "output/final_output.txt"
submitted_event = threading.Event() 

@app.route("/", methods=["GET", "POST"])
def editor():
    global edited_text
    if request.method == "POST":
        edited_text = request.form["edited_text"]
        with open(final_output_path, "w", encoding="utf-8") as f:
            f.write(edited_text)
        submitted_event.set()  
        return " Final version submitted. You may close this tab."
    else:
        with open(reviewed_text_path, "r", encoding="utf-8") as f:
            text = f.read()
        return render_template_string("""
            <html>
            <head><title>Editor UI</title></head>
            <body>
                <h2> Edit the text below and click Submit</h2>
                <form method="POST">
                    <textarea name="edited_text" rows="25" cols="100">{{text}}</textarea><br>
                    <button type="submit">Submit Final Version</button>
                </form>
            </body>
            </html>
        """, text=text)

def run_flask():
    app.run(port=5000, debug=False)

def launch_editor_ui(text):
    with open(reviewed_text_path, "w", encoding="utf-8") as f:
        f.write(text)

    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # Open browser
    webbrowser.open("http://127.0.0.1:5000")

    print("📝 Please edit the text in your browser and submit...")

    submitted_event.wait()

    with open(final_output_path, "r", encoding="utf-8") as f:
        final_text = f.read()

    return final_text
# if __name__ == "__main__":
#     # For testing purposes, you can run the Flask app directly
#     app.run(port=5000, debug=False)