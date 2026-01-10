# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****

def hollow_square(n):
    result = ""
    result += "*" * n
    result += "\n"

       
    if n == 1:
        return "*"
    
    for i in range(n - 2):
        result += ("*")
        result += str((n - 2) * " ")
        result += "*"
 

        result += "\n"

    result += "*" * n

    return result.rstrip()
 


# 1
# 12
# 123
# 1234
def number_pattern(n):
    result = ""

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            result += str(j)

        result += "\n"
     


    return result.rstrip()
    
    

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    result = 0
    count = 1
        
    for j in range(n):
            result += count
            count += 1

    return result

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    result = ""

    for i in range(1, n + 1):
        spaces = n - i
        result += " " * spaces
        stars = (i * 2) - 1
        result += "*" * stars
        result += "\n"

    return result.rstrip()

print(centered_star_pyramid(4))


    
