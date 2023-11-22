from ._anvil_designer import star_1_borrower_registration_form_begin_3a_1Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class star_1_borrower_registration_form_begin_3a_1(star_1_borrower_registration_form_begin_3a_1Template):
  def __init__(self, user_id,**properties):
    self.userId = user_id
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    street_adress_1 = self.text_box_1.text
    street_address_2 = self.text_box_2.text
    city = self.text_box_3.text
    user_id = self.userId
    if not street_adress_1 or not street_address_2 or not city:
      Notification("Please fill all the fields").show()
    else:
      anvil.server.call('add_lendor_four_form',street_adress_1,street_address_2,city,user_id)
      open_form(star_1_borrower_registration_form_begin_3a,user_id=user_id)
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form(borrower_registration_form.star_1_borrower_registration_form_begin_3.star_1_borrower_registration_form_begin_3,user_id=user_id)
