#Задание 1: Простые маршруты
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return ("Главная страница. Попробуйте перейти на:<br>"
            "/hello или /info<br>"
            "/calc/3/5<br>"
            "/reverse/hello<br>"
            "/reverse/python<br>"
            "/user/Anna/25<br>"
            "/user/John/30<br>"
            "/calc/a/b<br>"
            "/reverse/<br>"
            "/user/John/-2")

@app.route('/hello')
def hello():
    return "Hello, world!"

@app.route('/info')
def info():
    return "This is an informational page."

#Задание 2: Динамические маршруты
@app.route('/calc/<num1>/<num2>')
def calc(num1, num2):
    try:
        n1 = float(num1)
        n2 = float(num2)
        result = n1 + n2
        return f"The sum of {n1} and {n2} is {result}."
    except ValueError:
        return "Ошибка: введите корректные числа в адресную строку (например, /calc/5/10).", 400


#Задание 3. Создайте маршрут /reverse/, который переворачивает текст
@app.route('/reverse/')
@app.route('/reverse/<text>')
def reverse_text(text=""):
    if not text.strip():
        return "Ошибка: текст должен содержать хотя бы один символ.", 400
    return text[::-1]


#Задание 4. Реализуйте маршрут /user//, возвращающий:"Hello, {name}.
#You are {age} years old.".
@app.route('/user/<name>/<age>')
def user_info(name, age):
    try:
        age_num = int(age)
        if age_num < 0:
            return "Ошибка: возраст не может быть меньше 0.", 400
        if age_num > 120:
            return "Ошибка: введен слишком большой возраст.", 400
        return f"Hello, {name}. You are {age_num} years old."
    except ValueError:
        return "Ошибка: возраст должен быть целым числом.", 400


if __name__ == "__main__":
    app.run(debug=True)
