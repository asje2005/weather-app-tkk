import tkinter
from tkinter.constants import *
from tkinter import StringVar
from tkinter.ttk import *


class View(tkinter.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("700x500")

        #---- Variables ----
        self.varSearch = StringVar()
        self.varTemp = StringVar()
        self.varLocation = StringVar()
        self.varCondition = StringVar()
        self.varFeelsLike = StringVar()
        self.varWindSpeed = StringVar()
        self.varWindDir= StringVar()
        

        self.varTemp.set("Too hot")
        self.varLocation.set("The desert")

        #---- Frames ----
        self.mainframe = Frame(self)
        self.mainframe.pack()
        self._createFrameSearchBar()
        self._createFrameInfo()

    
    def _createFrameSearchBar(self):
        self.frameSearchBar = Frame(self.mainframe)

        self.comboSearch = Combobox(self.frameSearchBar, textvariable=self.varSearch)
        self.buttonSearch = Button(self.frameSearchBar, text="Search")

        self.comboSearch.pack(padx=10, side=LEFT)
        self.buttonSearch.pack(side=RIGHT)
        self.frameSearchBar.pack()


    def _createFrameInfo(self):
        self.frameInfo = Frame(self.mainframe)

        self.labelTemp = Label(self.frameInfo, textvariable=self.varTemp)
        self.labelLocation = Label(self.frameInfo, textvariable=self.varLocation)
        self.labelIcon = Label(self.frameInfo, text='image')

        self.labelTemp.pack(pady=5)
        self.labelLocation.pack(pady=5)
        self.labelIcon.pack(pady=5)
        self.frameInfo.pack()

    def _createFrameDetails(self):
        self.frameDetails = Frame(self.mainframe)

        labelConditionLeft = Label(self.frameDetails, text='Current Conditions:')
        labelFeelsLikeLeft = Label(self.frameDetails, text='Feels Like:')
        labelWindeSpeedLeft = Label(self.frameDetails, text='Wind Speed:')
        labelWindDirLeft = Label(self.frameDetails, text='Wind Direction:')

        labelConditionRight = Label(self.frameDetails, textvarible=self.varCondition)
        labelFeelsLikeRight = Label(self.frameDetails, textvariable=self.varFeelsLike)
        labelWindeSpeedRight = Label(self.frameDetails, textvariable=self.varWindSpeed)
        labelWindDirRight = Label(self.frameDetails, textvariable=self.varWindDir)

    def _createFrameControls(self):
        pass


    def main(self):
        self.mainloop()