import psycopg2
from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# update using db connection info
conn = psycopg2.connect(host='hospitalutil.cuo7ivhfh3jn.us-east-1.rds.amazonaws.com',user='root',password='postgress',dbname='hospitalutil')
cur = conn.cursor()


@app.route("/")
def welcome():
    """List all available api routes."""
    return (
       f"<h2>Welcome to Hospital API </h2><br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/pandemic/hospital<n><br/>"
    )

@app.route("/api/v1.0/pandemic/hospital")
def corona():
    try:
        cur.execute('SELECT * FROM hospitalutil')
        values = cur.fetchall()

        if values != []:
           return (jsonify(values))
        else:
            return ("<h3> No row found for </h3>")   

    except TypeError :
        print("I am here")
        return (f"<h2>An error occured</h2>")     
        

if __name__ == '__main__':
    app.debug = True
    app.run()
