import string
from .models import URL
import random

def short_code_generator():
    length = 8
    while True:
        code = ''.join(random.choices(string.ascii_letters + string.digits, k = length))
        if not URL.objects.filter(short_code = code).exists():
            return code