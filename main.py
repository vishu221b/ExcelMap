from src import FieldsMapToFile

FIELDS_MAP = {
    'LR ID*': None,
    'Consignor Name*': None,
    'Consignor GSTIN/ PAN': 'CONSIGNOR_GSTIN',
    'From Detailed Address*': None,
    'From Pincode*': None,
    'Contact Name*-': None,
    'Contact Phone*-': None,
    'Consignee Name*': 'RECEIVER_NAME',
    'Consignee GSTIN/ PAN': 'CONSIGNEER_GSTIN',
    'To Detailed Address*': [
        'RECEIVER_ADD1',
        'RECEIVER_ADD2',
        'RECEIVER_ADD3',
        'RECEIVER_CITY'],
    'To Pincode*': 'RECEIVER_PINCODE',
    'Contact Name*': 'RECEIVER_EMAIL',
    'Contact Phone*': 'RECEIVER_MOBILE_NO',
    'Total boxes*': 'NO_OF_PKGS',
    'Gross Wt (kg)*': 'ACTUAL_WT',
    'Unit of box dims*': None,
    'Box Length*': None,
    'Box Breadth*': None,
    'Box Height*': None,
    'Box Count*': None,
    'Invoice Number*': None,
    'Invoice Value*': None,
    'Ewaybill Number': 'EWB_NO',
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

pandu = FieldsMapToFile(file_name='fields.xlsx', fields_map=FIELDS_MAP)
