student_contact = {"Ali": "0300-1234567"}

# Contact number update
student_contact["Ali"] = "0300-9999999"

# Updated dictionary print 
print("Updated Dictionary:", student_contact)

# Check karein ke value change hui ya nahi
if student_contact["Ali"] == "0300-9999999":
    print("Contact number successfully updated.")
else:
    print("Contact number update failed.")