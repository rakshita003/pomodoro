import tkinter as tk
from tkinter import ttk
import time

class FlipClock(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.hours_var = tk.StringVar()
        self.minutes_var = tk.StringVar()
        self.seconds_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure('TLabel', font=('Helvetica', 36))

        self.hours_label = ttk.Label(self, textvariable=self.hours_var, style='TLabel')
        self.minutes_label = ttk.Label(self, textvariable=self.minutes_var, style='TLabel')
        self.seconds_label = ttk.Label(self, textvariable=self.seconds_var, style='TLabel')

        self.hours_label.grid(row=0, column=0)
        self.minutes_label.grid(row=0, column=1)
        self.seconds_label.grid(row=0, column=2)

        self.update_time()

    def update_time(self):
        current_time = time.strftime('%H: %M: %S').split()
        self.hours_var.set(current_time[0])
        self.minutes_var.set(current_time[1])
        self.seconds_var.set(current_time[2])
        self.after(1000, self.update_time)

class PomodoroTimer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pomodoro Timer")
        self.geometry("400x200")
        
        self.pomodoro_time = 25 * 60  # 25 minutes
        self.break_time = 5 * 60  # 5 minutes
        self.is_running = False
        
        self.flip_clock = FlipClock(self)
        self.flip_clock.pack()

        self.time_var = tk.StringVar()
        self.time_var.set("25:00")
        
        self.timer_label = ttk.Label(self, textvariable=self.time_var, font=('Helvetica', 36))
        self.timer_label.pack()

        self.start_button = ttk.Button(self, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=5, pady=20)

        self.reset_button = ttk.Button(self, text="Reset", command=self.reset_timer)
        self.reset_button.pack(side=tk.RIGHT, padx=5, pady=20)

        self.update_timer_display()

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.count_down(self.pomodoro_time)
    
    def reset_timer(self):
        self.is_running = False
        self.time_var.set("25:00")
    
    def count_down(self, remaining_time):
        if self.is_running:
            minutes, seconds = divmod(remaining_time, 60)
            self.time_var.set(f"{minutes:02}:{seconds:02}")
            if remaining_time > 0:
                self.after(1000, self.count_down, remaining_time - 1)
            else:
                self.is_running = False
                self.break_time_alert()

    def break_time_alert(self):
        self.time_var.set("Break Time!")
        self.after(1000 * self.break_time, self.reset_timer)
    
    def update_timer_display(self):
        self.flip_clock.update_time()
        self.after(1000, self.update_timer_display)

if __name__ == "__main__":
    app = PomodoroTimer()
    app.mainloop()
