"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Example





: Append  to the list, .
: Append  to the list, .
: Insert  at index , .
: Print the array.
Output:
[1, 3, 2]
list of inputs

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

output
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""

if __name__ == '__main__':
    N = int(input())
    l=[]
    for x in range(N):
        raw_input = input().split(" ")
        if raw_input[0] == "print":
            print(l)
        else:
            cmd = raw_input[0]
            args = raw_input[1:]
            cmd += "("+",".join(args)+")"
            eval("l."+cmd)



"""
n = input()
l = []
for _ in range(n):
    s = raw_input().split()
    cmd = s[0]
    args = s[1:]
    if cmd !="print":
        cmd += "("+ ",".join(args) +")"
        eval("l."+cmd)
    else:
        print l

working 

{
"FirstName":"Swapnil",
"LastName": "Bhagat",
"AppointmentStatus":"now",
"AppointmentDate": "2021-12-30T19:19",
"AppointmentTime":"2022-01-14T14:30:08Z",
"AppointmentType": "gjjjs",
"AppointmentChannel":  "Walk In",
"ClinicId": 122990548,
"DoctorId": 45346070,
"Patient_BP": "234",
"Patient_Height": "4",
"Patient_Plus": "0",
"Patient_SPO2": "5",
"Patient_Temp": "7",
"Patient_Weight": "9",
"PrescriptionNote": "rgtdhbtdjntdjntd",
"ShortNote": "ewdeafsgsrg",
"Title": "shubham",
"UserId": 810459219
}














not working

SHUBHAM BANDAL2:41 PM
{
 "AppointmentChannel": "yes",
 "AppointmentDate": "2022-01-12",
 "AppointmentStatus": "active",
 "AppointmentTime": "14:28",
 "AppointmentType": "fhdhfd",
"BookedDate": "16-1-2022",
 "ClinicId": 122990548,
 "DoctorId": 45346070,
 "FirstName": "hfdf",
 "LastName": "hfdhf",
 "Patient_BP": "fhfd",
 "Patient_Height": "ffhd",
 "Patient_Plus": "fdhh",
 "Patient_SPO2": "hfddf",
 "Patient_Temp": "hfdh",
 "Patient_Weight": "hfh",
 "Pincode": "fdhf",
 "PrescriptionNote": "fhfhf",
 "ShortNote": "fdhhfh",
 "Title": "fdhh",
 "UserId": 810459219
"city": "fhd",
"country": "hfd",
"state": "hdfh"
}
"""
        