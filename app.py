from flask import Flask, request, json, render_template
from db_connect import connection, get_data_base
from tables_info import TablesInfo


app = Flask(__name__)


@app.route("/")
def doc():
    return render_template('doc.html', db_list = get_data_base())

@app.route("/<db_name>")
def db_info(db_name):
    bases = get_data_base()
    if db_name in bases:
        tables_info = TablesInfo(db_name)
        return render_template('index.html', db_name = db_name)
    else:
        return render_template('404.html')

    
        


if __name__ == '__main__':
    app.run(debug=True)