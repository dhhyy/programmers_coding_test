def solution(a, b):
    answer = 0
    
    for i in zip(a, b):
        answer += i[0] * i[1]
            
    return answer

a = [1,2,3,4]
b = [-3,-1,0,2]

print(solution(a,b))