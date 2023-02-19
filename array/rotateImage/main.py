# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]


# solution(a) =
#     [[7, 4, 1],       --> 0th index value of original image lists
#      [8, 5, 2],       --> 1st index value of original image lists
#      [9, 6, 3]]       --> Last index value of original image lists


def solution(a):
    orig_img_cols = len(a[0]) # width of original image
    orig_img_rows = len(a) # height of original image
    rotate_img = []

    for i in range(orig_img_cols):
        # set the height of rotated image
        rotate_img.append([])               # rotate_img = [[],
                                            #               [],
                                            #               []]

    for row_idx in range(orig_img_rows):
        for _, value in reversed(list(enumerate(a))):
            # print(value[row_idx])
            rotate_img[row_idx].append(value[row_idx])

    print(rotate_img)
    return rotate_img


a = [[1, 2, 3, 100],
     [4, 5, 6, 100],
     [7, 8, 9, 100],
     [0, 0, 0, 100]]

solution(a)

## Limitation of existing solution
# 1. If we increase column like 3x4 we get
#    [[7, 4, 1], [8, 5, 2], [9, 6, 3], []], which incorrect
# 2. If we increasem rows like 4x3, we get error
#     rotate_img[row_idx].append(value[row_idx])
#     IndexError: list index out of range
# Existing solution just work on matix when both rows and columns are equal