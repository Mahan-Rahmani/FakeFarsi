import random
import sys

try:
    from .data import male_names, female_names, l_names
except ImportError:
    from data import male_names, female_names, l_names


class FakeFarsi:
    def __init__(self):
        self.names = male_names + female_names
        self.last_names = l_names

    def fake_name(self):
        """Generate a fake first name."""
        return random.choice(self.names).strip()

    def fake_last_name(self):
        """Generate a fake last name."""
        return random.choice(self.last_names)

    def fake_full_name(self):
        """Generate a fake full name."""
        return f"{self.fake_name()} {self.fake_last_name()}"

    def fake_age(self):
        """Generate a fake age."""
        return random.randint(10, 99)

    def fake_phone(self):
        """Generate a fake phone number."""
        phone_number = "09"
        index2 = ["1", "3", "9"]
        phone_number += random.choice(index2)
        for _ in range(8):
            phone_number += str(random.randint(0, 9))
        return phone_number

    def translator(self, text):
        """Translate Persian characters to English."""
        mapping = {
            "آ": "a", "ا": "a", "ب": "b", "پ": "p", "ت": "t", "ث": "s", "ج": "j", "چ": "ch", "ه": "h",
            "خ": "kh", "د": "d", "ذ": "z", "ر": "r", "ز": "z", "س": "s", "ش": "sh", "ص": "s", "ظ": "z",
            "ط": "t", "ع": "a", "غ": "gh", "ق": "gh", "ف": "f", "ک": "k", "گ": "g", "ل": "l", "م": "m",
            "ن": "n", "و": "v", "ی": "i", "ء": "a", "ئ": "e", "ي": "i", "ح": "h", "ض": "z", "ك": "k"
        }
        for key, value in mapping.items():
            text = text.replace(key, value)
        return text

    def fake_email(self, name=None, lastname=None):
        """
        Generate a fake email address.
        اگر نام و فامیل داده نشود، خودش ابتدا آن‌ها را فیک تولید می‌کند.
        """
        if not name:
            name = self.fake_name()
        if not lastname:
            lastname = self.fake_last_name()

        email = self.translator(name) + self.translator(lastname) + str(random.randint(1, 999)) + "@gmail.com"
        return email.replace(" ", "").lower()

    def generate_fake_profile(self):
        """Generate a complete fake profile."""
        f = self.fake_name()
        l = self.fake_last_name()
        n = f"{f} {l}"
        a = self.fake_age()
        p = self.fake_phone()
        e = self.fake_email(f, l)
        s = f"نام و نام خانوادگی : {n} \nسن : {a} \nشماره تلفن : {p} \nایمیل : {e}"
        return s

    def cli_menu(self):
        """منوی خط فرمان برای تعامل مستقیم در ترمینال"""
        while True:
            print("\n" + "=" * 35)
            print("     ابزار تولید داده فیک فارسی     ")
            print("=" * 35)
            print("1. تولید نام فیک")
            print("2. تولید نام خانوادگی فیک")
            print("3. تولید سن فیک")
            print("4. تولید شماره تلفن فیک")
            print("5. تولید ایمیل فیک (کاملاً مستقل)")
            print("6. تولید پروفایل کامل")
            print("7. خروج")
            print("=" * 35)

            try:
                choice = input("یک گزینه انتخاب کنید (۱ تا ۷): ").strip()

                if choice == "1":
                    print(f"\n[+] نام: {self.fake_name()}")
                elif choice == "2":
                    print(f"\n[+] نام خانوادگی: {self.fake_last_name()}")
                elif choice == "3":
                    print(f"\n[+] سن: {self.fake_age()}")
                elif choice == "4":
                    print(f"\n[+] شماره تلفن: {self.fake_phone()}")
                elif choice == "5":
                    # حالا بدون پاس دادن ورودی هم کار می‌کند!
                    print(f"\n[+] ایمیل: {self.fake_email()}")
                elif choice == "6":
                    print(f"\n[+] مشخصات پروفایل کامل:\n{self.generate_fake_profile()}")
                elif choice == "7":
                    print("\nخروج از برنامه . <<اوقات خوبی رو براتون آرزومندیم>>")
                    break
                else:
                    print("\n[-] گزینه نامعتبر!")
            except (KeyboardInterrupt, EOFError):
                print("\n\nخروج ناگهانی.")
                break

def run_cli():
    """این تابع توسط pyproject.toml صدا زده می‌شود تا منو اجرا شود"""
    instance = FakeFarsi()
    instance.cli_menu()

if __name__ == "__main__":
    run_cli()
