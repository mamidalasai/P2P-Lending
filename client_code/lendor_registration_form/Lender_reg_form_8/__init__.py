from ._anvil_designer import Lender_reg_form_8Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Lender_reg_form_8(Lender_reg_form_8Template):
  def __init__(self,user_id, **properties):
    self.userId = user_id
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  

  def button_1_click(self, **event_args):
    open_form('lendor_registration_form.Lender_reg_form_7')
    """This method is called when the button is clicked"""

  def button_2_click(self, **event_args):
      lending_individual = self.radio_button_1.selected
      lending_institutional = self.radio_button_2.selected
      investment = self.text_box_1.text
      lending_period = str(self.text_box_2.text)  # Convert to string
      user_id = self.userId

        # Make sure 'lending_individual' and 'lending_institutional' are passed as booleans
      anvil.server.call('add_lendor_eight_form',  bool(lending_individual), bool(lending_institutional), investment,lending_period, user_id)

      if lending_individual:
            open_form('lendor_registration_form.Lender_reg_individual_form_1')
      elif lending_institutional:
            open_form('lendor_registration_form.Lender_reg_Institutional_form_1')
        

    
    
    
