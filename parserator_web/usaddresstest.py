import usaddress

addr = "215 N Norton Ave Tucson AZ 85719"

print(addr)
print(usaddress.tag(addr))

#SUDO CODE
# 1. Plug in usaddress tag function into the function class "ParseAddress".  This should receive the user input as "address".  When submitted, it will separate the address in components "address parts" and determine the address type.  This bits should be listed in tables.

# two pieces of data an arroyr of components and the address type.  As an object?  Ex: (OrderedDict([('AddressNumber', u'123'), ('StreetName', u'Main'), ('StreetNamePostType', u'St.'), ('OccupancyType', u'Suite'), ('OccupancyIdentifier', u'100'), ('PlaceName', u'Chicago'), ('StateName', u'IL')]), 'Street Address')

# 2. When a user submits an addres, the API call should receive the address and respond with the two components.

# 3. The API call script will be placed in the <script> tag of index.html

# 4.  Underneath the API, upon successful request, JS will create a table with the components and a header with the address type.  
#     If error, display error!

# 5. 