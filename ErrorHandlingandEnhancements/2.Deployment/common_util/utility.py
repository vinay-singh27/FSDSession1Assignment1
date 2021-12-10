from schema import Schema, Use, SchemaError
import re

#Write code here for exception handling

def exceptions(df):

    schema = Schema([{'Sepal_Length': Use(float),
                'Sepal_Width': Use(float),
                'Petal_Length': Use(float),
                'Petal_Width': Use(float),
                }])

    try : 
        output = schema.validate([df])[0]
        error_status = False

    except SchemaError as error:
        output =  parse_error_message(error.code)
        error_status = True

    return (output, error_status)


def parse_error_message(error_message) :

    value_error = 'ValueError'
    missing_values = 'Missing keys'

    if re.search(missing_values, error_message) :
        matches = re.search('Missing keys: (.*)', error_message)
        return 'Please provide values(float) for : ' + matches.group(1)

    #add generic exception to handle to make it as exhaustive

    if re.search(value_error, error_message) :
        matches =  re.search('Key (.*)error', error_message)
        return 'Invalid value entered for ' + matches.group(1) + '. Please provide float value '



        
    

    