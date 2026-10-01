import time
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from kivy.core.window import Window

# Mobil ekran boyutları ve 60 FPS ayarı
Window.size = (360, 640)
Clock.max_fps = 60

class BarisAIApp(App):
    def build(self):
        self.title = "Barış AI v1.0"
        
        # Ana Düzen
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Başlık / Banner
        header = Label(
            text="[b]BARIŞ AI v1.0[/b]",
            markup=True,
            font_size='22sp',
            size_hint_y=None,
            height=40,
            color=(0.2, 0.6, 1, 1)
        )
        main_layout.add_widget(header)
        
        # Sohbet Alanı (ScrollView)
        self.scroll_view = ScrollView(size_hint=(1, 1))
        self.chat_history = Label(
            text="[b]Barış AI:[/b] Merhaba! Ben Barış AI. Sana nasıl yardımcı olabilirim?\n\n",
            markup=True,
            size_hint_y=None,
            font_size='15sp',
            halign='left',
            valign='top'
        )
        self.chat_history.bind(texture_size=self._update_text_height)
        self.chat_history.bind(width=self._update_text_width)
        self.scroll_view.add_widget(self.chat_history)
        main_layout.add_widget(self.scroll_view)
        
        # Alt Giriş Alanı (Metin Kutusu + Gönder Butonu)
        input_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=5)
        
        self.user_input = TextInput(
            hint_text="Mesajınızı yazın...",
            multiline=False,
            font_size='16sp',
            size_hint_x=0.8
        )
        self.user_input.bind(on_text_validate=self.send_message)
        
        send_btn = Button(
            text="Gönder",
            size_hint_x=0.2,
            background_color=(0.2, 0.6, 1, 1),
            bold=True
        )
        send_btn.bind(on_press=self.send_message)
        
        input_layout.add_widget(self.user_input)
        input_layout.add_widget(send_btn)
        main_layout.add_widget(input_layout)
        
        return main_layout

    def _update_text_height(self, instance, value):
        instance.height = value[1]

    def _update_text_width(self, instance, value):
        instance.text_size = (value, None)

    def send_message(self, instance):
        text = self.user_input.text.strip()
        if text:
            # Kullanıcı mesajını ekle
            self.chat_history.text += f"[b]Sen:[/b] {text}\n"
            self.user_input.text = ""
            
            # Cevap simülasyonu
            Clock.schedule_once(lambda dt: self.generate_response(text), 0.3)

    def generate_response(self, user_text):
        # Basit AI yanıt mantığı
        query = user_text.lower()
        if "merhaba" in query or "selam" in query:
            reply = "Selam dostum! Çalışmalar nasıl gidiyor?"
        elif "kimsin" in query:
            reply = "Ben Barış AI v1.0! Kivy ve Buildozer ile geliştirilmiş yerli yapay zeka asistanıyım."
        elif "fps" in query or "kasmak" in query:
            reply = "Arayüzüm tam 60 FPS akıcılıkta kilitli!"
        else:
            reply = f"'{user_text}' mesajını aldım. Harika bir fikir üzerinde çalışıyoruz!"

        self.chat_history.text += f"[b]Barış AI:[/b] {reply}\n\n"
        self.scroll_view.scroll_y = 0  # En aşağı kaydır

if __name__ == '__main__':
    BarisAIApp().run()
# Anan