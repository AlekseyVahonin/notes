from controller.note_controller import NoteController


def main():
    note_controller = NoteController()
    try:
        note_controller.run()
    except KeyboardInterrupt:
        print("\nВыход из программы.")


if __name__ == "__main__":
   main()
