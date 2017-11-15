import cv2

img_path = '666.jpg'
image = cv2.imread(filename=img_path)
cv2.imshow(winname='raw image',mat=image)

#获取图片像素数组的行数和列数
row_num = image.shape[0]
column_num = image.shape[1]

#对image数据进行复制
bright_image = image.copy()

#对像素blue/green/red值整体变为原来的1.5倍，图片变亮
for row in range(row_num):
    for column in range(column_num):
        bright_image[row, column, 0] = bright_image[row, column, 0] * 1.5
        bright_image[row, column, 1] = bright_image[row, column, 1] * 1.5
        bright_image[row, column, 2] = bright_image[row, column, 2] * 1.5

cv2.imshow(winname='show bright image',mat=bright_image)

black_image = image.copy()
#对像素blue/green/red值整体变为原来的0.5倍，图片变黑暗
for row in range(row_num):
    for column in range(column_num):
        black_image[row, column, 0] = black_image[row, column, 0] * 0.5
        black_image[row, column, 1] = black_image[row, column, 1] * 0.5
        black_image[row, column, 2] = black_image[row, column, 2] * 0.5

cv2.imshow(winname='show black image',mat=black_image)
cv2.waitKey()
cv2.destroyAllWindows()