import random
import json

# Kıyafet veritabanı dosyası
CLOTHES_DB_FILE = "clothes.json"

# Kıyafet veritabanı
clothes = []

def load_clothes():
    global clothes
    try:
        with open(CLOTHES_DB_FILE, "r") as file:
            clothes = json.load(file)
    except FileNotFoundError:
        print("Kıyafet veritabanı bulunamadı. Yeni bir veritabanı oluşturulacak.")

def save_clothes():
    with open(CLOTHES_DB_FILE, "w") as file:
        json.dump(clothes, file)

def add_clothing():
    name = input("Kıyafet ismi: ").lower()
    clothing_type = input("Kıyafet türü (üst/alt/elbise/ayakkabı): ").lower()
    color = input("Renk: ").lower()
    style = input("Stil: ").lower()
    weather_conditions = input("Hangi hava durumlarında giyilebilir? (Virgülle ayırarak yazın): ").lower().split(",")
    clothes.append({"isim": name, "tür": clothing_type, "renk": color, "stil": style, "hava_durumu": weather_conditions})
    save_clothes()

def generate_outfit(preferred_style, preferred_weather, preferred_colors):
    filtered_dress = [cloth for cloth in clothes if cloth["tür"] == "elbise" and preferred_style in cloth["stil"] and preferred_weather in cloth["hava_durumu"]]
    filtered_tops = [cloth for cloth in clothes if cloth["tür"] == "üst" and preferred_style in cloth["stil"] and preferred_weather in cloth["hava_durumu"]]
    filtered_bottoms = [cloth for cloth in clothes if cloth["tür"] == "alt" and preferred_style in cloth["stil"] and preferred_weather in cloth["hava_durumu"]]
    filtered_shoes = [cloth for cloth in clothes if cloth["tür"] == "ayakkabı" and preferred_style in cloth["stil"] and preferred_weather in cloth["hava_durumu"]]

    if not filtered_shoes:
        print("Üzgünüz, uygun kombin bulunamadı. Lütfen kıyafetlerinizi güncelleyin.")
        return None

    if "farketmez" in preferred_colors:  # Eğer renk farketmezse, tüm renkleri kullan
        preferred_colors = [cloth["renk"] for cloth in clothes]
    else:
        preferred_colors = preferred_colors

    if filtered_dress and random.choice([True, False]):  # Elbise kombini oluştur
        dress = random.choice(filtered_dress)
        shoe = random.choice(filtered_shoes)
        return {"Elbise": dress["isim"], "Ayakkabı": shoe["isim"]}
    elif filtered_tops and filtered_bottoms:  # Üst-alt kombini oluştur
        top = random.choice(filtered_tops)
        bottom = random.choice(filtered_bottoms)
        shoe = random.choice(filtered_shoes)
        return {"Üst": top["isim"], "Alt": bottom["isim"], "Ayakkabı": shoe["isim"]}
    else:
        print("Üzgünüz, uygun kombin bulunamadı. Lütfen kıyafetlerinizi güncelleyin.")
        return None

def show_clothes():
    print("\nMevcut Kıyafetler:")
    print("{:<20} {:<10} {:<10} {:<15} {:<20}".format("İsim", "Tür", "Renk", "Stil", "Hava Durumu"))
    print("-" * 75)
    for cloth in clothes:
        print("{:<20} {:<10} {:<10} {:<15} {:<20}".format(cloth["isim"], cloth["tür"], cloth["renk"], cloth["stil"], ", ".join(cloth["hava_durumu"])))

def delete_clothing_by_name():
    clothing_name = input("Silmek istediğiniz kıyafetin ismini girin: ").lower()
    found = False
    for index, cloth in enumerate(clothes):
        if cloth["isim"].lower() == clothing_name:
            clothes.pop(index)
            found = True
    if found:
        save_clothes()  # Kıyafetin dosyadan da silinmesi için dosyayı yeniden kaydedin
        print("Kıyafet başarıyla silindi.")
    else:
        print("Belirtilen isimde bir kıyafet bulunamadı.")


def main():
    load_clothes()
    while True:
        print("\n1. Kıyafet ekle")
        print("2. Kıyafetleri göster")
        print("3. Kombin oluştur")
        print("4. Kıyafet sil")
        print("5. Çıkış")
        choice = input("Seçiminizi yapın: ")

        if choice == "1":
            add_clothing()
        elif choice == "2":
            show_clothes()
        elif choice == "3":
            preferred_style = input("Bugün hangi stilde giyinmek istiyorsunuz? ").lower()
            preferred_weather = input("Bugün hava nasıl? (sıcak/ılık/soğuk): ").lower()
            preferred_colors_input = input("Hangi renkleri giymek istiyorsunuz? (Virgülle ayırarak yazın, 'farketmez' yazarak renk önemsememenizi belirtebilirsiniz): ").lower()
            if preferred_colors_input.strip() == "farketmez":
                preferred_colors = [cloth["renk"] for cloth in clothes]
            else:
                preferred_colors = preferred_colors_input.split(",")
            outfit = generate_outfit(preferred_style, preferred_weather, preferred_colors)
            if outfit:
                print("\nİşte kombininiz:")
                for key, value in outfit.items():
                    print(f"{key.capitalize()}: {value}")
        elif choice == "4":
            delete_clothing_by_name()
        elif choice == "5":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()








































































































































