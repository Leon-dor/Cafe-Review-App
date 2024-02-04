# Cafe-Review-App
 This is a Flask web application that allows users to add and view information about cafes.

Here’s a breakdown of what the code does:

Imports: The necessary modules and packages are imported. This includes Flask for the web application, Flask-Bootstrap for styling, Flask-WTF and WTForms for form handling, and pandas and csv for data handling.
App Configuration: An instance of the Flask application is created and configured. Bootstrap is also initialized with the app.
Form Class: A form class CafeForm is defined using Flask-WTF and WTForms. This form asks for details about a cafe, including its name, location, opening time, closing time, coffee rating, wifi strength, and power socket availability.
Routes:
@app.route('/'): The home route renders an ‘index.html’ template.
@app.route('/add', methods=["GET", "POST"]): The ‘add’ route handles the submission of the CafeForm. If the form is valid upon submission, the data is appended to a CSV file (‘cafe-data.csv’). The form and the data from the CSV file are then rendered in an ‘add.html’ template.
@app.route('/cafes'): The ‘cafes’ route reads the data from the CSV file and renders it in a ‘cafes_2.html’ template.
Main: If this script is run directly (not imported), the Flask app is run in debug mode.
