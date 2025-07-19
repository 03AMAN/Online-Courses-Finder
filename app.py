from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Load all courses from JSON
def load_courses():
    with open('courses.json', 'r') as file:
        return json.load(file)

# Filter courses by skill
def get_courses_by_skill(skill):
    courses = load_courses()
    if skill:
        return [course for course in courses if course["skill"] == skill]
    return courses

@app.route('/', methods=['GET', 'POST'])
def index():
    skill_selected = None
    filtered_courses = []
    
    if request.method == 'POST':
        skill_selected = request.form.get('skill')
        filtered_courses = get_courses_by_skill(skill_selected)
    else:
        filtered_courses = load_courses()

    return render_template('index.html', courses=filtered_courses, selected_skill=skill_selected)

if __name__ == '__main__':
    app.run(debug=True)
