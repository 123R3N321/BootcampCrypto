# this generates the firebase id
import hashlib

def sha1_hash_string(input_string):
    # Encode the string to bytes, then generate the SHA-1 hash
    sha1_hash = hashlib.sha1(input_string.encode())

    # Return the hexadecimal representation of the hash
    return sha1_hash.hexdigest()


def firebaseFormat(info):
    res = ''
    for i in range(len(info)):
        if not info[i].isdigit():
            res += info[i:]
            break
    final = ''
    for i in range(len(res)):
        if i <= 29:
            final += res[i]
        else:
            break
    return final

def firebaseID(info):
    '''

    :param info: pass in the name of the project in firebase
    :return: the id of it.
    '''
    return firebaseFormat(sha1_hash_string(info))

# debug code
print(firebaseID("BootcampCrypto"))