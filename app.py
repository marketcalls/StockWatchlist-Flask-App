from flask import Flask, render_template, request, redirect, url_for, flash
import yfinance as yf
from extensions import db
from models import Stock

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///watchlist.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

def create_tables():
    with app.app_context():
        db.create_all()

create_tables()

@app.route('/')
def index():
    try:
        stocks = Stock.query.all()
        print(f"Fetched stocks: {stocks}")  # Debug print statement
        return render_template('index.html', stocks=stocks)
    except Exception as e:
        print(f"Error fetching stocks: {e}")  # Print any errors to the console
        return render_template('index.html', stocks=[])

@app.route('/add', methods=['GET', 'POST'])
def add_stock():
    if request.method == 'POST':
        try:
            symbol = request.form['symbol']
            stock = yf.Ticker(symbol)
            hist = stock.history(period='1d')
            open_price = round(hist['Open'].iloc[-1], 2)
            high_price = round(hist['High'].iloc[-1], 2)
            low_price = round(hist['Low'].iloc[-1], 2)
            close_price = round(hist['Close'].iloc[-1], 2)
            new_stock = Stock(symbol=symbol, open=open_price, high=high_price, low=low_price, close=close_price)
            db.session.add(new_stock)
            db.session.commit()
            flash('Stock added successfully!', 'success')
        except Exception as e:
            print(f"Error adding stock: {e}")
            flash('Error adding stock. Stock Symbol Not Found', 'error')
        return redirect(url_for('index'))
    return render_template('add_stock.html')

@app.route('/delete/<int:stock_id>', methods=['POST'])
def delete_stock(stock_id):
    try:
        stock = Stock.query.get(stock_id)
        db.session.delete(stock)
        db.session.commit()
        flash('Stock removed successfully!', 'success')
    except Exception as e:
        print(f"Error deleting stock: {e}")
        flash('Error removing stock', 'error')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
