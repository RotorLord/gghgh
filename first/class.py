class CopyBook:
    def __init__(self, color, ManyPaper, ShapePaper, TypePaper, Subj, Creator, Num, Year, StatusWrite = "None", StatusOpen = "Clode", StatusOwner = "None"   ):
        self.color = color
        self.ManyPaper = ManyPaper
        self.ShapePaper = ShapePaper
        self.TypePaper = TypePaper
        self.Subj = Subj
        self.Creator = Creator
        self.Num = Num
        self.Year = Year
        self.StatusWrite = StatusWrite
        self.StatusOpen = StatusOpen
        self.StatusOwner = StatusOwner


    def show(self):
        print(self.color)
        print(self.ManyPaper)
        print(self.ShapePaper)
        print(self.TypePaper)
        print(self.Subj)
        print(self.Creator)
        print(self.Num)
        print(self.Year)
        print(self.StatusWrite)
        print(self.StatusOpen)
        print(self.StatusOwner)





    def SatusCopyBook(self):
        if(self.StatusWrite == "start"):
            self.StatusWrite = "Finished"
        else :
            self.StatusWrite = "Start"

        if(self.StatusOpen == "Close"):
            self.StatusOpen = "Open"
        else:
            self.StatusOpen = "Close"

        if(self.StatusOwner == "Available"):
            self.StatusOwner = "Not Available"
        else:
            self.StatusOwner = "Available"


SashaCopyBook = CopyBook
SashaCopyBook = CopyBook("White", "48", "A5", "Square", "Ukrain Language", "Yes", "9348939", "2020", "Finished", "Close", "Available" )


SashaCopyBook.SatusCopyBook()
SashaCopyBook.show()

