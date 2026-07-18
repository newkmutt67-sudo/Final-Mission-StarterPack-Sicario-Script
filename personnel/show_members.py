# =====================================================
#  personnel/show_members.py — คนรับผิดชอบ: ______________________
#  หน้าที่: แสดงรายชื่อลูกน้องทั้งหมดในแฟมิลี่
# =====================================================
from data import family_members

def show_members():
    for i in family_members :
        print(f"ชื่อ : {i['name']} , ตำแหน่ง : {i['role']} , พละกำลัง : {i['power']} , อาวุธ : {i['equipment']}")


# ทดสอบเฉพาะไฟล์ตัวเอง: พิมพ์  python -m personnel.show_members
if __name__ == "__main__":
    show_members()   # ต้องเห็น Tony กับ Luigi คนละบรรทัด
