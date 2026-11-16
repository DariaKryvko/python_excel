from implementations import Application, Qt6ApplicationGUI, TableStateImpl

def main():
    table_state = TableStateImpl()
    gui = Qt6ApplicationGUI()
    app = Application(table_state, gui)
    app.run()

if __name__ == "__main__":
    main()
