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
                self.datetime_created = row['datetime_created']
                self.src_address.append(row['src_address'])
                self.src_netmask.append(row['src_netmask'])
                self.dst_address.append(row['dst_address'])
                self.dst_netmask.append(row['dst_netmask'])
                self.ports.append(row['ports'])
                self.action.append(row['action'])
        with open('fw_rules_v2.csv', 'r', newline='') as csvfile:
            spamreader = csv.DictReader(csvfile, delimiter=';')
            #  self.list_of_my_rules = list()
            for row in spamreader:
                self.datetime_created = row['datetime_created']
                self.src_address.append(row['src_address'])
                self.src_netmask.append(row['src_netmask'])
                self.dst_address.append(row['dst_address'])
                self.dst_netmask.append(row['dst_netmask'])
                self.ports.append(row['ports'])
                self.action.append(row['action'])

        with open('fw_rules_v3.csv', 'r', newline='') as csvfile:
            spamreader = csv.DictReader(csvfile, delimiter=';')
            # self.list_of_my_rules = list()
            for row in spamreader:
                self.datetime_created = row['datetime_created']
                self.src_address.append(row['src_address'])
                self.src_netmask.append(row['src_netmask'])
                self.dst_address.append(row['dst_address'])
                self.dst_netmask.append(row['dst_netmask'])
                self.ports.append(row['ports'])
                self.action.append(row['action'])
                #  print(self.src_netmask)
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

        # ip = self.src_address + '/' + self.src_netmask
        # test_address = ipaddress.IPv4Interface(ip)
        # print(test_address.network)


a = FWrule()
print(a.adr_mask())
#  print(a.src_netmask)
#  sample_rule = list_of_my_rules[0]






# import csv
# import datetime
# import ipaddress
#
#
# class FWrule:
#     datetime_created: datetime.datetime
#     src_address: str
#     src_netmask: str
#     dst_address: str
#     dst_netmask: str
#     ports: list[int]
#     action: str
#
#     def adr_mask(self):
#         ip = self.src_address + '/' + self.src_netmask
#         test_address = ipaddress.IPv4Interface(ip)
#         print(test_address.network)
#

# def generate_list():
#     with open('fw_rules_v1.csv', 'r', newline='') as csvfile:
#         spamreader = csv.DictReader(csvfile, delimiter=';')
#         list_of_my_rules = list()
#         for row in spamreader:
#             rule = FWrule()
#
#             rule.datetime_created = row['datetime_created']
#             rule.src_address = row['src_address']
#             rule.src_netmask = row['src_netmask']
#             rule.dst_address = row['dst_address']
#             rule.dst_netmask = row['dst_netmask']
#             rule.port = row['ports']
#             rule.action = row['action']
#
#             list_of_my_rules.append(rule.datetime_created)
#             list_of_my_rules.append(rule.src_address)
#             list_of_my_rules.append(rule.src_netmask)
#             list_of_my_rules.append(rule.dst_address)
#             list_of_my_rules.append(rule.dst_netmask)
#             list_of_my_rules.append(rule.port)
#             list_of_my_rules.append(rule.action)
#
#             return list_of_my_rules
#
#
# list_of_my_rules = generate_list()
# print(list_of_my_rules)
# generate_list()
#
# a = FWrule()
#
# sample_rule = list_of_my_rules[0]
