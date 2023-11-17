from ._anvil_designer import Lender_reg_Institutional_form_3Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Lender_reg_Institutional_form_3(Lender_reg_Institutional_form_3Template):
  def __init__(self,user_id, **properties):
    self.userId = user_id
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    industry_type = self.text_box_1.text
    turn_over = self.text_box_2.text
    last_six_statements = self.file_loader_1.file
    user_id = self.userId
    anvil.server.call('add_lendor_institutional_form_3',industry_type,turn_over,last_six_statements,user_id)
    open_form('lendor_registration_form.Lender_reg_Institutional_form_4',user_id = user_id)
    """This method is called when the button is clicked"""

  def button_1_click(self, **event_args):
    user_id = self.userId
    open_form('lendor_registration_form.Lender_reg_Institutional_form_2',user_id = user_id)
    """This method is called when the button is clicked"""

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("bank_users.user_form")
    
