import tkinter

import tkinter.ttk as ttk

from tkinter.filedialog import askopenfile, asksaveasfile

from tkinter.messagebox import showinfo

from tkinter.font import Font

from PIL import Image

from moviepy.audio.io.AudioFileClip import AudioFileClip

from moviepy.video.VideoClip import ImageClip

import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)


class App:

    def __init__(self) -> None:

        self.pic_path = None

        self.audio_path = None

        self.create_window()

        self.create_font()

        self.create_ui()

        self.load_ui()

    def upload_pic(self) -> None:

        path = askopenfile(defaultextension='png', filetypes =[('PNG FILE', '*.png'),('JPG FILE', '*.jpg'),("all files", "*.*")]).name

        self.pic_path = path

        self.label_pic_path.config(text=path)

        print(path)

    def upload_audio(self) -> None:

        path = askopenfile(defaultextension='wav', filetypes =[('WAV FILE', '*.wav'),('MP3 FILE', '*.mp3'),("all files", "*.*")]).name

        self.audio_path = path

        self.label_audio_path.config(text=path)

        print(path)

    def generate(self) -> None:

        save_path = asksaveasfile(initialfile='output.mp4', filetypes =[('MP4 FILE', '*.mp4'),("all files", "*.*")])

        print(save_path.name)

        img = Image.open(self.pic_path)

        audio = AudioFileClip(self.audio_path)

        video = ImageClip(self.pic_path).set_duration(audio.duration)

        final_clip = video.set_audio(audio)

        final_clip.fps = 30

        final_clip.write_videofile(save_path.name)

        showinfo('Success', f'Video  {save_path.name} successfully generated!')

    def create_window(self) -> None:

        self.window = tkinter.Tk()

        self.window.config(background='#00cc99')

        self.window.title('Sound Includer')

    def create_font(self) -> None:
        
        self.font = Font(family='Roboto', size=18)

    def create_space(self, bg='#00cc99'):

        tkinter.Label(self.window, background=bg).pack()

    def create_ui(self) -> None:

        self.label_1 = tkinter.Label(self.window, text='Your Picture File Path: ', font=self.font, foreground='#00cc99')

        self.label_pic_path = tkinter.Label(font=self.font, foreground='#00cc99')

        self.button_pic_upload = tkinter.Button(self.window, text='Upload Picture', command=self.upload_pic, font=self.font, foreground='#00cc99')

        self.label_2 = tkinter.Label(self.window, text='Your Audio File Path: ', font=self.font, foreground='#00cc99')

        self.label_audio_path = tkinter.Label(self.window, font=self.font, foreground='#00cc99')

        self.button_audio_upload = tkinter.Button(self.window, text='Upload Audio', command=self.upload_audio, font=self.font, foreground='#00cc99')

        self.button_generate = tkinter.Button(self.window, text='Generate', command=self.generate, font=self.font, foreground='#00cc99')

    def load_ui(self) -> None:

        self.create_space()

        self.label_1.pack()

        self.label_pic_path.pack()

        self.button_pic_upload.pack()

        self.create_space()

        self.label_2.pack()

        self.label_audio_path.pack()

        self.button_audio_upload.pack()

        self.create_space()

        self.button_generate.pack()

        self.create_space()

    def run(self) -> None:

        self.window.mainloop()


if __name__ == '__main__':

    app = App()

    app.run()