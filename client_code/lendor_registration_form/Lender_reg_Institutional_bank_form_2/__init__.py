from ._anvil_designer import Lender_reg_Institutional_bank_form_2Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Lender_reg_Institutional_bank_form_2(Lender_reg_Institutional_bank_form_2Template):
  def __init__(self,user_id, **properties):
    self.userId = user_id
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    open_form('lendor_registration_form.dashboard')

  def button_1_click(self, **event_args):
    open_form('lendor_registration_form.Lender_reg_Institutional_bank_form_1',user_id=self.userId)
    
