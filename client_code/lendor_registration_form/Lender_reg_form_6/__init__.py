from ._anvil_designer import Lender_reg_form_6Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Lender_reg_form_6(Lender_reg_form_6Template):
  def __init__(self,user_id, **properties):
    self.userId = user_id
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  

  def button_1_click(self, **event_args):
    open_form('lendor_registration_form.Lender_reg_form_5',user_id=self.userId)

  def button_2_click(self, **event_args):
      lending_type = self.lending_type_dropdown.selected_value
      investment = self.drop_down_1.selected_value
      lending_period = self.drop_down_2.selected_value  
      user_id = self.userId
      anvil.server.call('add_lendor_six_form', lending_type, investment,lending_period, user_id)

      if lending_type == 'Individual':
            open_form('lendor_registration_form.Lender_reg_individual_form_1',user_id=user_id)
      elif lending_type == 'Institutional':
            open_form('lendor_registration_form.Lender_reg_Institutional_form_1',user_id=user_id)

  def button_3_click(self, **event_args):
    open_form("bank_users.user_form")
        

    
    
    
