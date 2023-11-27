from ._anvil_designer import borrower_approveTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class borrower_approve(borrower_approveTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Binding
    self.init_components(**properties)
    
    user=app_tables.loan_details.search()
    if user==approve:
      open_form('bank_users.borrower_dashboard.application_tracker.borrower_approve')
    # Any code you write here will run before the form opens.
