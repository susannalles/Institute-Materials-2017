from flask import Flask
from flask import render_template
from flask import request

defaults = { 'title': 'Hola... dynamic request header index.html' ,
             'header': 'Encabezado por defecto....Default "header" is used. Give request parameter header with a value to change it.',
             'paragraph': 'Si ejecutas flask-request-get-resource.py This is index.html with dynamic contents in response to a request for / (ROOT) in flask-request.py'
}

app = Flask(__name__)
@app.route("/")
def get_my_index():
    header = get_request_value_with_fallback('header')
    values = {
        'title': defaults['title'],
        'header': header,
        'paragraph': defaults['paragraph'] 
    }
    return render_template("index-dyn-dict.html", dict=values)

@app.route("/resource/<resource_name>")
def get_local_resource(resource_name = ''):
    return render_template("resource.html", resource_name=resource_name)  
    
@app.route("/catalogo/<item1>")
def get_catalogo(item1 = ''):
    return ("Aquí tienes la info del item: " + item1)

@app.route("/resource/<resource_name>/value/<value>")
def get_local_resource_with_value(resource_name = '', value = ''):
    return render_template("resource.html", resource_name=resource_name, value=value)

def get_request_value_with_fallback(key):
    if request.args.get(key):
        return request.args.get(key)
    return defaults[key]

if __name__ == '__main__':
    app.run(port=5000, debug=True)
