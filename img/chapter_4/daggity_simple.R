dag {
"28 days mortality" [outcome,pos="-0.289,1.089"]
"Albumin + crystalloids" [exposure,pos="-0.739,1.081"]
"albumin stock" [pos="-0.858,0.769"]
Age [pos="-0.196,0.787"]
Sofa [adjusted,pos="-0.536,0.790"]
"Albumin + crystalloids" -> "28 days mortality"
"albumin stock" -> "Albumin + crystalloids"
Age -> "28 days mortality"
Sofa -> "28 days mortality"
Sofa -> "Albumin + crystalloids"
}
