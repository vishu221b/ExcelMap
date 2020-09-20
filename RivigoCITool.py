from src import FieldsMapToFile
from gooey import GooeyParser, Gooey
import os

# FIELDS_MAP = {
#     'LR ID*': None,
#     'Consignor Name*': None,
#     'Consignor GSTIN/ PAN': 'CONSIGNOR_GSTIN',
#     'From Detailed Address*': None,  # {"default": "Domino Printech India LLP,Plot Number-1117, Sector-8, IMT Manesar- Gurgaon"},
#     'From Pincode*': None,  # {"default": 122050},
#     'Contact Name*-': None,
#     'Contact Phone*-': None,
#     'Consignee Name*': 'RECEIVER_NAME',
#     'Consignee GSTIN/ PAN': 'CONSIGNEER_GSTIN',
#     'To Detailed Address*': [
#         'RECEIVER_ADD1',
#         'RECEIVER_ADD2',
#         'RECEIVER_ADD3',
#         'RECEIVER_CITY'],
#     'To Pincode*': 'RECEIVER_PINCODE',
#     'Contact Name*': 'RECEIVER_EMAIL',
#     'Contact Phone*': 'RECEIVER_MOBILE_NO',
#     'Total boxes*': 'NO_OF_PKGS',
#     'Gross Wt (kg)*': 'ACTUAL_WT',
#     'Unit of box dims*': None,
#     'Box Length*': None,
#     'Box Breadth*': None,
#     'Box Height*': None,
#     'Box Count*': None,
#     'Invoice Number*': None,
#     'Invoice Value*': None,
#     'Ewaybill Number': 'EWB_NO',
#     'HSN CODE': None,
#     'Retail Type^': None,
#     'Payment Mode^': None,
#     'Tax ID Number^': None,
#     'Tax ID Type^': None,
#     'Packaging': None,
#     'Contents': None,
#     'Is Fragile*': None,
#     'Error Remarks': None
# }
FIELDS_MAP = {
    'LR ID*': None,
    'Consignor Name*': None,
    'Consignor GSTIN/ PAN': None,  # 'CONSIGNOR_GSTIN' Missing
    'From Detailed Address*': None,  # {"default": "Domino Printech India LLP,Plot Number-1117, Sector-8, IMT Manesar- Gurgaon"},
    'From Pincode*': None,  # {"default": 122050},
    'Contact Name*-': None,
    'Contact Phone*-': None,
    'Consignee Name*': 'Consigneename',
    'Consignee GSTIN/ PAN': 'GST Number',
    'To Detailed Address*': [
        'Address1',
        'Address2',
        'Address3',
        'City'],
    'To Pincode*': 'Pin',
    'Contact Name*': 'Email',
    'Contact Phone*': 'Phone',
    'Total boxes*': None,  # 'NO_OF_PKGS',  # Missing
    'Gross Wt (kg)*': 'Actualwt',
    'Unit of box dims*': None,
    'Box Length*': None,
    'Box Breadth*': None,
    'Box Height*': None,
    'Box Count*': None,
    'Invoice Number*': 'Invoice No',
    'Invoice Value*': 'Cargovalue SUM',
    'Ewaybill Number': None,  # 'EWB_NO',  # Missing
    'HSN CODE': None,
    'Retail Type^': None,
    'Payment Mode^': None,
    'Tax ID Number^': None,
    'Tax ID Type^': None,
    'Packaging': None,
    'Contents': None,
    'Is Fragile*': None,
    'Error Remarks': None
}

DEFAULTS = {'From Detailed Address*': "Domino Printech India LLP,Plot Number-1117, Sector-8, IMT Manesar- Gurgaon",
            'From Pincode*': 122050,
            'Consignor Name*': "Domino Printech India LLP"}


path__curr = os.path.dirname(os.path.realpath(__file__))
print(path__curr)


@Gooey(program_name="Rivigo Format Converter Tool")
def FieldMapper():
    parser = GooeyParser(description="Rivigo Excel Format Converter")
    parser.add_argument('Filename', help="Select the xlsx file to process.", widget='FileChooser')
    parsed = parser.parse_args()
    print(parsed.Filename)
    FieldsMapToFile(file_name=str(parsed.Filename), fields_map=FIELDS_MAP, default_map=DEFAULTS)
    return "Done."


if __name__ == '__main__':
    FieldMapper()
