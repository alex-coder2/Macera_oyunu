def start_adventure():
    print("Mağaraya hoş geldiniz! Bir maceraya atılmaya hazır mısınız?")
    print("Önünüzde iki yol var: soldaki yol ve sağdaki yol.")
    choice = input("Hangi yolu seçmek istersiniz? (sol/sağ): ").strip().lower()
    
    if choice == "sol":
        left_path()
    elif choice == "sağ":
        right_path()
    else:
        print("Geçersiz seçim. Lütfen 'sol' ya da 'sağ' yazın.")
        start_adventure()

def left_path():
    print("Sol yoldan ilerliyorsunuz ve karşınıza bir yaratık çıkıyor!")
    print("Savaşacak mısınız yoksa kaçacak mısınız?")
    choice = input("Seçiminiz? (savaş/kaç): ").strip().lower()
    
    if choice == "savaş":
        fight_creature()
    elif choice == "kaç":
        print("Kaçmayı başardınız, ama yolunuzu kaybettiniz.")
        end_game(False)
    else:
        print("Geçersiz seçim. Lütfen 'savaş' ya da 'kaç' yazın.")
        left_path()

def right_path():
    print("Sağ yoldan ilerliyorsunuz ve bir hazine sandığı buluyorsunuz!")
    print("Sandığı açacak mısınız yoksa devam mı edeceksiniz?")
    choice = input("Seçiminiz? (aç/devam): ").strip().lower()
    
    if choice == "aç":
        print("Tebrikler! Sandığın içinde büyük bir hazine buldunuz!")
        end_game(True)
    elif choice == "devam":
        print("Devam ettiniz, ama sonunda bir uçurumla karşılaştınız.")
        end_game(False)
    else:
        print("Geçersiz seçim. Lütfen 'aç' ya da 'devam' yazın.")
        right_path()

def fight_creature():
    print("Yaratıkla savaşıyorsunuz...")
    print("Kazandınız! Yaratığı yendiniz ve yolunuza devam ediyorsunuz.")
    print("Biraz ilerledikten sonra başka bir hazine sandığı buluyorsunuz.")
    print("Sandığı açacak mısınız yoksa devam mı edeceksiniz?")
    choice = input("Seçiminiz? (aç/devam): ").strip().lower()
    
    if choice == "aç":
        print("Tebrikler! Sandığın içinde büyük bir hazine buldunuz!")
        end_game(True)
    elif choice == "devam":
        print("Devam ettiniz, ama sonunda bir uçurumla karşılaştınız.")
        end_game(False)
    else:
        print("Geçersiz seçim. Lütfen 'aç' ya da 'devam' yazın.")
        fight_creature()

def end_game(won):
    if won:
        print("Macera sona erdi. Kazandınız!")
    else:
        print("Macera sona erdi. Kaybettiniz. Tekrar deneyin.")
    play_again()

def play_again():
    choice = input("Tekrar oynamak ister misiniz? (evet/hayır): ").strip().lower()
    
    if choice == "evet":
        start_adventure()
    elif choice == "hayır":
        print("Oyunu oynadığınız için teşekkürler! Görüşmek üzere!")
    else:
        print("Geçersiz seçim. Lütfen 'evet' ya da 'hayır' yazın.")
        play_again()

start_adventure()