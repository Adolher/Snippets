import os
from contextlib import contextmanager

@contextmanager
def generic(card_type, senders_name, recipient):
    card = open(os.path.join(os.path.dirname(__file__), card_type), "r")

    generic_card_file_name = f"{senders_name}_generic.txt"
    generic_card = open(os.path.join(os.path.dirname(__file__), generic_card_file_name), "w")

    try:
        text = f"Dear {recipient},\n"
        text += card.read()
        text += f"\nSincerely, {senders_name}"
        generic_card.write(text)
        yield generic_card
    finally:
        card.close()
        generic_card.close

card_type ="happy_bday.txt"
senders_name = "Jörg"
recipient =  "Sarah"

with generic(card_type,senders_name,recipient) as g:
    print("Card generated")

generic_card_file_name = f"{senders_name}_generic.txt"
with open(os.path.join(os.path.dirname(__file__), generic_card_file_name), "r") as g:
    print(g.read())

class Personalized:
    def __init__(self, senders_mame, recipient) -> None:
        self.sender = senders_mame
        self.recipient = recipient
        self.file_name = f"{self.sender}_personalized.txt"
        self.file_path  = os.path.join(os.path.dirname(__file__), self.file_name)
        self.mode = "w"
    def __enter__(self):
        self.open_file = open(self.file_path, self.mode)
        self.open_file.write(f"Dear {self.recipient},\n")
        return self.open_file
    def __exit__(self, *exc):
        self.open_file.write(f"\nSincerely, {self.sender}")
        self.open_file.close()
    def write_text(self, text):
        self.open_file.write(text)

with Personalized("Jörg", "Sarah") as p:
    p.write("I am so proud of you! Being your friend for all these years has been nothing but a blessing. I don\’t say it often but I just wanted to let you know that you inspire me and I love you! All the best. Always.")

senders_name = 'Josiah'
with Personalized(senders_name, 'Esther') as p, generic(card_type, senders_name, 'Remy') as g:
    p.write("Happy Birthday!! I love you to the moon and back. Even though you’re a pain sometimes, you’re a pain I can't live without. I am incredibly proud of you and grateful to have you as a sister. Cheers to 25!! You’re getting old!")
    