# Test cases for comment column alignment

# Default (+2 spaces after code)
def function_with_comment_plus2(param1, param2, param3, param4, param5, param6, param7, param8, param9, param10):  # This comment should be 2 spaces after the code
    pass

# Column 60
def function_with_comment_60(param1, param2, param3, param4, param5, param6, param7, param8, param9, param10):  # This comment should align at column 60
    pass

# Preserve original indentation
def function_with_comment_preserve(param1, param2, param3, param4, param5, param6, param7, param8, param9, param10):  # This comment should keep its original position
    pass

# Test with pragma comments
def function_with_pragma(param1, param2, param3, param4, param5, param6, param7, param8, param9, param10):  # type: ignore
    pass

# Test with multiple comments
def function_with_multiple_comments(param1, param2, param3, param4, param5, param6, param7, param8, param9, param10):  # First comment
    # Second comment
    pass 