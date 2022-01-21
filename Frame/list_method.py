import tkinter as tk
import platform
from Frame import Register_Details
# ************************
# Scrollable Frame Class
# ************************
def trosa(window):
    class ScrollFrame(tk.Frame):
        def __init__(self, parent):
            super().__init__(parent) # create a frame (self)

            self.canvas = tk.Canvas(self, borderwidth=0, background="#ffffff")          #place canvas on self
            self.viewPort = tk.Frame(self.canvas, background="#ffffff")                    #place a frame on the canvas, this frame will hold the child widgets 
            self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview) #place a scrollbar on self 
            self.canvas.configure(yscrollcommand=self.vsb.set)                          #attach scrollbar action to scroll of canvas

            self.vsb.pack(side="right", fill="y")                                       #pack scrollbar to right of self
            self.canvas.pack(side="left", fill="both", expand=True)                     #pack canvas to left of self and expand to fil
            self.canvas_window = self.canvas.create_window((4,4), window=self.viewPort, anchor="nw",            #add view port frame to canvas
                                    tags="self.viewPort")

            self.viewPort.bind("<Configure>", self.onFrameConfigure)                       #bind an event whenever the size of the viewPort frame changes.
            self.canvas.bind("<Configure>", self.onCanvasConfigure)                       #bind an event whenever the size of the canvas frame changes.
                
            self.viewPort.bind('<Enter>', self.onEnter)                                 # bind wheel events when the cursor enters the control
            self.viewPort.bind('<Leave>', self.onLeave)                                 # unbind wheel events when the cursorl leaves the control

            self.onFrameConfigure(None)                                                 #perform an initial stretch on render, otherwise the scroll region has a tiny border until the first resize

        def onFrameConfigure(self, event):                                              
            '''Reset the scroll region to encompass the inner frame'''
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))                 #whenever the size of the frame changes, alter the scroll region respectively.

        def onCanvasConfigure(self, event):
            '''Reset the canvas window to encompass inner frame when required'''
            canvas_width = event.width
            self.canvas.itemconfig(self.canvas_window, width = canvas_width)            #whenever the size of the canvas changes alter the window region respectively.

        def onMouseWheel(self, event):                                                  # cross platform scroll wheel event
            if platform.system() == 'Windows':
                self.canvas.yview_scroll(int(-1* (event.delta/120)), "units")
            elif platform.system() == 'Darwin':
                self.canvas.yview_scroll(int(-1 * event.delta), "units")
            else:
                if event.num == 4:
                    self.canvas.yview_scroll( -1, "units" )
                elif event.num == 5:
                    self.canvas.yview_scroll( 1, "units" )
        
        def onEnter(self, event):                                                       # bind wheel events when the cursor enters the control
            if platform.system() == 'Linux':
                self.canvas.bind_all("<Button-4>", self.onMouseWheel)
                self.canvas.bind_all("<Button-5>", self.onMouseWheel)
            else:
                self.canvas.bind_all("<MouseWheel>", self.onMouseWheel)

        def onLeave(self, event):                                                       # unbind wheel events when the cursorl leaves the control
            if platform.system() == 'Linux':
                self.canvas.unbind_all("<Button-4>")
                self.canvas.unbind_all("<Button-5>")
            else:
                self.canvas.unbind_all("<MouseWheel>")



    # ********************************
    # Example usage of the above class
    # ********************************

    class Example(tk.Frame):
        def __init__(self, root):

            tk.Frame.__init__(self, root)
            self.scrollFrame = ScrollFrame(self) # add a new scrollable frame.
            
            # Now add some controls to the scrollframe. 
            # NOTE: the child controls are added to the view port (scrollFrame.viewPort, NOT scrollframe itself)
            list_states=['Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh',
                            'Goa','Gujarat','Haryana','Himachal Pradesh','Jammu & Kashmir','Jharkhand',
                            'Karnataka','Kerala','Madhya Pradesh','Maharashtra','Manipur','Meghalaya',
                            'Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu',
                            'Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal']
            
            for row in range(len(list_states)):
                a = row
                t=list_states[row]
                tk.Button(self.scrollFrame.viewPort, text=t,background="#D8E9FB",font=("Poppins",9),activebackground="#D8E9FB",width = 43,borderwidth=0, command=lambda selected_row=row: executeButton(list_states[selected_row])).grid(row=row, column=1)
            # when packing the scrollframe, we pack scrollFrame itself (NOT the viewPort)
            self.scrollFrame.pack(side="top", fill="both", expand=True)

    def executeButton(item):
        Register_Details.Reg_details.updateState(item)
        root.destroy()
    # if __name__ == "__main__":
    root=tk.Toplevel(window)
    def on_close(event):
        root.destroy()
    window.bind('<ButtonRelease-1>', on_close)
    Example(root).pack(side="top", fill="both", expand=True)
    root.geometry("326x180")
    root.configure(bg="#D8E9FB")
    root.geometry('%dx%d+%d+%d' % (326, 180, 849.5, 498.5))
    root.resizable(False,False)
    root.overrideredirect(True)
    root.mainloop()