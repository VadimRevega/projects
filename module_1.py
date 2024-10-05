grades=[[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
student={"Johnny",'Biilbo','Steve','Khendrik','Aaron'}


students_list =sorted(student) # упорядоченная последовательность имён всех учеников в классе

print("список студентов", students_list)
print(grades)

score_sum = [sum(grades[0])/len(grades[0]),
            sum(grades[1])/len(grades[1]),
            sum(grades[2])/len(grades[2]),
            sum(grades[3])/len(grades[3]),
            sum(grades[4])/len(grades[4])]


dictionary = dict(zip(students_list, score_sum))

print('Средняя оценка студентов :',dictionary)