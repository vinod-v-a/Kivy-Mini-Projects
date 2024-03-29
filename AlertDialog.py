from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton



class AlertDialog(MDApp):
    dialog = None
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('AlertDialog.kv')

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title ="Pretty Neat",
                text ="Are you seeing popup",
                buttons =[
                    MDFlatButton(
                        text = "Cancel", text_color=self.theme_cls.primary_color, on_release= self.close_dialog ),
                    MDRectangleFlatButton(
                        text ="YES It's neat ", text_color=self.theme_cls.primary_color, on_release= self.neat_dialog),
                ],
            )

        self.dialog.open()

    def close_dialog(self,obj):
        self.dialog.dismiss()

    def neat_dialog(self,obj):
        self.dialog.dismiss()
        self.root.ids.my_label.text="Yes It's Neat"





AlertDialog().run()
