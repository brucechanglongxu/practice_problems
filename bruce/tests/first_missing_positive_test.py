from bruce import first_missing_positive

def first_test_case(sol: first_missing_positive.Solution) -> None:
    """
    Tests for an array of consecutive elements from 1 through to N
    """
    arr = [1, 2, 3, 4, 5, 6]
    assert sol.first_missing_positive(arr) == 7
    

def second_test_case(sol: first_missing_positive.Solution) -> None:
    """
    Tests for an array of consecutive elements missing the number 1
    """
    arr  = [2, 3, 4, 5, 6, 7]
    assert sol.first_missing_positive(arr) == 1
    
def third_test_case(sol: first_missing_positive.Solution) -> None:
    """
    Tests for an array that consists entirely of negative numbers
    """
    arr = [-1, -2, -3, -4]
    assert sol.first_missing_positive(arr) == 1
    
def fourth_test_case(sol: first_missing_positive.Solution) -> None:
    """
    Tests for an array that is a mixture of positive and negative numbers
    """
    arr = [-1, -2, 1, 2]
    assert sol.first_missing_positive(arr) == 3

def main() -> None:
    solution = first_missing_positive.Solution()
    first_test_case(solution)
    second_test_case(solution)
    third_test_case(solution)
    fourth_test_case(solution)

if __name__ == "__main__":
    main()
    print("Our solutions passes")
