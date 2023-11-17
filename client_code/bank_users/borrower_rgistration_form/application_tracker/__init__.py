from ._anvil_designer import application_trackerTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import borrower_main_form_module

class application_tracker(application_trackerTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    #self.user_id=main_form_module.userId
    self.user_id=1000
    # Any code you write here will run before the form opens.
    self.repeating_panel_5.items=app_tables.loan_details.get(coustmer_id=self.user_id)
    if self.repeating_panel_5:
      
      alert("Loan already exists for this user.")
    else:
      alert("No existing loan for this user.")
  def home_borrower_registration_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('bank_users.borrower_rgistration_form')
