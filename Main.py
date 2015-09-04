import Tkinter, Tkconstants, tkFileDialog

class TkFileDialogExample(Tkinter.Frame):

    latList = []
    longList = []
    JSONbuild = ""

    def __init__(self, root):

        Tkinter.Frame.__init__(self, root)

        # options for buttons
        button_opt = {'fill': Tkconstants.BOTH, 'padx': 5, 'pady': 5}

        # define buttons
        Tkinter.Button(self, text='askopenfile', command=self.askopenfile).pack(**button_opt)


        # define options for opening or saving a file
        self.file_opt = options = {}
        options['defaultextension'] = '.gpx'
        options['filetypes'] = [('Garmin Nav File', '.gpx')]
        options['initialdir'] = 'C:\\'
        options['parent'] = root
        options['title'] = 'Open GPX file'

    def Convert2JSON(self):
        self.JSONbuild += "["
        lstLength = len(self.latList)
        for num in range(0, lstLength):
            self.JSONbuild+="\n\t{\n\t\t\"pointLatitude\":" + self.latList[num] +","
            self.JSONbuild+="\n\t\t\"pointLatitude\":" + self.longList[num] + "\n\t},"

        self.JSONbuild = self.JSONbuild[:-1]
        self.JSONbuild += "\n]"

        print self.JSONbuild
        self.asksaveasfile()

    def asksaveasfile(self):

        """Returns an opened file in write mode."""
        self.file_opt = options = {}
        options['defaultextension'] = '.json'
        options['filetypes'] = [('JSON File', '.json')]
        options['initialdir'] = 'C:\\'
        options['parent'] = root
        options['title'] = 'Save JSON file'

        JSave = tkFileDialog.asksaveasfile(mode='w', **self.file_opt)
        JSave.write(self.JSONbuild)
        JSave.close()

    def askopenfile(self):

        """Returns an opened file in read mode."""
        content = []
        openF = tkFileDialog.askopenfile(mode='r', **self.file_opt)
        self.txt = openF.readlines()
        lineCount = 0
        for line in self.txt:
            strlat = []
            strlong = []
            if line.find('<gpxx:rpt') != -1:
                latLong = True
                count = 20

                while latLong == True:
                    if line[count] == "\"":
                        count += 7
                        latLong = False
                    else:
                        strlat.append(line[count])
                        count += 1

                latLong = True

                while latLong == True:
                    if line[count] == "\"":
                        latLong = False
                    else:
                        strlong.append(line[count])
                        count += 1


                strNum= ""

                for char in strlat:
                    strNum += char

                floatLat = strNum

                strNum= ""

                for char in strlong:
                    strNum += char
                floatLong = strNum


                self.latList.append(floatLat)
                self.longList.append(floatLong)
                print floatLat
                print floatLong

            lineCount += 1

        openF.close()

        self.Convert2JSON()


if __name__=='__main__':
    root = Tkinter.Tk()
    TkFileDialogExample(root).pack()
    root.mainloop()
