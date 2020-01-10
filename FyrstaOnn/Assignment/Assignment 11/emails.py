def get_emails ():
    email_list = []
    email_user_input = "True"
    while email_user_input.lower() != "q":
        email_user_input = input("Email address: ")
        if email_user_input.lower() != "q":
            email_list.append(email_user_input)
    return email_list

def get_names_and_domains (emails):
    names_and_domains_list = []
    for element in emails:
        names_and_domains_list.append(tuple(element.split("@")))
    return names_and_domains_list

# Main program starts here - DO NOT change it

email_list = get_emails()
print(email_list)
names_and_domains = get_names_and_domains(email_list)
print(names_and_domains)