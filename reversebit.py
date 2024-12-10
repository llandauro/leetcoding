def reverseBits(n):
    
    # reverse the bits of a given 32 bits unsigned integer
    
    list_n = str(n)
    answer = ""
    for number in list_n:
            if number == "1":
                answer = answer + "0"
            if number == "0":
                answer = answer + "1"


    return int(answer, 2)

print(reverseBits(11111111111111111111111111111101))
        