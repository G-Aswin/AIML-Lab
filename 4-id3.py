import math
import csv
from collections import Counter

def load_csv(filename):
    lines=csv.reader(open(filename,"r"));
    dataset = list(lines)
    headers = dataset.pop(0)
    return dataset,headers

class Node:
    def __init__ (self,attribute):
        self.attribute=attribute
        self.children=[]
        self.answer=""

def subtables(data,col,delete):
    # group table data according to column in col
    # return dict of rows grouped by mentioned col, and unique col values
    colwise_data = {}
    for i, row in enumerate(data):
        if row[col] not in colwise_data:
            colwise_data[row[col]] = []
        if delete:
            colwise_data[row[col]].append(row[:col] + row[col+1:])
            del data[i][col]
        else:
            colwise_data[row[col]].append(row)
            
    return list(colwise_data.keys()), colwise_data

def entropy(S):
    # S is a list of YES/NO
    # return entropy of the list
    count = Counter(S)
    if len(count.keys()) == 1:
        return 0
    
    entropy = 0
    for k, v in count.items():
        p = v / (1.0*len(S))
        entropy += -1 * p * math.log(p, 2)

    return entropy

def compute_gain(data,col):
    # gets the data and column
    # calls subtables to group data according to column
    # computes gain of the column
    values,dic = subtables(data,col,delete=False)
    total_size=len(data)
    entropies=[0]*len(values)
    ratio=[0]*len(values)
    total_entropy=entropy([row[-1] for row in data])
    for x in range(len(values)):
        ratio[x]=len(dic[values[x]])/(total_size*1.0)
        entropies[x]=entropy([row[-1] for row in dic[values[x]]])

        total_entropy-=ratio[x]*entropies[x]
    return total_entropy

def build_tree(data,features):
    lastcol=[row[-1] for row in data]
    
    # If only YES or NO
    if(len(set(lastcol)))==1:
        node=Node("")
        node.answer=lastcol[0]
        return node
    
    # n = number of attributes
    n=len(data[0])-1
    
    # get gain of each attribute
    gains=[0]*n
    for i in range(n):
        gains[i]=compute_gain(data,i)
    
    # split is the index with max gain
    split=gains.index(max(gains))
    
    # Create a node with max gain attribute
    node=Node(features[split])
    
    # Remove max gain column from features
    fea = features[:split]+features[split+1:]
    
    # get subtables with DELETE = TRUE
    attr,dic=subtables(data,split,delete=True)
    for x in range(len(attr)):
        child=build_tree(dic[attr[x]],fea)
        node.children.append((attr[x],child))
        
    return node

def print_tree(node,level):
    if node.answer!="":
        print("\t"*level,node.answer)
        return
    print("\t"*level,node.attribute)
    for value,n in node.children:
        print("\t"*(level+1),value)
        print_tree(n,level+2)

def classify(node,x_test,features):
    if node.answer!="":
        print(node.answer)
        return
    pos=features.index(node.attribute)
    for value, n in node.children:
        if x_test[pos]==value:
            classify(n,x_test,features)


dataset,features=load_csv("traintennis.csv")
node1=build_tree(dataset,features)
print("The decision tree for the dataset using ID3 algorithm is")
print_tree(node1,0)
testdata,features=load_csv("testtennis.csv")
for xtest in testdata:
    print("The test instance:",xtest)
    print("The label for test instance:",end=" ")
    classify(node1,xtest,features)