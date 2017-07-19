from flask import Flask, render_template, request

app = Flask ("MyApp")

@app.route("/")
def homepage(): 
	return render_template ("subscribe.html")


@app.route("/", methods=["POST"])
def sign_up(): 
	form_data = request.form
	print form_data["email"]
	return "All ok"


app.run(debug=True)
	
