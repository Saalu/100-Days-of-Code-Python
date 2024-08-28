student_scores =[42, 87, 13, 56, 99, 2,200,222,350, 71, 38, 60, 17]

max_score = 0
# print(student_scores)

for score in student_scores:
    if score > max_score:
        max_score  = score

print(max_score)