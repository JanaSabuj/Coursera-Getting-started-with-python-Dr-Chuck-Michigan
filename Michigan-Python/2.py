nax = None
nix = None

while(1):
    num = input("Enter a valid number. Press 'done' to quit")

    try:
        num = int(num)
    except:
        if(num == 'done'):
            print("Maximum is",nax)
            print("Minimum is",nix)
            quit()
        else:
            print("Invalid input")
            continue

    if nax is None and nix is None:
        nax = num
        nix = num
        # print('hello')
    else:
        if(num>nax):
            nax = num
        elif num<nix:
            nix = num
