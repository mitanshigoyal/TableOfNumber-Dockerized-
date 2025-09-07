from flask import Flask, render_template_string, request

app = Flask(__name__)

template = """
<!doctype html>
<html>
<head>
    <title>Multiplication Table</title>
</head>
<body>
    <h2>Enter a Number</h2>
    <form method="POST">
        <input type="number" name="num" required>
        <button type="submit">Submit</button>
    </form>

    {% if table %}
        <h3>Table of {{ num }}</h3>
        <ul>
            {% for line in table %}
                <li>{{ line }}</li>
            {% endfor %}
        </ul>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    table = []
    num = None
    if request.method == "POST":
        num = int(request.form["num"])
        table = [f"{num} x {i} = {num*i}" for i in range(1, 11)]
    return render_template_string(template, table=table, num=num)

if __name__ == "__main__":
    # IMPORTANT for Docker
    app.run(host="0.0.0.0", port=5000, debug=True)
