# Đọc file và in từng dòng
with open("demo_file1.txt", "r", encoding="utf-8") as file:
    print("Nội dung theo từng dòng:")
    
    for line in file:
        print(line.strip())  # Xóa ký tự xuống dòng