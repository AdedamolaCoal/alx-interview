def generate_row(previous_row):
    """
    Recursive helper function to generate a row based on the previous row.
    Handles errors such as invalid input types or empty lists.
    """
    try:
        if not previous_row:
            return [1]

        new_row = [1] * (len(previous_row) + 1)

        for i in range(1, len(previous_row)):
            new_row[i] = previous_row[i - 1] + previous_row[i]

        return new_row
    except Exception as e:
        print(f"An error occurred in row generation: {e}")
        return []


def pascal_triangle(n):
    """
    Main function to generate Pascal's triangle up to row n.
    Includes error handling for invalid input types or values.
    """
    try:
        if not isinstance(n, int) or n <= 0:
            raise ValueError("n must be a positive integer.")

        triangle = [[1]]

        for i in range(1, n):
            prev_row = triangle[-1]
            current_row = generate_row(prev_row)
            triangle.append(current_row)

        return triangle

    except ValueError as ve:
        print(f"Input error: {ve}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []
