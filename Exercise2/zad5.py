def letters(string,n):
    if len(string) == n:
        return [string]
    
    return letters(string + "A",n) + letters(string + "B",n)+letters(string + "C",n)


string=""
print(letters(string,5))

