import random 
import datetime
from costumer import costumer

atm =  costumer(id)
while True:

        id = int(input("Masukan pin Anda: "))
        trial = 0

        while (id != int(atm.checkPin( ) ) and trial < 3 ):
            id = int(input("Pin Anda Salah. Silahkan Masukkan kembali dengan Benar: "))
            trial += 1
 
            if trial == 3:
                print("Error. Silahkan ambil kartu dan coba lagi...")
                exit()

while True:
        print("Selamat datang di ATM Faisaru...")
        print("\n 1 - Cek Saldo \t 2 - Debet \t 3 - Simpan \t 4 - Ganti Pin \t 5 - Keluar")
        selectmenu = int(input("\nSilahkan pilih menu: ") )
        if selectmenu == 1:
            print("\nSaldo Anda sekarang: Rp. "+str(atm.checkBalance() ) + "\n")
        elif selectmenu == 2:
                nominal = float(input("Masukan nominal saldo: "))
                verify_withdraw = input("Konfirmasi: Anda akan melakukan debet dengan nominal berikut ? y/n" +str(nomina) + "" )
                if verify_withdraw =="Y":
                    print("Saldo awal anda adalah Rp. " +str(atm.checkBalance()) + "")
                else:
                    break
                if nominal < atm.checkBalance():
                    atm.withdrawBalance(nominal)
                    print("Transaksi debet berhasil!")
                    print("Saldo sisa sekarang: Rp. " +str(atm.checkBalance()) + "")
                else:
                    print("Maaf. saldo Anda tidak cukup untuk melakukan debet!")
                    print("Silahkan lakukan penambahan nominal saldo")
        elif selectmenu == 3:
                nominal = float(input("Masukkan nominal saldo: "))
                verify_deposit = input("Konfirmasi: Anda akan melakukan penyimpanan dengan nominal berikut ? Y/N " + str(nominal) + "")
                if verify_deposit == "Y":
                    atm.depositBalance(nominal)
                    print("Saldo Anda sekarang adalah: Rp." + str(atm.checkBalance()) + "\n")
                else:
                    break
        elif selectmenu == 4:
            verify_pin = int(input("Masukkan pin Anda: "))
            while verify_pin != int(atm.checkPin()) :
                print("Pin Anda berhasil diganti.")
                verify_newpin = int(input("COba masukkan pin baru: "))

                if verify_newpin == updated_pin:
                    print("pin baru Anda Sukses!")
                else:
                    print("Maaf, Pin Anda salah. Silahkan dicoba kembali dengan benar")
        elif selectmenu == 5:
            print("Resi tercetak otomatis saat Anda keluar. \n Harap simpan tanda terima ini \n senagai bukti trasanksi Anda.")
            print("No. Record : ", random.randint(100000, 1000000))
            print("Tanggal : ", datetime.datetime.now())
            print("Saldo akhir : ", atm.checkBalance())
            print("Terima Kasih telah menggunakan ATM Faisaru!")
            exit()
        else:
            print("ERROR. Maaf, Menu tidak tersedia")
                  