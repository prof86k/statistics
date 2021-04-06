import statistics_basics_methods as st

import tkinter as tk

root = tk.Tk()

root.geometry("450x520")


list_variable= tk.IntVar()
entry_list = tk.Entry(master=root,textvariable=list_variable,width=50)
entry_list.pack()

start_variable = tk.IntVar()
start_value = tk.Entry(master=root,textvariable=start_variable)
start_value.pack()

end_variable = tk.IntVar()
end_value = tk.Entry(master=root,textvariable=end_variable)
end_value.pack()


def print_name():
    statistics_list = entry_list.get().split(",")
    started_value = int(start_value.get())
    last_value = int(end_value.get())
    # 
    run(statistics_list,started_value,last_value)
    # 
    entry_list.delete(0,tk.END)
    start_value.delete(0,tk.END)
    end_value.delete(0,tk.END)

def run(lsv,sv,lv):
    tk.Label(master=root,text="====================================================").pack()
    tk.Label(master=root,text="\nRange\t Frequency").pack()
    while len(st.fin) != len(lsv):    
        gets = st.range_sort(lsv,sv,lv)
        for i ,k in gets.items():
            tk.Label(master=root,text=str(i)+'\t'+str(k[1])).pack() 
        sv += lv+1

btn = tk.Button(master=root,text="Print",command=print_name)
btn.pack()

if __name__ == "__main__":
    root.mainloop()