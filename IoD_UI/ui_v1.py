import tkinter as tk


root = tk.Tk()
root.title("Control Panel")
root.geometry('1000x600')

top_frame = tk.Frame(root)
uav_control_frame = tk.Frame(top_frame, pady=10, padx=10, bg='#f90')
iot_control_frame = tk.Frame(top_frame, pady=10, padx=10, bg='#09c')
gcs_control_frame = tk.Frame(root, pady=10, padx=10, bg='#fc0')

top_frame.pack(fill='both',side='top',expand=1)
uav_control_frame.pack(fill='both',side='left',expand=1)
iot_control_frame.pack(fill='both',side='right', expand=1)
gcs_control_frame.pack(fill='x',side='bottom')

#gcs
gcsip_label = tk.Label(gcs_control_frame,text='GCS IP:')
gcsip_label.grid(column=0, row=0)

gcsip_entry = tk.Entry(gcs_control_frame)
gcsip_entry.grid(column=1, row=0)

gcsip_button = tk.Button(gcs_control_frame)
gcsip_button["text"] = "save"
gcsip_button.grid(column=2, row=0)

tk.LabelFrame


root.mainloop()