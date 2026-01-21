import base64
import os

def banner():
    print("""
    ######################################
    #    PYTHON GÜVENLİ ŞİFRELEME ARACI   #
    #    (XOR Cipher + Base64 Encoding)  #
    ######################################
    """)

def xor_encrypt_decrypt(data, key):
    """
    XOR mantığı ile veriyi şifreler veya çözer.
    Siber güvenliğin en temel şifreleme mantığıdır.
    """
    encrypted = []
    for i in range(len(data)):
        # Karakterlerin ASCII değerlerini al ve XOR işlemine sok
        xor_val = ord(data[i]) ^ ord(key[i % len(key)])
        encrypted.append(chr(xor_val))
    return "".join(encrypted)

def main():
    banner()
    while True:
        print("\n[1] Metin Şifrele (Encrypt)")
        print("[2] Şifre Çöz (Decrypt)")
        print("[3] Çıkış")
        
        choice = input("Seçiminiz: ")

        if choice == '1':
            text = input("Şifrelenecek Metni Girin: ")
            key = input("Gizli Anahtar (Key) Belirleyin: ")
            
            # Önce XOR yap, sonra okunabilir olması için Base64'e çevir
            encrypted_data = xor_encrypt_decrypt(text, key)
            encoded_data = base64.b64encode(encrypted_data.encode()).decode()
            
            print(f"\n[+] ŞİFRELENMİŞ VERİ (Kopyalayın): {encoded_data}")

        elif choice == '2':
            try:
                text = input("Şifreli Veriyi Yapıştırın: ")
                key = input("Gizli Anahtarı Girin: ")
                
                # Önce Base64'ten çöz, sonra XOR işlemini tersine çevir
                decoded_data = base64.b64decode(text).decode()
                original_data = xor_encrypt_decrypt(decoded_data, key)
                
                print(f"\n[+] ÇÖZÜLMÜŞ (ORİJİNAL) MESAJ: {original_data}")
            except:
                print("\n[!] HATA: Yanlış format veya yanlış anahtar!")

        elif choice == '3':
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim!")

if __name__ == "__main__":
    main()
