# Link deployment : http://fadiansah-feryan-tugas2.pbp.cs.ui.ac.id/


<details>
<summary> <h1> Tugas 1 </h1> </summary>
<br>

# Pertanyaan 1

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Saya pertama menginitialize git repo (tetapi belum disambung dengan repo di github), lalu membuat virtual environment dan menginisialisasi Django project. Saya lalu memenuhi syarat tugas 2 pada bagian - bagian yang berbeda.

# Pertanyaan 2

Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html

https://imgur.com/a/WQYfBpF or pbpbagan.png

# Pertanyaan 3

### Jelaskan fungsi git dalam pengembangan perangkat lunak!

Git digunakan untuk melakukan version control dan melihat apa saja yang ditambahkan pada proyek pada timestamp tertentu. Git juga bisa digunakan untuk melakukan rollback ke versi sebelumnya jika ada masalah pada prod.

# Pertanyaan 4

### Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Karena Django pas untuk projek kecil dan memiliki paradigma yang cukup mudah untuk dimengerti.

# Pertanyaan 5

### Mengapa model pada Django disebut sebagai ORM?

Karena model pada Django berfungsi sebagai basis data untuk apa yang akan ditunjukkan kepada end-user dengan template.

</details>

<details>
<summary> <h1> Tugas 2 </h1> </summary>
<br>

# Pertanyaan 1

### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

_Data delivery_ sangat penting dalam implementasi platform untuk memastikan transfer informasi yang akurat dan tepat waktu antara _user_, sistem, dan _service_. Pengiriman data yang efisien juga membuat _user experience_ yang baik dengan memastikan keandalan platform. Tanpa mekanisme pengiriman data yang tepat, fungsi platform bisa terganggu, yang dapat menyebabkan disatisfaksi _user_.

# Pertanyaan 2

### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Saya pribadi lebih menyukai JSON karena dalam pandangan sekilas struktur data dapat dicerna dengan jelas. Saya rasa hal ini juga berpengaruh atas popularitasnya dibanding dengan XML.

# Pertanyaan 3

### Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?

method `is_valid()` dalam form Django digunakan untuk memastikan data dalam field form dapat diterima oleh model yang sudah di deklarasikan. method `is_valid()` diperlukan supaya saat data diberikan ke database tidak ada error yang terjadi.

# Pertanyaan 4

### Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

`csrf_token` pada django digunakan untuk memastikan bahwa semua request pengubahan data datang dari `user` yang benar. Jika tidak menggunakan `csrf_token` pada form, penyerang dapat memberi request yang tidak divalidasi, tetapi diterima sebagai request valid oleh server dan melakukan request tersebut.

# Pertanyaan 5

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

</details>
