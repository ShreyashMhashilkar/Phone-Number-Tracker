import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

def parse_number(num):
    ph_num = phonenumbers.parse(num,"ch")
    yourlocation = geocoder.description_for_number(ph_num,"en")
    # print(yourlocation)
    service_num = phonenumbers.parse(num,"RO")
    service_provider = carrier.name_for_number(service_num,"en")
    # print(service_provider)
    return [yourlocation,service_provider]
    


