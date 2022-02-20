"""
Question:

Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example

The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:

alpha
beta
Input Format

The first line contains an integer, , the number of students.
The  subsequent lines describe each student over  lines.
- The first line contains a student's name.
- The second line contains their grade.

Constraints

There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

smaple input:

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39


sample output:
Berry
Harry

sudo code:
sort - 
select 2 most
make list of 2 most
if True

Test case:
5
Harsh
20
Beria
20
Varun
19
Kakunami
19
Vikas
21


Beria
Harsh


"""

from os import dup


if __name__ == '__main__':
    l2 = []
    for _ in range(int(input())):
        l1= []
        name = input()
        score = float(input())
        l1.append(name)
        l1.append(score)
        l2.append(l1)

    for j in range(len(l2)-1):
        for i in range(len(l2)- j - 1):
            if l2[i][1] > l2[i+1][1]:
                l2[i], l2[i+1] = l2[i+1], l2[i]
    
    val = []
    [val.append(i[1]) for i in l2]
    second_val = sorted(list(set(val)))[1]    
    # second_val = l2[1][1]
    l = []
    [l.append(items[0])  for items in l2 if items[1] == second_val]
    print(l)
    for i in sorted(l):
        print(i)


    # if __name__ == '__main__':
    # l2 = []
    # for _ in range(int(input())):
    #     l1= []
    #     name = input()
    #     score = float(input())
    #     l1.append(name)
    #     l1.append(score)
    #     l2.append(l1)

    # for j in range(len(l2)-1):
    #     for i in range(len(l2)- j - 1):
    #         if l2[i][1] > l2[i+1][1]:
    #             l2[i], l2[i+1] = l2[i+1], l2[i]
    # second_val = l2[1][1]
    # l = []
    # for items in l2:
    #     if items[1] == second_val:
    #         l.append(items[0])
    # for i in sorted(l):
    #     print(i)
    
    
        
    
        

    

    










