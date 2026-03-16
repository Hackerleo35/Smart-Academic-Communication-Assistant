from flask import Flask, render_template, request

app = Flask(__name__)

def generate_message(type, purpose, audience, points):

    if type == "Notice":
        return f"""
NOTICE

All {audience} are hereby informed about {purpose}.

Important Points:
{points}

Please follow the instructions carefully.

Department Administration
"""

    elif type == "Email":
        return f"""
Subject: {purpose}

Dear {audience},

This email is to inform you about {purpose}.

Important Points:
{points}

Regards,
Administration
"""

    else:
        return f"""
Hello {audience},

Reminder regarding {purpose}.

Important points:
{points}

Thank you.
"""


@app.route("/", methods=["GET", "POST"])
def home():

    message = ""

    if request.method == "POST":

        communication_type = request.form["type"]
        purpose = request.form["purpose"]
        audience = request.form["audience"]
        points = request.form["points"]

        message = generate_message(communication_type, purpose, audience, points)

    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)