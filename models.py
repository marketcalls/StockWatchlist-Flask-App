from extensions import db

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(50), nullable=False)
    open = db.Column(db.Float, nullable=False)
    high = db.Column(db.Float, nullable=False)
    low = db.Column(db.Float, nullable=False)
    close = db.Column(db.Float, nullable=False)

    def __init__(self, symbol, open, high, low, close):
        self.symbol = symbol
        self.open = open
        self.high = high
        self.low = low
        self.close = close
