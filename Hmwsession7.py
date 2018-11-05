#Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print:Longest substring in alphabetical order is: begghIn the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print: Longest substring in alphabetical order is: abc

string = input("Hi, please enter a string of characters ")
solution = ""
string1 = ""
alphabet = "a"

for c in string:
    if c>= alphabet:
        string1 += c
    else:
        if len(string1) > len(solution):
            solution = string1
        string1 = c
    alphabet = c

print("The solution is " +solution )

