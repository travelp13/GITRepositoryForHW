# Task1
# Написати функцію, яка за допомогою регулярних виразів розбиває текст на окремі слова і знаходить частоту окремих слів.
import re

pattern = r"\b\w[\w'-]*\b"
text = """Тут п'ятниця субота, тут ще 
раз привіт міні-маркет! субота"""

words = re.findall(pattern, text.lower())
print (words)

unq_words = set(words)
for word in unq_words:
    cnt = words.count(word)
    print(f"{word} - {cnt}")

# Task2
# Написати функцію, яка за допомогою регулярних виразів з файлу витягує дані про дату народження, 
# телефон та електронну адресу. Дані потрібно записати до іншого файлу.
import re, os

INPUT_PATH = os.path.join(os.path.abspath(__file__ + '/..'), 'input.txt')
OUTPUT_PATH = os.path.join(os.path.abspath(__file__ + '/..'), 'output.txt')

birth_pattern = r'\b\d{2}/\d{2}/\d{4}\b' 
phone_pattern = r'\+380\d{9}|\b0\d{2}-\d{7}\b' 
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' 


def main():
    with open(INPUT_PATH, 'r') as file:
        text = file.read()

    births = re.findall(birth_pattern, text)
    phones = re.findall(phone_pattern, text)
    emails = re.findall(email_pattern, text)

    with open(OUTPUT_PATH, 'w') as file:
        file.write("Дати народження:\n")
        for date in births:
            file.write(f"{date}\n")
        
        file.write("\nНомери телефонів:\n")
        for phone in phones:
            file.write(f"{phone}\n")
        
        file.write("\nЕлектронні адреси:\n")
        for email in emails:
            file.write(f"{email}\n")

main()

# Task3
# Користувач вводить з клавіатури пропозицію. 
# Написати функцію, яка друкуватиме на екран останні 3 символи кожного слова.
import re

def main(text):
    
    words = re.findall(r'(\b\w+\b)', text)

    for word in words:
        print (word[-3:])

text = input("Введіть текст: ")
main(text)

# Task4
# Напишіть функцію, яка буде аналізувати текст, що надходить до неї, 
# і виводити тільки унікальні слова на екран, загальну кількість слів і кількість унікальних слів.
import re

def main(text):
    pattern = r'\b\w+\b'
    words = re.findall(pattern, text.lower()) 

    cnt_words = len(words)

    unq_words = set(words)

    print("Унікальні слова:")
    for word in unq_words:
        print(word)

    print(f"Кількість слів: {cnt_words}")
    print(f"Кількість унікальних слів: {len(unq_words)}")

text = input("Введіть текст: ")
main(text)

# Task5
# З клавіатури вводиться рядок, в якому є інформація про прізвище, ім'я, дату народження, 
# електронну адресу та відгук про курси учня. Написати функцію, яка, використовуючи регулярні вирази, 
# витягне дані з рядка і поверне словник.
import re

name_pattern = r'([А-ЯA-Z][а-яa-z]+)\s([А-ЯA-Z][а-яa-z]+)'  
birth_pattern = r'\b\d{2}/\d{2}/\d{4}\b' 
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' 
feedback_pattern = r'Відгук: (.+)'  

def main(text: str):

    name = re.search(name_pattern, text)
    birth = re.search(birth_pattern, text)
    email = re.search(email_pattern, text)
    feedback = re.search(feedback_pattern, text)

    student = {}

    if name:
        student['Прізвище'] = name.group(1)
        student['Ім\'я'] = name.group(2)

    if birth:
        student['Дата народження'] = birth.group()

    if email:
        student['Електронна адреса'] = email.group()

    if feedback:
        student['Відгук'] = feedback.group(1)

    return student

text = input("Введіть дані про учня: ")
student = main(text)

for key, value in student.items():
    print(f"{key}: {value}")
