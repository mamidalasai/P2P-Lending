from ._anvil_designer import borrower_view_loansTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class borrower_view_loans(borrower_view_loansTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.items=app_tables.loan_details.search(loan_updated_status='open')
    self.repeating_panel_2.items=app_tables.loan_details.search(loan_updated_status='closed')
    self.repeating_panel_3.items=app_tables.loan_details.search(loan_updated_status='rejected')
    self.repeating_panel_4.items=app_tables.loan_details.search(loan_updated_status='underprocess')

    self.label_5.text = str(len(self.repeating_panel_1.items))
    self.label_6.text=str(len(self.repeating_panel_2.items))
    self.label_7.text=str(len(self.repeating_panel_3.items))
    self.label_8.text=str(len(self.repeating_panel_4.items))
    # Any code you write here will run before the form opens.

  def home_borrower_registration_form_copy_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('bank_users.borrower_dashboard')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.label_1.visible=True
    self.label_2.visible=False
    self.label_3.visible=False
    self.label_4.visible=False
    self.data_grid_1.visible=True
    self.data_grid_2.visible=False
    self.data_grid_3.visible=False
    self.data_grid_4.visible=False
    
  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.label_1.visible=False
    self.label_2.visible=True
    self.label_3.visible=False
    self.label_4.visible=False
    self.data_grid_1.visible=False
    self.data_grid_2.visible=True
    self.data_grid_3.visible=False
    self.data_grid_4.visible=False

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.label_1.visible=False
    self.label_2.visible=False
    self.label_3.visible=True
    self.label_4.visible=False
    self.data_grid_1.visible=False
    self.data_grid_2.visible=False
    self.data_grid_3.visible=True
    self.data_grid_4.visible=False

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.label_1.visible=False
    self.label_2.visible=False
    self.label_3.visible=False
    self.label_4.visible=True
    self.data_grid_1.visible=False
    self.data_grid_2.visible=False
    self.data_grid_3.visible=False
    self.data_grid_4.visible=True
