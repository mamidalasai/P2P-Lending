from ._anvil_designer import star_1_borrower_registration_form_begin_9Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class star_1_borrower_registration_form_begin_9(star_1_borrower_registration_form_begin_9Template):
  def __init__(self,user_id, **properties):
    self.userId = user_id
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    ifsc = self.text_box_1.text
    salary_type = self.drop_down_1.selected_value
    select_bank = self.text_box_2.text
    net_bank = self.text_box_3.text
    user_id = self.userId
    if not ifsc or not salary_type or not select_bank or not net_bank:
      Notification("please fill all required fields").show()
    else:
      anvil.server.call('add_lendor_bank_details_form_2', ifsc,salary_type,select_bank,net_bank, user_id)
      open_form('lendor_registration_form.dashboard')

  def button_1_click(self, **event_args):
    open_form('lendor_registration_form.Lender_reg_bothdirect_bank_form_1',user_id=self.userId)

  def button_3_click(self, **event_args):
    open_form("bank_users.user_form")
