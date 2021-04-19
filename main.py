from menu import Menu, MenuCommand, ExitCommand, StartCommand, OptionCommand, AddCommand
from calendar import ListingStrategy, list_calendar

#
# w tym miejscu możesz napisać kod odpowiedzialny za menu (polecenia)
# i strategie wyświetlania wydarzeń z kalendarza
#
"""
class SecondMenuCommand(MenuCommand):

    def 

    
   execute = MenuCommand()
   execute.execute()
   executeII = ListingStrategy
   executeII.event(list_calendar())

"""

def main():
    # wydarzenia przechowuj w liście
    calendar = []

    # zakładamy, że wydarzenie to słownik z kluczami title, date, time
    # jeśli chcesz przechowywać wydarzenie w innej strukturze danych
    # to pamiętaj o zmianie jej obsługi w funkcji list_calendar
    event = {
        'title': 'Programowanie obiektowe w jezyku PYTHON - Cwiczenia',
        'date': '28.03.2020',
        'time': '12:45',
    }

    calendar.append(event)

    menu = Menu()

    # tutaj możesz dodać kolejne polecenia do menu
#    menu.add_command(MenuCommand(menu)
    menu.add_command(StartCommand(menu))
    menu.add_command(OptionCommand(menu))
    menu.add_command(AddCommand(menu))
    menu.add_command(ExitCommand(menu))
    menu.run()

main()

