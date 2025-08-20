import re

patterns = [
    [r"\d*\.\d+|\d+\.\d*|\d+","number"], #numbers
    [r"\+", "+"], #plus operator
    [r".", "Error"] #anything that isn't a pattern, is an unexpected error.
]

for pattern in patterns: 
    pattern[0] = re.compile(pattern[0])

def tokenize(characters):
    tokens = []
    position = 0
    while position < len(characters):
        #find the first token that matches
        for pattern, tag in patterns:
            match = pattern.match(characters, position)
            if match:
                break
    assert match
        
    if tag == "error":
        raise Exception(f"[Syntax Error] -> Illegal Character: {[match.group(0)]}")       

    token = {"tag":tag, "position":position}
    value = match.group(0) 
    if token["tag"] == "number":
        if "." in value:
            token["value"] == float(value)
        else:
            token["value"] == float(value)
    tokens.append(token)
    position = match.end()
    
    tokens.append({"tag":None, "position":position})
    return tokens

if __name__ == "__main__":
    print("Testing Tokenizer")
    def test_simple_tokens():
        assert tokenize("+") [
            {"tag":"+", "position":0},
            {"tag":None, "posistion":1}
        ]
        assert tokenize("3") [
            {"tag":"number", "position":0, "value":3},
            {"tag":None, "posistion":1}
        ]
    print("Done Testing")