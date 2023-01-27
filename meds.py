def main():
    s=input("Enter string-")
    k=int(input('Enter k-'))
    sl=len(s)
    ts=''
    ml=[]

    if sl%k != 0:
        print("Invalid")
    else:
        for i in range (sl):
            ts=ts+s[i]
            if len(ts)==k:
                p=''
                for char in ts:
                    if char not in p:
                        p=p+char
                ml.append(p)
                ts=''
        print(ml)


main()