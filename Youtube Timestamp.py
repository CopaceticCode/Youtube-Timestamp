import tkinter as tk
import pyperclip
# import webbrowser
window = tk.Tk()
fontface = 'Calibri'

window.geometry('500x220')
window.configure(bg='#383838')
window.title('Youtube Timestamp URL')

def getLink():

    time = str(int(minutes.get()) * 60 + int(seconds.get()))
    if 'youtu' in url.get():
        result = str('https://youtu.be/' + url.get()[url.get().find('.com')+5:])
        result = result.replace('watch?v=','') + '?t=' + time
        # link.delete('1.0',tk.END)
        # link.insert('1.0',result)
        link.config(text=result)
        link.pack()
        pyperclip.copy(result)
    else:
        result = url.get() + '&t=' + str(time) + 's'
        # link.delete('1.0',tk.END)
        # link.insert('1.0', result)
        link.config(text=result)
        link.pack()
        pyperclip.copy(result)

def callback(event):
    webbrowser.open_new(event.widget.cget(result))

frame1 = tk.Frame()
frame2 = tk.Frame()
frame3 = tk.Frame()
frame4 = tk.Frame()
frame5 = tk.Frame()
frame1.config(bg='#383838')
frame2.config(bg='#383838')
frame3.config(bg='#383838')
frame4.config(bg='#383838')
frame5.config(bg='#383838')

#-------------------------------------------------------------

label = tk.Label(master=frame1,text='Enter Youtube URL',fg='#F8F9F9',bg='#383838')
label.configure(font=(fontface,16))
label.pack()

url = tk.Entry(master=frame2,fg='#F8F9F9',bg='#7B7D7D',width=40,justify='center')
url.configure(font=(fontface,16))
url.pack()


minutes = tk.Entry(master=frame3,fg='#F8F9F9',bg='#7B7D7D',width=3,justify='center')
minutes.configure(font=(fontface,16))
minutes.pack(side=tk.LEFT,padx=10)

m = tk.Label(master=frame3,text='minutes',fg='#F8F9F9',bg='#383838')
m.pack(side=tk.LEFT)

seconds = tk.Entry(master=frame3,fg='#F8F9F9',bg='#7B7D7D',width=3,justify='center')
seconds.configure(font=(fontface,16))
seconds.pack(side=tk.LEFT,padx=10)

s = tk.Label(master=frame3,text='seconds',fg='#F8F9F9',bg='#383838')
s.pack(side=tk.LEFT)

button = tk.Button(master=frame4, text='Get link',width=25,height=1,bg='#7B7D7D',fg='#F8F9F9',command=getLink)
button.configure(font=(fontface,12))
button.pack()


# link = tk.Text(master=frame5)
# link.configure(font=(fontface,16),fg='#FFFFFF',bg='#383838',borderwidth=0,highlightthickness=0,width=10)
# link.pack(side=tk.LEFT,padx=10,pady=10)

link = tk.Label(master=frame5,fg='#F8F9F9',bg='#383838')
link.configure(font=(fontface,16),fg='#FFFFFF',bg='#383838',borderwidth=0,highlightthickness=0)
link.pack()

#-------------------------------------------------------------

frame1.pack(pady=5)
frame2.pack(pady=5)
frame3.pack(pady=5)
frame4.pack(pady=5)
frame5.pack(pady=5)

window.mainloop()

# url = input("Enter Youtube URL: ")
# time = input('Enter timestamp in the format \'m:s: ')

# seconds = str(int(time.split(':')[0])*60 + int(time.split(':')[1]))

# result = 'https://youtu.be/' + url[str.find(url,'.com/')+5:]
# result = result.replace('watch?v=','')
# result += '?t=' + seconds

# if 'youtu' in url: 
#     print(result) 
#     pyperclip.copy(result)
# else: 
#     print(url + '&t=' + str(seconds) + 's')
#     pyperclip.copy(url + '&t=' + str(seconds) + 's')
