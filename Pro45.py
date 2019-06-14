m=input()
if m==m[::-1]:
    print("yes")
else:
    value=m.strip("0")
    
    if value==value[::-1]:
        print("yes")
    else:
        value=m.lstrip("0")
        
        if value==value[::-1]:
            print("yes")
        else:
            print("no")
