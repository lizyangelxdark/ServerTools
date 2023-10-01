python
import time
from pywhatsapp import WhatsAPIDriver

def send_message(phone_number, message):
    driver = WhatsAPIDriver()
    driver.wait_for_login()

    contact = driver.get_contact_by_phone_number(phone_number)
    if contact:
        driver.send_message_to_id(contact.id, message)
        print(f"Message sent to {contact.name}")
    else:
        print(f"Contact {phone_number} not found")

    driver.quit()

def main():
    phone_number = "1234567890"
    message = "Hello, this is a test message."

    # Send a message every 5 minutes
    while True:
        send_message(phone_number, message)
        time.sleep(300) # 300 seconds = 5 minutes

if __name__ == "__main__":
    main()
