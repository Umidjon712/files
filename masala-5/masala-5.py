"""
Vazifa: Foydalanuvchidan so’z kiritadi. Kiritilgan so’zning birinchi yarmini ekranga chop eting.
Input:
Salom dunyo
Output:
Natija: Salom

"""

soz = str(input("so'z kiriting = "))

yarim = soz[:len(soz) // 2]

print(f"birinchi yarmi: {yarim}")