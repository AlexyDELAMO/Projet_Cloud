from flask import Flask, render_template, request, jsonify
import webbrowser
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configurer la base de données SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quizzes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optionnel pour éviter les avertissements
db = SQLAlchemy(app)

# Définir le modèle Quiz
class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    questions = db.relationship('Question', backref='quiz', lazy=True)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(200), nullable=False)
    options = db.Column(db.String(300), nullable=False)  # Options sous forme de chaîne
    correct_answer = db.Column(db.String(100), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)

# Route pour afficher la page d'accueil (home.html)
@app.route('/')
def home():
    # Récupérer une liste de quiz populaires (par exemple, les 5 derniers quiz créés)
    quizzes = Quiz.query.limit(5).all()  # Vous pouvez ajuster cette requête selon vos besoins
    return render_template('home.html', quizzes=quizzes)

@app.route('/create')
def create():
    return render_template('create.html')


# Route pour afficher la page avec les quiz
@app.route('/browse-quizzes')
def browse_quizzes():
    quizzes = Quiz.query.all()  # Charger les quiz depuis la base de données
    return render_template('browse-quiz.html', quizzes=quizzes)

# Route pour afficher un quiz spécifique
@app.route('/quiz/<int:quiz_id>', methods=['GET'])
def quiz(quiz_id):
    quiz = Quiz.query.get(quiz_id)
    if quiz:
        questions = Question.query.filter_by(quiz_id=quiz_id).all()
        return render_template('quiz.html', quiz=quiz, questions=questions)
    else:
        return "Quiz not found", 404

# Route pour traiter la soumission du quiz (avec un ID de quiz spécifique)
@app.route('/submit-quiz/<int:quiz_id>', methods=['POST'])
def submit_quiz_by_id(quiz_id):
    quiz = Quiz.query.get(quiz_id)
    questions = Question.query.filter_by(quiz_id=quiz_id).all()
    user_answers = request.form  # Récupère les réponses de l'utilisateur

    results = []  # Liste pour stocker les résultats

    for question in questions:
        correct = question.correct_answer
        user_answer = user_answers.get(f"question{question.id}", None)  # Réponse de l'utilisateur
        is_correct = user_answer == correct
        results.append({
            "question_text": question.question_text,
            "correct_answer": correct,
            "user_answer": user_answer,
            "is_correct": is_correct,
            "options": question.options.split(',')  # Séparer les options
        })

    return render_template('quiz_results.html', quiz=quiz, results=results)

# Route pour créer et soumettre un nouveau quiz
@app.route('/submit-quiz', methods=['POST'])
def submit_quiz():
    # Récupérer les données du formulaire
    title = request.form['quiz-title']
    description = request.form['quiz-description']

    # Créer un nouveau quiz
    new_quiz = Quiz(title=title, description=description)
    db.session.add(new_quiz)
    db.session.commit()  # Sauvegarder le quiz dans la base de données

    # Ajouter les questions
    questions = request.form.getlist('questions[]')
    correct_answers = [request.form.get(f'correct-answer-{i+1}') for i in range(len(questions))]

    for i, question_text in enumerate(questions):
        # Récupérer les options
        options = request.form.getlist(f'answers-{i+1}[]')
        correct_answer = options[int(correct_answers[i]) - 1]  # Utiliser l'index de la bonne réponse

        # Créer une nouvelle question et l'ajouter à la base de données
        new_question = Question(
            question_text=question_text,
            options=','.join(options),
            correct_answer=correct_answer,
            quiz_id=new_quiz.id
        )
        db.session.add(new_question)

    db.session.commit()  # Sauvegarder les questions dans la base de données

    return render_template('create.html', quiz=new_quiz)  # Afficher une page confirmant la création du quiz


# API pour récupérer les quiz
@app.route('/api/quizzes')
def get_quizzes():
    quizzes = Quiz.query.all()
    quiz_list = [{"id": quiz.id, "title": quiz.title, "description": quiz.description} for quiz in quizzes]
    return jsonify(quiz_list)

if __name__ == '__main__':
    webbrowser.open("http://127.0.0.1:5000/")  # Ouvre le navigateur à l'URL du serveur local
    app.run(debug=True, host='0.0.0.0')  # Change '127.0.0.1' en '0.0.0.0'
