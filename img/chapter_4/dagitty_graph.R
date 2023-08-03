dag {
"28 days mortality" [outcome,pos="-0.643,0.240"]
"AKI stage" [adjusted,pos="-0.289,-0.056"]
"Age at admission" [adjusted,pos="-1.131,-0.739"]
"Albumin + crystalloids" [exposure,pos="-1.167,0.233"]
"Dialysis (RRT)" [adjusted,pos="-0.321,0.238"]
"Emergency at admission" [adjusted,pos="-0.983,-0.534"]
"Heart rate" [adjusted,pos="-0.663,-0.614"]
"Insurance, Medicare" [adjusted,pos="-0.356,-0.525"]
"Mean Blood Pressure" [adjusted,pos="-0.722,-0.747"]
"Respiratory rate" [adjusted,pos="-0.222,-0.234"]
"Socio-economical factor" [latent,pos="-0.899,-0.656"]
"Urine output" [adjusted,pos="-0.196,-0.060"]
Antibiotics [adjusted,pos="-0.223,-0.609"]
Comorbidity [latent,pos="-0.605,-0.471"]
Gender [adjusted,pos="-0.973,-0.787"]
Lactate [adjusted,pos="-0.738,-0.602"]
Race [adjusted,pos="-1.018,-0.784"]
SAPSII [adjusted,pos="-0.573,-0.258"]
SOFA [adjusted,pos="-0.512,-0.379"]
SpO2 [adjusted,pos="-0.336,-0.150"]
Temperature [adjusted,pos="-0.394,-0.333"]
Vasopressors [adjusted,pos="-1.155,-0.465"]
Ventilation [adjusted,pos="-0.212,-0.480"]
Weight [adjusted,pos="-1.117,-0.629"]
lifestyle [latent,pos="-0.352,-0.736"]
"AKI stage" -> "28 days mortality"
"AKI stage" -> "Dialysis (RRT)"
"Age at admission" -> "28 days mortality"
"Age at admission" -> "Albumin + crystalloids"
"Albumin + crystalloids" -> "28 days mortality"
"Dialysis (RRT)" -> "28 days mortality"
"Emergency at admission" -> "28 days mortality"
"Emergency at admission" -> "Albumin + crystalloids"
"Heart rate" -> "28 days mortality"
"Heart rate" -> "Albumin + crystalloids"
"Insurance, Medicare" -> "28 days mortality"
"Mean Blood Pressure" -> "28 days mortality"
"Mean Blood Pressure" -> "Albumin + crystalloids"
"Respiratory rate" -> SpO2
"Socio-economical factor" -> "28 days mortality"
"Socio-economical factor" -> "Age at admission"
"Socio-economical factor" -> "Albumin + crystalloids"
"Socio-economical factor" -> Weight
"Urine output" -> "AKI stage"
Antibiotics -> "28 days mortality"
Comorbidity -> "28 days mortality"
Comorbidity -> "Albumin + crystalloids"
Comorbidity -> SAPSII
Comorbidity -> SOFA
Gender -> "28 days mortality"
Gender -> "Albumin + crystalloids"
Gender -> "Socio-economical factor"
Lactate -> "28 days mortality"
Lactate -> "Albumin + crystalloids"
Race -> "28 days mortality"
Race -> "Albumin + crystalloids"
Race -> "Socio-economical factor"
SpO2 -> "28 days mortality"
Temperature -> "28 days mortality"
Vasopressors -> "28 days mortality"
Vasopressors -> "Albumin + crystalloids"
Ventilation -> "28 days mortality"
Weight -> "28 days mortality"
Weight -> "Albumin + crystalloids"
lifestyle -> "28 days mortality"
}
