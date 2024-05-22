import win32com.client as win32

outlook = win32.Dispatch("outlook.application")

emailoutlook = outlook.CreateItem(0)

emailoutlook.To = "ana@gmail.com"
emailoutlook.Subject = "Feliz Aniversário!"
emailoutlook.HTMLBody = """
<p>Parabéns, Ana!</p>
<p>Esse é um dia especial, aproveite seu dia!</p>
<p>Atenciosamente.</p>
"""
emailoutlook.save()