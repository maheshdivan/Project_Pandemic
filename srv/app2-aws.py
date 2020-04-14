import psycopg2
from flask import Flask, jsonify
from flask_cors import CORS
from flask import send_file

app = Flask(__name__)
CORS(app)

# update using db connection info
conn = psycopg2.connect(host='database-1.cpnwuinodiya.us-east-1.rds.amazonaws.com',user='postgres',password='postgres',dbname='market_data')
cur = conn.cursor()


@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"<h1>Welcome to Market Data API </h1><br/>"
        f"<h3>Returns Time Series data for various Stock Market Indexes</h3>"
        f"<h3>Includes :  Date, Open, High, Low, Close, Volume, Ticker and Daily Change</h3>"
        f"Available Routes:<br/>"
        f"<b>/market</b> Get data for Dow Jones Industrial, S&P 500, FTSE100, Nikkei 225 and Hang Seng Index<br/>"
        f"<b>/getCSV</b> get full dataset in CSV format<br/>"
        f"<br>   </br>"        
    )

@app.route("/market")
def market():
    try:
        cur.execute('SELECT * FROM index_table')
        values = cur.fetchall()

        if values != []:
           return (jsonify(values))
        else:
            return ("<h3> No row found for </h3>")   

    except TypeError :
        print("I am here")
        return (f"<h2>An error occured</h2>")     
        
@app.route('/getCSV')
def plot_csv():
    return send_file('markets.csv',
                     mimetype='text/csv',
                     attachment_filename='markets.csv',
                     as_attachment=True)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
