import binascii

def getHex(filename):
    with open(filename, "rb") as f:
        content = f.read().hex()
        return content

def ParseHex(str):
    string = ""
    count = 0
    for i in range(len(str)):
        count += 1
        if count != 2:
            string += str[i]
        if count == 2:
            string += str[i]
            string += " "
            count = 0
    return string

def Stringify(hex):
    hex_string = str(hex.replace(" ", ""))
    bytes_object = bytes.fromhex(hex_string)
    ascii_string = bytes_object.decode("ASCII")
    return ascii_string

class Hex:
    def __init__(self, filename):
        self.filename = filename
        pass

    def hexify(self):
        return ParseHex(getHex(self.filename))

    def createCopy(self):
        with open(self.filename + ".copy.txt", "w") as f:
            f.write(self.hexify())
            f.close()

    
    def SetupUI(self):
        import PySimpleGUI as sg
        layout = [[sg.Text("Hex Converter")],
                 [sg.Text('Enter Hex Code'), sg.InputText()],
                 [sg.Output(size=(60,15))],
                 [sg.Button('Run'), sg.Button('Exit')]]

        window = sg.Window("", layout)
        while True:            
            event, values = window.Read()
            if event in (None, 'Exit'):         
                exit
                break

            if event == 'Run':
                try:
                    print(Stringify(values[0]))
                except:
                    print("WARNING! Make sure its right formated, Example: 55 61 62 56")
                pass

        window.Close()
