Tautan menuju PWS: https://naila-khadijah-i-wear-soccer.pbp.cs.ui.ac.id/

<details>
<summary>Tugas 2</summary>
Step by step mengerjakan checklist: 
1. Untuk membuat proyek Django yang baru, saya membuat terlebih dahulu direktori baru bernama i-wear-soccer (nama proyek saya) lalu membuka command prompt di dalam direktori tersebut. Kemudian, saya membuat virtual environment dengan menjalankan perintah py -m venv env dan mengaktifkannya dengan menjalankan perintah env\Scripts\activate. Saya kemudian membuat file requirements.txt di dalam direktori yang berisi dependencies yang ingin saya install dan gunakan dalam pembuatan proyek dn menginstallnya dengan menjalankan pip install -r requirements.txt. Saya kemudian melakukan inisialisasi proyek Django dengan menjalankan: django-admin startproject football_news . 
2. Untuk membuat aplikasi main pada proyek, saya menjalankan perintah python manage.py startapp main di cmd dan menambahkan string 'main' sebagai elemen terakhir list INSTALLED_APPS di settings.py
3. Untuk mengonfigurasi routing proyek, saya menambahkan impor fungsi include dari django.urls dan menambahkan path('', include('main.urls')) sebagai elemen dari list urlpatterns di file urls.py level pada proyek (di luar aplikasi main).
4. Saya membuat model bernama Shop di models.py. Saya juga membuat list kategori berisi tuple string kategori. Saya membuat 7 variable field dan menentukan jenis fieldnya sebagai berikut:     
    name = models.CharField()
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField()
    is_featured = models.BooleanField(default=False)
    rating = models.DecimalField(max_digits=2, decimal_places=1, validators=[validate_rating])
    stock = models.IntegerField()
dan membuat fungsi validate_rating(value) sebagai validator.
5. Untuk checklist kelima, saya membuat terlebih dahulu direktori template di dalam aplikasi main dan membuat file main.html di dalamnya. Kemudian saya membuat fungsi show_main(request) di views.py yang berisi dictionary context dan mereturn value dictionary berdasarkan key yang direquest oleh main.html (render(request, "main.html", context)). Saya mengisi main.html dengan: <h1>{{ app }}</h1> <p>{{ name }}</p> <p>{{ class }}</p>
dimana app, name, dan class merupakan key dari dictionary context.
6. Untuk membuat routing aplikasi mainm saya membuat berkas urls.py dalam direktori main (level aplikasi) kemudian mengimpor path dari django.urls, show_main dari main.views (views.py aplikasi main), mendeklarasikan app_name = 'main', dan membuat list urlpatterns yang berisi satu elemen yaitu: path('', show_main, name='show_main')
7. Untuk melakukan deploy PWS, saya membuat proyek baru terlebih dahulu di pws saya bernama i-wear-soccer. Kemudian saya menambahkan url deployment ke ALLOWED_HOST di settings.py kemudian menjalankan perintah di cmd: git remote add pws <link_proyek>, git branch -M main, git push pws main kemudian mengisi kredensial yang saya dapatkan ketika pertama kali membuat proyek di pws.
    
Bagan alur: https://drive.google.com/file/d/1I_olazt7Q9YMaL2zTSE65_saWtLjRndF/view?usp=sharing

settings.py berfungsi sebagai file konfigurasi utama untuk sebuah proyek Django. File ini berisi semua pengaturan untuk sebuah website, termasuk konfigurasi database, opsi spesifik Django, dan pengaturan untuk setiap aplikasi di dalamnya. Salah satu fungsi utamanya adalah mendaftarkan semua aplikasi yang digunakan oleh proyek melalui daftar INSTALLED_APPS, yang memberitahu Django aplikasi mana yang harus diaktifkan dan disertakan dan menentukan host yang bisa mendeploy proyek (ALLOWED_HOSTS)

Migrasi database django bekerja dalam 2 langkah. Setelah mengubah model di models.py, untuk menerapkan ke database, jalankan python manage.py makemigrations di cmd. Perintah ini akan membuat file migrasi yang berisi instruksi untuk mempersiapkan perubahan skema model agar sesuai dengan database lokal Django. Untuk menerapkannya, kemudian jalankan perintah python manage.py migrate yang mengambil file migrasi yang telah dibuat sebelumnya dan menerapkan skema model yang baru ke dalam database Django.

Menurut saya, alasan django dijadikan permulaan pembelajaran pengembangan perangkat lunak adalah karena framework ini adalah framework paling stabil dari framework lainnya. Berdasarkan benchmark https://sharkbench.dev/web, stabilitas django mencapai 93.76%. Django juga menggunakan arsitektur MVT yang memudahkan mahasiswa untuk memahami hubungan model dengan template dengan mudah. Familiaritas dengan bahasa python yang dikenal sebagai bahasa high level juga mendukung proses pemahaman yang lebih mudah.

Tidak ada, asdos sangat helpful :D

</details>

---

# TUGAS 3

## Mengapa butuh _data delivery_ dalam pengimplementasian sebuah platform?

Data delivery penting untuk diimplementasikan agar komunikasi antara client dan server lancar. Dengan mengimplementasikan data delivery, kita dapat mengirim berbagai komponen yang membangun platform seperti file HTML, CSS, dan JavaScript. Data delivery juga membantu platform dinamis untuk mengirimkan raw data dalam format JSON atau XML.

## Mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Dalam konteks web development, menurut saya, JSON merupakan pilihan yang lebih baik dari XML. Alasan pertama adalah karena sintaksnya yang simpel yaitu pasangan key-value dengan bracket seperti dictionary dibandingkan XML yang lebih padat. JSON juga membedakan data type seperti string, angka, dan lainnya sementara XML memperlakukan semua data sebagai teks. Parsing JSON juga sangat efisien dan _computing cost_-nya lebih murah dibanding Parsing XML. JSON lebih populer dibanding XML karena merupakan standar format data jika menggunakan REST API (Representational State Transfer), dimana REST API banyak digunakan pada program dan aplikasi dinamis. Selain itu, JSON juga memiliki ukuran payload minimal sehingga banyak diandalkan oleh developer.

## Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?

Method is_valid() menjalankan validasi data yang diinput oleh user ke dalam form, apakah sesuai dengan spesifikasi fieldnya yang sudah diatur di model, seperti panjang, berbentuk angka atau huruf, dan lainnya. Method ini dibutuhkan agar tidak terjadi error walaupun input yang diberikan user ke form tidak sesuai dengan spesifikasi data yang seharusnya.

## Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

`csrf_token` dibutuhkan ketika membuat form di django karena mekanisme CSRF (Cross-Site Request Forgery) yang built-in membutuhkan token unik per sesi agar server bisa memastikan bahwa request/POST berasal dari halaman/form aplikasi kita dan bukan dari situs jahat. Jika kita tidak menambahkan `csrf_token`, proses verifikasi token ini akan dilewati sehingga keaslian request tidak bisa diketahui. Penyerang bisa memanfaatkan browser korban yang otomatis mengirim cookie otentikasi untuk mengirim request berbahaya lewat halaman tersembunyi dan bisa melakukan tindakan atas nama pengguna tanpa persetujuan mereka.

## Step by step mengerjakan checklist

- #### Menambahkan fungsi show_xml dan show_json ke views.py

  Fungsi-fungsi ini menerima parameter request dan mereturn HttpResponse berupa data yag sudah diserialisasi menjadi JSON. Fungsi ini mengembalikan semua objek produk yang ada pada web.

- #### Menambahkan fungsi show_xml_by_id dan show_json_by_id ke views.py

  Fungsi-fungsi ini menerima parameter request dan id produk dan mereturn HttpResponse berupa data yag sudah diserialisasi menjadi JSON. Fungsi ini mengembalikan objek produk tertentu yang ada pada web. Saya juga menambahkan try-except untuk verifikasi apakah produk dengan ID tersebut benar benar ada.

- #### Menambahkan routing untuk show_xml, show_json, show_xml_by_id dan show_json_by_id di Views.py

  Menambahkan routing endpoint `json/` ke fungsi show_json, `xml/` ke fungsi show_xml, `xml/<str:news_id>/` ke fungsi show_xml_by_id, dan `json/<str:news_id>/` ke fungsi show_json_by_id dengan menambahkan elemen path ke list urlpatterns.

- #### Membuat halaman yang menampilkan data objek model yang memiliki tombol "Add" yang akan redirect ke halaman `form`, serta tombol "Detail" pada setiap data objek model yang akan menampilkan halaman detail objek.

  - Membuat direktori templates level projek dan menambahkan base.html sebagai template dasar yang berisi:

  ```html{% load static %}
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      {% block meta %} {% endblock meta %}
  </head>

  <body>
      {% block content %} {% endblock content %}
  </body>
  </html>
  ```

  - Menambahkan string `templates` ke key `DIRS` variabel `TEMPLATES` yang ada di settings.py agar terdeteksi sebagai kerangka utama.
  - Menambahkan button `Add Product` ke main.html yang ada di templates level aplikasi. Button akan mengarah ke fungsi add_product di views.py.Mengecek apakah ada objek di product_list dan jika ada, menampilkan informasi generalnya dan menambahkan button `Detail` yang akan mengarahkan ke `product_detail`.

- #### Membuat halaman `form` untuk menambahkan objek model pada app sebelumnya.
  Membuat file forms.py di direktori main yang mengimpor objek Shop dan ModelForm, berisi class `ProductForm` (subclass ModelForm) yang menggunakan shop sebagai model dan field: "name", "price", "description", "thumbnail", "is_featured", "category", "rating", "stock". Kemudian, menambahkan impor NewsForm, redirect, dan get_object_or_404 di views.py. Membuat fungsi add_product yang menambahkan produk baru jika input valid dan show_product yang menampilkan detail deskripsi produk jika produk dengan id tersebut ada. Menambahkan routing aplikasi path `add_product/` dan `/product/<str:id>/` ke urlpatterns di urls.py di direktori main.
- #### Membuat halaman yang menampilkan detail dari setiap data objek mode
  Membuat berkas product_detail.html di templates aplikasi yang berisi deskripsi produk dan detail harga, stok, rating, dll dan sebuah tombol back to produck list yang akan mengarahkan kembali ke aplikasi main:

```html
{% extends 'base.html' %} {% block content %}
<p>
  <a href="{% url 'main:show_main' %}">
    <button>← Back to product List</button></a
  >
</p>
<h1>{{ product.title }}</h1>
<p>
  <b>{{ product.get_category_display }}</b>{% if product.is_featured %} |
  <b>Featured</b>{% endif %} | Price: Rp{{ product.price}} | Stock: {{
  product.stock }} | Rating: {{product.rating}} ⭐
</p>
{% if product.thumbnail %}
<img src="{{ product.thumbnail }}" alt="product thumbnail" width="300" />
<br /><br />
{% endif %}
<p>{{ product.description }}</p>
{% endblock content %}
```

## Feedback

Tidak ada :), asdos sangat helpful. Terima kasih bimbingannya 🙏

## Screenshot Postman

- #### show_json

  https://drive.google.com/file/d/10xRQI310lbT2HZyedSemOZTnF4lAEpE-/view?usp=sharing

- #### show_xml

  https://drive.google.com/file/d/17DluTv4-HiAgZcm5rjo6dhqnnZzX3Y-h/view?usp=sharing

- #### show_json_by_id

  https://drive.google.com/file/d/1ZWANGZHUK1bxzKwTRmB0Ys0IJolsqwgL/view?usp=sharing

- #### show_xml_by_id
  https://drive.google.com/file/d/1sZ7JYPD5qTrq_VdEpLox7H9iJY8GVhQV/view?usp=sharing

# Tugas 4

## Step by step mengerjakan checklist

- #### Menambahkan fungsi registrasi, login_user, logout_user ke views.py

  Fungsi-fungsi ini menerima parameter request dan meredirect user ke halaman utaam jika login/registrasi berhasil. Jika tidak, meminta user untuk mengisi form lagi. Untuk logout melakukan logout dan redirect ke halaman login.

- #### Menambahkan fungsi show_xml_by_id dan show_json_by_id ke views.py

  Fungsi-fungsi ini menerima parameter request dan id produk dan mereturn HttpResponse berupa data yag sudah diserialisasi menjadi JSON. Fungsi ini mengembalikan objek produk tertentu yang ada pada web. Saya juga menambahkan try-except untuk verifikasi apakah produk dengan ID tersebut benar benar ada.

- #### Membuat dua (2) akun pengguna dengan masing-masing tiga (3) dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal

  Run server dengan py manage.py runserver di virtual environment direktori dan melakukan registrasi manual 2 akun. Setelah registrasi, login dan tambahkan produk masing2 3 untuk setiap user.

- #### Menghubungkan model Shop dan User

  - Import user dari library django.contrib.auth.models ke models.py dan menambahkan atribut user berupa models.ForeignKey(User, on_delete=models.CASCADE, null=True)  ke class Shop.

  - Mengubah add_product di views.py menjadi login required dengan menambahkan decorator @login_required(login_url='/login') yang telah di import (restriksi agar setiap produk memiliki user)
  - Mengubah add_product di views.py menjadi:
```html
@login_required(login_url='/login')
def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "add_product.html", context)
```


  - Menambahkan button filter type ke show_main di views.py dengan default 'all' yang akan mengembalikan semua produk dan hanya produk milik user untuk filter selain 'all'.
  - Menambahkan button filter my dan all di main.html yang akan mengubah tipe filter ke all (untuk button all) dan ke my (untuk button my).
  - Menambahkan tampilan nama seller di product_details.

- #### Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last_login pada halaman utama aplikasi.
  - Menambahkan impor datetime, HttpResponseRedirect, dan reverse ke views.py
  - Mengubah fungsi login_user ketika berhasil login agar mengambil cookie dari aktivitas login. Return type menjadi HttpResponseRedirect(reverse("main:show_main")) yang cookienya last loginnya sudah di set ke waktu sekarang.
  - Menambahkan konteks last_login ke context di show_main, `'last_login': request.COOKIES.get('last_login', 'Never')`
  - Mengubah fungsi logout_user di views.py menjadi menghapus cookie lastlogin
  - Menambahkan tampilah sesi terakhir login di main.html

##  Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.

Django authentication form adalah form untuk login user yang menggunakan modul user dan login built in django untu verifikasi identitas user. Kelebihannya adalah sistem ini aman dan cepat karena pre-built sehingga developer tidak perlu susah membuat sistem login dari scratch. Form ini sudah menghandle aspek keamanan seperti hashing password. Kekurangannya adalah form ini kaku dab hanya menggunakan username sebagai pengenal, sehingga kalau mau menggunakan email (atau akun lain), perlu kustomisasi. Form ini juga belum menggunakan 2FA yang merupakan keamanan terbaik untuk menghindari hack.

## Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?

Autentikasi adalah proses verifikasi identitas seperti login, sementara otorisasi adalah verifikasi akses/izin untuk mengakses suatu data. Django mengimplementasikan authentication dengan django authentication form untuk menyimpan kredensial dan fungsi authenticate untuk login. Untuk otorisasi, django mengimplementasikannya melalui interface admin yang memiliki seksi terdedikasi "AUTHENTICATION AND AUTHORIZATION" untuk mengurus perizinan dan mengorganisir user ke group untuk mengontrol akses yang mereka dapatkan.

## Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?

Untuk session cookie, kelebihannya adalah lebih aman karena hanya disimpan di memori browser, tapi kekurangannya sangat sementara dan akan terhapus ketika browser ditutup. Untuk persistent cookie, lebih awet untuk tracking informasi dalam waktu panjang tetapi kurang aman karena dapat dibaca pengguna atau program lain. Untuk session, kelebihannya mengatasi masalah keamanan karena menyimpan daya di database server dan hanya mengirim ID sesi melalui ke client, tetapi ada resiko session forgery jika IDnya dipalsukan.

## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?

Penggunaan cookie tidak aman secara default .  Resiko potensialnya adalah Cross-site scripting (XSS) dan pemalsuan sesi. Django menangani resiko ini dengan tidak menyimpan data sesitif langsung di dalam cookie, tetapi di server side session, dimana cookie di browser hanya berisi ID dari sesi yang kemudian digunakan untuk mengambil data sesi yang disimpan dengan aman di database server. Django juga menyediakan perlindungan bawaan terhadap XSS dan CSRF secara default, dan menawarkan pengaturan seperti SESSION_COOKIE_SECURE untuk memastikan cookie hanya dikirim melalui https yang aman.