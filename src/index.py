from tkinter import Tk
from ui.ui import UI

def main():

    window = Tk()
    window.title('RSA-salaus')
    user_interface = UI(window)
    user_interface.start()

    window.mainloop()

if __name__ == '__main__':
    main()
