def format_name(f_name,l_name):
    '''Takes First and Last name from user and formats it to return title case version of the input '''
    if f_name== "" or l_name == "":
        return "No input found"
    formatted_fname = f_name.title()
    formatted_lname = l_name.title()
    return f"Result: {formatted_fname} {formatted_lname}"

print(format_name(input("What is your First Name?"),input("What is your Second Name?")))