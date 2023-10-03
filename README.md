# Prueba_tecnica_Ciencia_de_Datos
Realizar un modelo de predicción que determine si un paciente será readmitido en el hospital en menos de 30 días.

- Eliminamos estas variables del proceso de datos con baja correlacion o muy desbalanceadas
- Encoder = ['age', 'admission_type_id', 'discharge_disposition_id',
       'time_in_hospital', 'medical_specialty', 'num_lab_procedures',
       'num_procedures', 'num_medications', 'number_outpatient',
       'number_emergency', 'number_inpatient', 'number_diagnoses',
       'max_glu_serum', 'A1Cresult', 'metformin', 'repaglinide', 'change',
       'diabetesMed', 'readmitted']
---
- Transformamos variables (TODAS??)
  - Log
  - standar
---
- Imputamos faltantes
- modelamos y evaluamos modelos
