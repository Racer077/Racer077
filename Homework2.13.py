#№1#
import json
class UserProfile:
    def __init__(self, name, age, interests):
        self.name = name
        self.age = age
        self.interests = interests
    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'interests': self.interests
        }
    @classmethod
    def from_dict(cls, data):
        try:
            name = data['name']
            age = data['age']
            interests = data['interests']
            return cls(name, age, interests)
        except KeyError as e:
            raise ValueError(f"Отсутствует обязательное поле: {e}")
def save_profile(user_profile, filename):
    try:
        with open(filename, 'w') as f:
            json.dump(user_profile.to_dict(), f, indent=4)
    except Exception as e:
        raise IOError(f"Ошибка при сохранении профиля: {e}")
def load_profile(filename):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        return UserProfile.from_dict(data)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл не найден: {filename}")
    except json.JSONDecodeError:
        raise ValueError("Невалидный JSON")
    except ValueError as e:
        raise ValueError(f"Ошибка при загрузке профиля: {e}")
    except Exception as e:
        raise IOError(f"Неизвестная ошибка при загрузке: {e}")
if __name__ == '__main__':
    try:
        user = UserProfile("Alice", 25, ["Python", "AI"])
        save_profile(user, "profile.json")
        print("Профиль успешно сохранен в profile.json")
        new_user = load_profile("profile.json")
        print("Профиль успешно загружен из profile.json")
        print(f"Имя: {new_user.name}, Возраст: {new_user.age}, Интересы: {new_user.interests}")
    except (IOError, ValueError, FileNotFoundError) as e:
        print(f"Произошла ошибка: {e}")
    try:
        with open("profile.json", "w") as f:
            f.write("{'name': 'Bob', 'age': 30") 
        load_profile("profile.json")
    except (IOError, ValueError, FileNotFoundError) as e:
        print(f"Произошла ошибка (поврежденный JSON): {e}")
    try:
        with open("profile.json", "w") as f:
            json.dump({"name": "Bob", "interests": ["Coding"]}, f) 
        load_profile("profile.json")
    except (IOError, ValueError, FileNotFoundError) as e:
        print(f"Произошла ошибка (отсутствует поле): {e}")
    try:
        load_profile("nonexistent_profile.json")
    except (IOError, ValueError, FileNotFoundError) as e:
        print(f"Произошла ошибка (файл не найден): {e}")


#№2#
import pickle
import os
class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
        self.completed = False
    def __repr__(self):
        return f"Task(name='{self.name}', priority={self.priority}, completed={self.completed})"
def load_tasks(filename="tasks.pickle"):
    try:
        with open(filename, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []
    except EOFError: 
        return []
    except Exception as e:
        print(f"Ошибка при загрузке задач: {e}")
        return [] 
def save_tasks(tasks, filename="tasks.pickle"):
    try:
        with open(filename, 'wb') as f:
            pickle.dump(tasks, f)
    except Exception as e:
        print(f"Ошибка при сохранении задач: {e}")
def add_task(tasks, name, priority):
    tasks.append(Task(name, priority))
def remove_task(tasks, name):
    tasks[:] = [task for task in tasks if task.name != name] 
def mark_completed(tasks, name):
    for task in tasks:
        if task.name == name:
            task.completed = True
            break  
if __name__ == '__main__':
    filename = "tasks.pickle"
    tasks = load_tasks(filename)
    add_task(tasks, "Купить хлеб", 1)
    add_task(tasks, "Выучить Python", 2)
    add_task(tasks, "Помыть посуду", 3)
    save_tasks(tasks, filename)
    print("Задачи добавлены и сохранены.")
    loaded_tasks = load_tasks(filename)
    print("Загруженные задачи:")
    for task in loaded_tasks:
        print(task)
    mark_completed(loaded_tasks, "Купить хлеб")
    print("\nЗадача 'Купить хлеб' помечена как выполненная.")
    remove_task(loaded_tasks, "Помыть посуду")
    print("\nЗадача 'Помыть посуду' удалена.")
    save_tasks(loaded_tasks, filename)
    print("Измененный список задач сохранен.")
    final_tasks = load_tasks(filename)
    print("\nОкончательный список задач:")
    for task in final_tasks:
        print(task)