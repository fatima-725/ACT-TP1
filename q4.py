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
        updated_roofline.append(roofline1[i])
        i +=1
    while j < len(roofline2):
        updated_roofline.append(roofline2[j])
        j += 1

    return updated_roofline      

roofline1 = [(1, 10), (5, 6), (8, 0), (10, 8), (12, 0)]
roofline2 = [(2, 12), (7, 0), (9, 4), (11, 2), (14, 0)]

merged_roofline = merged_rooflines(roofline1, roofline2)
print(merged_roofline)                 