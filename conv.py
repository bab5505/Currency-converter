from flask import Flask, render_template, request, make_response
from conv import currency_converter

app = Flask(__name__)

# Route for home page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get form inputs
        currency_from = request.form['currency_from']
        currency_to = request.form['currency_to']
        amount = request.form['amount']

        # Call the currency_converter function from conv module
        converted_amount, error = currency_converter(currency_from, currency_to, amount)

        if error:
            return render_template('index.html', error=error)
        else:
            # Create Response object
            response = make_response(render_template('index.html', converted_amount=converted_amount))

            # Set SameSite attribute for the cookie
            response.set_cookie('my_cookie', 'cookie_value', samesite='None', secure=True)

            return response

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
