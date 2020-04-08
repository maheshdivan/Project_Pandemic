import psycopg2
from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# update using db connection info
conn = psycopg2.connect(host='localhost',user='postgres',password='postgres',dbname='marketing_db')
cur = conn.cursor()


@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"<h2>Welcome to Market Data API </h2><br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/index/market<br/>"
        f"n=DJI,FTSE,GSPC,N225,HSI"
        f"<br>   </br>"        
    )

@app.route("/api/v1.0/index/market")
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
        

if __name__ == '__main__':
    app.run(host='localhost', port=50000, threaded=True, debug=True)
