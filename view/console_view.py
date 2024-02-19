from exception.empty_value_error import EmptyValueError
from exception.invalid_value_error import InvalidValueError


class ConsoleView:
    @staticmethod
    def display_notes(notes):
        for note in notes:
            print(f"ID: {note.id}, "
                  f"Название: {note.title},  "
                  f"Дата добавления: {note.created_at.strftime('%Y-%m-%d %H:%M')}, "
                  f"Дата обновления: {note.updated_at.strftime('%Y-%m-%d %H:%M')}"
                  f"\nТекст: {note.body}")

    @staticmethod
    def input_note_details():
        title = input("Введите заголовок заметки: ")
        body = input("Введите текст заметки: ")
        return title, body

    @staticmethod
    def input_note_id():
        temp = input("Введите id заметки: ")
        if not temp:
            raise EmptyValueError()
        if not temp.isdigit():
            raise InvalidValueError()
        return temp

    @staticmethod
    def input_date():
        return input("Введите дату (YYYY-MM-DD): ")
