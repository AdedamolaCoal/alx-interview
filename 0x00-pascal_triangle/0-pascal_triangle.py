def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []

    # Using a 'for' loop to iterate through the rows
    for i in range(n):
        row = [1] * (i + 1)

        # Using a 'while' loop to handle middle elements
        j = 1
        while j < i:
            if j == 0 or j == i:
                row[j] = 1
            elif j > 0 and j < i:
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            else:
                row[j] = 1
            j += 1

        triangle.append(row)

    return triangle
