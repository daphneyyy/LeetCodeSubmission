-- Write a solution to find the patient_id, patient_name, and conditions of the patients who have Type I Diabetes. Type I Diabetes always starts with DIAB1 prefix.

-- Return the result table in any order.

select *
from patients
where conditions regexp '\\bDIAB1'
