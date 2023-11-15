from ._anvil_designer import admin_view_profile_5Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class admin_view_profile_5(admin_view_profile_5Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.data = tables.app_tables.user_profile.search()

    a = -1
    self.list_1 = []
    self.list_2 = []
    self.list_3 = []
    
    for i in self.data:
      a+=1
      self.list_1.append(i['spouse_profficen'])
      self.list_2.append(i['usertype'])
      self.list_3.append(i['registration_approve'])
      
    print(a)

    self.result = []
    self.index = []
    if a == -1:
      alert("No Data Available Here!")
    else:
      b = -1
      for i in self.list_2:
        b+=1
        if i == 'borrower' or i == 'Borrower':
          self.index.append(b)
          
      for i in self.index:
        self.result.append({'spouse_profficen' : self.list_1[i], 'usertype' : self.list_2[i], 'registration_approve' : self.list_3[i]})

      self.repeating_panel_1.items = self.result

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.admin_view_profile.admin_view_profile_4')

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.dashboard.borrowers')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.view_profile.edit_form')

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.view_profile.update_form')
