import anvil.email
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42

@anvil.server.callable
def product_details(product_id, product_name, product_categories, processing_fee, extension_fee, membership_type, interest_type, max_days, min_days, roi, discount_coupons):
  row = app_tables.product_details.add_row(product_id=product_id,
                                           product_name=product_name,
                                           product_categories = product_categories,
                                           processing_fee=processing_fee,
                                           extension_fee=extension_fee,
                                           membership_type=membership_type,
                                           interest_type= interest_type,
                                           max_days = max_days,
                                           min_days = min_days,
                                           roi = roi,
                                           discount_coupons = discount_coupons)