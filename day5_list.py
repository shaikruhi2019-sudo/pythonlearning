students = ["Ruhi", "Ghashia", "Luqman"]
print("Students list:", students)

students.append("Ananya")
print("Updated list:", students)

details = {
    "name": "Ruhi",
    "branch": "CSE",
    "year": 4
}

print("\nStudent Details")
for key, value in details.items():
    print(key, ":", value)
