# String Processing: Spreadsheet Encoding - conversting string to integer - here A correspond to 1 instead of 0 , B = 2, Z = 26
# how to solve the problem of implementing a function that converts a spreadsheet column ID (i.e. "A", "B", "C", ..., "Z", "AA", etc.)
# to the corresponding integer.
# e.g. AA = A * 26^1 + A * 26^0 = 1 * 26^1 + 1 * 26^0 = 27
# n is length of string len(314) = 3

def spreadsheet_encode_column(col_str):
    num = 0  # num variable will return the final number will return
    # it is exponent and will decrement it by 1 everytime ^1 - ^0
    count = len(col_str) - 1
    for s in col_str:  # s is character in col_str given
        # () = this is representation of current character processed in string
        num += 26**count * (ord(s) - ord("A") + 1)
        count -= 1  # will accumulate that is num and decrease count by 1
    return num


print(spreadsheet_encode_column("A"))  # return 1
print(spreadsheet_encode_column("AA"))  # return 27
print(spreadsheet_encode_column("ZZ"))  # return 702

# ord("A") # python function for unicode = return 65, ord("B") = return 66 ...
