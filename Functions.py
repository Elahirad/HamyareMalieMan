# jdatetime Should be installed via pip install jdatetime


import csv
from random import randrange
import datetime

import jdatetime


def JalaliToGrg(dateString):
    y, m, d = [int(x) for x in dateString.split('/')]
    dateTuple = jdatetime.JalaliToGregorian(y, m, d).getGregorianList()
    return datetime.date(dateTuple[0], dateTuple[1], dateTuple[2])


def dataCatching(username):  # Reading all data from txt file
    with open(f"{username}.csv", 'r', encoding='utf-8') as csv_open:
        csv_reading = csv.DictReader(csv_open)
        return list(csv_reading)


def dataAdding(username, amount, subject, type, date):  # Adding new item to txt file
    with open(f"{username}.csv", mode='a', encoding='utf-8') as csv_open:
        field_names = ['id', 'amount', 'subject', 'type', 'date']
        csv_writing = csv.DictWriter(csv_open, fieldnames=field_names)
        randID = randrange(1000000000, 9999999999, 1)
        csv_writing.writerow({'id': randID, 'amount': amount, 'subject': subject, 'type': type, 'date': date})


def deleteItem(username, targetID):
    csv_reader = []
    field_names = ['id', 'amount', 'subject', 'type', 'date']
    with open(f"{username}.csv", mode='r', encoding='utf-8') as dataopening:
        csv_reader = list(csv.DictReader(dataopening, fieldnames=field_names))
        i = 0
        END = len(csv_reader)
        while i < END:
            if csv_reader[i]['id'] == targetID:
                csv_reader.pop(i)
                break
            i += 1
    with open(f"{username}.csv", mode='w', encoding='utf-8') as datawriting:
        csv_writer = csv.DictWriter(datawriting, fieldnames=field_names)
        csv_writer.writerows(csv_reader)


def sortDataByDate(username, state):
    csv_reader = []
    field_names = ['id', 'amount', 'subject', 'type', 'date']
    with open(f"{username}.csv", mode='r', encoding='utf-8') as dataopening:
        csv_reader = list(csv.DictReader(dataopening, fieldnames=field_names))
        tempDict = csv_reader[0]
        csv_reader.pop(0)
        csv_reader = sorted(csv_reader, key=lambda x: datetime.date(
            jdatetime.JalaliToGregorian(int(x['date'].split('/')[0]), int(x['date'].split('/')[1]),
                                        int(x['date'].split('/')[2])).getGregorianList()[0],
            jdatetime.JalaliToGregorian(int(x['date'].split('/')[0]), int(x['date'].split('/')[1]),
                                        int(x['date'].split('/')[2])).getGregorianList()[1],
            jdatetime.JalaliToGregorian(int(x['date'].split('/')[0]), int(x['date'].split('/')[1]),
                                        int(x['date'].split('/')[2])).getGregorianList()[2]), reverse=state)
        csv_reader.insert(0, tempDict)
    with open(f"{username}.csv", mode='w', encoding='utf-8') as datawriting:
        csv_writer = csv.DictWriter(datawriting, fieldnames=field_names)
        csv_writer.writerows(csv_reader)


def sortDataByAmount(username, state):
    csv_reader = []
    field_names = ['id', 'amount', 'subject', 'type', 'date']
    with open(f"{username}.csv", mode='r', encoding='utf-8') as dataopening:
        csv_reader = list(csv.DictReader(dataopening, fieldnames=field_names))
        tempDict = csv_reader[0]
        csv_reader.pop(0)
        csv_reader = sorted(csv_reader, key=lambda x: int(x['amount']), reverse=state)
        csv_reader.insert(0, tempDict)
    with open(f"{username}.csv", mode='w', encoding='utf-8') as datawriting:
        csv_writer = csv.DictWriter(datawriting, fieldnames=field_names)
        csv_writer.writerows(csv_reader)


def dataReplacing(username, targetID, amount, subject, type, date):
    csv_reader = []
    field_names = ['id', 'amount', 'subject', 'type', 'date']
    with open(f"{username}.csv", mode='r', encoding='utf-8') as dataopening:
        csv_reader = list(csv.DictReader(dataopening, fieldnames=field_names))
        for data in csv_reader:
            if data['id'] == targetID:
                data['amount'] = amount
                data['subject'] = subject
                data['type'] = type
                data['date'] = date
    with open(f"{username}.csv", mode='w', encoding='utf-8') as datawriting:
        csv_writer = csv.DictWriter(datawriting, fieldnames=field_names)
        csv_writer.writerows(csv_reader)
