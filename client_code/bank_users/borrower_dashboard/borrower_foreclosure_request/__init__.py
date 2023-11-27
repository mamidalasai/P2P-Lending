from ._anvil_designer import borrower_foreclosure_requestTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class borrower_foreclosure_request(borrower_foreclosure_requestTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.repeating_panel_1.items=app_tables.loan_details.search()

  

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('bank_users.borrower_dashboard')

 
