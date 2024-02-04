from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import pandas as pd
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe Location on Google Maps(URL)', validators=[URL(require_tld=True)])
    opening_time = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    closing_time = StringField('Closing Time e.g. 5:30PM', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=['☕️', '☕️☕️', '☕️☕️☕️', '☕️☕️☕️☕️', '☕️☕️☕️☕️☕️'],
                                validators=[DataRequired()])
    wifi = SelectField('Wifi Strength Rating',
                       choices=['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'], default='✘')
    power_socket = SelectField('Power Socket Availability',
                               choices=['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'], default='✘')
    submit = SubmitField('Submit')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    data = pd.read_csv('cafe-data.csv', on_bad_lines='skip')
    if form.validate_on_submit():
        with open('cafe-data.csv', 'a', encoding='utf-8') as same_data:
            writer = (csv.writer(same_data))
            writer.writerow([str(form.cafe.data), str(form.location.data), str(form.opening_time.data),
                             str(form.closing_time.data), str(form.coffee_rating.data), str(form.wifi.data),
                             str(form.power_socket.data)])
        return render_template('cafes_2.html', data=data.fillna("None").to_dict(orient='records'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    data = pd.read_csv('cafe-data.csv')
    return render_template('cafes_2.html', data=data.to_dict(orient='records'))


if __name__ == '__main__':
    app.run(debug=True)
