'''from ._anvil_designer import ldTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ld(ldTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.items = app_tables.loan_disbursement.search()
  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.avlbal")

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard")

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.vblr")

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.opbal")

  def link_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.vlo")

  def link_5_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.td")

  def link_6_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.vcl")

  def link_7_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.vler")

  def link_8_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.vlfr")

  def link_9_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.rta")

  def link_10_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.vdp")

  def link_11_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.vep")

  def link_12_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.vsn")

  def link_13_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.cp")





    # Any code you write here will run before the form opens.'''


from ._anvil_designer import ldTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ld(ldTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
       # Set Form properties and Data Bindings.
        self.init_components(**properties)
        
        # Get final_rta values for all lenders
        lender_rows = app_tables.lender.search()
        
        # Calculate and display the total final_rta value
        total_final_rta = sum(row['final_rta'] for row in lender_rows)
        
        self.label_2.text = f"{total_final_rta:,}"
        
        # Get loan amounts for all customers, filtering out None values
        loan_amounts = [row['loan_amount'] for row in app_tables.loan_disbursement.search() if row['loan_amount'] is not None]

        # Calculate and display the total loan amount
        total_loan_amount = sum(loan_amounts)
        self.label_3.text = f"{total_loan_amount}"

        
        
        # Load loan disbursement data into the repeating panel
        self.repeating_panel_1.items = app_tables.loan_disbursement.search()

    def link_1_click(self, **event_args):
        """This method is called when the link is clicked"""
        open_form("lendor_registration_form.dashboard.avlbal")

    # ... (other link methods)

    def link_13_click(self, **event_args):
        """This method is called when the link is clicked"""
        open_form("lendor_registration_form.dashboard.cp")

    def button_1_click(self, **event_args):
      """This method is called when the button is clicked"""
      open_form('lendor_registration_form.dashboard')

