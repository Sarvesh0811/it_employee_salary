from flask import Flask, request, render_template, jsonify
from utlis import ITSalary, load_dataset
import config
from flask_cors import CORS

df = load_dataset()
salary = ITSalary()

app = Flask(__name__)
CORS(app)

@app.route('/')
def login():
    return render_template('index.html')

@app.route('/gender_options')
def gender_option():
    return jsonify(list(df['Gender'].unique()))
    
@app.route('/position_options')
def position_option():
    return jsonify(list(df['Position'].unique()))

@app.route('/predictions', methods=['GET'])  
def get_prediction():
    data = request.args    
    print(data)
    
    Gender = data.get('Gender')
    Experience = data.get('Experience')
    Position = data.get('Position')
    
    salary = ITSalary()
    pred_salary = salary.get_predicted_salary(Gender, Experience, Position)

    print(f"Predicted Salary: {pred_salary}") 
    return jsonify({'Predicted Salary': pred_salary})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=config.FLASK_PORT_NUMBER, debug=True)
