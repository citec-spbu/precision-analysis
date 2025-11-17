import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from matplotlib.figure import Figure
import matplotlib

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
        
        self.submit_btn = ttk.Button(
            self.root,
            text="Выполнить",
            command=self.run_methods
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
    

    def create_sample_plots(self):
        """Создает примеры графиков для демонстрации"""
        plots = []
        
        fig1 = Figure(figsize=(6, 4), dpi=80)
        ax1 = fig1.add_subplot(111)
        x = np.linspace(0, 4*np.pi, 100)
        y = np.sin(x)
        ax1.plot(x, y, 'b-', linewidth=2)
        ax1.set_title('Синусоида')
        ax1.grid(True)
        plots.append(fig1)
        
        fig2 = Figure(figsize=(6, 4), dpi=80)
        ax2 = fig2.add_subplot(111)
        y2 = np.cos(x)
        ax2.plot(x, y2, 'r-', linewidth=2)
        ax2.set_title('Косинусоида')
        ax2.grid(True)
        plots.append(fig2)
        
        fig3 = Figure(figsize=(6, 4), dpi=80)
        ax3 = fig3.add_subplot(111)
        data = np.random.normal(0, 1, 1000)
        ax3.hist(data, bins=30, alpha=0.7, color='green')
        ax3.set_title('Гистограмма')
        ax3.grid(True)
        plots.append(fig3)
        
        fig4 = Figure(figsize=(6, 4), dpi=80)
        ax4 = fig4.add_subplot(111)
        x4 = np.random.normal(0, 1, 50)
        y4 = np.random.normal(0, 1, 50)
        ax4.scatter(x4, y4, color='purple', alpha=0.6)
        ax4.set_title('Точечный график')
        ax4.grid(True)
        plots.append(fig4)
        
        fig5 = Figure(figsize=(6, 4), dpi=80)
        ax5 = fig5.add_subplot(111)
        x5 = np.linspace(0, 5, 100)
        y5 = np.exp(x5)
        ax5.plot(x5, y5, 'orange', linewidth=2)
        ax5.set_title('Экспонента')
        ax5.grid(True)
        plots.append(fig5)
        
        for i in range(6, 9):
            fig = Figure(figsize=(6, 4), dpi=80)
            ax = fig.add_subplot(111)
            x = np.linspace(0, 10, 100)
            y = np.sin(x) * np.cos(i * x / 2)
            ax.plot(x, y, color=plt.cm.tab10(i-5), linewidth=2)
            ax.set_title(f'График {i}')
            ax.grid(True)
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

    
    def run_methods(self):
        if not self.file1_path or not self.file2_path:
            messagebox.showwarning("Предупреждение", "Пожалуйста, выберите оба файла!")
            return
        data = {
            "file1": self.file1_path,
            "file2": self.file2_path,
        }

        # Логика обработки файлов

        # parser(data['file1'])
        # parser(data['file2'])
        # method_1(file1, file2)
        # method_2(file1, file2)
        # method_3(file1, file2)


        messagebox.showinfo("Информация", "Файлы загружены! Генерация графиков...")
        
        sample_plots = self.create_sample_plots()
        
        self.display_plots(sample_plots)
        


if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleApp(root)
    root.mainloop()