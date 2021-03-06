import psycopg2
from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# update using db connection info
conn = psycopg2.connect(host='corona.cuo7ivhfh3jn.us-east-1.rds.amazonaws.com',user='root',password='postgress',dbname='corona')
cur = conn.cursor()


@app.route("/")
def welcome():
    """List all available api routes."""
    return (
       f"<h2>Welcome to Corona API </h2><br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/pandemic/corona<n><br/>"
    )

@app.route("/api/v1.0/pandemic/corona")
def corona():
    try:
        cur.execute('SELECT * FROM corona_db')
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
    return send_file('corona.csv',
                     mimetype='text/csv',
                     attachment_filename='corona.csv',
                     as_attachment=True)     
        

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
