import re


def fancy_barcodes(num):

    condition = r'\@[\#]+([A-Z][A-Za-z0-9]{5,}[A-Z])\@[\#]+'

    for _ in range(num):
        barcode = input()

        matches = re.match(condition, barcode)

        if matches:
            product_group = ''.join([i for i in matches.group() if i.isdigit()])
            if product_group == '':
                print(f"Product group: 00")
            else:
                print(f"Product group: {product_group}")
        else:
            print('Invalid barcode')


        #
        # matches = re.findall(condition, barcode)
        # if matches:
        #     matches = ''.join(matches)
        #     product_group = ''.join([i for i in matches if i.isdigit()])
        #     if product_group == '':
        #         print(f"Product group: 00")
        #     else:
        #         print(f"Product group: {product_group}")
        # else:
        #     print('Invalid barcode')


number = int(input())
fancy_barcodes(number)

