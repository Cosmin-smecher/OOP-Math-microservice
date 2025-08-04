from flask import Flask, request, jsonify, render_template
from services.MathService import MathService
from db.Database import init_db, save_request_log
from models.inputs import FibonacciInput, FactorialInput, PowerInput
from pydantic import ValidationError

app = Flask(__name__)

#Inițializare DB la pornire
init_db()
math_service = MathService()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/factorial')
def factorial():
    try:
        n = request.args.get('n')
        data = FactorialInput(n=int(n))
    except (ValidationError, ValueError) as e:
        return jsonify({'error': str(e)}), 400

    result = math_service.factorial(data.n)
    save_request_log('factorial', f'n={data.n}', result)
    return jsonify({'operation': 'factorial', 'input': data.n, 'result': result})

@app.route('/fibonacci')
def fibonacci():
    try:
        n = request.args.get('n')
        data = FibonacciInput(n=int(n))
    except (ValidationError, ValueError) as e:
        return jsonify({'error': str(e)}), 400

    result = math_service.fibonacci(data.n)
    save_request_log('fibonacci', f'n={data.n}', result)
    return jsonify({'operation': 'fibonacci', 'input': data.n, 'result': result})

@app.route('/pow')
def power():
    try:
        x = request.args.get('x')
        y = request.args.get('y')
        data = PowerInput(x=float(x), y=float(y))
    except (ValidationError, ValueError) as e:
        return jsonify({'error': str(e)}), 400

    result = math_service.power(data.x, data.y)
    save_request_log('power', f'x={data.x},y={data.y}', result)
    return jsonify({'operation': 'power', 'inputs': {'x': data.x, 'y': data.y}, 'result': result})

if __name__ == '__main__':
    app.run(debug=True)
