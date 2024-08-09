import json

class JsonKu:
    def __init__(self, file_name):
        self.file_name = file_name

    def baca(self):
        try:
            with open(self.file_name, 'r') as file:
                data = json.load(file)
                print(json.dumps(data, indent=4))
        except Exception as e:
            print(f"Error: {e}")

    def tulis(self):
        try:
            with open(self.file_name, 'r') as file:
                data = json.load(file)
            if not isinstance(data, list):
                data = [data]

            Nama_Buah = input("Masukkan Nama Buah: ")
            Harga = int(input("Masukkan Harga Buah (angka): "))

            data.append({"Nama Buah": Nama_Buah, "Harga": Harga})

            with open(self.file_name, 'w') as file:
                json.dump(data, file, indent=4)
            print("Data berhasil ditulis.")
        except Exception as e:
            print(f"Error: {e}")

    def update(self):
        try:
            with open(self.file_name, 'r') as file:
                data = json.load(file)
            if not isinstance(data, list):
                print("Data tidak dalam format list.")
                return

            index = int(input("Masukkan indeks baris yang ingin diperbarui (mulai dari 0): "))
            if index < 0 or index >= len(data):
                print("Indeks tidak valid.")
                return

            key_to_update = input("Masukkan kunci yang ingin diperbarui (Nama_Buah/Harga): ")
            if key_to_update not in data[index]:
                print(f"Kunci {key_to_update} tidak ditemukan.")
                return

            if key_to_update == "Harga":
                try:
                    new_value = int(input("Masukkan nilai baru (angka): "))
                except ValueError:
                    print("Nilai harus berupa angka.")
                    return
            else:
                new_value = input("Masukkan nilai baru: ")

            data[index][key_to_update] = new_value
            with open(self.file_name, 'w') as file:
                json.dump(data, file, indent=4)
            print(f"{key_to_update} berhasil diperbarui.")
        except Exception as e:
            print(f"Error: {e}")

    def hapus(self):
        try:
            with open(self.file_name, 'r') as file:
                data = json.load(file)
            if not isinstance(data, list):
                print("Data tidak dalam format list.")
                return

            index = int(input("Masukkan indeks baris yang ingin dihapus (mulai dari 0): "))
            if index < 0 or index >= len(data):
                print("Indeks tidak valid.")
                return

            del data[index]
            with open(self.file_name, 'w') as file:
                json.dump(data, file, indent=4)
            print(f"Data pada baris {index} berhasil dihapus.")
        except Exception as e:
            print(f"Error: {e}")