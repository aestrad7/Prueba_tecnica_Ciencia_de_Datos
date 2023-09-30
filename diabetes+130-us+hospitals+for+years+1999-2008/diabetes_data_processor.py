from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import joblib


class DiabetesDataProcessor:
    
    def __init__(self, data_test):
    #     self.final_colums = ['encounter_id', 'patient_nbr', 'race', 'gender', 'age',
    #    'admission_type_id', 'discharge_disposition_id', 'admission_source_id',
    #    'time_in_hospital', 'num_lab_procedures', 'num_procedures',
    #    'num_medications', 'number_outpatient', 'number_emergency',
    #    'number_inpatient', 'diag_1', 'diag_2', 'diag_3', 'number_diagnoses',
    #    'max_glu_serum', 'A1Cresult', 'metformin', 'glipizide', 'glyburide',
    #    'insulin', 'change', 'diabetesMed', 'readmitted', 'total_meds',
    #    'severity_indicator']
        self.scaler = joblib.load('scaler.pkl')
        self.median_value = joblib.load('median_time_in_hospital.pkl')
        self.encoder = joblib.load('encoders.pkl')
        self.colums_log = ['num_procedures', 'number_outpatient', 'number_emergency', 'number_inpatient', 'time_in_hospital']
        self.colums_stand = ['num_lab_procedures', 'number_diagnoses', 'num_medications']
        self.data_test = data_test
        
    def encode(self):
        for column, label_encoder in self.encoder.items():
            if column in self.data_test.columns:
                self.data_test[column] = label_encoder.transform(self.data_test[column])
        return self.data_test
    
    def transform_log(self):
        for col in self.colums_log:
            self.data_test[col] = self.data_test[col].apply(lambda x: np.log1p(x))
        return self.data_test
    
    def standardize(self):
        self.data_test[self.colums_stand] = self.scaler.transform(self.data_test[self.colums_stand])
        return self.data_test
    
    def create_features(self):
        self.data_test['total_meds'] = self.data_test['metformin'] + self.data_test['glipizide'] + self.data_test['glyburide'] + self.data_test['insulin']
        self.data_test['severity_indicator'] = self.data_test['number_outpatient'] + self.data_test['number_emergency'] + self.data_test['number_inpatient']
        return self.data_test
    
    def impute_missing(self, column = 'time_in_hospital'):
        if not self.median_value:
            self.median_value = self.data_test[column].median() # suponiendo que no cambia la distribución en X_train
        self.data_test[column].fillna(self.median_value, inplace=True)
        return self.data_test
    
    def process_data(self):
        self.data_test = self.create_features() #TODO: estas variables no estan dentro del encoder, hay que crearlas
        self.data_test = self.encode()
        self.data_test = self.transform_log()
        self.data_test = self.standardize()
        self.data_test = self.impute_missing('time_in_hospital')
        return self.data_test[[self.final_colums]]
