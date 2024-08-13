grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

average_grades = {}

# Создание словаря с средними баллами
for i, student in enumerate(students):
  average_grades[student] = sum(grades[i]) / len(grades[i])

# Вывод результата
print(average_grades)