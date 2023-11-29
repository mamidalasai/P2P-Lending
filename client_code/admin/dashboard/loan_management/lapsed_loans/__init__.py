from ._anvil_designer import lapsed_loansTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime


class lapsed_loans(lapsed_loansTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.data = tables.app_tables.loan_details.search()

    self.date_list = []
    self.payment_done = []
    
    for i in self.data:
      self.date_list.append(i['timestamp'].date())
      self.payment_done.append(i['payment_done'])

    print(self.date_list)
    print(self.payment_done)

    a = -1
    self.result = []
    for i in self.date_list:
      a += 1
      initial_date = datetime.strptime(i, '%Y-%m-%d').date()

    # Add 12 months to the initial date
    self.result.append(initial_date.months() + self.payment_done[a])
    
    # Print the resulting date
    print(result_date)
  