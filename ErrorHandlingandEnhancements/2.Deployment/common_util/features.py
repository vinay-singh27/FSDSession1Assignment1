import math

#Write a command to create 5 the feature that create log(log_Peatal_Width)
#Will need to retrain the model on 5 features and create new model.pkl file

def process(data):

    return log_petal_length(data)


def log_petal_length(data) :

    data['log_Petal_Length'] = math.log(data['Petal_Length'])

    return data

    
