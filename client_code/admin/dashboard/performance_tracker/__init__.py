from ._anvil_designer import performance_trackerTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class performance_tracker(performance_trackerTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.data = tables.app_tables.loan_details.search()

    self.name_list = []
    
    a = 0
    for i in self.data:
      self.name_list.append(i['loan_updated_status'])
      
      a += 1
    self.label_9.text = a
    



    a

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard')


    
      
      

    
      