import pandas
from clientMacrosScript.exceptions import (
    InvalidFieldToFileMapException,
    InvalidFileFormatException,
    FileNotFoundException
)


class FieldsMapToFile:
    ALLOWED_EXTENSIONS = ['xlsx']

    def __init__(self, file_name: str, fields_map: dict = None):
        if fields_map is None:
            self._fields_map = dict()
        self.ALLOWED_SUBTYPES = (list, tuple)
        self.new_df = None
        self._new_file_name = None
        self._name_before_extension = None
        self._extension = None
        self._fields_map = fields_map
        try:
            self.new_file_name = self.clean_file_name(file_name)
        except Exception as e:
            print(e)

    def clean_file_name(self, file_name: str):
        try:
            self._name_before_extension, self._extension = file_name.rsplit(".", maxsplit=1)
            print(self._extension)
            if self._extension not in FieldsMapToFile.ALLOWED_EXTENSIONS:
                raise InvalidFileFormatException
            return file_name
        except __exceptions__ as e:
            raise e

    @property
    def new_file_name(self):
        return self._new_file_name

    @new_file_name.setter
    def new_file_name(self, file_name: str):
        try:
            df = pandas.read_excel(f'./files/{file_name}')
            fieldMapList = [c for c in self._fields_map.keys()]
            self.new_df = pandas.DataFrame(columns=fieldMapList)
            print("FML-", fieldMapList)
            _INDEX_ = fieldMapList[0]
            for i in range(0, len(df)):
                itemDict = {}
                for k, v in self._fields_map.items():
                    if k is not None:
                        if not isinstance(v, self.ALLOWED_SUBTYPES):
                            if v:
                                itemDict.__setitem__(k, df[v][i])
                                print(k, v, i, df[v][i], "\n===========\n")
                            elif v is None:
                                itemDict.__setitem__(k, "")
                        elif isinstance(v, self.ALLOWED_SUBTYPES):
                            finalString = ""
                            for inst in v:
                                finalString += f'{str(df[inst][i])} '
                            itemDict.__setitem__(k, finalString)
                print(itemDict)
                self.new_df = self.new_df.append(itemDict, ignore_index=True)
                print(self.new_df)
                # self.new_df.set_index(keys=_INDEX_, inplace=True, verify_integrity=False)
                print("asdad")
                print(self.new_df)
        except FileNotFoundError as e:
            # print(e)
            raise FileNotFoundException(f"Could not locate file {file_name}.")
        except Exception as e:
            print(e)
            raise InvalidFieldToFileMapException("There is some mis-match. Please check your file fields-map's values.")
        self._new_file_name = f'{self._name_before_extension}-result.xlsx'
        self.new_df.to_excel(self._new_file_name)
        ran = True
        while ran:
            va = input("Exit?")
            if va.lower() == 'y':
                ran = False


__exceptions__ = [FileNotFoundException, InvalidFileFormatException, InvalidFieldToFileMapException]


#  Utility Excel tool to Export certain columns from one file to certain columns in new file?
