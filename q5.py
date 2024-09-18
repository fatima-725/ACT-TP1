def merged_rooflines(roofline1, roofline2):
    h1 = 0 
    h2 = 0
    i = 0
    j = 0
    prevH = 0

    updated_roofline = []
    while i < len(roofline1) and j < len(roofline2):
        if roofline1[i][0] < roofline2[j][0]:
            x = roofline1[i][0]
            h1 = roofline1[i][1]
            i += 1
        else:
            x = roofline2[j][0]
            h2 = roofline2[j][1]
            j += 1

        maxH = max(h1, h2)

        if maxH != prevH:
            updated_roofline.append((x, maxH))
            prevH = maxH

    while i < len(roofline1):
        x, h1 = roofline1[i]
        if h1 != prevH:
            updated_roofline.append((x, h1))
            prevH = h1
        i +=1
    while j < len(roofline2):
        x, h2 = roofline2[j]
        if h2 != prevH:
            updated_roofline.append((x, h2))
            prevH = h2
        j += 1

    return updated_roofline      

def compute_roofline(buildings):
    if len(buildings) == 1:
        l, h, r = buildings[0]
        return [(l, h), (r, 0)]

    mid = len(buildings) // 2
    left_half = buildings[:mid]
    right_half = buildings[mid:]

    left_roofline = compute_roofline(left_half)
    right_roofline = compute_roofline(right_half)

    return merged_rooflines(left_roofline, right_roofline)

buildings = [(98, 41, 127), (154, 16, 176), (195, 89, 231), (201, 22, 215), (167, 34, 191)]

roofline = compute_roofline(buildings)
print(roofline)
