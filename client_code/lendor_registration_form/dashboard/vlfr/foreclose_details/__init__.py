from ._anvil_designer import foreclose_detailsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class foreclose_details(foreclose_detailsTemplate):
  def __init__(self,selected_row, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.name.text=f"{selected_row['borrower_name']}"
    self.loan.text=f"{selected_row['loan_amount']}"
    self.reason.text=f"{selected_row['reason']}"
    self.name.text=f"{selected_row['borrower_name']}"
    self.oa.text=f"{selected_row['outstanding_amount']}"
    self.total.text=f"{selected_row['paid_amount']}"

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.vlfr")

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    Notification("")
