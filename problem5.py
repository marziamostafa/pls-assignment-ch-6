# record type
employee_record = {
    "Name": "Marzia Mostafa",
    "Age": 24,
    "Department": "Engineering",
    "Salary": 85000
}

# Accessing fields in the record
print(f"Employee Name: {employee_record['Name']}")
print(f"Employee Age: {employee_record['Age']}")

# Modifying a field
employee_record["Salary"] = 90000
print(f"Updated Salary: {employee_record['Salary']}")

# Adding a new field
employee_record["Position"] = "Senior Engineer"
print(f"Employee Position: {employee_record['Position']}")


print("\nFull Employee Record:")
for field, value in employee_record.items():
    print(f"{field}: {value}")