from ._anvil_designer import add_groupTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class add_group(add_groupTemplate):
  def __init__(self,product_id, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
   
    self.get = product_id
    
  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home.manage_products.view_product')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('log_in_form.Home.manage_products.manage_products1')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""    
    get_product_id = []
    data = app_tables.product_details.search()
    for i in data:
      get_product_id.append(i['product_id'])
    if self.get in get_product_id :
      b = get_product_id.index(self.get)
      data[b]['product_group'] = self.drop_down_1.selected_value
      
    get_customer_id_value = self.drop_down_1.selected_value
    open_form('admin.dashboard.manage_products.add_categories',get_customer_id_value, self.get)



