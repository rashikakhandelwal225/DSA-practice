def flipAndInvertImage(image):   
    for row in image:
        left =0
        right = len(row)-1
        while left <= right:
            row[left] , row[right] = row[right]^1 , row[left]^1
            right -=1
            left +=1
    return image

image = [[1,1,0],[1,0,1],[0,0,0]]
print(flipAndInvertImage(image))
image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
print(flipAndInvertImage(image))