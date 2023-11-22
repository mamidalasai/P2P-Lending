from ._anvil_designer import admin_view_profile_4Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class admin_view_profile_4(admin_view_profile_4Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.data = tables.app_tables.user_profile.search()

    a = -1
    self.list_1 = []
    self.list_2 = []
    self.list_3 = []
    self.list_4 = []
    self.list_5 = []
    self.list_6 = []
    self.list_7 = []
    self.list_8 = []
    
    for i in self.data:
      a+=1
      self.list_1.append(i['building_name'])
      self.list_2.append(i['house_no'])
      self.list_3.append(i['house_landmark'])
      self.list_4.append(i['pincode'])
      self.list_5.append(i['state'])
      self.list_6.append(i['spouse_mobile'])
      self.list_7.append(i['spouse_company_name'])
      self.list_8.append(i['spouse_company_address'])
    print(a)

    self.result = []
    if a == -1:
      alert("No Data Available Here!")
    else:
      for i in range(a+1):
        print(self.list_2[i])
        self.result.append({'building_name' : self.list_1[i], 'house_no' : self.list_2[i], 'house_landmark' : self.list_3[i], 'pincode' : self.list_4[i], 'state' : self.list_5[i],
                          'spouse_mobile' : self.list_6[i], 'spouse_company_name' : self.list_7[i], 'spouse_company_address' : self.list_8[i]})

      self.repeating_panel_1.items = self.result
    

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.admin_view_profile.admin_view_profile_5')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.admin_view_profile.admin_user_profile_3')
