from ._anvil_designer import update_formTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users

class update_form(update_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.text_box_2.text == "" or  self.text_box_3.text == "" or self.text_box_4.text == "" or self.text_box_5.text == ""  or self.text_box_7.text == "" or self.text_box_8.text == "" or self.text_box_9.text == "" or self.text_box_10.text == "" or self.text_box_11.text == "" or self.text_box_12.text == "" or self.text_box_13.text == "" or self.text_box_14.text == "" or self.text_box_15.text == "" or self.text_box_17.text == "" or self.text_box_18.text == "" or self.text_box_19.text == "" or self.text_box_20.text == "" or self.text_box_21.text == "" or self.text_box_22.text == "" or self.text_box_23.text == "" or self.text_box_24.text == "" or self.text_box_25.text == "" or self.text_box_26.text == "" or self.text_box_27.text == "" or self.text_box_28.text == "" or self.text_box_29.text == "" or self.text_box_30.text == "" or self.text_box_32.text == "" or self.text_box_33.text == "" or self.text_box_34.text == "" or self.text_box_35.text == "" :
      Notification("Fill All Required Details").show()
    else:
      data = tables.app_tables.user_profile.search()
      a = -1
      for row in data:
        a += 1

      if a == -1:
        alert("No Data Available Here")
      else:
        data[a]['full_name'] = self.text_box_2.text
        data[a]['profile_status'] = bool(self.text_box_3.text)
        data[a]['gender'] = self.text_box_4.text
        data[a]['user_age'] = int(self.text_box_5.text)
        data[a]['date_of_birth'] = self.date_picker_1.date
        data[a]['mobile'] = self.text_box_7.text
        data[a]['aadhaar_no'] = self.text_box_8.text
        data[a]['pan_number'] = self.text_box_9.text
        data[a]['city'] = self.text_box_10.text
        data[a]['last_confirm'] = bool(self.text_box_12.text)
        data[a]['mobile_check'] = bool(self.text_box_13.text)
        data[a]['mouther_tounge'] = self.text_box_14.text
        data[a]['marital_status'] = self.text_box_15.text
        data[a]['Date_mariage'] = self.date_picker_2.date
        data[a]['spouse_name'] = self.text_box_17.text
        data[a]['spouse_mobile'] = self.text_box_18.text
        data[a]['spouse_company_name'] = self.text_box_19.text
        data[a]['spouse_company_address'] = self.text_box_20.text
        data[a]['spouse_profficen'] = self.text_box_21.text
        data[a]['usertype'] = self.text_box_22.text
        data[a]['registration_approve'] = bool(self.text_box_23.text)
        data[a]['about'] = self.text_box_24.text
        data[a]['address_type'] = self.text_box_25.text
        data[a]['alerts'] = bool(self.text_box_26.text)
        data[a]['building_name'] = self.text_box_27.text
        data[a]['house_landmark'] = self.text_box_28.text
        data[a]['house_no'] = self.text_box_29.text
        data[a]['pincode'] = self.text_box_30.text
        data[a]['qualification'] = self.text_box_32.text
        data[a]['state'] = self.text_box_33.text
        data[a]['street'] = self.text_box_34.text
        data[a]['terms'] = bool(self.text_box_35.text)
        print(a)
  
    open_form('admin.dashboard.view_profile')
