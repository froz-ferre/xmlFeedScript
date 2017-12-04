from flask import Flask, request, json, render_template
from db_connect import connection, get_schemas, get_tables_info


app = Flask(__name__)


@app.route("/")
def doc():
    return render_template('doc.html', db_list = get_schemas())

@app.route("/<db_name>")
def db_info(db_name):
    bases = get_schemas()
    if db_name in bases:
        return render_template('index.html', db_name = db_name, ti = get_tables_info(db_name) )
    else:
        return render_template('404.html')

@app.route('/src')
def files():
    return 'files' 
        


if __name__ == '__main__':
    app.run(debug=True)