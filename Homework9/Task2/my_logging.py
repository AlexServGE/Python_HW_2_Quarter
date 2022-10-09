from datetime import datetime


def logging(update, context):
    with open('Log.txt', 'a', encoding='utf-8') as log_file:
        date_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        log = f'{date_time} - {update.effective_chat.id} - {update.effective_user.first_name} - {update.message.text}\n'
        log_file.write(log)
