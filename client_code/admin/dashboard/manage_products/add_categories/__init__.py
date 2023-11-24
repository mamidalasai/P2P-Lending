from ._anvil_designer import add_categoriesTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class add_categories(add_categoriesTemplate):
  def __init__(self,get_customer_id_value, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.get = get_customer_id_value
    print(self.get)
    if self.get == 'Home Loan':
      self.label_2.visible = True
      self.drop_down_1.visible = True
      self.label_3.visible = False
      self.drop_down_2.visible = False
      self.label_4.visible = False
      self.drop_down_3.visible = False
      self.label_5.visible = False
      self.drop_down_4.visible = False
    elif self.get == 'Personal Loan':
      self.label_2.visible = False
      self.drop_down_1.visible = False
      self.label_3.visible = True
      self.drop_down_2.visible = True
      self.label_4.visible = False
      self.drop_down_3.visible = False
      self.label_5.visible = False
      self.drop_down_4.visible = False
    elif self.get == 'Vehicle Loan':
      self.label_2.visible = False
      self.drop_down_1.visible = False
      self.label_3.visible = False
      self.drop_down_2.visible = False
      self.label_4.visible = True
      self.drop_down_3.visible = True
      self.label_5.visible = False
      self.drop_down_4.visible = False
    elif self.get == 'Business Loan':
      self.label_2.visible = False
      self.drop_down_1.visible = False
      self.label_3.visible = False
      self.drop_down_2.visible = False
      self.label_4.visible = False
      self.drop_down_3.visible = False
      self.label_5.visible = True
      self.drop_down_4.visible = True

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.dashboard.manage_products.add_group')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    
