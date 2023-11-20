from ._anvil_designer import manage_productsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class manage_products(manage_productsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_copy_click(self, **event_args):
    """This method is called when the link is clicked"""
      
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""

    product_id = self.text_box_1.text
    product_name = self.text_box_2.text
    product_discription = self.text_area_1.text
    product_categories = self.drop_down_1.selected_value
    processing_fee = self.text_box_3.text
    extension_fee = self.text_box_4.text
    discount_coupons = self.radio_button_3.selected
    membership_type = self.drop_down_2.selected_value
    print(membership_type)
    interest_type = self.radio_button_1.selected
    if interest_type :
      print(self.radio_button_1.text)
    else :
      print(self.radio_button_2.text)
    min_days = self.drop_down_3.selected_value
    print(min_days)
    max_days = self.drop_down_4.selected_value
    print(max_days)
    roi = self.text_box_5.text
    print(roi)

    if product_id == "" or product_name == "" or membership_type == "" or processing_fee == "" or extension_fee == "" or interest_type == "" or max_days == "" or min_days == "" or product_categories == "" or discount_coupons == "" or roi == "":
      Notification("Fill All Required Details").show()
    else:
      anvil.server.call('product_details',
                        product_id,
                        product_name,
                        membership_type,
                        processing_fee,
                        extension_fee,
                        interest_type,
                        max_days,
                        min_days,
                        product_discription,
                        discount_coupons,
                        roi)
      alert("Submitted succesfully")


