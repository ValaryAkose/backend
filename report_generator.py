
def calculate_average(b_score, f_score, d_score):
    return ((b_score + f_score + d_score)/3)

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
    
def Report_card(name,b_score, f_score, d_score):
    avg=calculate_average(b_score, f_score, d_score)
    grade = get_grade(avg)
    
    return {
        'name': name,
        'Backend': b_score,
        'Frontend': f_score,
        'Design': d_score,
        'average': avg,
        'grade': grade
    }


name= str(input("Enter student name:  "))
b_score=  int(input("Enter the Backend score:  "))
f_score=  int(input("Enter the Frontend score:  "))
d_score=  int(input("Enter the Design score:  "))


final_report =Report_card(name ,b_score, f_score, d_score)

print("\nOutput:")
print(final_report)
