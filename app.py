from flask import Flask, render_template, request

app = Flask(__name__)


def load_history():
    history = []
    try:
        with open("history.txt", "r") as file:
            for line in file:
                history.append(line.strip())
    except FileNotFoundError:
        pass
    return history


def save_to_file(entry):
    with open("history.txt", "a") as file:
        file.write(entry + "\n")


@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    history = load_history()

    if request.method == "POST":
        expression = request.form["expression"]

        try:
            result_value = eval(expression)
            result = f"{expression} = {result_value}"
            save_to_file(result)
        except:
            result = "Error"

    return render_template("index.html", result=result, history=history)


if __name__ == "__main__":
    app.run(debug=True)