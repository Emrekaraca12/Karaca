import os

class File_properties:
    def __init__(self, path) -> None:
        self.path = path

    def does_exist(self) -> str:
        return os.path.exists(self.path)

    def is_readible(self) -> bool:
        return os.access(self.path, os.R_OK)
    
    def is_writable(self) -> bool:
        return os.access(self.path, os.W_OK)
    
    def is_executable(self) -> bool:
        return os.access(self.path, os.X_OK)
    
    def properties(self) -> str:
        if(os.path.exists(self.path)):
            print(f"""File is{"not" if not File_properties.is_readible else ""} readible
File is{"not" if not File_properties.is_writable else ""} writable
File is{"not" if not File_properties.is_executable else ""} executable""")
        else:
            print("File does not exist...")

class_object = File_properties("C:\\Study\\Database_user_inf\\AusUniversum.txt")
class_object.properties()

class_object = File_properties("C:\\Study\\Database_user_inf\\AusUniversum")
class_object.properties()