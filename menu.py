'''
W tym pliku znajdziesz obsługę menu.
Aby utworzyć własny wpis w menu musisz:
1. Stworzyć nową klasę dziedziczącą po MenuCommand.
   * funkcja description() powinna zwracać napis, który zostanie wyświetlony użytkownikowi
   * funkcja execute() powinna zawierać kod, który zostanie wykonany w przypadku wywołania danej opcji w menu
2. Za pomocą funkcji add_command() dodać utworzony obiekt stworzonej przez siebie klasy do menu.
'''

#
# Może musisz zmienić zachowanie klasy Menu, aby uzyskać maksymalną liczbę punktów?
#

class MenuCommand:
    def description(self):
        '''Return menu item name.'''
        raise NotImplementedError

    def execute(self):
        '''Code will be executed on menu action.'''
        raise NotImplementedError

class StartCommand(MenuCommand):
    def __init__(self, menu):
        super().__init__()
        self._menu = menu

    def description(self):
        return "New Event"

    def execute(self):
        event =["Title: ", "Date (DD, MM, YYYY): ", "Time (HH, MM):"]
        for i in event:
            input(i)
        self._menu.run()


class OptionCommand(MenuCommand):
    def __init__(self, menu):
        super().__init__()
        self._menu = menu

    def description(self):
        return "List calendar"

    def execute(self):
        print(self._menu)

class AddCommand(MenuCommand):
    def __init__(self, menu):
        super().__init__()
        self._menu = menu

    def description(self):
        return "Export calendar to iCalendar"

    def execute(self):
        self._menu.run()


class ExitCommand(MenuCommand):
    def __init__(self, menu):
        super().__init__()
        self._menu = menu

    def description(self):
        return "Exit"

    def execute(self):
        self._menu.stop()


class Menu:
    def __init__(self):
        self._commands = []
        self._should_running = True

    def add_command(self, cmd):
        self._commands.append(cmd)


    def run(self):
        while self._should_running:
            self._display_menu()
            self._execute_selected_command()

    def stop(self):
        self._should_running = False

    def _display_menu(self):
        for i, cmd in enumerate(self._commands):
            print("{}. {}".format(i + 1, cmd.description()))

    def _execute_selected_command(self):
        cmd_num = int(input("Select menu item (1-{}): ".format(len(self._commands))))

        cmd = self._commands[cmd_num - 1]
        cmd.execute()

