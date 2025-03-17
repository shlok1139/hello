from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.label import Label
from kivy.uix.image import Image
import fitz  # PyMuPDF

class PDFReader(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.label = Label(text="Select a PDF to Read", size_hint=(1, 0.1))
        self.add_widget(self.label)

        self.filechooser = FileChooserIconView(path="./books", filters=["*.pdf"])
        self.filechooser.bind(selection=self.load_pdf)
        self.add_widget(self.filechooser)

        self.image = Image(size_hint=(1, 0.8))
        self.add_widget(self.image)

    def load_pdf(self, filechooser, selection):
        if selection:
            pdf_path = selection[0]
            self.label.text = f"Reading: {pdf_path}"

            doc = fitz.open(pdf_path)
            page = doc[0]
            pix = page.get_pixmap()
            img_path = "temp_page.png"
            pix.save(img_path)

            self.image.source = img_path

class EbookApp(App):
    def build(self):
        return PDFReader()

if __name__ == "__main__":
    EbookApp().run()
