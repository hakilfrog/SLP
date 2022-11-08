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
        with open('fw_rules_v1.csv', 'r', newline='') as csvfile:
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
        return adr_mask

    def per_88_3389(self):
        b = list()
        c = '22'
        d = '3389'
        k = 0
        for i in self.action:
            if i == 'permit':
                if '22' in self.ports[i] and '3389' in self.ports[i]:
                    b.append(self.src_address[k])
            k += 1
        return b

        # ip = self.src_address + '/' + self.src_netmask
        # test_address = ipaddress.IPv4Interface(ip)
        # print(test_address.network)


a = FWrule()
print(a.adr_mask())
print(a.per_88_3389())
