def pascal_triangle(n):
    """
    Generate Pascal's triangle up to row n.
    Incorporates loops, conditional statements, recursion-like logic, arithmetic operations,
    indexing, and error handling.
    """

    # Error and exception handling
    try:
        # Validate input (must be a positive integer)
        if not isinstance(n, int) or n <= 0:
            raise ValueError("Input must be a positive integer greater than 0.")

        triangle = []  # Initialize triangle as an empty list

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
                for j in range(
                    1, row_index
                ):  # Nested for loop to calculate internal elements
                    # Sum of the two values from the previous row
                    row.append(
                        triangle[row_index - 1][j - 1] + triangle[row_index - 1][j]
                    )
                row.append(1)  # Last element is always 1
                triangle.append(row)

            # Recursion-like approach with while loop continuing until row_index < n
            row_index += 1

        return triangle

    # Catch and handle errors (input validation or unexpected errors)
    except ValueError as ve:
        print(f"Error: {ve}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []


# Function to print the Pascal's triangle in a readable way
def print_triangle(triangle):
    """
    Prints the Pascal's triangle in a formatted way.
    """
    for row in triangle:
        print(row)


# Example execution
if __name__ == "__main__":
    n = 5  # You can change this to generate more or fewer rows
    triangle = pascal_triangle(n)
    print_triangle(triangle)
