
"""

The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

Example




The query_name is 'beta'. beta's average score is .

Input Format

The first line contains the integer , the number of students' records. The next  lines contain the names and marks obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to query.

Constraints

Output Format

Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

Sample Input 0

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

output 
56.00


"""



if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_scores = student_marks[query_name]
    print("{0:.2f}".format(sum(query_scores)/(len(query_scores))))
    # sum = 0
    # for x in student_marks[query_name]:
    #     sum += x
    # percentage = sum/len(student_marks[query_name])
    # percentage = str(percentage)
    # n, after_decimal = percentage.split('.')
    # if len(after_decimal)<2:
    #     print(percentage+"0")
    # else:
    #     print(round(float(percentage), 2))

    
