import argparse

from clicker import Clicker

parser = argparse.ArgumentParser(description='One Pick Clicker')
parser.add_argument('--hour', type=int, default=9, help='Sugang Start time (0~23) (default: 9)')
parser.add_argument('--minute', type=int, default=0, help='Sugang Start min (0~60) (default: 0)')
parser.add_argument('--second', type=int, default=0, help='Sugang Start sec (0~60) (default: 0)')
parser.add_argument('--safety_margin_as_ms', type=int, default=1,
                    help='click after safety_margin_as_ms millisecond (default: 1ms)')
parser.add_argument('--server_url', type=str, default="time2.kriss.re.kr", help="Time server URL")

args = parser.parse_args()


def main(parsed_args):
    Clicker.start(parsed_args.hour, parsed_args.minute, parsed_args.second, parsed_args.safety_margin_as_ms,
                  parsed_args.server_url)


if __name__ == '__main__':
    main(args)
