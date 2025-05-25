from flask import Flask, request, jsonify, render_template
from gen_ai import get_llm  


# Initialize Chatbot
path = r"C:\chatbot_project_updated\chatbot_project\data\financial_risk.pdf"
chatbot = get_llm(path)

# Flask app
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_answer", methods=["POST"])
def get_answer():
    question = request.form["question"]
    response = chatbot.invoke({"question": question, "chat_history": []})
    answer = response.get("answer","i'm not sure about that.")
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)  # Enable debug mode for development
