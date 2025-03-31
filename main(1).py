
from flask import Flask, render_template_string, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cyber.db'
db = SQLAlchemy(app)

# Delete existing database file
if os.path.exists('instance/cyber.db'):
    os.remove('instance/cyber.db')

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200), nullable=False)
    correct_answer = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)

with app.app_context():
    db.create_all()
    questions = [
        # Основной тест
        Quiz(question="Можно ли делиться паролем с друзьями?", correct_answer="Нет", category="basic"),
        Quiz(question="Нужно ли защищать свой телефон паролем?", correct_answer="Да", category="basic"),
        Quiz(question="Безопасно ли открывать письма от незнакомцев?", correct_answer="Нет", category="basic"),
        Quiz(question="Можно ли использовать один пароль везде?", correct_answer="Нет", category="basic"),
        Quiz(question="Нужно ли делать резервные копии важных файлов?", correct_answer="Да", category="basic"),
        
        # Тест по социальным сетям
        Quiz(question="Можно ли добавлять незнакомых людей в друзья?", correct_answer="Нет", category="social"),
        Quiz(question="Стоит ли публиковать свой домашний адрес в соцсетях?", correct_answer="Нет", category="social"),
        Quiz(question="Нужно ли спрашивать разрешение перед публикацией фото друга?", correct_answer="Да", category="social"),
        Quiz(question="Безопасно ли встречаться с друзьями из интернета без родителей?", correct_answer="Нет", category="social"),
        Quiz(question="Можно ли рассказывать незнакомцам о своей школе?", correct_answer="Нет", category="social"),
        
        # Тест по вредоносным программам
        Quiz(question="Безопасно ли скачивать игры с неизвестных сайтов?", correct_answer="Нет", category="malware"),
        Quiz(question="Нужен ли антивирус на компьютере?", correct_answer="Да", category="malware"),
        Quiz(question="Можно ли нажимать на яркие рекламные баннеры?", correct_answer="Нет", category="malware"),
        Quiz(question="Стоит ли обновлять программы на компьютере?", correct_answer="Да", category="malware"),
        Quiz(question="Опасно ли открывать файлы с расширением .exe от незнакомцев?", correct_answer="Да", category="malware")
    ]
    db.session.add_all(questions)
    db.session.commit()

@app.route('/')
def home():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Кибер Щит - Для Детей</title>
        <style>
            body { font-family: Arial; margin: 20px; }
            .menu { background: #f0f0f0; padding: 20px; border-radius: 10px; }
            .content { margin-top: 20px; }
            button { padding: 10px; margin: 5px; }
        </style>
    </head>
    <body>
        <h1>🛡️ Кибер Щит - Твой защитник в интернете!</h1>
        <div class="menu">
            <a href="/lesson/1"><button>Урок 1: Безопасность паролей</button></a>
            <a href="/lesson/2"><button>Урок 2: Безопасность в соцсетях</button></a>
            <a href="/lesson/3"><button>Урок 3: Защита от вирусов</button></a>
            <h3>Тесты:</h3>
            <a href="/quiz/basic"><button>Базовый тест</button></a>
            <a href="/quiz/social"><button>Тест по соцсетям</button></a>
            <a href="/quiz/malware"><button>Тест по вирусам</button></a>
        </div>
    </body>
    </html>
    ''')

@app.route('/lesson/<int:lesson_id>')
def lesson(lesson_id):
    lessons = {
        1: {
            'title': 'Безопасность паролей',
            'video': 'https://www.youtube.com/embed/dQw4w9WgXcQ',
            'content': '''
                <div class="lesson-content">
                    <h3>🔐 Как создать надёжный пароль:</h3>
                    <div class="tips-box">
                        <h4>Золотые правила:</h4>
                        <ul>
                            <li>✨ Используй длинные пароли (минимум 12 символов)</li>
                            <li>🔄 Комбинируй буквы, цифры и специальные символы</li>
                            <li>🚫 Не используй личную информацию в пароле</li>
                            <li>🔑 Используй разные пароли для разных сайтов</li>
                            <li>📱 Храни пароли в надёжном месте</li>
                        </ul>
                    </div>
                    <div class="fun-fact">
                        <h4>🎯 Интересный факт:</h4>
                        <p>Знаешь ли ты, что самый распространённый пароль в мире - "123456"? 
                           Его очень легко взломать! Давай создадим что-то более надёжное!</p>
                    </div>
                    <div class="practice">
                        <h4>🎮 Попробуй:</h4>
                        <p>Придумай пароль, используя свою любимую фразу из мультфильма и замени некоторые буквы цифрами!</p>
                    </div>
                </div>
                <ul>
                    <li>Используй длинные пароли (минимум 12 символов)</li>
                    <li>Комбинируй буквы, цифры и специальные символы</li>
                    <li>Не используй личную информацию в пароле</li>
                    <li>Используй разные пароли для разных сайтов</li>
                    <li>Храни пароли в надёжном месте</li>
                </ul>
            '''
        },
        2: {
            'title': 'Безопасность в социальных сетях',
            'video': 'https://www.youtube.com/embed/dQw4w9WgXcQ',
            'content': '''
                <h3>Правила безопасности в соцсетях:</h3>
                <ul>
                    <li>Настрой приватность профиля</li>
                    <li>Не принимай заявки от незнакомцев</li>
                    <li>Не публикуй личную информацию</li>
                    <li>Уважай других пользователей</li>
                </ul>
            '''
        },
        3: {
            'title': 'Защита от вредоносных программ',
            'video': 'https://www.youtube.com/embed/dQw4w9WgXcQ',
            'content': '''
                <h3>Как защититься от вирусов:</h3>
                <ul>
                    <li>Установи антивирус</li>
                    <li>Регулярно обновляй программы</li>
                    <li>Не скачивай файлы с непроверенных сайтов</li>
                    <li>Не открывай подозрительные письма</li>
                </ul>
            '''
        }
    }
    
    lesson = lessons.get(lesson_id)
    if not lesson:
        return redirect('/')
        
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>{{ lesson.title }} - Кибер Щит</title>
            <style>
                body { 
                    font-family: 'Arial', sans-serif; 
                    margin: 20px;
                    background-color: #f5f7fa;
                }
                .video-container { 
                    margin: 20px 0;
                    border-radius: 10px;
                    overflow: hidden;
                    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                }
                .content { 
                    margin: 20px 0;
                    padding: 20px;
                    background: white;
                    border-radius: 10px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
                }
                .lesson-content {
                    padding: 15px;
                }
                .tips-box {
                    background: #e3f2fd;
                    padding: 15px;
                    border-radius: 8px;
                    margin: 10px 0;
                }
                .fun-fact {
                    background: #fff3e0;
                    padding: 15px;
                    border-radius: 8px;
                    margin: 10px 0;
                }
                .practice {
                    background: #e8f5e9;
                    padding: 15px;
                    border-radius: 8px;
                    margin: 10px 0;
                }
                button {
                    background: #2196F3;
                    color: white;
                    border: none;
                    padding: 10px 20px;
                    border-radius: 5px;
                    cursor: pointer;
                    transition: background 0.3s;
                }
                button:hover {
                    background: #1976D2;
                }
            </style>
        </head>
        <body>
            <h1>{{ lesson.title }}</h1>
            <div class="video-container">
                <iframe width="560" height="315" src="{{ lesson.video }}" frameborder="0" allowfullscreen></iframe>
            </div>
            <div class="content">
                {{ lesson.content | safe }}
            </div>
            <a href="/"><button>На главную</button></a>
        </body>
        </html>
    ''', lesson=lesson)

@app.route('/quiz/<category>', methods=['GET', 'POST'])
def quiz(category):
    if request.method == 'POST':
        score = 0
        questions = Quiz.query.filter_by(category=category).all()
        for question in questions:
            if request.form.get(str(question.id)) == question.correct_answer:
                score += 1
        percentage = (score / len(questions)) * 100
        if percentage == 100:
            grade = "Отлично! 🌟"
            feedback = "Ты настоящий эксперт по кибербезопасности!"
        elif percentage >= 70:
            grade = "Хорошо! 👍"
            feedback = "Ты хорошо разбираешься в безопасности, но есть куда расти!"
        elif percentage >= 50:
            grade = "Удовлетворительно 🤔"
            feedback = "Неплохо, но стоит повторить материал!"
        else:
            grade = "Стоит повторить 📚"
            feedback = "Рекомендуем вернуться к урокам и попробовать снова!"

        return render_template_string('''
            <!DOCTYPE html>
            <html>
            <head>
                <title>Результаты теста - Кибер Щит</title>
                <style>
                    body { font-family: Arial; margin: 20px; text-align: center; }
                    .result { margin: 20px 0; padding: 20px; background: #f0f0f0; border-radius: 10px; }
                    .grade { font-size: 24px; color: #2196F3; margin: 10px 0; }
                    .feedback { color: #666; margin: 10px 0; }
                </style>
            </head>
            <body>
                <div class="result">
                    <h1>Твой результат: {{ score }} из {{ total }}</h1>
                    <div class="grade">{{ grade }}</div>
                    <div class="feedback">{{ feedback }}</div>
                </div>
                <a href="/lesson/{{ (category == 'basic')|int + 1 }}"><button>Повторить урок</button></a>
                <a href="/"><button>На главную</button></a>
            </body>
            </html>
        ''', score=score, total=len(questions), grade=grade, feedback=feedback, category=category)

    questions = Quiz.query.filter_by(category=category).all()
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Тест - Кибер Щит</title>
            <style>
                body { font-family: Arial; margin: 20px; }
                .question { margin: 20px 0; }
            </style>
        </head>
        <body>
            <h1>Проверь свои знания!</h1>
            <form method="POST">
                {% for question in questions %}
                <div class="question">
                    <p>{{ question.question }}</p>
                    <input type="radio" name="{{ question.id }}" value="Да"> Да
                    <input type="radio" name="{{ question.id }}" value="Нет"> Нет
                </div>
                {% endfor %}
                <button type="submit">Проверить ответы</button>
            </form>
            <a href="/"><button>На главную</button></a>
        </body>
        </html>
    ''', questions=questions)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
