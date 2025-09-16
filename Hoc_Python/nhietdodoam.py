import datetime

def tao_file_du_lieu(filename="data.txt"):
    try:
        with open(filename, "w", encoding="utf-8") as f:

            # Ví dụ 5 dòng dữ liệu mẫu
            du_lieu = [
                (25.6, 60),

            ]

            for nhiet_do, do_am in du_lieu:
                thoigian = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                dong = f"{thoigian}, {nhiet_do}, {do_am}\n"
                f.write(dong)
        print(f"✅ Đã tạo file '{filename}' thành công.")
    except Exception as e:
        print("Lỗi khi tạo file:", e)

if __name__ == "__main__":
    tao_file_du_lieu()
