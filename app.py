from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load data from CSV
def load_data():
    file_path = '/mnt/data/Auction_data (1).csv'  # Path to your uploaded CSV file
    data = pd.read_csv(file_path)
    return data

@app.route('/')
def index():
    # Load and convert data to dictionary format for HTML
    data = load_data()
    data_dict = data.to_dict(orient='records')  # Convert to list of dictionaries
    return render_template('index.html', data=data_dict)

if __name__ == '__main__':
    app.run(debug=True)
