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
  def __init__(self, value_to_display, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.data = tables.app_tables.loan_details.search()

    a = -1
    self.list_1 = []
    self.list_2 = []
    self.list_3 = []
    self.list_4 = []
    
    
    for i in self.data:
      a+=1
      self.list_1.append(i['loan_id'])
      self.list_2.append(i['coustmer_id'])
      self.list_3.append(i['full_name'])
      self.list_4.append(i['loan_status'])
    print(a)

    if value_to_display in self.list_2:
      b = self.list_2.index(value_to_display)
      self.label_2.text = self.list_1[b]
      self.label_4.text = self.list_2[b]
      self.label_6.text = self.list_3[b]
      self.label_8.text = self.list_4[b]

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.dashboard.loan_management.approved_loans')
    