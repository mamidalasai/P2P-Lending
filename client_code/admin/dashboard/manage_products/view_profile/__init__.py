from ._anvil_designer import view_profileTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class view_profile(view_profileTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.data = tables.app_tables.product_details.search()
    
    self.id_list = []
    self.name_list = []
    self.categories_list = []
    self.profee_list = []
    self.extfee_list = []
    self.type_list = []
    self.int_type = []
    self.max_days = []
    self.min_days = []
    self.roi = []
    self.dis_cou = []

    a = -1
    for i in self.data:
      a+=1
      self.id_list.append(i['product_id'])
      self.name_list.append(i['product_name'])
      self.categories_list.append(i['product_categories'])
      self.profee_list.append(i['processing_fee'])
      self.extfee_list.append(i['extension_fee'])
      self.type_list.append(i['membership_type'])
      self.int_type.append(i['interest_type'])
      self.max_days.append(i['max_days'])
      self.min_days.append(i['min_days'])
      self.roi.append(i['roi'])
      self.dis_cou.append(i['discount_coupons'])

    print(self.company_adress_list)
    if a == -1:
      alert("No Data Available Here!!")
    else:
      if value_to_display in self.id_list:
        b = self.id_list.index(value_to_display)
        
      