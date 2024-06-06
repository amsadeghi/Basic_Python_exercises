# -*- coding: utf-8 -*-
"""bioinformatic01.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZfyjI2E80fuIHiEJmTQT_HlsRp8GBOwO
"""

#Given two input lists L1 and L2, write a function which selects all elements which are present both in
#L1 and in L2, and returns them in a list L3

def intersection (L1,L2):
  L=[]
  for i in range(len(L1)):
    for j in range(len(L2)):
      if L1[i]==L2[j]:
        L.append(L1[i])
  return L

def intersection2(L1,L2):
  L=[]
  for i in range(len(L1)):
    if L1[i] in L2:
      L.append(L1[i])
  return L
#test
L1=[1,2,3,4,5]
L2=[3,4,5,6,7]
A=intersection2(L1,L2)
A

#Build a nxm 0s matrix

def zero_matrix (n,m):
  M=[]
  for i in range(n):
    L=[]
    for j in range(m):
      L.append(0)
    M.append(L)
  return M
#test
A=zero_matrix(3,4)
A

#Sum two matrixes

def sum_2_matrices(M1,M2):
  if len(M1)!=len(M2) or len(M1[0])!=len(M2[0]):
    return "must the same dim"
  M=[]
  for i in range(len(M1)):
    L=[]
    for j in range(len(M1[0])):
      a=M1[i][j]+M2[i][j]
      L.append(a)
    M.append(L)
  return M
#test
M1=[[1,1,2,1],[1,1,1,1],[1,1,1,1]]
M2=[[1,1,1,1],[1,1,1,1],[1,1,1,1]]
A=sum_2_matrices(M1,M2)
A

#Multiply two matrixes

def matmul (M1,M2):
  if len(M1[0])!=len(M2):
    return "unfeasible"
  M=[]
  for i in range(len(M1)):
    L=[]
    for j in range(len(M2[0])):
      a=0
      for k in range(len(M2)):
        a+=M1[i][k]*M2[k][i]
      L.append(a)
    M.append(L)
  return M
M1=[[1,1,1,1],[1,1,1,1],[1,1,1,1]]
M2=[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
A=matmul(M1,M2)
A

#Compute the transposed matrix of a given input matrix of size NxN

def Tmatrix(M):
  M1=[]
  for i in range(len(M)):
    L=[]
    for j in range(len(M[i])):
      L.append(M[j][i])
    M1.append(L)
  return M1
M=[[1,1,1],[2,2,2],[3,3,3]]
A=Tmatrix(M)
A

#Given a rectangular input matrix M, write a function which returns a boolean value True if and only
#if there exist two different rows in M,
#whose sum gives the null vector.

def Matcheckrow(M):
  L=[]
  for i in range(len(M)-1):
    for j in range(i+1,len(M)):
      L1=[]
      for k in range(len(M[0])):
        a=M[i][k]+M[j][k]
        L1.append(a)
      L.append(L1)
  b=0
  for i in range(len(L)):
    if sum(L[i])==0:
      b+=1
  if b==1:
    return True
  else: return False

#Do the same for two different columns.

def Matcheckcolumn(M):
  L=[]
  for i in range(len(M[0])-1):
    for j in range(i+1,len(M[0])):
      L1=[]
      for k in range(len(M)):
        a=M[k][i]+M[k][j]
        L1.append(a)
      L.append(L1)
  b=0
  for i in range(len(L)):
    if sum(L[i])==0:
      b+=1
  if b==1:
    return True
  else: return False
#test
M=[[1,1,1,1],
   [-1,-1,-1,-1],
   [-1,1,-2,-1]]
A=Matcheckcolumn(M)
print("column:",A)
B=Matcheckrow(M)
print("Row:",B)

#Eliminate all the negative elements from a list

def eleminate_negative(L):
  for i in range(len(L)-1,-1,-1):
    if L[i]<0:
      L.pop(i)
  return L
#test
L=[-1,2,-2,4,-5]
A=eleminate_negative(L)
L

#Eliminate all the negative elements in position multiple of 3 from a list

def eleminate_negative3(L):
  for i in range(len(L)-1,-1,-1):
    if L[i]<0 and i%3==0:
      L.pop(i)
  return L
#test
L=[-1,2,-2,4,-5,-2,-1]
A=eleminate_negative3(L)
L

#Define a class for binary trees

class Tree:
  def __init__(self, root=None , left=None,right=None):
    self.root=root
    self.left=left
    self.right=right

def print_tree(T):
  if T is not None:
    print_tree(T.left)
    print(T.root)
    print_tree(T.right)
# test
T=Tree("a",Tree("b",Tree("c"),Tree("d",Tree("f"))),Tree("e"))
print_tree(T)

#Compute the height of a tree
def height_T(T):
  if T is None or T.root is None:
    h=-1
  else:
    hl=height_T(T.left)+1
    hr=height_T(T.right)+1
    h=max(hl,hr)
  return h
A=height_T(T)
A

#Convert a binary tree into a list (in order traversal)

def T2list(T):
  if T is None or T.root is None:
    return []
  else:
    L=T2list(T.left)
    Ro=[T.root]
    R=T2list(T.right)
  return L+Ro+R
A=T2list(T)
A

#Verify if two binary trees are balance

def isbalance(T):
  if T is None or T.root is None:
    return True
  else:
    L=height_T(T.left)
    R=height_T(T.right)
    if L-R<-1 or L-R>1:
      return False
    else:
      isbalance(T.left)
      isbalance(T.right)
  return True
M=Tree(10,(Tree(8,Tree(6),Tree(7))),Tree(12,Tree(11),Tree(13)))
A=isbalance(M)
A

#input two rectangular matrixes M, and M1 of integer values, having the same size NxM,
# and which returns a boolean value True if and only if there exist one column from M and
#one from M1 such that the sum of the values in each of the two columns is the same.

def columnchecker(M,M1):
  L1=[]
  L=[]
  for j in range(len(M[0])):
    a=0
    for i in range(len(M)):
      a+=M[i][j]
    L.append(a)
  print(L)
  for j in range(len(M1[0])):
    a=0
    for i in range(len(M1)):
      a+=M1[i][j]
    L1.append(a)
  for n in range(len(L)):
    for m in range(len(L1)):
      if L[n]==L1[m]:
        return True
      else:
        return False
M =[[0,2,0],[4,0,5]]
M1 =[[4,0,1],[6,6,6]]
print(columnchecker(M,M1))

#Write a Python function, which, given two input binary trees of integers T1 and T2, defined following class Tree:
#returns a boolean value True if and only if all values in T1 appear at least twice in T2.
#The value False is returned otherwise.

def nodefinder(T):
  if T==None or T.root==None:
    return []
  else:
    L1=nodefinder(T.left)
    L2=nodefinder(T.right)
    L3=[T.root]
    return L1+L3+L2
def compareTree(T1,T2):
  A=nodefinder(T1)
  B=nodefinder(T2)
  print(A)
  print(B)
  for i in range(len(A)):
    if B.count(A[i])<2*A.count(A[i]):
      return False
  return True

T2= Tree(9,Tree(2),Tree(9,Tree(2,Tree(11),Tree(5)),Tree(11)))
T1= Tree(11,Tree(9,Tree(2)))

R=compareTree(T1,T2)
R

#Write a pattern for recognizing a string which must contain at least two of the
#following words: legal, Trump, policy

import re
def finder(s):
  pattern=r"(policy|Trump|legal)"
  string=s
  a=re.findall(pattern,string)
  print(a)
  print(len(a))
  if len(a)>1:
    return True
  else: return False

string= "the policy have to got Trump order"
b=finder(string)
b

#Consider the module “re” for defining Python regular expressions. Write a Python function which,
#given a string S and a positive integer N, checks if S contains occurrences of a substring which
#begins with one initial substring ‘xx’, contains the substring ‘yy’, ends with a substring 'zz' and
#has length >N. The function has to print all occurrences of such substrings in S.

def finder(s,n):
  p=r'xx.*?yy.*?zz'
  a=re.findall(p,s)
  # print(len(a[1]))
  for i in range(len(a)):
    if len(a[i])>n:
      print(a[i])
    # else: print("not found")
string = "abxxa1yydfczzbxxbbbyyxxzzcaaa12cccyy"
b=finder(string,8)
b