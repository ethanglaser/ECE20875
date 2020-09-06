def histogram(data, n, b, h):
    # data is a list
    # n is an integer
    # b and h are floats
    
    # Write your code here

    #can add error checker to make sure n is int greater than 0

    final = [0] * n
    for value in data:
        if value < h and value > b:
            final[int((value - b) / ((h - b) / n))] += 1
    return final

    # return the variable storing the histogram
    # Output should be a list

    pass


def addressbook(name_to_phone, name_to_address):
    #name_to_phone and name_to_address are both dictionaries
    
    # Write your code here
    final = {}
    for addressKey in name_to_address.keys():
        if name_to_address[addressKey] in final.keys():
            final[name_to_address[addressKey]][0].append(addressKey)
            if final[name_to_address[addressKey]][1] != name_to_phone[addressKey]:
                print("Warning: " + addressKey + " has a different number for " + name_to_address[addressKey] + " than " + final[name_to_address[addressKey]][0][0] + ". Using the number for " + final[name_to_address[addressKey]][0][0] + ".")
        else:
            final[name_to_address[addressKey]] = ([addressKey], name_to_phone[addressKey])
    return final

    # return the variable storing address_to_all
    # Output should be a dictionary
    
    pass