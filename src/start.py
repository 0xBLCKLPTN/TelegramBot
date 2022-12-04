from time import sleep


sleep(3)

from dispatcher import *
from keyboards.response import *
from keyboards.registration import *
from keyboards.admin_response import *
from utils import in_threads

    
in_threads.start_threads()


if __name__ == '__main__':
    executor.start_polling(dp)

    pass
