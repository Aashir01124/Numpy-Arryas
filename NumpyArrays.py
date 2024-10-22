import numpy as np
dataType = [('Name', 'S15'), ('class', int), ('Height', float)]
StudentDetails = [('James', 7, 152.8), ('John', 8, 164.3), ('Ben', 7, 162.6), ('Batman', 10, 183.2)]
Students = np.array(StudentDetails, dtype = dataType)
print("Original Array :")
print(Students)
print("Sort by height:")
print(np.sort(Students, order = 'Height'))