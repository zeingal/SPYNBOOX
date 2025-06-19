from tkinter import Tk
from modules.pages_home import display_home_page
from modules.navigator import navigate_to

def run_debug():
    root = Tk()
    root.title("SPYNBOOX DEBUG")
    root.geometry("480x320")
    root.configure(bg="black")

    def navigate_callback(page_name):
        navigate_to(page_name, root)

    display_home_page(root, navigate_callback)

    root.mainloop()

if __name__ == "__main__":
    run_debug()
