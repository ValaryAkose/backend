
def calculate_average(backend , frontend , design):
    return ((backend + frontend + design)/3)

def get_grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "E"
    
def Report_card(name, backend , frontend , design):
    avg=calculate_average(backend , frontend , design)
    grade = get_grade(avg)
    
    return {
        'name': name,
        'Backend': backend , 
        'Frontend': frontend,
        'Design':  design,
        'average': avg,
        'grade': grade
    }


name= str(input("Enter student name:  "))
backend=  int(input("Enter the Backend score:  "))
frontend=  int(input("Enter the Frontend score:  "))
design=  int(input("Enter the Design score:  "))


final_report =Report_card(name ,backend , frontend , design)

print("\nOutput:")
print(final_report)
