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
      id_list = []
      for i in data:
        id_list.append(i['coustmer_id'])

      if int(self.text_box_1.text) in id_list:
        c = id_list.index(int(self.text_box_1.text))
        data[c]['full_name'] = self.text_box_2.text
        data[c]['profile_status'] = bool(self.text_box_3.text)
        data[c]['gender'] = self.text_box_4.text
        data[c]['user_age'] = int(self.text_box_5.text)
        data[c]['date_of_birth'] = self.date_picker_1.date
        data[c]['mobile'] = self.text_box_7.text
        data[c]['aadhaar_no'] = self.text_box_8.text
        data[c]['pan_number'] = self.text_box_9.text
        data[c]['city'] = self.text_box_10.text
        data[c]['last_confirm'] = bool(self.text_box_12.text)
        data[c]['mobile_check'] = bool(self.text_box_13.text)
        data[c]['mouther_tounge'] = self.text_box_14.text
        data[c]['marital_status'] = self.text_box_15.text
        data[c]['Date_mariage'] = self.date_picker_2.date
        data[c]['spouse_name'] = self.text_box_17.text
        data[c]['spouse_mobile'] = self.text_box_18.text
        data[c]['spouse_company_name'] = self.text_box_19.text
        data[c]['spouse_company_address'] = self.text_box_20.text
        data[c]['spouse_profficen'] = self.text_box_21.text
        data[c]['usertype'] = self.text_box_22.text
        data[c]['registration_approve'] = bool(self.text_box_23.text)
        data[c]['about'] = self.text_box_24.text
        data[c]['address_type'] = self.text_box_25.text
        data[c]['alerts'] = bool(self.text_box_26.text)
        data[c]['building_name'] = self.text_box_27.text
        data[c]['house_landmark'] = self.text_box_28.text
        data[c]['house_no'] = self.text_box_29.text
        data[c]['pincode'] = self.text_box_30.text
        data[c]['qualification'] = self.text_box_32.text
        data[c]['state'] = self.text_box_33.text
        data[c]['street'] = self.text_box_34.text
        data[c]['terms'] = bool(self.text_box_35.text)
        print(c)
      else:
        alert("No data available here")
  
    

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.admin_view_profile.admin_view_profile_5')

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    data = tables.app_tables.user_profile.search()
    id_list = []
    for i in data:
      id_list.append(i['coustmer_id'])

    if int(self.text_box_1.text) in id_list:
      c = id_list.index(int(self.text_box_1.text))
      self.button_2_click()
      
        