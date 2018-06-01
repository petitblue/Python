import re

def paren_references(article,word):
    """
    capture references to the given words found in a given file
    inside parentheses
    :param article: (string)
    :param word:(string)
    :return: all_references(string) references to the word inside parenthese
    separated by new characters
    an empty string if there is no such references
    """
    all_references = ''
    #  extract text inside parentheses containing the word
    pattern = r'\(([^\)]*\b{}\b.*?)\)'.format(word)
    #[^5] will match any character except '5'
    matches = re.findall(pattern,article,re.IGNORECASE|re.DOTALL)
    if matches:
        all_references = '\n'.join(matches)
    return all_references

article = """
Invoke the interpreter (by typing python at the prompt.)
The core philosophy of Python is summarized in the document "PEP 20" (The Zen of Python)
Guido van Rossum, (the original creator of the Python language and the Benevolent Dictator 
For Life), decided to clean up Python properly, with less regard for backwards compatibility. 
We use several programming languages (Python is the best!)
classSize,  (a nonpythonic variable name) is acceptable in JavaScript.
We use several programming languages (Java, Python, JavaScript)
Make sure you follow the guidelines (pythonic style, documentation)
"""
result =paren_references(article, 'python')
print(result)
result = 0
pattern = 'test'
if re.match(pattern,'testsocial.py'):
    result+=2
print(result)
if re.match(pattern, 'socialtest.py'):  # cann't match the test here
    result +=4
print(result)
if re.search(pattern, 'testsocial.py'):
    result += 8
print(result)
if re.search(pattern, 'socialtest.test'):
    result += 16
print(result)

pattern = r'e.'
result =re.findall(pattern,'Explicit is better than implicit.',re.IGNORECASE)
# Lower and upper case will generate two different strings
print(result)
pattern = r'\S'  # will print every character
result = re.findall(pattern,'Hello there')
print(result)
print(len(result))

pattern = r'<img\s+id\s*=\s*"(\S+)"\s+'
text =  '<img id ="smile" src="smile.gif" alt="smiley face">'
result = re.search(pattern,text)
print(result.group(0))
print(result.group(1))

def name_of_email(addr):
    pattern = r'(^(\w*.\w*)\s+\w+@(\w+\.\w+))'
    match = re.search(pattern,addr,re.IGNORECASE)
    if match:
        return(match.group())
print(name_of_email('tom@voyager.org'))
