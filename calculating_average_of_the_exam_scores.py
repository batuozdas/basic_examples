# In this example average of student's scores will be calculated. Firstly, student's scores will be taken from the user.
# There will be 2 scores. One of them is called midterm exam, other is called final exam. Now final scores will be
# calculated from this scores, while midterm exam will be affecting the final score 40 percent, final exam will affect
# the final score 60 percent. In other words, the final score will be equal to (0.4*midterm exam score + 0.6*final exam score).
# After that, the average of midterm exam scores, the average of final exam scores and the average of final scores will
# be calculated.
# !!! Please do not confuse the 'final score' with the 'final exam score'. (final score = 0.4*midterm exam score + 0.6*final exam score)


# Firstly, we are taking information that how many students user has.
number_of_students = int(input('Please enter the number of students:'))

# Then, we are creating empty series to be filled later by the user.
final_scores = []
midterm_exam_scores = []
final_exam_scores = []

midterm_exam_pct = 0.4 # Percentage of midterm exam
final_exam_pct = 0.6 # Percentage of final exam
# Final scores will be calculated according to these percentage values. If you want, you can change these values.

# We are getting in a for loop. For loop will continue until 'i' value will reach the value of number_of_students.
for i in range(1,number_of_students+1):
    midterm_exam_score = int(input("Student's midterm exam score:")) # We are asking midterm exam score of every student.
    final_exam_score = int(input("Student's final exam score:")) # We are asking final exam score of every student.
    final_score = (midterm_exam_score * midterm_exam_pct) + (final_exam_score * final_exam_pct)  # Calculating the final score.
    print("This student's final score is: {}".format(final_score))
    midterm_exam_scores.append(midterm_exam_score) # We are adding midterm_exam_score value to our empty midterm_exam_scores series.
    final_exam_scores.append(final_exam_score) # We are adding final_exam_score value to our empty final_exam_scores series.
    final_scores.append(final_score) # We are adding final_score value to our empty final_scores series.

print('********************************************************************')
print("Midterm exam scores of the students: {}".format(midterm_exam_scores))
print("Final exam scores of the students: {}".format(final_exam_scores))
print("Final scores of the students: {}".format(final_scores))

# midterm_exam_scores, final_exam_scores and final_scores series will have the same length with the number of students.

# Now we can calculate the average of the scores.

# Average of the final scores;
total_score = 0 # We are creating a value named total_score and we are equating it to 0. The reason we are doing this
#is to calculate the sum of scores. We will get in a for loop. After each loop, this value will be updated.
for i in final_scores:
    total_score += i # Every loop, total_score will be increased by the value of i.
final_scores_average = total_score / len(final_scores) # And finally average will be equal to (sum of final scores / number of students)

# Average of the final_exam_scores;
total_score = 0
for i in final_exam_scores:
    total_score += i
final_exam_scores_average = total_score / len(final_exam_scores)

# Average of the midterm_exam_scores;
total_score = 0
for i in midterm_exam_scores:
    total_score += i
midterm_exam_scores_average = total_score / len(midterm_exam_scores)

print('********************************************************************')
print("Average of the midterm exam scores: {}".format(midterm_exam_scores_average))
print("Average of the final exam scores: {}".format(final_exam_scores_average))
print("Average of the final scores: {}".format(final_scores_average))







































    






















































