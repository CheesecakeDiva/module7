#Задание 1: "Создание мини-аналитики профиля GitHub"
from collections import Counter
import requests

def get_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    try:
        response = requests.get(url)

        if response.status_code == 404:
            print(f"Ошибка: Пользователь '{username}' не найден")
            return None

        elif response.status_code == 403:
            print("Ошибка: Превышен лимит запросов к API GitHub")
            return None

        elif response.status_code != 200:
            print(f"Ошибка: Не удалось получить данные (Статус: {response.status_code})")
            return None

        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Сетевая ошибка при подключении к GitHub: {e}")
        return None

def analyze_repos(repos):
    if not repos:
        return {
            "total_repos": 0,
            "total_stars": 0,
            "best_repo_name": "Нет",
            "best_repo_stars": 0,
            "top_languages": [],
        }

    total_repos = len(repos)
    total_stars = 0
    best_repo_name = ""
    best_repo_stars = -1
    languages = []

    for repo in repos:
        stars = repo.get("stargazers_count", 0)
        total_stars += stars

        if stars > best_repo_stars:
            best_repo_stars = stars
            best_repo_name = repo.get("name", "Неизвестно")

        lang = repo.get("language")
        if lang:
            languages.append(lang)

    language_counts = Counter(languages).most_common()

    analytics = {
        "total_repos": total_repos,
        "total_stars": total_stars,
        "best_repo_name": best_repo_name,
        "best_repo_stars": best_repo_stars,
        "top_languages": language_counts,
    }

    return analytics


def main():
    print("Задание 1. Аналитика профиля GitHub")
    username = input("Введите имя пользователя GitHub (Пример: torvalds): ").strip()
    if not username:
        print("Имя пользователя не может быть пустым")
        return

    repos = get_repos(username)

    if repos is not None:
        data = analyze_repos(repos)

        print("-" * 34)
        print(f"Аналитика профиля GitHub {username}:")
        print(f"- Количество публичных репозиториев: {data['total_repos']}")
        print(f"- Общее количество звёзд: {data['total_stars']}")

        if data["total_repos"] > 0:
            print(
                f"- Самый популярный репозиторий: "
                f"{data['best_repo_name']} (⭐ {data['best_repo_stars']})"
            )
        else:
            print("- Самый популярный репозиторий: Нет репозиториев")

        print("- Топ языков программирования:")
        if data["top_languages"]:
            for lang, count in data["top_languages"]:
                print(f"  - {lang}: {count} репозиторий(ев)")
        else:
            print("  - Нет данных о языках")


if __name__ == "__main__":
    main()

#Задание 2: Работа с API сервиса на выбор
#https://jsonplaceholder.typicode.com/

import requests

def get_todo_task():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(
                f"Ошибка: Сервер вернул код {response.status_code} вместо данных"
            )
            return None

    except requests.exceptions.RequestException as e:
        print(f"Сетевая ошибка: {e}")
        return None

def main():
    print("-" * 34)
    print("Задание 2. Работа с API сервиса на выбор")
    data = get_todo_task()

    if data:
        task_id = data.get("id", "Не указан")
        title = data.get("title", "Без названия")
        completed = data.get("completed", False)
        status = "Выполнена" if completed else "Не выполнена"

        print(f"Номер задачи: {task_id}")
        print(f"Текст задачи: {title}")
        print(f"Статус: {status}")
        print("-" * 34)
    else:
        print("\nНе удалось извлечь и обработать JSON-данные.")


if __name__ == "__main__":
    main()

