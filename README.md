Tautan menuju PWS: https://naila-khadijah-i-wear-soccer.pbp.cs.ui.ac.id/

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

Migrasi database django bekerja dalam 2 langkah. Setelah mengubah model di models.py, untuk menerapkan ke database, jalankan  python manage.py makemigrations di cmd. Perintah ini akan membuat file migrasi yang berisi instruksi untuk mempersiapkan perubahan skema model agar sesuai dengan database lokal Django. Untuk menerapkannya, kemudian jalankan perintah python manage.py migrate yang mengambil file migrasi yang telah dibuat sebelumnya dan menerapkan skema model yang baru ke dalam database Django.

Menurut saya, alasan django dijadikan permulaan pembelajaran pengembangan perangkat lunak adalah karena framework ini adalah framework paling stabil dari framework lainnya.  Berdasarkan benchmark https://sharkbench.dev/web, stabilitas django mencapai 93.76%. Django juga menggunakan arsitektur MVT yang memudahkan mahasiswa untuk memahami hubungan model dengan template dengan mudah. Familiaritas dengan bahasa python yang dikenal sebagai bahasa high level juga mendukung proses pemahaman yang lebih mudah.

Tidak ada, asdos sangat helpful :D
