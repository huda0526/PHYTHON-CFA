#MAIN MENU
def main():
    print('SELAMAT DATANG DI GAME TEKA NOMBOR')
    nama = input('Hello, Silakan Input Nama Anda : ')
    mulaiGame = input(f'Halo {nama}, kamu mahu bermain teka nombor? (ya/tidak) : ')

 #struktur kawalan pilihan
 # output nombor antara 1 hingga 10
  
    import random

    if mulaiGame.lower() == 'ya':
        kesempatan = 3
        nombor_rahsia = random.randint(1, 10)
        
        print('Silakan pilih angka antara 1 sampai 10')
        print(f'Anda memiliki {kesempatan} kesempatan untuk meneka angka tersebut!')
    #ulangan
        while kesempatan > 0:
            nombor_tekaan = int(input('Silakan masukkan nombor tekaan anda : '))
          
            if nombor_tekaan == nombor_rahsia: #jika pilihan yang sama dengan komputer
                print(f'TAHNIAH Anda Berhasil Meneka Nombor Rahsia. \nAngka yang Anda Pilih : {nombor_tekaan}')
                break
            elif nombor_tekaan < nombor_rahsia: #jika nombor tidak sama dengan komputer
                print('Tekaan anda salah. Angka yang anda pilih terlalu rendah')
            elif nombor_tekaan > nombor_rahsia:
                print('Tekaan anda salah. Angka yang anda pilih terlalu tinggi')
            
            kesempatan -= 1
            if kesempatan > 0:
                print(f'Anda memiliki {kesempatan} kesempatan lagi')
        else:
            print(f'Sayang sekali , anda gagal meneka nombor rahsia. \nNombor rahsianya adalah {nombor_rahsia}.')
main()