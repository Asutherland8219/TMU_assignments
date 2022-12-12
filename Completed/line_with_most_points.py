def line_with_most_points(points):
    slope_count = 0  
    if len(points) <= 2:  
        return len(points)
    for point_a in points: 
        point_dict = {}
        duplicate = 0
        max_current = 0
        for point_b in points:
            if point_a != point_b:
                if point_a[0] == point_b[0]:
                    slope = 10000  
                else:
                    slope = float(point_b[1] - point_a[1]) / float(point_b[0] - point_a[0])  
                point_dict[slope] = point_dict.get(slope, 0) + 1
                max_current = max(max_current, point_dict[slope])
            else:
                duplicate += 1
        slope_count = max(slope_count, max_current + duplicate)
    return slope_count