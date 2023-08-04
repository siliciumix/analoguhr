import tkinter as tk
import time
import math


class AnalogClock(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Analoguhr mit Sekundenzeiger")
        self.geometry("300x350")
        self.canvas = tk.Canvas(self, width=300, height=350, bg="white")
        self.canvas.pack()

        self.draw_clock()

    def draw_clock(self):
        self.canvas.delete("all")
        width = self.winfo_width()
        height = self.winfo_height()
        center_x = width // 2
        center_y = (height - 50) // 2  # Leaving space for the date text
        clock_radius = min(center_x, center_y) - 10

        # Uhrumrandung
        self.canvas.create_oval(
            center_x - clock_radius,
            center_y - clock_radius,
            center_x + clock_radius,
            center_y + clock_radius,
            outline="black",
            width=2,
        )

        # Zeichne Stundenmarkierungen
        for hour in range(1, 13):
            angle = math.radians(360 * hour / 12 - 90)
            x1 = center_x + (clock_radius - 20) * math.cos(angle)
            y1 = center_y + (clock_radius - 20) * math.sin(angle)
            x2 = center_x + clock_radius * math.cos(angle)
            y2 = center_y + clock_radius * math.sin(angle)
            self.canvas.create_line(x1, y1, x2, y2, width=2)

            # Zahlen für 12, 3, 6 und 9 Uhr hinzufügen
            if hour in [3, 6, 9, 12]:
                number_x = center_x + (clock_radius - 40) * math.cos(angle)
                number_y = center_y + (clock_radius - 40) * math.sin(angle)
                self.canvas.create_text(
                    number_x, number_y, text=str(hour), font=("Helvetica", 14, "bold")
                )

        # Zeichne Minutenmarkierungen
        for minute in range(0, 60, 5):
            angle = math.radians(360 * minute / 60 - 90)
            x1 = center_x + (clock_radius - 10) * math.cos(angle)
            y1 = center_y + (clock_radius - 10) * math.sin(angle)
            x2 = center_x + clock_radius * math.cos(angle)
            y2 = center_y + clock_radius * math.sin(angle)
            self.canvas.create_line(x1, y1, x2, y2, width=1)

        # Zeigerpositionen berechnen
        now = time.localtime()
        hour_angle = math.radians(
            360 * ((now.tm_hour % 12) + now.tm_min / 60) / 12 - 90
        )
        minute_angle = math.radians(360 * now.tm_min / 60 - 90)
        second_angle = math.radians(360 * now.tm_sec / 60 - 90)

        # Stundenzeiger
        hour_hand_length = clock_radius * 0.5
        hour_hand_x = center_x + hour_hand_length * math.cos(hour_angle)
        hour_hand_y = center_y + hour_hand_length * math.sin(hour_angle)
        self.canvas.create_line(
            center_x, center_y, hour_hand_x, hour_hand_y, width=4, fill="black"
        )

        # Minutenzeiger
        minute_hand_length = clock_radius * 0.7
        minute_hand_x = center_x + minute_hand_length * math.cos(minute_angle)
        minute_hand_y = center_y + minute_hand_length * math.sin(minute_angle)
        self.canvas.create_line(
            center_x, center_y, minute_hand_x, minute_hand_y, width=3, fill="black"
        )

        # Sekundenzeiger
        second_hand_length = clock_radius * 0.8
        second_hand_x = center_x + second_hand_length * math.cos(second_angle)
        second_hand_y = center_y + second_hand_length * math.sin(second_angle)
        self.canvas.create_line(
            center_x, center_y, second_hand_x, second_hand_y, width=2, fill="red"
        )

        # Zeigermittelpunkt
        self.canvas.create_oval(
            center_x - 5, center_y - 5, center_x + 5, center_y + 5, fill="black"
        )

        # Draw the date text below the center point
        date_str = time.strftime("%d.%m.%Y", now)
        self.canvas.create_text(
            center_x,
            center_y + 65,
            text=date_str,
            font=("Helvetica", 12, "bold"),
            fill="blue",
        )

        # Aktualisiere Uhr alle 200 Millisekunden
        self.after(200, self.draw_clock)


if __name__ == "__main__":
    app = AnalogClock()
    app.mainloop()
