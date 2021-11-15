import datetime
import json
import plyer
import argparse
import sys
import time


def task_add(args):
        task_name = args.n
        task_date = args.t
        dictt = {task_name.lower(): (str(task_date), args.r, args.d)}
        with open("tasks.json") as f:
            data = json.load(f)
            data.update(dictt)
        with open('tasks.json', "w") as f:
            json.dump(data, f, indent=4)

        return "Completed"


def main():
	parser = argparse.ArgumentParser()

    parser.add_argument("--n", type=str, default='newtask',
                        help="Add a new Task")
    parser.add_argument(
        "--t", type=str, default=str(datetime.date.today().strftime("%d-%m-%Y")))
    parser.add_argument("--r", type=int, default=10)

    parser.add_argument("--d", type=str, default="No Description")

    args = parser.parse_args()
    sys.stdout.write(task_add(args))

if __name__ == '__main__':
	main()
