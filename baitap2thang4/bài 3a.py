# Đọc file và in nội dung trên một dòng
with open("demo_file1.txt", "r", encoding="utf-8") as file:
    content = file.read()              # Đọc toàn bộ nội dung
    content = content.replace("\n", " ")  # Thay xuống dòng bằng khoảng trắng
    
    print("Nội dung trên một dòng:")
    print(content)