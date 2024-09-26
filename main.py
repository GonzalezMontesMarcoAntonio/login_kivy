from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class LoginScreen(BoxLayout):
    def check_credentials(self):
        email = self.ids.email_input.text
        password = self.ids.password_input.text
        
        # Simulación de credenciales correctas
        if email == "test@domain.com" and password == "password123":
            self.show_popup("Login Exitoso", "¡Bienvenido!")
        else:
            self.show_popup("Error", "Correo o contraseña incorrectos")
    
    def show_popup(self, title, message):
        popup_content = BoxLayout(orientation='vertical')
        popup_label = Label(text=message)
        popup_button = Button(text="Cerrar", size_hint=(1, 0.25))
        popup_content.add_widget(popup_label)
        popup_content.add_widget(popup_button)
        
        popup = Popup(title=title, content=popup_content, size_hint=(0.5, 0.5))
        popup_button.bind(on_press=popup.dismiss)
        popup.open()

class LoginApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    LoginApp().run()



