import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from matplotlib.figure import Figure
import matplotlib
from functions_call import get_error_data

class SimpleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Precision analysis")
        root.geometry('800x600')
        
        self.file1_path = None
        self.file2_path = None
        self.figures = []
        
        self.create_widgets()
    
    def create_widgets(self):
        file_frame = ttk.Frame(self.root)
        file_frame.pack(pady=10)
        
        self.btn_file1 = ttk.Button(
            file_frame,
            text="Загрузить файл 1",
            command=self.load_file1
        )
        self.btn_file1.pack(side=tk.LEFT, padx=5)
        
        self.btn_file2 = ttk.Button(
            file_frame,
            text="Загрузить файл 2",
            command=self.load_file2
        )
        self.btn_file2.pack(side=tk.LEFT, padx=5)

        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=10)
        self.label_file1 = ttk.Label(btn_frame, text="Файл 1 не выбран")
        self.label_file1.pack(side=tk.LEFT, padx=5)
        
        self.label_file2 = ttk.Label(btn_frame, text="Файл 2 не выбран")
        self.label_file2.pack(side=tk.RIGHT, padx=5)

        tsai_lenz_var = tk.IntVar()  # Переменная для хранения состояния чекбокса tsai-lenz
        tsai_lenz_check = tk.Checkbutton(root, text="tsai-lenz", variable=tsai_lenz_var)
        tsai_lenz_check.pack()

        park_martin_var = tk.IntVar()  # Переменная для хранения состояния чекбокса park-martin
        park_martin_check = tk.Checkbutton(root, text="park-martin", variable=park_martin_var)
        park_martin_check.pack()

        daniilidis_var = tk.IntVar()  # Переменная для хранения состояния чекбокса daniilidis
        daniilidis_check = tk.Checkbutton(root, text="daniilidis", variable=daniilidis_var)
        daniilidis_check.pack()

        li_wang_wu_var = tk.IntVar()  # Переменная для хранения состояния чекбокса li-wang-wu
        li_wang_wu_check = tk.Checkbutton(root, text="li-wang-wu", variable=li_wang_wu_var)
        li_wang_wu_check.pack()

        shah_var = tk.IntVar()  # Переменная для хранения состояния чекбокса shah
        shah_check = tk.Checkbutton(root, text="shah", variable=shah_var)
        shah_check.pack()
        
        self.submit_btn = ttk.Button(
        self.root,
        text="Выполнить",
        command=lambda: self.run_methods([
            name for name, var in [
                ("tsai-lenz", tsai_lenz_var),
                ("park-martin", park_martin_var),
                ("daniilidis", daniilidis_var),
                ("li-wang-wu", li_wang_wu_var),
                ("shah", shah_var)
            ] if var.get()
        ])
        )

        self.submit_btn.pack(pady=10)

        self.create_scrollable_plot_area()


    def create_scrollable_plot_area(self):
        main_container = ttk.Frame(self.root)
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        canvas_frame = ttk.Frame(main_container)
        canvas_frame.pack(fill=tk.BOTH, expand=True)
        
        self.canvas = tk.Canvas(canvas_frame, bg='white')
        h_scrollbar = ttk.Scrollbar(canvas_frame, orient=tk.HORIZONTAL, command=self.canvas.xview)
        
        self.canvas.configure(xscrollcommand=h_scrollbar.set)
        h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.plots_frame = ttk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.plots_frame, anchor="nw")
    

    def load_file1(self):
        file_path = filedialog.askopenfilename(title="Выберите первый файл")
        if file_path:
            self.file1_path = file_path
            self.label_file1.config(text=f"Файл 1: {file_path.split('/')[-1]}")
    

    def load_file2(self):
        file_path = filedialog.askopenfilename(title="Выберите второй файл")
        if file_path:
            self.file2_path = file_path
            self.label_file2.config(text=f"Файл 2: {file_path.split('/')[-1]}")
    

    def create_plots(self, t_data, r_data):
        plots = []
        for name in t_data:
            metrics = [ "mean", "median", "rmse", "p95", "max"]
            translation = [t_data[name][m] for m in metrics]
            rotation = [r_data[name][m] for m in metrics]
            x = np.arange(len(metrics))
            width = 0.35
            fig, ax = plt.subplots()
            ax.bar(x - width/2, translation, width, label='transplantation')
            ax.bar(x + width/2, rotation, width, label='rotation') 
            ax.legend(loc='upper right', frameon=False)
            ax.legend(loc='upper right', fontsize=10)
            ax.set_xticks(x)
            ax.set_xticklabels(metrics)
            ax.set_xlabel('Метрики')
            ax.set_ylabel('Ошибка')
            ax.set_title('Метод '+ name)
            plots.append(fig)
        return plots
    

    def display_plots(self, figures):
        for widget in self.plots_frame.winfo_children():
            widget.destroy()
        
        self.figures = figures
        self.plot_frames = []
        
        for i, fig in enumerate(figures):
            plot_frame = ttk.Frame(self.plots_frame, relief='solid', borderwidth=1)
            plot_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=False)
            self.plot_frames.append(plot_frame)
            
            title_label = ttk.Label(plot_frame, text=f"График {i+1}", font=('Arial', 10, 'bold'))
            title_label.pack(pady=5)
            
            canvas = FigureCanvasTkAgg(fig, master=plot_frame)
            canvas.draw()
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.config(width=500, height=350)
            canvas_widget.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
            
            save_btn = ttk.Button(
                plot_frame,
                text="Сохранить",
                command=lambda f=fig, n=i: self.save_plot(f, n)
            )
            save_btn.pack(pady=5)
        
        self.plots_frame.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
        self.canvas.xview_moveto(0)
    

    def save_plot(self, fig, plot_number):
        filename = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("PDF files", "*.pdf"), ("All files", "*.*")],
            title=f"Сохранить график {plot_number + 1}"
        )
        if filename:
            fig.savefig(filename, dpi=300, bbox_inches='tight')
            messagebox.showinfo("Успех", f"График сохранен как {filename}")

    
    def run_methods(self, methods):
        if not self.file1_path or not self.file2_path:
            messagebox.showwarning("Предупреждение", "Пожалуйста, выберите оба файла!")
            return
        data = {
            "file1": self.file1_path,
            "file2": self.file2_path,
        }

        t_data, r_data = get_error_data(methods,self.file1_path,self.file2_path)

        messagebox.showinfo("Информация", "Файлы загружены! Генерация графиков...")
        
        sample_plots = self.create_plots(t_data, r_data)
        
        self.display_plots(sample_plots)
        


if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleApp(root)
    root.mainloop()