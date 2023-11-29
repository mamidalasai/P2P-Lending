from ._anvil_designer import borrower_today_duesTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import datetime
from ..import borrower_main_form_module as main_form_module 
class borrower_today_dues(borrower_today_duesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    today=datetime.now().date()
    self.repeating_panel_1.items=app_tables.loan_details.search('due_date','to')
    # Any code you write here will run before the form opens.

  def home_borrower_registration_form_copy_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('bank_users.borrower_dashboard')
