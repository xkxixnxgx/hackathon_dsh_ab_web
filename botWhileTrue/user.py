from time import strftime

user_dict = {}

def create(chat_id: str, username: str):
    user_dict[chat_id] = dict({
        "username": username,
        "reg_form": None,
        "service": "",
        "proposal": "",
        "status": "",
        "data": {}
    })

def check(chat_id: str) -> bool:
    if chat_id in user_dict: return True
    return False

def get(chat_id: str) -> dict:
    if chat_id in user_dict: return user_dict[chat_id]
    else: return {}

def set(chat_id: str, data=False, **args):
    if data: 
        for key, value in args.items(): user_dict[chat_id][data][key] = value
    else:
        for key, value in args.items(): user_dict[chat_id][key] = value
    
def prapare(chat_id: str) -> dict:
    user_data = get(chat_id)
    del user_data['reg_form']
    user_data['chat_id'] = chat_id
    user_data['status'] = "В обработке"
    user_data['date_time'] = strftime("%H:%M %d.%m.%Y")
    return user_data

