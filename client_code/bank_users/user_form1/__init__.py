from ._anvil_designer import user_form1Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class user_form1(user_form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
     alert("Logged out sucessfully")
     anvil.users.logout()
     open_form('bank_users.main_form')

  def home_main_form_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("bank_users.user_form1")
  
    

  
