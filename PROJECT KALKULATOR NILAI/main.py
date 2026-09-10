import streamlit as st


st.title("🎓 Prediksi Pencapaian Nilai")


st.header("1. Tentukan Target Semester")
total_mapel_target = st.number_input("Berapa banyak mapel semester ini?", min_value=1, value=5)
target_rata_rata = st.number_input("Berapa target rata-rata nilai akhir kamu?", min_value=0.0, max_value=100.0, value=85.0)

st.divider()


st.header("2. Masukkan Nilai Mapel yang Sudah Ada")
st.write("Isi nilai mapel kamu di bawah. Nanti komputer yang hitung totalnya otomatis!")


if "daftar_nilai" not in st.session_state:
    st.session_state.daftar_nilai = {}


with st.form("form_mapel"):
    nama_mapel = st.text_input("Nama Mata Pelajaran (misal: Matematika)")
    nilai_mapel = st.number_input("Nilai", min_value=0.0, max_value=100.0, value=80.0)
    tombol_tambah = st.form_submit_button("Tambah Mapel")

    if tombol_tambah and nama_mapel:
        st.session_state.daftar_nilai[nama_mapel] = nilai_mapel
        st.success(f"Berhasil menambah {nama_mapel}: {nilai_mapel}")


if st.session_state.daftar_nilai:
    st.subheader("Daftar Nilai Kamu Saat Ini:")
    for mapel, nilai in st.session_state.daftar_nilai.items():
        st.write(f"- **{mapel}**: {nilai}")
    
    if st.button("Hapus Semua Mapel"):
        st.session_state.daftar_nilai = {}
        st.rerun()

st.divider()


st.header("3. Hasil Prediksi")

banyak_mapel = len(st.session_state.daftar_nilai)

if banyak_mapel > 0:
    
    jumlah_nilai = sum(st.session_state.daftar_nilai.values())
    rata_rata = jumlah_nilai / banyak_mapel
    
    sisa_mapel = total_mapel_target - banyak_mapel
    sisa_nilai_butuh = (target_rata_rata * total_mapel_target) - jumlah_nilai

    st.write(f"Total nilai terkumpul: **{jumlah_nilai}** dari **{banyak_mapel}** mapel.")
    st.write(f"Rata-rata saat ini: **{rata_rata:.2f}**")

    
    if sisa_mapel > 0:
        nilai_minimal = sisa_nilai_butuh / sisa_mapel
        if nilai_minimal > 100:
            st.error(f"Target tidak memungkinkan karena butuh nilai minimal **{nilai_minimal:.2f}** di tiap sisa mapel!")
        else:
            st.success(f"Kamu butuh nilai minimal **{nilai_minimal:.2f}** di **{sisa_mapel}** mapel sisanya.")
    elif sisa_mapel == 0:
        st.info("Semua mapel sudah terisi penuh!")
    else:
        st.warning("Jumlah mapel yang diinput melebihi target semester!")
else:
    st.info("Masukkan minimal 1 nilai mapel di atas untuk melihat prediksi.")