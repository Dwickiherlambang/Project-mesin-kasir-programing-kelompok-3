import os
def clear_screen():
    os.system('cls')
clear_screen()
#--------------------------------------------list-------------------------------------------
mytim = ['Dwicki Herlambang',
         'Adikari Hutama Jaya',
         'MUH FAJRIN NUR',
         'Bagas Juliansyah']
nim = ['231031113',
       '231031120',
       '231031113',
       '231031124']
djual = ['Ayam Goreng',
         'Ayam Geprek',
         'Ayam Penyet',
         'Ayam Bakar',
         'Mineral']
dharga = [15000, 10000, 18000, 20000, 3000]
pesanan = []
harga = []
total_harga = 0
a = True
#--------------------------------------------Tampilan Pertama-------------------------------------------
while a:
    try:
        print('Selamat datang di menu kasi sederhana:)')
        print('1. Masuk Ke Project','\n2. Daftar Anggota')
        opsi = int(input('\nMasukkan Opsi :'))

        #-------------------------------------------------tampilan kedua-------------------------------------
        if opsi==1:
            while a:
                try:
                    clear_screen()
                    print('- '*38)
                    print('UD. Ayam Pak Asep'.center(77))
                    print('Jl. Jend Sudirman No 15, Kota parepare'.center(77))
                    print('        --“Ketika ada waktu, jangan gunakan waktu itu untuk mengeluh”--'.center(1))
                    print('\n*Silahkan Memilih opsi yang telah disediakan')
                    print('1. Menambah Menu',
                        '\n2. Menu ',
                        '\n3. Struk')
                    opsi = int(input('\nPilih Opsi :'))
                    
                    #---------------------------------------Menambah menu------------------------------------------------------------------------
                    if opsi ==1 :
                        while a:
                            try:
                                print('Silahkan Masukkan Menu Baru !!!')
                                tmbh_menu = str(input('\n\tNama Makanan : ').capitalize())
                                tmbh_harga = int(input('\tMasukkan Harga :'))
                                djual.append(tmbh_menu)
                                dharga.append(tmbh_harga)
                                print(input('\n Terimah kasih :))'))
                                clear_screen()
                                break
                            except ValueError:
                                print('Harap masukkan data dengan benar!!')
                                
                    #---------------------------------------------Menu--------------------------------------------------------------------------
                    elif opsi == 2:
                        print('-Daftar Menu-'.center(55))
                        print('- '*26)
                        print("| Kode Pesanan |   Nama Makanan    |   H. Satuan   |")
                        print('- '*26)
                        for i in range(0, len(djual)):
                            print(f'|AA{i+1}'.ljust(15)+'|'+f'{djual[i]}'.ljust(19)+'|'+f'Rp {dharga[i]},-'.rjust(15)+'|')
                            print('- '*26)   

                    #--------------------------------------------Memasukkan Menu------------------------------------------------------------
                        while True:
                            psnan = input('\nMasukkan Kode Pesanan (tekan Enter untuk selesai): ')
                            if psnan == '':
                                print(input('Terima kasih Telah Memesan'))
                                clear_screen()
                                break
                            try:
                                psnan = int(psnan)
                                if 1 <= psnan <= len(djual):
                                    pesanan.append(djual[psnan -1 ])
                                    harga.append(dharga[psnan -1 ])
                                    total_harga += (dharga[psnan -1 ])
                                else:
                                    print('Barang Tidak Terdaftar')
                            except ValueError:
                                print('Masukkan kode pesanan yang valid')

                    #--------------------------------------------Struk-----------------------------------------------------------------------------
                    elif opsi == 3 :
                        clear_screen()
                        print("\n------------------ Struk ------------------")
                        for i in range(len(pesanan)):
                            print(f'{i+1}. {pesanan[i]}'+f'\t\tRp {harga[i]},-')
                        print('_ '*17,'+')
                        print(f"\nTotal Harga:    \t Rp {total_harga},-")
                        print("\n--- Terima kasih atas pembelian Anda! ---")
                        input("\nTekan Enter untuk keluar...")
                        exit()
                    
                    else:
                        print(input('Masukkan pilihan dengan benar'))
                except ValueError:
                    print(input('Harap masukkan opsi yang benar'))
                    
        #--------------------------------------------------Daftar anggota-----------------------------------------------------------------
        elif opsi == 2:
            print('- '*22)
            print("| NO |       Anggota       |      Nim      |")
            print('- '*22)
            for i in range(0, len(mytim)):
                print(f'|{i+1}'.ljust(6)+'|'+f'{mytim[i]}'.ljust(20)+'|'+f'{nim[i]}'.center(15)+'|')
                print('- '*22)
            input('\n Tekan Enter untuk Kembali Ke menu Utama...')
            clear_screen()
        else :
            print('Harap Masukkan angka yang benar!!!')
            print(input('COBA LAGI!!'))
            clear_screen()
    except ValueError:
        print(input('Harap Masukkan opsi yang benar!!'))
        clear_screen()