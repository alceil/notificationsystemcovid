from plyer import notification;

def notifyMe(title,message):
    notification.notify(
        title = title,
        message =message,
        timeout = 6
    )

if __name__ == "__main__":
    notifyMe("Kindi","Odra myre")    