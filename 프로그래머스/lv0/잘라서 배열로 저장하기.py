def solution(my_str, n):
    result = []
    
    for i in range(0,len(my_str),n):
        result.append(my_str[i:i+n])
    return result

# def solution(my_str, n):
#     return [my_str[i: i + n] for i in range(0, len(my_str), n)]w