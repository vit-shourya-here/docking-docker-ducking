
from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Calculator V2</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
    <h2>Menu-Driven Calculator — V2</h2>

    <form method="post">
        <input name="a" type="number" step="any"
               placeholder="First number" required>

        <input name="b" type="number" step="any"
               placeholder="Second number" required>

        <select name="op">
            <option value="add">Addition (+)</option>
            <option value="sub">Subtraction (-)</option>
            <option value="mul">Multiplication (*)</option>
            <option value="div">Division (/)</option>
        </select>

        <button type="submit">Calculate</button>
    </form>

    {% if result is not none %}
        <h3>Result: {{ result }}</h3>
    {% endif %}
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None

    if request.method == "POST":
        try:
            a = float(request.form["a"])
            b = float(request.form["b"])
            op = request.form["op"]

            if op == "add":
                result = a + b
            elif op == "sub":
                result = a - b
            elif op == "mul":
                result = a * b
            elif op == "div":
                result = a / b if b != 0 else "Cannot divide by zero"
            else:
                result = "Invalid operation"

        except (ValueError, KeyError):
            result = "Invalid input"

    return render_template_string(HTML, result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
