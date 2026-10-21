from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)  # This exposes /metrics

# In-memory database
students = []

@app.route('/')
def index():
    # Feature: Search functionality
    search_query = request.args.get('search', '').lower()
    if search_query:
        filtered_students = [s for s in students if search_query in s.lower()]
    else:
        filtered_students = students
    
    # Feature: Dashboard metrics
    total_students = len(students)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    return render_template('index.html', 
                           students=filtered_students, 
                           total_students=total_students,
                           current_time=current_time,
                           search_query=search_query)

@app.route('/add', methods=['POST'])
def add_student():
    name = request.form.get('name')
    if name and name not in students:
        students.append(name)
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_student(id):
    # Note: Because we added search, the ID needs to match the original list
    try:
        student_to_delete = students[id]
        students.remove(student_to_delete)
    except IndexError:
        pass
    return redirect(url_for('index'))

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)