from flask import Flask
from flask import render_template
from flask import url_for

import stripe

app = Flask(__name__)


app.config['STRIPE_PUBLIC_KEY'] = 'pk_test_51HpbsrFSAlWtvCh5SI05irafAHEl2lxXhEWtOXtQBqqMKVfv6E7TKbBy4U7k6EPqhE6J5u4JIgCVovyvC5Pwv0yo00WdQ4X2FI'
app.config['STRIPE_SECRET_KEY'] = 'sk_test_51HpbsrFSAlWtvCh5qdj70FLml1GNou6Fsi7kf2v8LPP0ITonQKvmdaUd7NqJVbPHiiyvtu04gmDcLDEec9IWbx4D00MRIHH8WN'

stripe.api_key = app.config['STRIPE_SECRET_KEY']


@app.route('/')
def index():

    session = stripe.checkout.Session.create(
      customer='cus_IRCi3t4OfaNs1U',
      payment_method_types=['card'],
      line_items=[{
        'price': 'price_1HqJQnFSAlWtvCh52GbGAoFM',
        'quantity': 1,
      }],
      mode='payment',
      success_url=url_for('thanks', _external=True) + '?session_id={checkout_session_id}',
      cancel_url=url_for('index', _external=True),
    )

    return render_template(
        'index.html',
        checkout_session_id=session['id'],
        checkout_public_key=app.config['STRIPE_PUBLIC_KEY']
    )

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

if __name__ == '__main__':
    app.run()