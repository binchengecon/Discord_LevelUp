from maxtan import selfbot
import time

token = "Njk0MzE2MjI0NTgyMTIzNTgy.G5bGrv.fjGDkJ2Obz3_mA17-FPcBEW8SQnH5sYFLCtzbw"
message_number = 100000
message_wait = 30
message_content = "Auto"

bot = selfbot(token=token)
channel = bot.get_channel(1163681998607503420)


for i in range(0, message_number):
    message_id = channel.send_message(message_content)
    channel.delete_message(message_id)
    time.sleep(message_wait)
    print("Iteration " + str(i) + " complete.")
