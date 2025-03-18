import numpy as np

scores = np.array([[90, 87, 56], 
                  [76, 74, 77], 
                  [56, 61, 92], 
                  [54, 49, 39]], dtype=int)

flattened_scores = scores.flatten()
print(f"Flattened scores:\n{flattened_scores}\n")

flattened_scores.sort()
print(f"Sorted ascending:\n{flattened_scores}\n")

d_flat_scores = flattened_scores[::-1]
print(f"Sorted descending:\n{d_flat_scores}\n")

transposed_scores = scores.T
print(f"Transposed scores:\n{transposed_scores}\n")

v_flipped_scores = np.flip(scores, axis=0)
print(f"Vertically flipped scores:\n{v_flipped_scores}\n")

h_flipped_scores = np.flip(scores, axis=1)
print(f"Horizontally flipped scores:\n{h_flipped_scores}\n")

reshaped_scores = np.reshape(scores, (2, 6))
print(f"Reshaped scores:\n{reshaped_scores}\n")

scores_2 = np.array([[40, 27, 16], 
                  [60, 74, 77], 
                  [10, 17, 12], 
                  [0, 0, 0]], dtype=int)

combined_scores = np.concatenate((scores, scores_2))
print(f"Concatenated scores:\n{combined_scores}\n")

h_stacked_scores = np.hstack((scores, scores_2))
print(f"Horizontally stacked scores:\n{h_stacked_scores}\n")

v_stacked_scores = np.vstack((scores, scores_2))
print(f"Vertically stacked scores:\n{v_stacked_scores}\n")

avg_scores_subjects = np.mean(scores, axis=0)
print(f"Average score for each subject:\n{avg_scores_subjects}\n")

total_scores_students = np.sum(scores, axis=1)
print(f"Total scores for each student:\n{total_scores_students}\n")

science_higher_than_math = scores[:, 1] > scores[:, 0]
print(f"Students whose Science score is higher than Math:\n{science_higher_than_math}\n")

total_scores_column = np.sum(scores, axis=1)
new_scores_with_total = np.column_stack((scores, total_scores_column))
print(f"Scores with Total Scores added:\n{new_scores_with_total}\n")

sorted_by_total_scores = new_scores_with_total[new_scores_with_total[:, -1].argsort()]
print(f"Students sorted by total scores:\n{sorted_by_total_scores}\n")

avg_score_per_subject = np.mean(scores, axis=0)
print(f"Average score per subject:\n{avg_score_per_subject}\n")