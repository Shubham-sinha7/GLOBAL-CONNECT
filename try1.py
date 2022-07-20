import pyttsx3
import speech_recognition as sr  
import datetime
import wikipedia
import random 
import webbrowser
import sys
import time
import os
import os.path
import requests
import cv2      
from requests import get
import smtplib      
import pyjokes         
import pyautogui        
import PyPDF2
import pywhatkit as kit
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import instaloader #pip install instaloader
import operator #for calculation using voice
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#from PyQt5.uic import loadUiType
from zizzyUi import Ui_zizzyUi

from tkinter import*  
from tkinter import messagebox
from PIL import Image,ImageTk 
import pymysql  

# !
# *
# ?
# TODO
# &
# ^
# ~
# //

                                         #*  (1) VOICE and ITS CONVERSIONS

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices');
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# * WISHING WELCOME
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    speak("Welcome back") #
    if hour >= 0 and hour < 12:
        speak(f"Good Morning, its {tt} and i am here to assist you!")
    elif hour >= 12 and hour < 18:
        speak(f"Glad to see you! Good Afternoon, its {tt} ,I hope you are doing alright.")
    else:
        speak(f"How was your day today? Good Evening, its {tt}")
    speak("So tell me how could i be serving you Dear?")





#! to send email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sinhashubham318@gmail.com', 'Mahi@007')
    server.sendmail('sinhashubham318@gmail.com', to, content)
    server.close()






# ^ For news updates :
def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=83263a48521a48a797182dbc3926e513'

    main_page = requests.get(main_url).json()
    # print(main_page)
    articles = main_page["articles"]
    # print(articles)
    head = []
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        # print(f"today's {day[i]} news is: ", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")

# def Sweather():
#     ipAdd = requests.get('https://api.ipify.org').text
#     print(ipAdd)
#     url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
#     geo_requests = requests.get(url)
#     geo_data = geo_requests.json()
#     # print(geo_data)
#     city = geo_data['city']
#     api_key = "30b2e680ad9c7790ec02fdb4f97f4573" #generate your own api key from open weather
#     base_url = "http://api.openweathermap.org/data/2.5/weather?"
#     city_name = (f'{city}')
#     complete_url = base_url + "appid=" + api_key + "&q=" + city_name
#     response = requests.get(complete_url)
#     x = response.json()
#     if x["cod"] != "404":
#         y = x["main"]
#         current_temperature = y["temp"]
#         # current_pressure = y["pressure"]
#         # current_humidiy = y["humidity"]
#         z = x["weather"]
#         weather_description = z[0]["description"]
#         r = ("outside " + " the Temperature is " +
#              str(int(current_temperature - 273.15)) + " degree celsius " +
#              ", atmospheric pressure " + str(current_pressure) + " hpa unit" +
#              ", humidity is " + str(current_humidiy) + " percent"
#              " and " + str(weather_description))
#         speak(r)
#     else:
#         speak(" City Not Found ")


# ^ To read PDF
def pdf_reader():
    book = open('py3.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(book) #pip install PyPDF2
    pages = pdfReader.numPages
    speak(f"Total numbers of pages in this book {pages} ")
    speak("sir please enter the page number i have to read")
    pg = int(input("Please enter the page number: "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)
    
                             #*  (2)  GUI AND DATABASE
# & interface GUI work done here :

class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Window")
        self.root.geometry("1350x700+0+0")

        
        self.bg=ImageTk.PhotoImage(file="images/a2.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

      
        self.left=ImageTk.PhotoImage(file="images/a1.png")
        left=Label(self.root,image=self.left).place(x=330,y=20,width=613,height=173)
        
        Frame1=Frame(self.root,bg="dodgerblue2")
        Frame1.place(x=450,y=370,width=400,height=300)

        title=Label(Frame1,text="LOGIN FORM",font=("showcard gothic",20,"bold"),bg="hot pink",fg="black").place(x=100,y=30)
        
        username=Label(Frame1,text="Username",font=("kristen itc",15,"bold",),bg="orange",fg="black").place(x=50,y=100)
        self.txt_username=Entry(Frame1,font=("times new roman",15),bg="lightgray")
        self.txt_username.place(x=50,y=130,width=300)

        password=Label(Frame1,text="Password",font=("kristen itc",15,"bold"),bg="deep sky blue",fg="black").place(x=50,y=170)
        self.txt_password=Entry(Frame1,font=("times new roman",15),show="*",bg="lightgray")
        self.txt_password.place(x=50,y=200,width=300)

        btn=Button(Frame1,text="Please Login Here",command=self.login,font=("showcard gothic",15,"bold"),bg="gold",bd=0,cursor="hand2").place(x=100,y=250,width="250")
        left_btn=Button(self.root,text="Sign Up Here !",command=self.signup_window, font=("jokerman",18,"bold"),bg="gold",bd=0,cursor="hand2").place(x=200,y=300,width="250")




    # & Database work here
    
    def signup_window(self):
        self.root.destroy()
        import signup


    def login(self):
        if self.txt_username.get()=="" or self.txt_password.get()=="": 
            messagebox.showerror("Error","Dont Hurry. All Fields Are Required to enter :/",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="signupp")
                cur=con.cursor()
                cur.execute("select * from admin where username=%s and password=%s",(self.txt_username.get(),self.txt_password.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","OOPS Watch it, Invalid Username or password detected!!",parent=self.root)    
                else:
                    messagebox.showinfo("Success","LOGGED IN SUCCESSFULLY, Welcome Back to your Voice Robot!! :) ",parent=self.root)
                    self.root.destroy()
            except Exception as es: 
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)



root=Tk()
obj=login_window(root)
root.mainloop()

# ! GUI WORK DONE 


                                  #*  (3)   RUNNING MAIN GUI


class MainThread(QThread):                                ## ! main func for gui work
    def __init__(self):
        super(MainThread,self).__init__()

    def  takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening...")
            r.pause_threshold = 1
            # r.adjust_for_ambient_noise(source)
            # audio = r.listen(source)
            audio = r.listen(source,timeout=4,phrase_time_limit=7)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}")

        except Exception as e:
            # speak("Say that again please...")
            return "none"
        query = query.lower()
        return query


    def run(self):
        self.TaskExecution()
        # print("searching...")
        # Sweather()
        # while True:
        #     self.query = self.takecommand()
        #     if "wake up" in self.query or "are you there" in self.query or "hello" in self.query:
        #         wish()
        #         self.TaskExecution()
        #     elif "goodbye" in self.query:
        #         speak("thanks for using me sir, have a good day")
        #         sys.exit()
                

    def TaskExecution(self):             ############### ! MAIN RUNNING   ##############3
        wish()
        while True:
            self.query = self.takecommand()
            
            

                                 #*  (4) ALL FUNCTIONS
                                 
            # TODO # THE ACTIONS OR FUNCTIONALITIES DONE HERE :

            if "launch notepad" in self.query:
                npath = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(npath)

            elif "launch adobe reader" in self.query:
                apath = "C:\\Program Files (x86)\\Adobe\\Reader 11.0\\Reader\\AcroRd32.exe"
                os.startfile(apath)

            elif "launch command prompt" in self.query:
                os.system("start cmd")

                                     #^ ADVANCE FEATURES

    # ^ # 1st OPEN CAMERA

            elif "open camera" in self.query:
                speak("wait sir opening camera")
                cap = cv2.VideoCapture(0)
                while True:

                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k==27:

                        break;
                speak("Closing Camera")
                cap.release()
                cv2.destroyAllWindows()
                speak("i am done sir, Is there any other command?")
                
        #^ #2 to find a joke
        
        
            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)
                
            elif "tell me another joke" in self.query:
                joke = pyjokes.get_joke(language='en', category= 'all')
                speak(joke)
                
                
        #^ #3    WHATSAPP MSG

            elif "send whatsapp message" in self.query:
                kit.sendwhatmsg("+91 8057294017", "Whats up, this is just a Test message",12,26)
                #time.sleep(120)
                speak("message has been sent")
        
        
        #^ #4    #   News
            elif "tell me news" in self.query or "what are the headlines of today" in self.query :
                speak("please wait sir, fetching the latest news")
                news()
        
        #^ #5 # YOUTUBE MOOD SONG PLAY
        #todo youtube mood songs
            elif "play happy song on youtube" in self.query:
                kit.playonyt("sunflower by post malone")
                speak("i am done sir, the song is gonna play soon. Is there any other command?")
            elif "play song on youtube" in self.query:
                kit.playonyt("incomplete jay sean")
                speak("i am done sir, the song is gonna play soon. Is there any other command?")
            elif "play hindi song on youtube" in self.query:
                kit.playonyt("Pehla Nasha")
                speak("i am done sir, the song is gonna play soon. Is there any other command?")
            elif "play sad song on youtube" in self.query:
                kit.playonyt("heavy linkin park")
                speak("i am done sir, the song is gonna play soon. Is there any other command?")
        

        #^ #7. Gmail with msg and with attachment
################################# !  EMAIL #######################
############################################ TODO ####################################################################
###### ???????????????????????????????????????????????????????????????????????????/##################


            elif "email to shubham" in self.query:
                
                speak("sir what should i say to shubham")
                self.query = self.takecommand()
                if "send a file" in self.query:
                    email = 'sinhashubham318@gmail.com' # Your email
                    password = 'Mahi@007' # Your email account password
                    send_to_email = 'Shubhamsinha737@gmail.com' # Whom you are sending the message to
                    speak("okay sir, what is the subject for this email")
                    self.query = self.takecommand()
                    subject = self.query   # The Subject in the email
                    speak("and sir, what is the message for this email")
                    self.query2 = self.takecommand()
                    message = self.query2  # The message in the email
                    speak("sir please enter the correct path of the file into the shell")
                    file_location = input("please enter the path here")    # The File attachment in the email

                    speak("please wait,i am sending email now")

                    msg = MIMEMultipart()
                    msg['From'] = email
                    msg['To'] = send_to_email
                    msg['Subject'] = subject

                    msg.attach(MIMEText(message, 'plain'))

                    #* Setup the attachment
                    filename = os.path.basename(file_location)
                    attachment = open(file_location, "rb")
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

                    #* Attach the attachment to the MIMEMultipart object
                    msg.attach(part)

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(email, password)
                    text = msg.as_string()
                    server.sendmail(email, send_to_email, text)
                    server.quit()
                    speak("email has been sent to shubhi")

                else:                
                    email = 'sinhashubham318@gmail.com' # Your email
                    password = 'Mahi@007' # Your email account password
                    send_to_email = 'shubhamsinha737@gmail.com' # Whom you are sending the message to
                    message = query # The message in the email

                    server = smtplib.SMTP('smtp.gmail.com', 587) # Connect to the server
                    server.starttls() # Use TLS
                    server.login(email, password) # Login to the email server
                    server.sendmail(email, send_to_email , message) # Send the email
                    server.quit() # Logout of the email server
                    speak("email has been sent to shubham sinha")
        
        
        #^ 2ND PART
        
            elif "email to suraj" in self.query:
                    
                try:
                        speak("Dear, what should I say to suraj?")
                        content = self.takecommand().lower()
                        to = "Shubhamsinha737@gmail.com"
                        sendEmail(to, content)
                        speak("email has been sent to suraj")

                except Exception as e:
                        print(e)



                
                        speak("i am sorry sir, there was some error sending the mail")
        
        
        # #& TEMPERATURE #todo
        #     elif "what is the temperature here?" in self.query or "tell me the temperature" in self.query:
        #         # speak("sir, which city temperature you want to know ?")
        #         temperature = "temperature in Dehradun"
        #         url = f"https://www.google.com/search?q={temperature}"
        #         r = requests.get(url)
        #         data = BeautifulSoup(r.text, "html.parser")
        #         temp = data.find("div", class_="BNeawe").text
        #         speak(f"Current {temperature} is {temp}")
        
        # todo &To find my   #! location using IP Address

            elif "where i am" in self.query or "where we are" in self.query or "what is our location" in self.query:
                speak("wait sir, let me check our location")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    # print(geo_data)
                    city = geo_data['city']
                    # state = geo_data['state']
                    country = geo_data['country']
                    speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
                except Exception as e:
                    speak("sorry sir, Due to network issue i am not able to find where we are.")
                    pass


# & MUSIC PLAYING
            elif "play music" in self.query:
                music_dir = "D:\\music"
                songs = os.listdir(music_dir)
                # rd = random.choice(songs)
                for song in songs:
                    if song.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir, song))


# & IP ADDRESS
            elif "tell my ip address" in self.query or "ip address" in self.query :
                ip = get('https://api.ipify.org').text
                speak(f"your IP address is {ip}")

# ? WIKIPEDIA 
            elif "wikipedia" in self.query:
                speak("searching wikipedia....")
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query, sentences=2)
                speak("according to wikipedia")
                speak(results)
                # print(results)
            

# & ###########         OPENING WEBSITES


            elif "open youtube" in self.query:
                webbrowser.open("www.youtube.com")

            elif "open facebook" in self.query:
                webbrowser.open("www.facebook.com")

            elif "open stackoverflow" in self.query or "open stack overflow" in self.query :
                webbrowser.open("www.stackoverflow.com")

            elif "open google" in self.query:
                speak("sir, what should i search on google")
                cm = self.takecommand()
                webbrowser.open(f"{cm}")


# ! #############          EXITING COMMANDS

            elif "goodbye" in self.query or "go offline" in self.query:
                speak("okay sir, i am going to sleep you can call me anytime.")
                sys.exit()
                gifThread.exit()
                # break
                

#! TO CLOSE APPS
            
            elif "close notepad" in self.query:
                speak("okay sir, closing notepad")
                os.system("taskkill /f /im notepad.exe")

# & to set an alarm
            elif "set alarm" in self.query:
                nn = int(datetime.datetime.now().hour)
                if nn==22: 
                    music_dir = 'E:\\music'
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, songs[0]))


            # TODO ###########       SYSTEM STATUS ###

            # elif "system status" in self.query:
            #     sys_info = obj.system_info()
            #     print(sys_info)
            #     speak(sys_info)

            ################### TODO doneee
        
            # elif "tell me another joke" in query:
            #     joke = pyjokes.get_joke(language='en', category= 'all')
            #     speak(joke)


            # elif "shut down the system" in self.query:
            #     os.system("shutdown /s /t 5")

            # elif "restart the system" in self.query:
            #     os.system("shutdown /r /t 5")

            # elif "sleep the system" in self.query:
            #     os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

#! ###############################        MORE INTRO CONVO COMMANDS

            elif "hello" in self.query or "hey" in self.query:
                speak("hello sir, may i help you with something.")
            
            elif "how are you" in self.query:
                speak("i am fine sir, what about you.")

            elif "wake up" in self.query:
                speak("sir, let me sleep ten minutes more, i will be there.")

            elif "thank you" in self.query or "thanks" in self.query:
                speak("it's my pleasure sir.")



            ###################################################################################################################################
            ###########################################################################################################################################



            elif 'switch the window' in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")
                    
            #if "make a note" in command or "write this down" in command or "remember this" in command:
             #   speak("What would you like me to write down?")
              #  note_text = obj.mic_input()
                #obj.take_note(note_text)
                #speak("I've made a note of that")


############&          CALCULATIONS 

            elif "do some calculations" in self.query or "can you calculate" in self.query:            
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak("Say what you want to calculate, example: 7 plus 25")
                    print("listening.....")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                my_string=r.recognize_google(audio)
                print(my_string)
                def get_operator_fn(op):
                    return {
                        '+' : operator.add,
                        '-' : operator.sub,
                        'x' : operator.mul,
                        'divided' :operator.__truediv__,
                        'Mod' : operator.mod,
                        'mod' : operator.mod,
                        '^' : operator.xor,
                        }[op]
                def eval_binary_expr(op1, oper, op2):
                    op1,op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)
                print(eval_binary_expr(*(my_string.split())))


            

            

            #------------------- #& To check a instagram profile----
            elif "instagram profile" in  self.query or "profile on instagram" in self.query:
                speak("sir please enter the user name correctly.")
                name = input("Enter username here:")
                webbrowser.open(f"www.instagram.com/{name}")
                speak(f"Sir here is the profile of the user {name}")
                time.sleep(5)
                speak("sir would you like to download profile picture of this account.")
                condition = self.takecommand()
                if "yes" in condition:
                    mod = instaloader.Instaloader() #pip install instadownloader
                    mod.download_profile(name, profile_pic_only=True)
                    speak("i am done sir, profile picture is saved in our main folder. now i am ready for next command")
                else:
                    pass

            #-------------------  #& To take screenshot -------------
            elif "take screenshot" in self.query or "take a screenshot" in self.query:
                speak("sir, please tell me the name for this screenshot file")
                name = self.takecommand()
                speak("please sir hold the screen for few seconds, i am taking sreenshot")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("i am done sir, the screenshot is saved in our main folder. now i am ready for next command")

            # elif "show me the screenshot" in self.query:
            #     try:
            #         img = Image.open('C://USERS//DEEPANSHI KALRA//ONEDRIVE//DESKTOP//ZIZZYGUI//' + name)
            #         img.show(img)
            #         speak("Here it is sir")
            #         time.sleep(2)

                # except IOError:
                #     speak("Sorry sir, I am unable to display the screenshot")



            #speak("sir, do you have any other work")

            #-------------------#*  To Read PDF file -------------
            elif "read pdf" in self.query:
                pdf_reader()

            #& --------------------- To Hide files and folder ---------------
            elif "hide all files" in self.query or "hide this folder" in self.query or "visible for everyone" in self.query:
                speak("sir please tell me you want to hide this folder or make it visible for everyone")
                condition = self.takecommand()
                if "hide" in condition:
                    os.system("attrib +h /s /d") #os module
                    speak("sir, all the files in this folder are now hidden.")                

                elif "visible" in condition:
                    os.system("attrib -h /s /d")
                    speak("sir, all the files in this folder are now visible to everyone. i wish you are taking this decision in your own peace.")
                    
                elif "leave it" in condition or "leave for now" in condition:
                    speak("Ok sir")

                speak("Its done as u asked, any other work you want me to perform?")


startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_zizzyUi()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("../gifs/gif3.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../gifs/GIF4.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../gifs/GIF5.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("../more gifs/GIF12.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../more gifs/GIF10.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../more gifs/GIF11.gif")
        self.ui.label_6.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../load.gif")
        self.ui.label_7.setMovie(self.ui.movie)
        self.ui.movie.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

#speak("Its done as u asked, any other work you want me to perform?")
app = QApplication(sys.argv)
zizzy = Main()
zizzy.show()
exit(app.exec_())


