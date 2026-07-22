insert={"name":"VAISHU","AGE":21}
MSG="HAPPY BIRTHDAY {name} YOU ARE TURNING INTO {AGE} IN 2026"
print(MSG.format_map(insert))
#The format_map() method formats the specified values of a dictionary and insert them inside the string's placeholders.
#The format_map() method returns the formatted string.
#string.format_map(dictionary)