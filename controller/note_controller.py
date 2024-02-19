import datetime

from exception.empty_value_error import EmptyValueError
from exception.invalid_value_error import InvalidValueError
from model.note import Note
from model.note_manager import NoteManager
from view.console_view import ConsoleView


def display_menu():
    print("\n1. Добавить заметку")
    print("2. Редактировать заметку")
    print("3. Удалить заметку")
    print("4. Показать все заметки")
    print("5. Фильтр по дате")
    print("6. Выход")


class NoteController:
    def __init__(self):
        self.note_manager = NoteManager("notes.json")

    def run(self):
        self.note_manager.load_notes()
        while True:
            display_menu()
            choice = input("Введите команду: ")
            if choice == "1":
                self.add_note()
            elif choice == "2":
                self.edit_note()
            elif choice == "3":
                self.delete_note()
            elif choice == "4":
                self.display_notes()
            elif choice == "5":
                self.filter_notes_by_date()
            elif choice == "6":
                break
            else:
                print("Нет такой команды")

    def add_note(self):
        title, body = ConsoleView.input_note_details()
        note = Note(title, body)
        self.note_manager.add_note(note)
        self.note_manager.save_notes()
        print("Заметка успешно добавлена!")

    def edit_note(self):
        try:
            note_id = ConsoleView.input_note_id()
            note = self.note_manager.get_note_by_id(int(note_id))
            if note:
                title, body = ConsoleView.input_note_details()
                self.note_manager.update_note_by_id(int(note_id), title, body)
                self.note_manager.save_notes()
                print("Заметка успешно обновлена")
            else:
                print("Заметка не найдена!")
        except EmptyValueError as e:
            print("Произошла ошибка:", e.message)
        except InvalidValueError as e:
            print("Произошла ошибка:", e.message)

    def delete_note(self):
        try:
            note_id = ConsoleView.input_note_id()
            note = self.note_manager.get_note_by_id(int(note_id))
            if note:
                self.note_manager.delete_note_by_id(int(note_id))
                self.note_manager.save_notes()
                print("Заметка успешно удалена!")
            else:
                print("Заметка не найдена!")
        except EmptyValueError as e:
            print("Произошла ошибка:", e.message)
        except InvalidValueError as e:
            print("Произошла ошибка:", e.message)

    def display_notes(self):
        ConsoleView.display_notes(self.note_manager.notes)

    def filter_notes_by_date(self):
        date_str = ConsoleView.input_date()
        try:
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            filtered_notes = self.note_manager.filter_notes_by_date(date)
            ConsoleView.display_notes(filtered_notes)
        except ValueError:
            print("Не правильный формат даты. Введите дату в формате YYYY-MM-DD.")
