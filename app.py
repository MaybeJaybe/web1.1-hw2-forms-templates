from flask import Flask, request, render_template
import random

app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))

@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

# froyo section
@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return render_template('froyo_form.html')

@app.route('/froyo_results')
def show_froyo_results():
    """Shows the user what they ordered from the previous page."""
    context = {
        'users_froyo_flavor': request.args.get('flavor'),
        'users_toppings': request.args.get('toppings')
    }
    return render_template('froyo_results.html', **context)

# favorites section
@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return """
    <form action="/favorites_results" method="GET">
        What is your favorite color?<br/>
        <input type="text" name="color"><br/>
        What is your favorite animal?<br/>
        <input type="text" name="animal"><br/>
        What is your favorite city?<br/>
        <input type="text" name="city"<br/>
        <input type="submit" value="Submit">
    </form>
    """
    
@app.route('/favorites_results')
def show_favorites_results():
    fav_color = request.args.get('color')
    fav_animal = request.args.get('animal')
    fav_city = request.args.get('city')
    """Shows the user a nice message using their form results."""
    return f'I bet your dream would be to have a {fav_color} colored {fav_animal} plushie to cuddle when you live in {fav_city}.'

# secret message section
@app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return """
    <form action="/message_results" method="POST">
        Enter the phrase you would like to make secret:
        <input type="text" name="message">
        <input type="submit" name="Submit">
    </form>
    """

@app.route('/message_results', methods=['POST'])
def message_results():
    """Shows the user their message, with the letters in sorted order."""
    message = request.form.get('message')
    secret_message = sort_letters(message)
    return f'Here\'s your secret message: <br/>{secret_message}'

# calculator section
@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return render_template('calculator_form.html')

@app.route('/calculator_results')
def calculator_results():
    """Shows the user the result of their calculation."""

    operation = request.args.get('operation')
    num1 = request.args.get('operand1')
    num2 = request.args.get('operand2')
    num1=int(num1)
    num2=int(num2)

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    else:
        result = num1 / num2

    context = {
    'operation': request.args.get('operation'),
    'num1': request.args.get('operand1'),
    'num2': request.args.get('operand2'),
    'result': result
    }

    return render_template('calculator_results.html', **context)


# List of compliments to be used in the `compliments_results` route (feel free 
# to add your own!) 
# https://systemagicmotives.com/positive-adjectives.htm
list_of_compliments = [
    'awesome',
    'beatific',
    'blithesome',
    'conscientious',
    'coruscant',
    'erudite',
    'exquisite',
    'fabulous',
    'fantastic',
    'gorgeous',
    'indubitable',
    'ineffable',
    'magnificent',
    'outstanding',
    'propitioius',
    'remarkable',
    'spectacular',
    'splendiferous',
    'stupendous',
    'super',
    'upbeat',
    'wondrous',
    'zoetic'
]

@app.route('/compliments')
def compliments():
    """Shows the user a form to get compliments."""
    return render_template('compliments_form.html')

@app.route('/compliments_results')
def compliments_results():
    """Show the user some compliments."""
    context = {
        # TODO: Enter your context variables here.
    }

    return render_template('compliments_results.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
