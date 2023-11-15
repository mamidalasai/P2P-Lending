from ._anvil_designer import admin_view_profile_3Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class admin_view_profile_3(admin_view_profile_3Template):
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
    self.user_type = []
    
    for i in self.data:
      a+=1
      self.list_1.append(i['spouse_name'])
      self.list_2.append(i['about'])
      self.list_3.append(i['alerts'])
      self.list_4.append(i['terms'])
      self.list_5.append(i['mail_id'])
      self.list_6.append(i['qualification'])
      self.list_7.append(i['address_type'])
      self.list_8.append(i['street'])
      self.user_type.append(i['usertype'])
    print(a)

    self.result = []
    self.index = []
    if a == -1:
      alert("No Data Available Here!")
    else:
      b = -1
      for i in self.user_type:
        b+=1
        if i == 'borrower' or i == 'Borrower':
          self.index.append(b)
          
      for i in self.index:
        self.result.append({'spouse_name' : self.list_1[i], 'about' : self.list_2[i], 'alerts' : self.list_3[i], 'terms' : self.list_4[i], 'mail_id' : self.list_5[i],
                          'qualification' : self.list_6[i], 'address_type' : self.list_7[i], 'street' : self.list_8[i]})

      self.repeating_panel_1.items = self.result
    

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.admin_view_profile.admin_view_profile_4')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.admin_view_profile.admin_view_profile_3')

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.dashboard.borrowers')
