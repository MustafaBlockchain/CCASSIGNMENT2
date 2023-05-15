import re

# Define regular expressions for each token
token_regexes = [
    (r'[ \n\t]+', None),           # Whitespace
    (r'\d+', 'NUMBER'),            # Integer number
    (r'[a-zA-Z_]\w*', 'IDENTIFIER'),# Identifier (variable/function name)
    (r'\+', 'PLUS'),                # Addition operator
    (r'-', 'MINUS'),                # Subtraction operator
    (r'\*', 'MULTIPLY'),            # Multiplication operator
    (r'/', 'DIVIDE'),               # Division operator
    (r'=', 'EQUALS'),               # Assignment operator
    (r';', 'SEMICOLON'),            # Statement terminator
]

# Define a function to perform lexical analysis
def lex(input_string):
    tokens = []
    position = 0
    while position < len(input_string):
        match = None
        for token_regex in token_regexes:
            pattern, tag = token_regex
            regex = re.compile(pattern)
            match = regex.match(input_string, position)
            if match:
                if tag:
                    tokens.append((tag, match.group(0)))
                break
        if not match:
            raise Exception('Illegal character: %s' % input_string[position])
        else:
            position = match.end(0)
    return tokens

# Example usage
input_string = 'x = 3 + y;'
tokens = lex(input_string)
print(tokens)
