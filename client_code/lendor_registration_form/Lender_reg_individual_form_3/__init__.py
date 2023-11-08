from ._anvil_designer import Lender_reg_individual_form_3Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Lender_reg_individual_form_3(Lender_reg_individual_form_3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    open_form('lendor_registration_form.Lender_reg_individual_bank_form_1')
    """This method is called when the button is clicked"""

  def button_1_click(self, **event_args):
    open_form('lendor_registration_form.Lender_reg_individual_form_2')
    """This method is called when the button is clicked"""
    
