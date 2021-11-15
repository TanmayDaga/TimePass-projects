import datetime
import json
import plyer


def reminder(dicti, keyOfIt):
    plyer.notification.notify(
        title=keyOfIt, message=f"{dicti[keyOfIt][2]}")


def days_finder(dictionary):
    for keys in dictionary.keys():
        datetime_obj = datetime.datetime.strptime(
            dictionary[keys][0], "%d-%m-%Y")
        datedeltaobj = datetime_obj - datetime.datetime.today()
        days = int(datedeltaobj.days)
        if days < dictionary[keys][1]:
            reminder(dictionary, keys)


def main():
    today = datetime.date.today().strftime("%d:%m:%Y")
    with open("tasks.json") as f:
        python_object = json.load(f)
        days_finder(python_object)


if __name__ == '__main__':
    main()
