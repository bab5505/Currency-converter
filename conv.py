from flask import Flask, render_template, request, make_response

app = Flask(__name__)

# Currency conversion rates
CONVERSION_RATES = {
    'USD': {'EUR': 0.8516, 'GBP': 0.7331},
    'EUR': {'USD': 1.1737, 'GBP': 0.8594},
    'GBP': {'USD': 1.3637, 'EUR': 1.1628}
}

@app.route('/', methods=['GET', 'POST'])
def currency_converter():
    if request.method == 'POST':
        try:
            # Get form data
            from_currency = request.form['from_currency'].upper()
            to_currency = request.form['to_currency'].upper()
            amount = float(request.form['amount'])

            # Perform conversion
            if from_currency in CONVERSION_RATES and to_currency in CONVERSION_RATES[from_currency]:
                exchange_rate = CONVERSION_RATES[from_currency][to_currency]
                converted_amount = amount * exchange_rate
                converted_amount_rounded = round(converted_amount, 2)

                # Create Response object
                response = make_response(render_template('result.html', from_currency=from_currency, to_currency=to_currency,
                                           amount=amount, exchange_rate=exchange_rate,
                                           converted_amount=converted_amount_rounded))

                # Set SameSite attribute for the cookie
                response.set_cookie('my_cookie', 'cookie_value', samesite='None', secure=True)

                return response
            else:
                error_message = 'Invalid currency codes'
                return render_template('error.html', error_message=error_message)
        except ValueError:
            error_message = 'Invalid amount'
            return render_template('error.html', error_message=error_message)
    return render_template('form.html')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
