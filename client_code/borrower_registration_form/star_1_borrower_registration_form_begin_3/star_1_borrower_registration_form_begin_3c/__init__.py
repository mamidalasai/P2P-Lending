from ._anvil_designer import star_1_borrower_registration_form_begin_3cTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class star_1_borrower_registration_form_begin_3c(star_1_borrower_registration_form_begin_3cTemplate):
  def __init__(self,user_id, **properties):
    self.userId = user_id
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def home_borrower_registration_form_copy_1_click(self, **event_args):
    open_form('bank_users.user_form')

  def button_1_copy_1_copy_1_click(self, **event_args):
    open_form('borrower_registration_form.star_1_borrower_registration_form_begin_3.star_1_borrower_registration_form_begin_3a',user_id=self.userId)

  def button_1_next_click(self, **event_args):
    status_of_user = self.Profesion_borrower_registration_form_drop_down.selected_value
    user_id = self.userId
    anvil.server.call('add_borrower_step3c',status_of_user,user_id)
    if status_of_user == 'Student':
      open_form('borrower_registration_form.star_1_borrower_registration_form_begin_3.star_1_borrower_registration_form_begin_3b_student',user_id=user_id)
    elif status_of_user == 'Employee':
      open_form('borrower_registration_form.star_1_borrower_registration_form_begin_3.star_1_borrower_registration_form_begin_3d',user_id=user_id)
    else:
      open_form('borrower_registration_form.star_1_borrower_registration_form_begin_3.star_1_borrower_registration_form_begin_3b_business',user_id=user_id)
    
