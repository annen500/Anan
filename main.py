from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.utils import escape_markup


# Keep the default window usable on school laptops with smaller screens.
Window.size = (480, 600)
Clock.max_fps = 60


class BarisAIApp(App):
    def build(self):
        self.title = "Barış AI v1.0 - Desktop Edition"

        main_layout = BoxLayout(orientation="vertical", padding=12, spacing=8)

        header = Label(
            text="[b]BARIŞ AI v1.0[/b]",
            markup=True,
            font_size="24sp",
            size_hint_y=None,
            height=45,
            color=(0.2, 0.6, 1, 1),
        )
        main_layout.add_widget(header)

        self.scroll_view = ScrollView(size_hint=(1, 1), do_scroll_x=False)
        self.chat_history = Label(
            text="[b]Barış AI:[/b] Merhaba! Ben Barış AI. Sana nasıl yardımcı olabilirim?\n\n",
            markup=True,
            size_hint_y=None,
            size_hint_x=1,
            font_size="16sp",
            halign="left",
            valign="top",
        )
        self.chat_history.bind(texture_size=self._update_text_height)
        self.chat_history.bind(width=self._update_text_width)
        self.scroll_view.add_widget(self.chat_history)
        main_layout.add_widget(self.scroll_view)

        input_layout = BoxLayout(
            orientation="horizontal", size_hint_y=None, height=52, spacing=8
        )
        self.user_input = TextInput(
            hint_text="Mesajınızı yazın...",
            multiline=False,
            font_size="16sp",
            size_hint_x=1,
            padding=[10, 12, 10, 10],
        )
        self.user_input.bind(on_text_validate=self.send_message)

        send_btn = Button(
            text="Gönder",
            size_hint_x=None,
            width=100,
            background_color=(0.2, 0.6, 1, 1),
            bold=True,
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
            self.chat_history.text += f"[b]Sen:[/b] {escape_markup(text)}\n"
            self.user_input.text = ""
            self._schedule_scroll_to_bottom()
            Clock.schedule_once(lambda dt: self.generate_response(text), 0.3)

    def generate_response(self, user_text):
        query = user_text.lower()
        if "merhaba" in query or "selam" in query:
            reply = "Selam dostum! Çalışmalar nasıl gidiyor?"
        elif "kimsin" in query:
            reply = "Ben Barış AI v1.0! Windows ve Android ortamlarında çalışan asistanınım."
        elif "fps" in query or "kasmak" in query:
            reply = "Arayüzüm masaüstünde de tam 60 FPS akıcılıkta kilitli!"
        else:
            reply = f"'{user_text}' mesajını aldım. Sistemin harika çalışıyor!"

        self.chat_history.text += f"[b]Barış AI:[/b] {escape_markup(reply)}\n\n"
        self._schedule_scroll_to_bottom()

    def _schedule_scroll_to_bottom(self):
        Clock.schedule_once(lambda dt: setattr(self.scroll_view, "scroll_y", 0), 0.1)


if __name__ == "__main__":
    BarisAIApp().run()