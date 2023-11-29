from ._anvil_designer import borrower_loan_closeTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class borrower_loan_close(borrower_loan_closeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.items=app_tables.loan_details.search(loan_updated_status='closed' or 'close loans' or 'close loan' or 'closedloan' or 'closed_loan')

    # Any code you write here will run before the form opens.

  def home_borrower_registration_form_copy_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('bank_users.borrower_dashboard')
