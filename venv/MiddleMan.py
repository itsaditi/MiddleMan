import random
from tkinter import *
root = Tk()
root.attributes('-fullscreen', True)
root.title("Game: MiddleMan")

# Defining frames
_landingscreen_=Frame(root)
_gamingconsole_=Frame(root)
_resultscreen_=Frame(root)

_global_letters = ['S', 'K', 'H']

def _defaultFrame_(inputframe):
    inputframe.grid()

def _switchFrames(sourceframe, destframe):
    sourceframe.destroy();
    destframe.grid();


def _randomseqgen(size):
    genseq=[]
    for y in range(0,size):
        genseq.append(_global_letters[random.randint(0,2)])
    return genseq

leftKeyPressed=0;
rightKeyPressed=0;
gameoverstat=[0]
options = []
correctoption = []
optionbyuser = []
count=0


def _gamingconsoleframe_():
    _landingscreen_.destroy()
    _gamingconsole_.grid()
    _gamingconsole_.focus_set()
    _gamingconsole_.bind("<Key>", key)
    # print("in gamingconsole", inputkey)
    # Label(_gamingconsole_, text=inputkey).pack()

def _tryagain_():
    _resultscreen_.destroy()
    _gamingconsole_.grid()
    _gamingconsole_.focus_set()
    _gamingconsole_.bind("<Key>", key)
    # print("in gamingconsole", inputkey)
    # Label(_gamingconsole_, text=inputkey).pack()

def _excludedoptions(correctoption):
    for x in _global_letters:
        # print(x, correctoption)
        if(x != correctoption):
            return x

def _computeresult(optbyuser):
    print(options, correctoption,optbyuser)
    print('Here_77', correctoption)
    print('Here',options[0][optbyuser])
    if(correctoption[0]==options[0][optbyuser]):
        print("correct")
        _CorrectLabel_=Label(_gamingconsole_, text="Correct")
        _CorrectLabel_.grid(row=10, column=1)
        _gamingconsoleframe_()
    else:
        _GameOverLabel_=Label(_gamingconsole_, text="Game Over")
        _GameOverLabel_.grid(row=10, column=1)
        gameoverstat[0]=1
        _gamingconsole_.destroy()
        _resultscreen_.grid()



def _geninputseq():
    localoptions = []
    tempcorrectoption = ''
    tempoptionbyuser = ''
    inputkey = _randomseqgen(5)
    _inputstringLabel_=Label(_gamingconsole_, text=inputkey, font="none 12")
    _inputstringLabel_.grid(row=7, column=1)
    tempcorrectoption = inputkey[2]
    wrongoption = _excludedoptions(inputkey[2])
    tempoptions = [inputkey[2], wrongoption]
    print(tempoptions)
    _newLine_=Label(_gamingconsole_, text="\n")
    _newLine_.grid(row=8, column=1)
    localoptions = random.sample(tempoptions, 2)
    print(localoptions)
    _optionsLabel_=Label(_gamingconsole_, text=localoptions[0] + "                 " + localoptions[1], font="none 12")
    _optionsLabel_.grid(row=9, column=1)
    inputoptions = [correctoption, optionbyuser]
    correctoption.append(tempcorrectoption)
    options.append(localoptions)

def key(event):
    if(gameoverstat[0]==0):
        if(event.keycode==37):
            leftKeyPressed=1
            _computeresult(0)
            options.clear()
            correctoption.clear()
            optionbyuser.clear()
            if(gameoverstat[0]==0):
                _geninputseq()
        if(event.keycode==39):
            rightKeyPressed=1
            _computeresult(1)
            options.clear()
            correctoption.clear()
            optionbyuser.clear()
            if (gameoverstat[0] == 0):
                _geninputseq()

def enterkey(event):
    print(event)
    if(event.keycode==13):
        _gamingconsoleframe_()

# Setting Landing page as default page
_defaultFrame_(_landingscreen_)

# LANDING SCREEN

_game_title1_=Label(_landingscreen_, text="\n\n" + "MiddleMan", font="none 52 bold",)
_game_title2_=Label(_landingscreen_, text="Exercise for your brain" + "\n\n" , font="none 22 bold")
_game_title1_.grid(row=5, column=1)
_game_title2_.grid(row=6, column=1)

_instructionlabel_ = LabelFrame(_landingscreen_, text="How to play this game ?",font="none 16", height=700,padx=5, pady=5)
# _instructionlabel_.config(labelanchor="n")
_instructionlabel_.grid(row=7, column=1)

instructionstring="\n" + "(1) Look for the alphabet in the middle of the string." + "\n"\
                       + "(2) Choose the correct option using your keyboard. " + "\n"\
                       + "(3) Press A or left arrow to select alphabet on the left side of the screen." + "\n"\
                       + "(4) Press W or right arrow to select alphabet on the left side of the screen." + "\n\n"

left = Label(_instructionlabel_, text=instructionstring,font="none 10", padx=5, pady=5)
left.grid()



_startgamebutton_ = Button(_instructionlabel_, text ="Start Game",font="none 14",command=lambda:_gamingconsoleframe_())
_startgamebutton_.grid()


_startgamebutton_.config(text='Start Game', command=lambda:_gamingconsoleframe_())
root.bind('<Return>', lambda event=None: _startgamebutton_.invoke())


_newline_=Label(_gamingconsole_, text="\n\n\n\n")
_newline_.grid()
_geninputseq()

_newline_.grid()
_GameOverLabel_=Label(_resultscreen_, text="\n\n" + "Game Over" +"\n",font="none 52 bold")
_GameOverLabel_.grid(row=5, column=1)

_TryAgainBut=Button(_resultscreen_, text ="Try Again")
_TryAgainBut.grid(row=6, column=1)



root.columnconfigure(0, weight=1)

# raise_frame(_landingscreen_)
root.mainloop()


# from tkinter import *
#
#
# def raise_frame(frame):
#     frame.tkraise()
#
# root = Tk()
#
# f1 = Frame(root)
# f2 = Frame(root)
# f3 = Frame(root)
# f4 = Frame(root)
#
# for frame in (f1, f2, f3, f4):
#     frame.grid(row=0, column=0, sticky='news')
#
# Button(f1, text='Go to frame 2', command=lambda:raise_frame(f2)).pack()
# Label(f1, text='FRAME 1').pack()
#
# Label(f2, text='FRAME 2').pack()
# Button(f2, text='Go to frame 3', command=lambda:raise_frame(f3)).pack()
#
# Label(f3, text='FRAME 3').pack(side='left')
# Button(f3, text='Go to frame 4', command=lambda:raise_frame(f4)).pack(side='left')
#
# Label(f4, text='FRAME 4').pack()
# Button(f4, text='Goto to frame 1', command=lambda:raise_frame(f1)).pack()
#
# raise_frame(f1)
# root.mainloop()