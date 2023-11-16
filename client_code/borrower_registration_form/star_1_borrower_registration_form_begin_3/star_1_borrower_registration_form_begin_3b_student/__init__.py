from ._anvil_designer import star_1_borrower_registration_form_begin_3b_studentTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class star_1_borrower_registration_form_begin_3b_student(star_1_borrower_registration_form_begin_3b_studentTemplate):
  def __init__(self, **properties):
    self.user_id=user_id
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run before the form opens.

  def button_1_copy_1_copy_1_copy_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('borrower_registration_form.star_1_borrower_registration_form_begin_3.star_1_borrower_registration_form_begin_3c',use_id=user_id)

  def home_borrower_registration_form_copy_1_click(self, **event_args):
    open_form('bank_users.user_form')

  def button_1_next_copy_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    college_name=self.borrower_college_name_text.text
    college_id=self.borrower_college_id_text.text
    college_proof=self.borrower_college_proof_img.file
    college_address=self.borrower_college_address_text
    user_id=self.user_id
    if not college_name or not college_id or not college_proof or not college_address:
      Notification("please fill all requrired fields").show()
    else:
      open_form('borrower_registration_form.star_1_borrower_registration_form_begin_4',user_id=self.userId)
