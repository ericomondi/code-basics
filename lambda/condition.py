# So, when you see f"{num:e}", 
# it means format the value of num 
# in scientific notation, and f"{num:,.2f}"
# means format the value of num as a floating-point
# number with two decimal places and commas for 
# thousands separators.


format_numeric = lambda num: f"{num:e}" if isinstance(num, int) else f"{num:,.2f}"

print("Int formatting:", format_numeric(1000000))
print("float formatting:", format_numeric(999999.789541235))
