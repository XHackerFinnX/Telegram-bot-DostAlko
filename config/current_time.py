import time

async def time_day_mon():
    
    seconds = time.time()
    result = time.localtime(seconds)
    
    return result.tm_mday, result.tm_mon


async def time_hour_min():
    
    seconds = time.time()
    result = time.localtime(seconds)
    
    return result.tm_hour, result.tm_min


async def time_day_mon_year():
    
    seconds = time.time()
    result = time.localtime(seconds)
    
    return result.tm_mday, result.tm_mon, result.tm_year