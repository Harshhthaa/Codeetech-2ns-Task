from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load and process your HR employee data
def load_data():
    df = pd.read_csv('HR-Employee-Attrition.csv')
    # Perform any EDA or data processing here
    return df

@app.route('/')
def index():
    df = load_data()
    # Convert the DataFrame to HTML table
    data_html = df.to_html(classes='table table-striped')
    return render_template('D:\pandu\CodeTech\EDA\Templets\index.html', data_html=data_html)

if __name__ == '__main__':
    app.run(debug=True)
