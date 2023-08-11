#!/usr/bin/python3           
if __name__ == "__main__":
    import hidden_4
    
    lexis = dir(hidden_4)
    for lexi in lexis:
        if lexis[:2] != "__":
            print(lexi)
