triangle = []

with open("p067_triangle.txt") as txt_file:
    for i in txt_file.readlines():
        tmp_list = i.split()
        results = list(map(int, tmp_list))
        triangle.append(results)

for i in range(1,len(triangle)):
    for j in range(len(triangle[i])):
        if j == 0:
            triangle[i][j] = triangle[i][j] + triangle[i-1][j]
        elif j == len(triangle[i-1]):
            triangle[i][j] = triangle[i][j] + triangle[i-1][j-1]
        else:
            triangle[i][j] = max(triangle[i][j] + triangle[i-1][j],triangle[i][j] + triangle[i-1][j-1])
 
print(max(triangle[len(triangle)-1]))
        
