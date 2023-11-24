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
  def __init__(self,get_customer_id_value,product_id, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.get = get_customer_id_value
    self.get1 = product_id
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
    open_form('log_in_form.Home.manage_products.add_groups')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    get_product_id = []
    data = app_tables.product_details.search()
    for i in data:
      get_product_id.append(i['product_id'])
    if self.get1 in get_product_id :
      b = get_product_id.index(self.get1)
     
      if self.get == 'Home Loan':
        data[b]['product_categories'] = self.drop_down_1.selected_value

      elif self.get == 'Personal Loan':
        data[b]['product_categories'] = self.drop_down_2.selected_value
     
      elif self.get == 'Vehicle Loan':
        data[b]['product_categories'] = self.drop_down_3.selected_value
     
      elif self.get == 'Business Loan':
        data[b]['product_categories'] = self.drop_down_4.selected_value
    open_form('admin.dashboard.manage_products')
