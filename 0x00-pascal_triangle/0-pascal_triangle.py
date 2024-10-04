def pascal_triangle(n):
    """
    Generate Pascal's triangle up to row n.
    Incorporates loops, conditional statements, recursion-like logic, arithmetic operations,
    indexing, and error handling.
    """

    try:
        if not isinstance(n, int) or n <= 0:
            raise ValueError("Input must be a positive integer greater than 0.")

        triangle = []

        # Use while loop to iterate through n rows
        row_index = 0
        while row_index < n:
            # If row_index is 0, we just append [1] (base case)
            if row_index == 0:
                triangle.append([1])
            else:
                # Using list comprehension to generate the row
                # First and last elements are always 1, others are computed
                row = [1]  # First element
                for j in range(1, row_index):
                    row.append(
                        triangle[row_index - 1][j - 1] + triangle[row_index - 1][j]
                    )
                row.append(1)
                triangle.append(row)

            row_index += 1

        return triangle

    # Catch and handle errors (input validation or unexpected errors)
    except ValueError as ve:
        print(f"Error: {ve}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []
