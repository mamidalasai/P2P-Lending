from ._anvil_designer import admin_view_profile_2Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class admin_view_profile_2(admin_view_profile_2Template):
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
      self.list_1.append(i['pan_number'])
      self.list_2.append(i['city'])
      self.list_3.append(i['email_user'])
      self.list_4.append(i['last_confirm'])
      self.list_5.append(i['mobile_check'])
      self.list_6.append(i['mouther_tounge'])
      self.list_7.append(i['marital_status'])
      self.list_8.append(i['Date_mariage'])
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
        self.result.append({'pan_number' : self.list_1[i], 'city' : self.list_2[i], 'email_user' : self.list_3[i], 'last_confirm' : self.list_4[i], 'mobile_check' : self.list_5[i],
                          'mouther_tounge' : self.list_6[i], 'marital_status' : self.list_7[i], 'Date_mariage' : self.list_8[i]})

      self.repeating_panel_1.items = self.result

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.admin_view_profile.admin_view_profile_3')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.admin_view_profile')

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.dashboard.borrowers')
