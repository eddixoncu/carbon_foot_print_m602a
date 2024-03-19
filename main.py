
#Counting characters
def count_chars (string, char):
    num = string.count(char)
    print (f"Number of occurrences of {char} is {num}")


#Checking substrings
def checking_substring ( string, substring):
    exist = substring in string
    print(f"Is the substring {substring} exist in {string}?\n : {exist}")


def to_low(string:str):
    return string.lower()

def to_up(string:str):
    return string.upper()

def to_split(string:str, char):
    parts = string.split(char)
    return  parts

def to_unsplit(parts:[], separator):
    string = separator.join(parts)
    return string


def del_trail_white_space(string:str):
    return string.strip()


string = input("enter the input string >>: ")
substring = input("enter the character to search >>: ")
print("counting chars ", count_chars( string, substring))
print(f"is {substring} in {string}? : {checking_substring(string,substring)}")
print(to_low(string))
print(to_up(string))
tokens = to_split(string, substring)
print(tokens)
print ( to_unsplit(tokens, " & "))
print(del_trail_white_space(string))

#Un diablo se cayó al  agua Y otro diablo lo sacó Y otro diablo que pasaba Dijo: qué diablos pasó ? El diablito engarrotado dijo: Qué voy a saber A lo mejor fue la diabla La diabla de mi mujer