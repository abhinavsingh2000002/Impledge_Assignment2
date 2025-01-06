UPDATE Admissions SET attending_doctor_id = 29 WHERE attending_doctor_id = 3;
UPDATE Admissions SET patient_id = 4 WHERE patient_id = 35;

-- SELECT the details of Doctors(s) who has got Admissions...
SELECT DISTINCT d.*
FROM doctors d
JOIN admissions a ON d.doctor_id = a.attending_doctor_id;


--SELECT the details of Doctors(s) for whom there is no Admissions...
SELECT d.*
FROM doctors d
LEFT JOIN admissions a ON d.doctor_id = a.attending_doctor_id
WHERE a.attending_doctor_id IS NULL;


--SELECT the details of Patients(s) whose Admission can’t be completed due to missing doctor details....
SELECT p.*
FROM patients p
JOIN admissions a ON p.patient_id = a.patient_id
WHERE a.attending_doctor_id IS NULL;
