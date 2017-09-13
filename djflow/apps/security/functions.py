import random
import string


class SecurityUtils:
    """
    Utils for Security
    """

    def random_password(self):
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        size = random.randint(8, 12)
        return ''.join(random.choice(chars) for x in range(size))
