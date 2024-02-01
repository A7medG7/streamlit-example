# main.py

import streamlit as st
from streamlit_option_menu import option_menu
from home import run_home
from communication import run_communication

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        st.set_page_config(page_title="Main Menu")

        # Sidebar navigation using option_menu
        app = st.sidebar.radio('Main Menu', ['Home', 'Communication'])

        # Pages
        for a in self.apps:
            if app == a['title']:
                a['function']()

# Example usage
multi_app = MultiApp()

# Add your apps
multi_app.add_app('Home', run_home)
multi_app.add_app('Communication', run_communication)

# Run the MultiApp
multi_app.run()
