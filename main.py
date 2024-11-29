from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from jnius import autoclass
import android

class SmsApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.phone_input = TextInput(hint_text='Phone Number', multiline=False)
        self.message_input = TextInput(hint_text='Message Text', multiline=True)
        
        send_button = Button(text='Send Message')
        send_button.bind(on_press=self.send_sms)
        
        layout.add_widget(Label(text='Send SMS'))
        layout.add_widget(self.phone_input)
        layout.add_widget(self.message_input)
        layout.add_widget(send_button)
        
        return layout

    def send_sms(self, instance):
        phone_number = self.phone_input.text
        message = self.message_input.text
        if android:
            # Use Intent to send the message
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')
            context = autoclass('org.kivy.android.PythonActivity').mActivity

            sms_intent = Intent(Intent.ACTION_VIEW)  # Change to ACTION_VIEW
            sms_intent.setData(Uri.parse("sms:" + phone_number))
            sms_intent.putExtra("sms_body", message)
            context.startActivity(sms_intent)
        else:
            print(f"Phone Number: {phone_number}, Message: {message}")  # For testing on non-Android

if __name__ == '__main__':
    SmsApp().run()
