from ._anvil_designer import lapsed_loansTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime, timedelta


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
    m = 0
    y = 0
    for i in self.date_list:
      a += 1
      y = i.year
      m = i.month + self.payment_done[a]
      d = i.day
      if m > 12:
        m = m - self.payment_done[a]
        y += 1
      else:
        m = m + self.payment_done[a]
      date_object = datetime(y, m, d).date()
      self.result.append(date_object)
      
    print(self.result)
  