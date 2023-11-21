from ._anvil_designer import star_1_borrower_registration_form_begin_2Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class star_1_borrower_registration_form_begin_2(star_1_borrower_registration_form_begin_2Template):
  def __init__(self,user_id, **properties):
    # Set Form properties and Data Bindings.
    self.userId = user_id
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def home_borrower_registration_button_click(self, **event_args):
    open_form('bank_users.user_form')

  def borrower_registration_next_step1_button_click(self, **event_args):
    open_form('borrower_registration_form.star_1_borrower_registration_form_begin',self.userId)

  def button_2_click(self, **event_args):
    mobile_no = self.borrower_mobile_number_text_copy_1.text
    #if len(mobile_no)==0:
     # alert('enter a number')
    elif len(mobile_no)<10 or len(mobile_no)>10:
      alert('enter 10 digits number')
    user_photo = self.borrower_registration_img_file_loader.file
    alternate_email  = self.borrower_alternate_email.text
    user_id = self.userId
    if not mobile_no or not user_photo or not alternate_email:
      Notification("Please Fill The All required fileds")
    else:
      anvil.server.call('add_borrower_step2',mobile_no,user_photo,alternate_email,user_id)
      Notification("step 2 form fill up submited sucessfull")
      open_form('borrower_registration_form.star_1_borrower_registration_form_begin_3',user_id = user_id)