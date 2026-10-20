from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
students = []

@app.route('/')
def index():
    return render_template('index.html', students=students)

@app.route('/add', methods=['POST'])
def add_student():
    name = request.form.get('name')
    if name:
        students.append(name)
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_student(id):
    if 0 <= id < len(students):
        students.pop(id)
    return redirect(url_for('index'))

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)