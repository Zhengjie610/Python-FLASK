from flask import Flask, request, render_template

app = Flask(__name__) #create the Flask app

@app.route('/query-example')
def query_example():
    return 'Todo...'

@app.route('/form-example')
def form_example():
    language = request.args.get('language')
    return '''<h1>The language value is: %s</h1> ''' %language

@app.route('/json-example')
def json_example():
    return 'Todo...'



@app.route('/')
def root_example():
    type = request.args.get('date')
    #print(type)
    return render_template('DateTest.html',type=type)



if __name__ == '__main__':
    app.run(debug=True, port=80) #run app in debug mode on port 5000