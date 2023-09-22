from weasyprint import HTML

# Define dynamic data
name = "John Doe"
age = 30
address = "123 Main Street"
city = "Anytown"
state = "CA"
zip_code = "12345"

# HTML template with placeholders for dynamic data
html_template = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Dynamic Data PDF</title>
</head>
<body>
    <h1>Personal Information</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Age:</strong> {age}</p>
    <p><strong>Address:</strong> {address}</p>
    <p><strong>City:</strong> {city}</p>
    <p><strong>State:</strong> {state}</p>
    <p><strong>Zip Code:</strong> {zip_code}</p>
</body>
</html>
"""

# Output PDF file name
output_pdf = "output.pdf"

try:
    # Generate PDF from HTML
    HTML(string=html_template).write_pdf(output_pdf)

    print(f"PDF created: {output_pdf}")
except Exception as e:
    print(f"Error creating PDF: {str(e)}")


# class Person:
#     def __init__(self, name, age, sex, weight):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.weight = weight
#         self.diagnosed_disease = None
#         self.cure = None

# def diagnose_person(person):
#     # Simulated disease diagnosis based on age, sex, and weight
#     if person.age >= 18 and person.sex == 'female' and person.weight <= 60:
#         person.diagnosed_disease = "Iron Deficiency Anemia"
#         person.cure = "Iron supplements and a balanced diet."
#     elif person.age >= 40 and person.sex == 'male' and person.weight >= 80:
#         person.diagnosed_disease = "Hypertension"
#         person.cure = "Lifestyle changes, medication, and regular check-ups."
#     else:
#         person.diagnosed_disease = "No specific disease found."
#         person.cure = "Maintain a healthy lifestyle and regular check-ups."

# if __name__ == "__main__":
#     print("Welcome to the Person's Health Report Generator.")
    
#     name = input("Enter person's name: ")
#     age = int(input("Enter person's age: "))
#     sex = input("Enter person's sex (male or female): ").lower()
#     weight = float(input("Enter person's weight (in kilograms): "))
    
#     person = Person(name, age, sex, weight)
    
#     diagnose_person(person)
    
#     print("\nHealth Report:")
#     print(f"Name: {person.name}")
#     print(f"Age: {person.age} years")
#     print(f"Sex: {person.sex}")
#     print(f"Weight: {person.weight} kilograms")
#     print(f"Diagnosed Disease: {person.diagnosed_disease}")
#     print(f"Cure/Recommendations: {person.cure}")
