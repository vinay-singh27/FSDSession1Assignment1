from schema import Schema, And, Use, SchemaError, SchemaMissingKeyError
import re

data1 = {'Sepal_Length': '1', 'Sepal_Width': 'a', 'Petal_Length': 'b', 'Petal_Width' : 'a'}
data2 = {'Sepal_Length': '1', 'Sepal_Width': '2', }

schema = Schema([{'Sepal_Length': Use(float),
                'Sepal_Width': Use(float),
                'Petal_Length': Use(float),
                'Petal_Width': Use(float),
                }])

# a = schema.validate(data1)
# print(a)

def parse_error_message(error_message) :

    value_error = 'ValueError'
    missing_values = 'Missing keys'

    if re.search(missing_values, error_message) :
        matches = re.search('Missing keys: (.*)', error_message)
        return 'Please enter values for : ' + matches.group(1)

    if re.search(value_error, error_message) :
        matches =  re.search('Key (.*)error', error_message)
        return 'Invalid value entered for ' + matches.group(1)

try :             
    schema.validate([data1])
except SchemaError  as error:
    error_message1 = error.code
    print(parse_error_message(error_message1))

# print('------------------------------------------------------------\n')

# try :             
#     schema.validate(data1)
# except SchemaError  as error:
#     error_message2 = error.code


# import re
# def error_type(error_message) :

#     value_error = 'ValueError'
#     missing_values = 'Missing keys'

#     if re.search(missing_values, error_message) :
#         matches = re.search('Missing keys: (.*)', error_message)
#         return 'Please enter values for : ' + matches.group(1)

#     if re.search(value_error, error_message) :
#         matches =  re.search('Key (.*)error', error_message)
#         return 'Invalid value enter for ' + matches.group(1)



# print(error_type(error_message1))
# print(error_type(error_message2))


# def exceptions(data):

#     schema = Schema([{'Sepal_Length': Use(float),
#                 'Sepal_Width': Use(float),
#                 'Petal_Length': Use(float),
#                 'Petal_Width': Use(float),
#                 }])

#     try : 
#         return (schema.validate([data]), False)

#     except SchemaError as error:
#         final_msg = "Error : " + parse_error_message(error)
#         return (final_msg, True)




# import numpy as np
# print( np.array(list(exceptions(data1)[0][0].values()) ))
