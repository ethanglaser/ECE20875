import re

def problem1(searchstring):
    """
    Match phone numbers.

    :param searchstring: string
    :return: True or False
    """
    if re.match("([0-9]{3}[-])?([0-9]{3})[-][0-9]{4}", searchstring):
        return True
    if re.match("([(][0-9]{3}[)])[ ]([0-9]{3})[-][0-9]{4}", searchstring):
        return True
    return False
        
def problem2(searchstring):
    """
    Extract street name from address.

    :param searchstring: string
    :return: string
    """
    return re.search(r"([A-Z][a-z]*[ ])+", re.search(r"(\d)+[ ]([A-Z][a-z]*[ ])+([Rd.]*[Ave.]*[Dr.]*[St.]*)", searchstring).group()).group().strip()
    
def problem3(searchstring):
    """
    Garble Street name.

    :param searchstring: string
    :return: string
    """
    pass


if __name__ == '__main__' :
    print(problem1('765-494-4600')) #True
    print(problem1(' 765-494-4600 ')) #False
    print(problem1('(765) 494 4600')) #False
    print(problem1('(765) 494-4600')) #True    
    print(problem1('494-4600')) #True
    
    print(problem2('The EE building is at 465 Northwestern Ave.')) #Northwestern
    print(problem2('Meet me at 201 South First St. at noon')) #South First
    
    print(problem3('The EE building is at 465 Northwestern Ave.'))
    print(problem3('Meet me at 201 South First St. at noon'))