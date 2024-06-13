from tkinter import *
from random import *
from tkinter import messagebox
import time

ALL_WORD = ['HEDA', 'IHAR', 'EYE', 'SEAR', 'SEON', 'UHMTO', 'NICH', 'OEEAFHDR', 'AJW', 'EKEHC', 'BOEWEYR',
            'DHRSULOE', 'RSAM', 'ANDH', 'OBWEL', 'NGEIFR', 'GLE', 'FOTO', 'IHGTH', 'NEKE', 'DRBI', 'DGO', 'OENDYK',
            'GFRIEFA', 'GLOILARTA', 'TAC', 'EHSOR', 'OLIN', 'MYOEKN', 'EEB', 'KDUC',
            'RGFO', 'TPNLEHEA', 'ORCDCIELO', 'POLNIHD', 'LARLIGO', 'EMSUO', 'EGTRI', 'ABRITB', 'ATR', 'DRE', 'OELLYW',
            'LBEU', 'ERGNE', 'OREAGN', 'RPEULP', 'EMIL', 'ORWBN', 'NYAV', 'PNIK', 'LDGO', 'VRLSEI',
            'BLKAC', 'HTWIE', 'EALPP', 'VAAGU', 'PEHCA', 'PRAE', 'NGMAO', 'PAAPYA', 'EGNRAO', 'AGESPR', 'WIKI',
            'RRYCHE', 'LRTOANWEME',
            'PEELIPNPA', 'BELUEBRRY', 'NABAAN', 'NTUOCCO', 'SCURATD EALPP', 'MONLE', 'EREYBMUL', 'MARTAIND', 'CCLIER',
            'IDANDOM', 'RHATE', 'AOTNOCG', 'USQRAE', 'TARS', 'RITLANEG', 'OTCRRA', 'OIRCCOBL', 'ROUFCWIALEL', 'RNOC',
            'UCMUECRB', 'GGNALETP', 'EEGRN EREPPP', 'ECETTUL',
            'OSMROSMUH', 'INNOO', 'OATPTO', 'UNPMIPK', 'RED EPEPPR', 'MOTTOA', 'ETEBTROO', 'EPAS', 'HIRSAD',
            'CEBABAG', 'CLIHI', 'ICRGAL', 'WETSE OTPAOT', 'RERAOCDIN', 'RIHLPOEETC', 'NELAARIP', 'CKTREO', 'LITSAOBA',
            'UIECRS PIHS', 'ROAGC SPHI', 'TJE SKI', 'PIREAT IHSP',
            'TBOA', 'SHIP', 'RUISAEMNB', 'IYLCECB', 'CAR', 'BUS', 'TIANR', 'UTKCR', 'NVA', 'LRTOMCCYEO','ACT', 'HTEA', 'GADENR', 'OODR', 'MICEHAT', 'HATR',
            'ODNSE', 'LECOS', 'CUSOIN', 'TABLCE', 'IRBHTDA', 'ECAD', 'SUEP', 'KSWI', 'PULM', 'GIRDEN', 'TOUHT', 'VNEE', 'DLUEC', 'LUBGE', 'PLOPEE', 'ADTLO', 'SOTP', 'MLOB', 'RATS', 'OHTRS', 'MIA',
            'DPOC', 'YTE', 'CUNRCHO', 'LIK', 'TIT', 'THEC', 'SAEL', 'PAT', 'BOO', 'FOO', 'BAU', 'JU', 'YHO', 'ALL', 'AGR', 'RAM', 'MRA', 'MTA', 'UBT', 'BID', 'CAP', 'ARK', 'BAG' ]

ALL_WORD_ANSWER = ['HEAD', 'HAIR', 'EYE', 'EARS', 'NOSE', 'MOUTH', 'CHIN', 'FOREHEAD', 'JAW', 'CHEEK', 'EYEBROW',
                   'SHOULDER', 'ARMS', 'HAND', 'ELBOW', 'FINGER', 'LEG', 'FOOT', 'THIGH', 'KNEE', 'BIRD', 'DOG',
                   'DONKEY', 'GIRAFFE', 'ALLIGATOR', 'CAT', 'HORSE', 'LION', 'MONKEY', 'BEE', 'DUCK', 'FROG',
                   'ELEPHANT', 'CROCODILE', 'DOLPHIN', 'GORILLA', 'MOUSE', 'TIGER', 'RABBIT', 'RAT', 'RED', 'YELLOW',
                   'BLUE', 'GREEN', 'ORANGE', 'PURPLE', 'LIME', 'BROWN', 'NAVY', 'PINK', 'GOLD', 'SILVER', 'BLACK',
                   'WHITE', 'APPLE', 'GUAVA', 'PEACH', 'PEAR', 'MANGO', 'PAPAYA', 'ORANGE', 'GRAPES', 'KIWI', 'CHERRY',
                   'WATERMELON', 'PINEAPPLE', 'BLUEBERRY', 'BANANA', 'COCONUT', 'CUSTARD APPLE', 'LEMON', 'MULBERRY',
                   'TAMARIND', 'CIRCLE', 'DIAMOND', 'HEART', 'OCTAGON', 'SQUARE', 'STAR', 'TRIANGLE', 'CARROT',
                   'BROCCOLI ', 'CAULIFLOWER ', 'CORN ', 'CUCUMBER ', 'EGGPLANT', 'GREEN PEPPER ',
                   'LETTUCE ', 'MUSHROOMS', 'ONION', 'POTATO', 'PUMPKIN ', 'RED PEPPER', 'TOMATO ', 'BEETROOT', 'PEAS',
                   'RADISH', 'CABBAGE', 'CHILI', 'GARLIC', 'SWEET POTATO', 'CORIANDER', 'HELICOPTER', 'AIRPLANE',
                   'ROCKET', 'SAILBOAT', 'CRUISE SHIP', 'CARGO SHIP', 'JET SKI',
                   'PIRATE SHIP', 'BOAT', 'SHIP', 'SUBMARINE', 'BICYCLE', 'CAR', 'BUS', 'TRAIN', 'TRUCK', 'VAN',
                   'MOTORCYCLE','CAT', 'HEAT', 'GARDEN', 'DOOR', 'MATCH', 'HART', 'NODES', 'CLOSE', 'COUSIN', 'CABLE',
                   'BIRTHDAY', 'CADE', 'SPUE', 'WISK', 'LUMP', 'REIGN', 'THOU', 'EVEN', 'CLUE', 'BUGLE', 'PEEPOL', 'DOTAL',
                   'POST', 'BLOM', 'STAR', 'SHORT', 'AIM', 'COD', 'EYT', 'CONCUR', 'ILK', 'TIT', 'TECH', 'SALE', 'TAP', 'BOO',
                   'FOO', 'UBA', 'JU', 'HOY', 'ALL', 'RAG', 'ARM', 'RAM', 'MAT', 'TUB', 'DIB', 'PAC', 'KAR', 'GAB']

ran_num = randrange(0, (len(ALL_WORD)))
jumbled_rand_word = ALL_WORD[ran_num]

points = 0


def main():
    def back():
        my_window.destroy()
        import main_start
        main_start.start_main_page()

    def change():
        global ran_num
        ran_num = randrange(0, (len(ALL_WORD)))
        word.configure(text=ALL_WORD[ran_num])
        get_input.delete(0, END)
        ans_lab.configure(text="")

    def cheak():
        global points, ran_num
        user_word = get_input.get().upper()
        if user_word == ALL_WORD_ANSWER[ran_num]:
            points += 5
            score.configure(text="Score: " + str(points))
            messagebox.showinfo('correct', "Correct Answer.. Keep it Up!")
            ran_num = randrange(0, (len(ALL_WORD)))
            word.configure(text=ALL_WORD[ran_num])
            get_input.delete(0, END)
            ans_lab.configure(text="")
        else:
            messagebox.showerror("Error", "Inorrect Answer..Try your best!")
            get_input.delete(0, END)

    def show_answer():
        global points
        if points > 4:
            points -= 5
            score.configure(text="Score: " + str(points))
            time.sleep(0.3)
            ans_lab.configure(text=ALL_WORD_ANSWER[ran_num])
        else:
            ans_lab.configure(text='Not enough points')

    my_window = Tk()
    my_window.geometry("500x500+500+150")
    my_window.resizable(0, 0)
    my_window.title("Quizee jumbled_words ")
    my_window.configure(background="#e6fff5")
    my_window.iconbitmap(r'quizee_logo_.ico')
    img1 = PhotoImage(file="back.png")

    lab_img1 = Button(
        my_window,
        image=img1,
        bg='#e6fff5',
        border=0,
        justify='center',
        command=back,
    )
    lab_img1.pack(anchor='nw', pady=10, padx=10)

    score = Label(
        text="Score: 0",
        pady=10,
        bg="#e6fff5",
        fg="#000000",
        font="Titillium  14 bold"
    )
    score.pack(anchor="n")

    word = Label(
        text=jumbled_rand_word,
        pady=10,
        bg="#e6fff5",
        fg="#000000",
        font="Titillium  50 bold"
    )
    word.pack()

    get_input = Entry(
        font="none 26 bold",
        borderwidth=10,
        justify='center',
    )
    get_input.pack()

    submit = Button(
        text="Submit",
        width=18,
        borderwidth=8,
        font=("", 13),
        fg="#000000",
        bg="#99ffd6",
        command=cheak,
    )
    submit.pack(pady=(10, 20))

    change = Button(
        text="Change Word",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#99ffd6",
        font=("", 13),
        command=change,
    )
    change.pack()

    ans = Button(
        text="Answer",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#99ffd6",
        font=("", 13),
        command=show_answer,
    )
    ans.pack(pady=(20, 10))

    ans_lab = Label(
        text="",
        bg="#e6fff5",
        fg="#000000",
        font="Courier 15 bold",
    )
    ans_lab.pack()

    my_window.mainloop()
