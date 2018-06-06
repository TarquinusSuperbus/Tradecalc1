#TradeCalc©, a trade route calculator for Archeage by Kenneth Kawachi, 2014

from tkinter import *
from tkinter import ttk

def get_routes(filename):
    d = {}
    with open(filename) as f:
        for line in f:
           (key, val) = line.split()
           d[key] = val
    return d

routes_dict = get_routes('regiondict.txt')  #dictionary of traderoutes

def calculate(*args):
    try:
        interest = 0.05
        value = str(routestart.get())
        value2 = str(routeend.get())
        route = (value + "-" + value2)     #format "Arcum-Falcorth" etc.
        base = int(routes_dict[route]) / 1.3        #Base value per route
        packs = int(numberofpacks.get())               #Number of packs
        tax = (taxrate.get())
        tax = int(tax) / 100                       #Interest Rate
        interest = 0.05
        final = (base * tax * packs)
        profit = (final + (interest * final))
        gold = profit // 10000
        silver = (profit % 10000) / 100
        copper = round(profit % 100, 0)
        gold = '%.0f' % gold                        #convert to string
        silver = '%.0f' % silver
        copper = '%.0f' % copper
        final_str = (gold + 'g', silver + 's', copper + 'c')
        price.set(final_str)
    except ValueError:
        tkMessageBox.showinfo("Error", "Invalid Route") 

root = Tk()
root.title("TradeCalc©")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

routestart = StringVar()
routeend = StringVar()
numberofpacks = StringVar()
taxrate = StringVar()
price = StringVar()

start_entry = ttk.Entry(mainframe, width=21, textvariable=routestart)
start_entry.grid(column=2, row=1, sticky=(W, E))

end_entry = ttk.Entry(mainframe, width=21, textvariable=routeend)
end_entry.grid(column=2, row=2, sticky=(W, E))

tax_entry = ttk.Entry(mainframe, width=21, textvariable=taxrate)
tax_entry.grid(column=2, row=3, sticky=(W, E))

packs_entry = ttk.Entry(mainframe, width=7, textvariable=numberofpacks)
packs_entry.grid(column=2, row=4, sticky=(W, E))

ttk.Label(mainframe, textvariable=price).grid(column=2, row=6, sticky=(W, E))
ttk.Button(mainframe, text="Run the Route", command=calculate).grid(column=3, row=6, sticky=W)
ttk.Label(mainframe, text="Start of Route (first word only)").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="End of Route (first word only)").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="Interest Rate %").grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, text="You will gain").grid(column=1, row=6, sticky=E)
ttk.Label(mainframe, text="Number of Packs").grid(column=3, row=4, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

start_entry.focus()
root.bind('<Return>', calculate)

root.iconbitmap('TradeCalc.ico')
root.mainloop()

