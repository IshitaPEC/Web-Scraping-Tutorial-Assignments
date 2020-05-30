import re
#Specialised language used to search for text within a given document with precision and efficiency
#Special characters which cannot be matched are:
# META CHARACTERS: ^,$,*,+,?,{,},[,],\,|,(,)

#Regular expressions -> primarily used for string matching
#regex= re.compile(pattern)
#regex.match(main_string)
#We look for the pattern in our main string

regex= re.compile('a')
print(regex.match('a'))
#Output of the above statements is span(0,1), match='a'

regex= re.compile('ab')
print(regex.match('a'))
#Output of the above statements is None

#Any character present in the [] if matched with my main_string would yield a found match else none
regex= re.compile('[abc]')
print(regex.match('a'))
#Output of the above statements is a match

#This shows a range of characters which can be present in our range
regex= re.compile('[a-h]')
print(regex.match('z'))
#Output of the above statements is a match

#Complement of the range is the range that we are looking for
regex= re.compile('[^a-zA-Z]')
print(regex.match('1'))
#Output of the above statements is a match

#Represents repeated a-> lower limit= 0 and upper limit= infinity
regex= re.compile('a*')
print(regex.match('aaaaa'))
print(regex.match(''))
#Ouptput for both the above statements is a match-> whether the match string is a '','aaaa','aaaaaaaaaaaa'


#Repitition of all these digits in any order
#'a-c' -> any letters in the range are present infinitely
regex= re.compile('[a-c]*')
print(regex.match('acacccbb'))
#Output: It is a match-> We may have any number of 'a's, 'b's, 'c's in our string to match


#Everything is same as * in +
#Only difference is that not existance of a is not an option
#lower limit is 1 and upper limit is infinite
regex= re.compile('a+')
print(regex.match(''))
#OUTPUT: It is 'None' as the answer


#Repitition of all these digits in any order
#'a-c' -> any letters in the range are present infinitely
regex= re.compile('[a-c]+')
print(regex.match('acacccbb'))
#Output: It is a match-> We may not have a NULL string as our string to match,


#?
#digit before ? must be present only once or should be not present
#digit after ? may be present as many times as it wants
regex= re.compile('a?b')
print(regex.match('abb'))
#This is a match
print(regex.match('b'))
#This is also a match
print(regex.match('aab'))
#This is not a match as the letter a (letter before ?) may not be present more than once, it has to be present once or never

#'^'->string must start with the character following '^'
#regex= re.compile('^a')

#'|'->OR OPERATOR
#regex= re.compile('a|b')

#'$'->OR OPERATOR
#regex= re.compile('abc$')

#{m,n}-> minimum:m , maximum:n
regex= re.compile('a{2,4}')
print(regex.match('a'))
#The above statement yields 'NONE' as the answer as it is not a match

#regex= re.compile('a{0,1}')
#regex= re.compile('a{1,}') Assumes 2nd part to be INFINITY
#regex= re.compile('\d') It matches any decimal digits [0-9]
#regex= re.compile('\D') It matches any non digit character [^0-9]
#regex= re.compile('\s') It matches any whitespace character
#regex= re.compile('\S') It matches any non-whitespace character
#regex= re.compile('\w') It matches any alpha-numeric character[a-zA-Z0-9]
#regex= re.compile('\W') It matches any non-alpha-numeric character[^a-zA-Z0-9]

