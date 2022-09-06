from .models import AccountAuthentication
from datetime import datetime

def all_data(request):
    time = datetime.now()
    current_time = time.strftime("%H")
    split = int(current_time[0])
    if split == 0:
        current_ = int(time.strftime("%H")[1])
    else:
        current_= int(time.strftime("%H"))
    print(type(current_))
    print(current_)
    all_data = AccountAuthentication.objects.last()
    context = {'all_data':all_data, 'time':current_}
    return context