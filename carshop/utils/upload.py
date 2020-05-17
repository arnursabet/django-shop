import imghdr
import random
import string


def get_random_name(length=25):
    y = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(25))
    return y

def battery_upload(instance, filename):
  y = get_random_name()
  return 'batteries/{}.{}'.format(y, imghdr.what(instance.image))