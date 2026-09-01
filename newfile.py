from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class TestApp(App):
    def build(self):
        # Main Layout Setup
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        # Display Message
        self.label = Label(
            text="School Project Demo App", 
            font_size='24sp',
            bold=True
        )
        
        # Action Button
        btn = Button(
            text="Click Me!", 
            size_hint=(1, 0.3),
            background_color=(0.2, 0.6, 1, 1)
        )
        btn.bind(on_press=self.on_button_click)
        
        layout.add_widget(self.label)
        layout.add_widget(btn)
        return layout

    def on_button_click(self, instance):
        self.label.text = "Success! App is Working!"

if __name__ == "__main__":
    TestApp().run()
