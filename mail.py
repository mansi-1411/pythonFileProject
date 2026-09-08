import smtplib
from email.message import EmailMessage
msg = EmailMessage()
msg["Subject"]="greeting message"
msg["From"]="manasaedula14@gmail.com"
msg["TO"]="rizwanagosarapalli@gmail.com,kpbhargavi02@gmail.com"
msg.set_content("""
Dear guys,
HOW are you ,iam fine 
i hope your also fine
what about your job 
bangalore ala vudhiiii
baga enjoy chestunara
me suresh sir ala vunadu


""")
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login("manasaedula14@gmail.com","oficbzladmlsbdpq")
server.send_message(msg)
print("email sent successfully")
server.quit()