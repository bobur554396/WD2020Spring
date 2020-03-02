# import datetime
from datetime import datetime

# import my_lib

# my_lib.show_info("hi")


from my_lib import show_info as _

_('hi')
