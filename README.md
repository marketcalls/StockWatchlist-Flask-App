
# StockWatchlist-Flask-App

This is a Flask-based web application for managing a stock watchlist. The application allows users to add and remove stocks, and view details such as the opening, high, low, and closing prices for the day.

## Features

- Add stocks to the watchlist
- Remove stocks from the watchlist
- View stock details including open, high, low, and close prices

## Installation

### Prerequisites

- Python 3.6 or higher
- Git

### Step-by-Step Installation

1. **Clone the Repository**

   First, clone the repository to your local machine:

   \`\`\`sh
   git clone https://github.com/marketcalls/StockWatchlist-Flask-App.git
   cd StockWatchlist-Flask-App
   \`\`\`

2. **Create a Virtual Environment**

   It is recommended to use a virtual environment to manage dependencies. Create and activate a virtual environment using the following commands:

   \`\`\`sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use \`venv\Scripts\activate\`
   \`\`\`

3. **Install Dependencies**

   Install the required Python packages using \`pip\`:

   \`\`\`sh
   pip install -r requirements.txt
   \`\`\`

4. **Set Up the Database**

   The application uses SQLite as the database. The database will be initialized automatically when you run the application for the first time.

5. **Run the Application**

   Start the Flask development server:

   \`\`\`sh
   python app.py
   \`\`\`

6. **Access the Application**

   Open your web browser and navigate to:

   \`\`\`
   http://127.0.0.1:5000/
   \`\`\`

   You should see the home page of the Stock Watchlist application.

### Project Structure

\`\`\`plaintext
StockWatchlistApp/
│
├── app.py
├── models.py
├── extensions.py
├── static/
│   └── style.css
├── templates/
│   ├── base.html
│   ├── index.html
│   └── add_stock.html
├── requirements.txt
├── .gitignore
└── README.md
\`\`\`

## Usage

### Adding a Stock

1. Click on the "Add Stock" link in the navigation bar.
2. Enter the stock symbol (e.g., AAPL for Apple Inc.) and submit the form.
3. The stock will be added to your watchlist and you will see its details including open, high, low, and close prices.

### Removing a Stock

1. On the home page, you will see a list of stocks in your watchlist.
2. Click the "Remove" button next to the stock you want to remove.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for more details.
