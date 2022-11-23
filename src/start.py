from dispatcher import *
from keyboards.response import *
from keyboards.registration import *
from keyboards.admin_response import *

if __name__ == '__main__':
    executor.start_polling(dp)
    pass