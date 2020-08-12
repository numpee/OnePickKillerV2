from pynput.mouse import Button, Controller
import ntplib
from datetime import datetime

mouse = Controller()


class Clicker(object):
    @classmethod
    def start(cls, hour, minute, second, safety_margin_as_ms, server_url):
        print("Calculating server and local offset")
        target_time = datetime.now().replace(hour=hour, minute=minute, second=second,
                                             microsecond=safety_margin_as_ms * 1000)

        server_time, local_time = cls.get_server_and_device_time(server_url)
        offset = local_time - server_time
        real_target_time = target_time + offset
        print("Server time: {}".format(server_time.strftime("%H:%M:%S.%f")))
        print("Local time: {}".format(local_time.strftime("%H:%M:%S.%f")))
        if local_time > server_time:
            print("Local time is {} seconds and {} ms faster".format(offset.seconds, offset.microseconds/1000))
        else:
            print("Local time is {} seconds and {} ms slower".format((-offset).seconds, (-offset).microseconds/1000))

        print("Start process")
        last_left_seconds = None
        while True:
            now = datetime.now()
            if real_target_time < now:
                mouse.click(Button.left)
                print("Click on {} Local Time".format(now))
                print("End process!")
                break
            else:
                left_seconds = int((real_target_time - now).seconds)
                if last_left_seconds != left_seconds:
                    print("{} seconds left".format(left_seconds))
                    last_left_seconds = left_seconds


    @staticmethod
    def get_server_and_device_time(server_url):
        client = ntplib.NTPClient()
        server_response = client.request(server_url, version=3)
        local_time = datetime.now()
        server_time = datetime.fromtimestamp(server_response.tx_time)
        return server_time, local_time
