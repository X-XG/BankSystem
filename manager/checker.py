import string

def name(name: string):
    if len(name) > 16:
        raise Exception('the name is too long')

    # return True


def id(id: string):
    if len(id) != 18:
        raise Exception('the id length must be 18')