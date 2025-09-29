from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        return render_template('contact.html', success=True, name=name)
    return render_template('contact.html', success=False)

@app.route('/api/greet/<name>')
def greet(name):
    return jsonify({'message': f'Hello, {name}! Welcome to my Azure website!'})

if __name__ == '__main__':
    app.run(debug=True)
