grades = [('Ann', 9), ('John', 7), ('Smith', 5), ('George', 6)]
sort_grades = sorted(grades, lambda l1, l2: l2[1] -  l1[1])
for i in range(len(sort_grades)):
    print('Hello {0}! Your grade is {1}'.format(sort_grades[i][0], sort_grades[i][1]))
