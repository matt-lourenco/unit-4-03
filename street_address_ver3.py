# Created on 1 Nov 2016
# Created by: Matthew Lourenco
# This is a program that displays your address

import ui

def show_address(input_street, input_city, input_province, input_postal_code, input_apt_number = ''):
    if input_apt_number[1] == '':
        view['address_textview'].text = str(input_street[1]) + '\n' + str(input_city[1]) + ' ' + str(input_province[1]) + '\n' + str(input_postal_code[1])
    else:
        view['address_textview'].text = str(input_street[1]) + ', apartment number ' + str(input_apt_number[1]) + '\n' + str(input_city[1]) + ' ' + str(input_province[1]) + '\n' + str(input_postal_code[1])

def check_blank(input_blank_value):
    if input_blank_value[1] == '':
        view['address_textview'].text = view['address_textview'].text + input_blank_value[0] + ' cannot be blank.'
        return False
    else:
        return True

def done_touch_up_inside(sender):
    apt_number = ['Apartment number']
    street_address = ['Street address']
    city = ['City']
    province = ['Province']
    postal_code = ['Postal code']
    
    view['address_textview'].text = ''
    
    apt_number.append(str(view['apt_number_textfield'].text))
    street_address.append(str(view['street_address_textfield'].text))
    city.append(str(view['city_textfield'].text))
    province.append(str(view['province_textfield'].text))
    postal_code.append(str(view['postal_code_textfield'].text))
    
    if check_blank(street_address) and check_blank(city) and check_blank(province) and check_blank(postal_code):
        show_address(street_address, city, province, postal_code, input_apt_number = apt_number)

view = ui.load_view()
view.present('fullscreen')
