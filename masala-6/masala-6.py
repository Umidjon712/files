"""
Vazifa: Foydalanuvchidan so’z kiritadi. Kiritilgan so’zning ikkinchi yarmi bilan birinchi yarmini almashtiring ekranga chop eting.
Input:
Salom dunyo
Output:
Natija: dunyo Salom

"""

soz = str(input("so'z kiriting: "))

yarim_1 = soz[:len(soz) // 2]
yarim_2 = soz[len(soz) // 2:]

yarim_1, yarim_2 = yarim_2, yarim_1

print(f"natija:{yarim_1} {yarim_2}")