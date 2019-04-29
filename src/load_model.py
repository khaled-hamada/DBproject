import pickle 
#9- load the model
def load_model() :
    with open('text_classifier', 'rb') as training_model:  
         model =  pickle.load(training_model)
    return model

#load our model
model = load_model()

