from ._anvil_designer import Lender_reg_individual_bank_form_2Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
#import lendor_main_form_module



class Lender_reg_individual_bank_form_2(Lender_reg_individual_bank_form_2Template):
  def __init__(self, **properties):
    #self.userId = user_id
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
        # Update the 'usertype' to 'lender' in the user_profile table
        user = anvil.users.get_user()
        
        if user is not None:
            user_email = user['email']
            user_profile = app_tables.user_profile.get(email_user=user_email)

            if user_profile is not None:
                user_profile['usertype'] = 'lender'
        alert("Successfully Submitted!")
        open_form('lendor_registration_form.dashboard')

    

      #open_form('lendor_registration_form.dashboard')

  def button_1_click(self, **event_args):
    open_form('lendor_registration_form.Lender_reg_individual_bank_form_1')
    """This method is called when the button is clicked"""
    
