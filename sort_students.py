"""
There is a class with m students and n exams. 
You are given a 0-indexed m x n integer matrix score, 
where each row represents one student and score[i][j] 
denotes the score the ith student got in the jth exam. 
The matrix score contains distinct integers only.

You are also given an integer k. Sort the students (i.e., 
the rows of the matrix) by their scores in the kth (0-indexed) 
exam from the highest to the lowest.
"""

"""
need to create a data structure with scores and student number actually dont need the score 
then need to just rewrite matrix using the the new data structures. 
"""
def sortTheStudents(scores, k):
    students = len(scores)
    exams = len(scores[0])
    sorted_students = [[0] * exams] * students
    sorted_students[0][0]=1
    print(sorted_students[0][0])
    print(sorted_students[1][0])
    return 0
    # dict = {}
    # scores_sorted = [0] * students
    # for i in range (students):
    #     scores_sorted[i] = scores[i][k]
    #     dict[scores_sorted[i]] = i

    # scores_sorted.sort(reverse=True)
    # print('***********')
    # for i in range(students):
    #     print(sorted_students[0])
    #     print(sorted_students[1])
    #     for j in range(exams):
    #         print(scores[i][j])
    #         #sorted_students[i][j] = scores[i][j]
    #         sorted_students[0][0] = 3
    #         break
    #     print(sorted_students[0][0])
    #     print(sorted_students[1][0])
    #     print('------------')
    #     break
    
    return sorted_students


# score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]]
# k = 2 
# print(sortTheStudents(score, k))

students = 3
exams = 4
sorted_students = [[0] * exams] * students
sorted_students[0][0]=1
print(sorted_students[0][0])
print(sorted_students[1][0])
