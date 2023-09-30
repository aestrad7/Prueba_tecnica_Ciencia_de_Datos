class DiabetesInference:
    
    def __init__(self, model, data):
        self.model = model
        self.data_pro = data
    
    def predict(self):
        # Make predictions using the model
        predictions = self.model.predict(self.data_pro)
        return predictions