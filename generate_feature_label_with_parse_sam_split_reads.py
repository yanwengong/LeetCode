## python script to generate feature and label for training
## use the out put of parse_sam2.awk
## used 150x2, and 100 coverage simulation
## added the file containing split reads

## read in csv

import csv
#import pandas as pd
import os
import numpy as np

path = "/Users/yanwengong/Documents/spring_2019/roation/data/simulation/"
#file = pd.read_csv(os.path.join(path + "dup_to_sing.txt"), sep = '\t',index_col=False, header = None)

with open(os.path.join(path + "parse_sam2_dup_to_sing_sim_100x_sorted.txt"), "r") as f:
    file = f.readlines()

## expand feature for each read
## col: chr, start_pos, flag,  IDL, IDR, ON, OP, PL, PR
file_org = []

## TODO: here instead of fix feature na,me, I need to make it flexible based on the input file
## also print the available features
set_label_list = []
for line in file:
    x = line.strip().split('\t')
    if x[3] not in set_label_list:
        set_label_list.append(x[3])


## add the chrname, start_pos, flag, "IDL", "IDR", "ON", "OP", "PL", "PR" to each read
for line in file:
    x = line.strip().split('\t')
    label_list = [0, 0, 0, 0, 0, 0]
    label_index = set_label_list.index(x[3])
    label_list[label_index] = 1
    file_org.append([x[0], x[1], int(x[4])] + label_list)

## convert information per base, add coverage information
seq_len = 150
matrixLength = int(file_org[-1][1]) + seq_len
## equal to number of parse_sam2 output plus flag,(coverage and number of split, which will be added later)
feature_len = len(set_label_list) + 3 #9 I am doing all the features for now (0526)


matrix = [[0 for _ in range(feature_len)]for _ in range(matrixLength)]

label_matrix = [0 for _ in range(matrixLength)]


def sum_list(list1, list2):
    new_list = []
    for i in range(len(list2)):
        new_list.append(list1[i] + list2[i])
    ## why do i need to append the last additional one..? (0526)
    #new_list.append(int(list1[-1]))
    return new_list

list(np.multiply(list(range(20)), 100000))

## construct feature: flag,  set_label_list
## coverage to be added later
for i in range(len(file_org)):
    #flag = file_org[i][2]
    if i in list(np.multiply(list(range(20)), 100000)):
        print("processed "+ str(i))
    start_pos = int(file_org[i][1])
    ## need to add 0 here to save space for coverage
    feature_list = file_org[i][2:9] +[0, 0]
    for j in range(start_pos, start_pos+seq_len):
        #label_matrix[j] = j
        #matrix[j] = (np.sum([matrix[j], feature_list], axis = 0)).tolist()
        matrix[j] = sum_list(matrix[j], feature_list)


## assign coverage; divide flag number and feature count by coverage
## the second to the last is coverage column
## （0526: changed for i in range(len(file_org)): cov = max(matrix[i][1:-2])
## there is issue
for i in range(len(matrix)):
    cov = sum(matrix[i][1:-2])
    if cov != 0:
        matrix[i][-2] = cov
        matrix[i][:-2] = [x/cov for x in matrix[i][:-2]]

## assign label to label_matrix

for i in range(20):
    for j in range(1000):
        k = int(i*1e5 + 5e3+j)
        label_matrix[k] = 1

f.close()
len(label_matrix)
len(matrix)


## add split information to the matrix
len(matrix)
#split_cov_per_base = np.loadtxt(os.path.join(path + "split_cov_per_base.txt"))
split_cov_per_base =[]
with open(os.path.join(path + "split_cov_per_base.txt"), "r") as split_f:
    split_file = split_f.readlines()

## TODO:
## note, the first row in matrix does not have the same number of element, them there is no coverage nor split reads..
## todo: need to check if the following for loop is correct
## but ultimately need to solve the uneven element number issue
for i in range(len(matrix)):
    if len(matrix[i]) != 9:
        print(i)
        print(matrix[i])


for line in split_file:
    x = line.strip().split('\t')
    each_base = int(x[2])
    split_cov_per_base.append(each_base)

## the last col in matrix is split read count (0526)
for i in range(len(matrix)):
    matrix[i][-1]=(int(split_cov_per_base[i]))

###################################### train a random forest model ###################

from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier

x = matrix
y = label_matrix
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Choose some parameter combinations to try
parameters = {'n_estimators': 100,
              #'max_features': 14,
              'criterion': 'gini',
              #'max_depth': 20,
              #'min_samples_split': 20,
              'min_samples_leaf': 50,
              'random_state': 0,
              'n_jobs': -1
              }

clf = RandomForestClassifier(**parameters)
train_test_model(clf, X_train, y_train, X_test, y_test)
clf.feature_importances_
## function used were written below
%matplotlib inline
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

#np.count_nonzero(y_train_pred)
#len(y_train_pred)

def train_test_model(clf, X_train, y_train, X_test, y_test):
    # Fit a model by providing X and y from training set
    clf.fit(X_train, y_train)

    # Make prediction on the training data
    y_train_pred = clf.predict(X_train)
    p_train_pred = clf.predict_proba(X_train)[:,1]

    # Make predictions on test data
    y_test_pred = clf.predict(X_test)
    p_test_pred = clf.predict_proba(X_test)[:,1]

    # print model results
    get_performance_metrics(y_train, p_train_pred, y_test, p_test_pred)
    plot_roc_curve(y_train, p_train_pred, y_test, p_test_pred)

def plot_roc_curve(y_train, p_train_pred, y_test, p_test_pred):
    roc_auc_train = roc_auc_score(y_train, p_train_pred)
    fpr_train, tpr_train, _ = roc_curve(y_train, p_train_pred)

    roc_auc_test = roc_auc_score(y_test, p_test_pred)
    fpr_test, tpr_test, _ = roc_curve(y_test, p_test_pred)
    plt.figure()
    lw = 2
    plt.plot(fpr_train, tpr_train, color='green',
             lw=lw, label='ROC Train (AUC = %0.4f)' % roc_auc_train)
    plt.plot(fpr_test, tpr_test, color='darkorange',
             lw=lw, label='ROC Test (AUC = %0.4f)' % roc_auc_test)
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC curve')
    plt.legend(loc="lower right")
    # save fig to specify directory
    plt.savefig('/Users/yanwengong/Documents/spring_2019/roation/output/rf_cov_sam_parsesam2/roc.png')
    plt.show()




import pandas as pd
# Import metrics functions from sklearn
from sklearn.metrics import precision_score, accuracy_score, recall_score, f1_score, roc_auc_score
# Helper method to print metric scores
def get_performance_metrics(y_train, p_train_pred, y_test, p_test_pred, threshold=0.5):
    metric_names = ['AUC','Accuracy','Precision','Recall(sensitivity)','f1-score']
    metric_values_train = [roc_auc_score(y_train, p_train_pred),
                    accuracy_score(y_train, p_train_pred>threshold),
                    precision_score(y_train, p_train_pred>threshold),
                    recall_score(y_train, p_train_pred>threshold),
                    f1_score(y_train, p_train_pred>threshold)
                   ]
    metric_values_test = [roc_auc_score(y_test, p_test_pred),
                    accuracy_score(y_test, p_test_pred>threshold),
                    precision_score(y_test, p_test_pred>threshold),
                    recall_score(y_test, p_test_pred>threshold),
                    f1_score(y_test, p_test_pred>threshold)
                   ]
    all_metrics = pd.DataFrame({'metrics':metric_names,
                                'train':metric_values_train,
                                'test':metric_values_test},columns=['metrics','train','test']).set_index('metrics')
    print(all_metrics)

metric_names
metric_values_train
metric_values_test
