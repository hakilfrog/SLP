import csv
import datetime
import ipaddress


class FWrule:
    datetime_created: list = list()  # datetime.datetime
    src_address: list = list()
    src_netmask: list = list()
    dst_address: list = list()
    dst_netmask: list = list()
    ports: list = list()
    action: list = list()
    list_of_my_rules: list = list()

    def __init__(self):
        with open('fw_rules_v1.csv', 'r', newline='') as csvfile: # не получилось придумать как брать разные названия
            # файлов, т к из коснтруктора не получилось вызывать фукцию/метод для впихивания файла 
            spamreader = csv.DictReader(csvfile, delimiter=';')
            self.list_of_my_rules = list()
            for row in spamreader:
                self.datetime_created.append(row['datetime_created'])
                self.src_address.append(row['src_address'])
                self.src_netmask.append(row['src_netmask'])
                self.dst_address.append(row['dst_address'])
                self.dst_netmask.append(row['dst_netmask'])
                self.ports.append(row['ports'])
                self.action.append(row['action'])
        with open('fw_rules_v2.csv', 'r', newline='') as csvfile:
            spamreader = csv.DictReader(csvfile, delimiter=';')
            for row in spamreader:
                self.datetime_created.append(row['datetime_created'])
                self.src_address.append(row['src_address'])
                self.src_netmask.append(row['src_netmask'])
                self.dst_address.append(row['dst_address'])
                self.dst_netmask.append(row['dst_netmask'])
                self.ports.append(row['ports'])
                self.action.append(row['action'])

        with open('fw_rules_v3.csv', 'r', newline='') as csvfile:
            spamreader = csv.DictReader(csvfile, delimiter=';')
            for row in spamreader:
                self.datetime_created.append(row['datetime_created'])
                self.src_address.append(row['src_address'])
                self.src_netmask.append(row['src_netmask'])
                self.dst_address.append(row['dst_address'])
                self.dst_netmask.append(row['dst_netmask'])
                self.ports.append(row['ports'])
                self.action.append(row['action'])

        print(self.src_address)

    def adr_mask(self):
        adr_mask = list()
        t = 0
        for row in self.src_address:
            ip = row + '/' + self.src_netmask[t]
            current_address = ipaddress.IPv4Interface(ip)
            if current_address.network not in adr_mask:
                adr_mask.append(current_address.network)
            t += 1
        list_adr_mask = list()
        list_adr_mask.append(adr_mask)
        print(list_adr_mask)
        with open('adr_mask.csv', 'w', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            # writer.writerow(list_adr_mask)
            for row in list_adr_mask:
                writer.writerow(row)
        return adr_mask

    def per_88_3389(self):
        b = list()
        c = '22'
        d = '3389'
        k = 0
        for i in self.action:
            if i == 'permit':
                if c in self.ports[k] and d in self.ports[k]:
                    b.append(self.src_address[k])
            k += 1
        return b

    def per_80_443(self):
        b = list()
        port1 = '80'
        port2 = '443'
        k = 0
        for i in self.action:
            if i == 'permit':
                if port1 in self.ports[k] and port2 in self.ports[k]:
                    b.append(self.src_address[k])
            k += 1
        return b

    def per_21(self):
        b = list()
        port1 = '21'
        k = 0
        for i in self.action:
            if i == 'permit':
                if port1 in self.ports[k]:
                    b.append(self.src_address[k])
            k += 1
        return b

    def all_per(self):
        b = list()
        k = 0
        for i in self.action:
            if i == 'permit':
                b.append(self.src_address[k])
            k += 1
        return b

    def all_forb(self):
        b = list()
        k = 0
        for i in self.action:
            if i != 'permit':
                b.append(self.src_address[k])
            k += 1
        return b

    def one_year_ago(self):
        itog_date = list()
        for list_date in self.datetime_created:
            date_date = datetime.datetime.fromisoformat(list_date)

            delta = datetime.timedelta(days=365)
            if datetime.datetime.now(datetime.timezone.utc) - date_date > delta:
                itog_date.append(list_date)
        return itog_date

    def this_three_month(self):
        itog_date = list()
        for list_date in self.datetime_created:
            date_date = datetime.datetime.fromisoformat(list_date)

            delta = datetime.timedelta(days=92)
            if datetime.datetime.now(datetime.timezone.utc) - date_date < delta:
                itog_date.append(list_date)
        return itog_date


a = FWrule()
print('adr_mask:\n', a.adr_mask(), '\n', '-' * 3500)
print('per_88_3389:\n', a.per_88_3389(), '\n', '-' * 3500)
print('per_80_443:\n', a.per_80_443(), '\n', '-' * 3500)
print('per_21:\n', a.per_21(), '\n', '-' * 3500)
print('all_per:\n', a.all_per(), '\n', '-' * 3500)
print('all_forb:\n', a.all_forb(), '\n', '-' * 3500)
print('one_year_ago+:\n', a.one_year_ago(), '\n', '-' * 3500)
print('this_three_month:\n', a.this_three_month(), '\n', '-' * 3500)
