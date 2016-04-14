"""
results_table.py

Takes the table of accuracies generated by MATLAB, and populates the LaTeX table values
"""
from scipy.io import loadmat
import numpy as np

# MARKUS: change this line to the path of your .mat file
mat_file = 'crossval_accuracy_table_1e-9.mat'

f = loadmat(mat_file)
# A: array-like, shape (5,10)
    # rows are p value (0, 2, 3, 4, 5)
    # first 5 cols are train for C values...
    # second 5 cols are test for C values...
# MARKUS: change the dictionary key to the name of the matrix in MATLAB
A = f['final_accuracy_table'] # final_accuracy_table was the variable name of my matrix in MATLAB when I saved the .mat file

# sample nums to test
# nums = tuple(range(42))

soft = (np.array([0, 1, 2, 3, 5, 6, 7, 8]))

nums = [A[0,4], A[0, 9]] # train test hard linear
nums.extend(list(A[1:,4])) # hard polynomial train
nums.extend(list(A[1:,9])) # hard polynomial test
nums.extend(list(A[1, soft])) # p = 2, soft polynomial train test
nums.extend(list(A[2, soft])) # p = 3, soft polynomial train test
nums.extend(list(A[3, soft])) # p = 4, soft polynomial train test
nums.extend(list(A[4, soft])) # p = 5, soft polynomial train test
print len(nums)
nums = tuple(nums)

print nums

latex_table = """
\\begin{table*}
\centering
\\begin{tabular}{|r|c|c|c|c|c|c|c|c|} \hline
{\\bf Type of SVM} & \multicolumn{4}{c|}{\\bf Training accuracy} & \multicolumn{4}{c|}{\\bf Test accuracy} \\\\ \hline
Hard margin with & \multicolumn{4}{c|}{} & \multicolumn{4}{c|}{}\\\\
Linear kernel & \multicolumn{4}{c|}{%0.4f} & \multicolumn{4}{c|}{%0.4f}\\\\ \hline \hline  \hline
Hard margin with  & $p=2$ & $p=3$& $p=4$ & $p=5$
& $p=2$ & $p=3$& $p=4$ & $p=5$ \\\\ \cline{2-9}
polynomial kernel & %0.4f & %0.4f & %0.4f & %0.4f & %0.4f & %0.4f & %0.4f & %0.4f \\\\ \hline \hline \hline
Soft margin with   &  & & & & & & & \\\\
polynomial kernel & $C=0.1$ & $C=0.6$& $C=1.1$ & $C=2.1$
& $C=0.1$ & $C=0.6$& $C=1.1$ & $C=2.1$ \\\\
\hline
$p=2$ & %0.4f &%0.4f &%0.4f &%0.4f &%0.4f &%0.4f &%0.4f &%0.4f \\\\ \hline
$p=3$ & %0.4f &%0.4f &%0.4f &%0.4f &%0.4f &%0.4f &%0.4f &%0.4f \\\\ \hline
$p=4$ & %0.4f &%0.4f &%0.4f &%0.4f &%0.4f &%0.4f &%0.4f &%0.4f \\\\ \hline
$p=5$ & %0.4f &%0.4f &%0.4f &%0.4f &%0.4f &%0.4f &%0.4f &%0.4f \\\\ \hline
\end{tabular}
\caption{Results of SVM crossvalidation. $\alpha_{thresh} = 1 \times 10^{-8}$. Highest Test Accuracy: 0.9539}
\label{table:crossval_}
\end{table*}
""" % nums

print latex_table