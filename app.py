from modules.subscribers.utils import loadSubscribers
from modules.subscribers.email import sendEmail

subscribers = loadSubscribers()
print(subscribers)

sendEmail(subscribers[1]['email'], subscribers[1]['name'], '###@gmail.com', "pass1")
