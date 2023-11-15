from ._anvil_designer import edit_formTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users

class edit_form(edit_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    


  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
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

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
   
    data = tables.app_tables.user_profile.search()

    id_list = []
    name_list = []
    status_list = []
    gender_list = []
    age_list = []
    dob_list = []
    aadhar_list = []
    pan_list = []
    city_list = []
    email_user_list = []
    last_confirm_list = []
    mobile_check_list = []
    mother_tongue_list = []
    mother_status_list = []
    date_marrige_list = []
    space_name_list = []
    about_list = []
    alets_list = []
    terms_list = []
    mail_id_list = []
    qualification_list = []
    address_type_list = []
    street_list = []
    build_name_list = []
    house_no_list = []
    landmark_list = []
    pincode_list = []
    state_list = []
    spouse_number_list = []
    company_name_list = []
    company_adress_list = []
    proffic_list = []
    user_type_list = []
    approve_list = []
    mobile_list = []
    a = -1
    for i in data:
      a+=1
      id_list.append(i['coustmer_id'])
      name_list.append(i['full_name'])
      status_list.append(i['profile_status'])
      gender_list.append(i['gender'])
      age_list.append(i['user_age'])
      dob_list.append(i['date_of_birth'])
      aadhar_list.append(i['aadhaar_no'])
      pan_list.append(i['pan_number'])
      city_list.append(i['city'])
      email_user_list.append(i['email_user'])
      last_confirm_list.append(i['last_confirm'])
      mobile_check_list.append(i['mobile_check'])
      mother_status_list.append(i['marital_status'])
      mother_tongue_list.append(i['mouther_tounge'])
      date_marrige_list.append(i['Date_mariage'])
      space_name_list.append(i['spouse_name'])
      about_list.append(i['about'])
      alets_list.append(i['alerts'])
      terms_list.append(i['terms'])
      mail_id_list.append(i['mail_id'])
      qualification_list.append(i['qualification'])
      address_type_list.append(i['address_type'])
      street_list.append(i['street'])
      build_name_list.append(i['building_name'])
      house_no_list.append(i['house_no'])
      landmark_list.append(i['house_landmark'])
      pincode_list.append(i['pincode'])
      state_list.append(i['state'])
      spouse_number_list.append(i['spouse_mobile'])
      company_name_list.append(i['spouse_company_name'])
      company_adress_list.append(i['spouse_company_address'])
      proffic_list.append(i['spouse_profficen'])
      user_type_list.append(i['usertype'])
      approve_list.append(i['registration_approve'])
      mobile_list.append(i['mobile'])

    print(id_list)
    if int(self.text_box_1.text) in id_list:
      c = id_list.index(int(self.text_box_1.text))
      self.text_box_2.text = name_list[c]
      self.text_box_3.text = bool(status_list[c])
      self.text_box_4.text= gender_list[c]
      self.text_box_5.text = age_list[c]
      self.date_picker_1.text = dob_list[c]
      self.text_box_7.text = mobile_list[c]
      self.text_box_8.text = aadhar_list[c]
      self.text_box_9.text = pan_list[c]
      self.text_box_10.text = city_list[c]
      self.text_box_12.text = bool(last_confirm_list[c])
      self.text_box_13.text = bool(mobile_check_list[c])
      self.text_box_14.text = mother_tongue_list[c]
      self.text_box_15.text = mother_status_list[c]
      self.date_picker_2.text = date_marrige_list[c]
      self.text_box_17.text = space_name_list[c]
      self.text_box_24.text = about_list[c]
      self.text_box_26.text = bool(alets_list[c])
      self.text_box_35.text = bool(terms_list[c])
      self.text_box_32.text = qualification_list[c]
      self.text_box_25.text = address_type_list[c]
      self.text_box_34.text = street_list[c]
      self.text_box_27.text = build_name_list[c]
      self.text_box_29.text = house_no_list[c]
      self.text_box_28.text = landmark_list[c]
      self.text_box_30.text = pincode_list[c]
      self.text_box_33.text = state_list[c]
      self.text_box_18.text = spouse_number_list[c]
      self.text_box_19.text = company_name_list[c]
      self.text_box_20.text = company_adress_list[c]
      self.text_box_21.text =  proffic_list[c]
      self.text_box_22.text = user_type_list[c]
      self.text_box_23.text = bool(approve_list [c])
    else:
      alert("No data available here")
      
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.admin_view_profile.admin_view_profile_5')
