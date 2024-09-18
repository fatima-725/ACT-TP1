# def merge_skyline(skyline1, skyline2):
#     """ Merge two skylines into one, maintaining the correct height transitions. """
#     merged_skyline = []
#     h1, h2 = 0, 0  # Heights of skyline1 and skyline2
#     i, j = 0, 0  # Pointers for skyline1 and skyline2

#     # Merge the two skylines
#     while i < len(skyline1) and j < len(skyline2):
#         if skyline1[i][0] < skyline2[j][0]:
#             x, h1 = skyline1[i]
#             i += 1
#         else:
#             x, h2 = skyline2[j]
#             j += 1

#         max_height = max(h1, h2)
#         if not merged_skyline or merged_skyline[-1][1] != max_height:
#             merged_skyline.append((x, max_height))

#     # Append the remaining points from either skyline
#     merged_skyline.extend(skyline1[i:])
#     merged_skyline.extend(skyline2[j:])

#     return merged_skyline

# def compute_skyline(buildings):
#     """ Recursively compute the skyline using divide-and-conquer. """
#     # Base case: if there's only one building
#     if len(buildings) == 1:
#         g, h, d = buildings[0]
#         return [(g, h), (d, 0)]

#     # Divide: split the list of buildings into two halves
#     mid = len(buildings) // 2
#     left_half = buildings[:mid]
#     right_half = buildings[mid:]

#     # Conquer: recursively compute the skyline for each half
#     left_skyline = compute_skyline(left_half)
#     right_skyline = compute_skyline(right_half)

#     # Merge: combine the two skylines
#     return merge_skyline(left_skyline, right_skyline)

# # Example usage
# buildings = [(98, 41, 127), (154, 16, 176), (195, 89, 231), (167, 34, 191)]
# skyline = compute_skyline(buildings)
# print(skyline)

def update_roofline(roofline, l, r, h):
    new_roofline = []

    for i in range(len(roofline)):
        x, y = roofline[i]

        if x < l:
            new_roofline.append(roofline[i])

        elif l <= x <= r:
            if y >= h:
                new_roofline.append(roofline[i])
            else:
                new_roofline.append((x, h))

        else:
            break

    return new_roofline

# Example usage:
roofline = [(1,10), (5,6), (8,0), (10,8), (12,0)]
l, r, h = 4, 10, 7
updated_roofline = update_roofline(roofline, l, r, h)
print(updated_roofline)
