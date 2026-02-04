def xu_ly_thue(quan_he):
    mien = [
        "vo_chong",
        "cha_me_con",
        "ong_ba_chau",
        "anh_em_ruot"
    ]
    if quan_he in mien:
        return "📌 Thuộc diện miễn thuế TNCN và lệ phí trước bạ"
    return "💰 Phải nộp thuế TNCN và lệ phí trước bạ theo quy định"


def tu_van_cho_tang(d):
    ly_do = []
    huong = []

    if not d["nguoi_con_song"]:
        ly_do.append("Người cho tặng đã mất → không thể cho tặng")
    if not d["co_so_do"]:
        ly_do.append("Không có sổ đỏ")
    if d["dang_tranh_chap"]:
        ly_do.append("Đất đang tranh chấp")
    if d["dang_the_chap"]:
        ly_do.append("Đất đang thế chấp ngân hàng")
    if d["dong_so_huu"] and not d["tat_ca_dong_y"]:
        ly_do.append("Thiếu sự đồng ý của đồng sở hữu")
    if not d["tu_nguyen"]:
        ly_do.append("Cho tặng không tự nguyện")

    if ly_do:
        return {
            "ket_luan": "❌ Không đủ điều kiện cho tặng",
            "ly_do": ly_do,
            "huong_xu_ly": ["Khắc phục các vấn đề trên trước khi làm thủ tục"]
        }

    huong = [
        "Lập hợp đồng cho tặng tại văn phòng công chứng",
        "Kê khai thuế và lệ phí",
        "Nộp hồ sơ sang tên tại Văn phòng đăng ký đất đai",
        xu_ly_thue(d["quan_he_nhan_than"])
    ]

    return {
        "ket_luan": "✅ Đủ điều kiện cho tặng quyền sử dụng đất",
        "ly_do": [],
        "huong_xu_ly": huong
    }


def tu_van_chuyen_nhuong(d):
    ly_do = []

    if not d["co_so_do"]:
        ly_do.append("Không có sổ đỏ")
    if d["dang_tranh_chap"]:
        ly_do.append("Đất đang tranh chấp")
    if d["dang_the_chap"]:
        ly_do.append("Đất đang thế chấp")
    if d["dong_so_huu"] and not d["tat_ca_dong_y"]:
        ly_do.append("Thiếu chữ ký đồng sở hữu")

    if ly_do:
        return {
            "ket_luan": "❌ Không đủ điều kiện chuyển nhượng",
            "ly_do": ly_do,
            "huong_xu_ly": []
        }

    return {
        "ket_luan": "✅ Đủ điều kiện chuyển nhượng quyền sử dụng đất",
        "ly_do": [],
        "huong_xu_ly": [
            "Công chứng hợp đồng chuyển nhượng",
            "Kê khai thuế TNCN và lệ phí trước bạ",
            "Nộp hồ sơ sang tên",
            "💰 Luôn phải nộp thuế theo giá chuyển nhượng"
        ]
    }


def tu_van_thua_ke(d):
    ly_do = []

    if d["nguoi_con_song"]:
        ly_do.append("Người để lại đất còn sống → chưa phát sinh thừa kế")
    if not d["co_so_do"]:
        ly_do.append("Không có sổ đỏ")
    if d["dang_tranh_chap"]:
        ly_do.append("Đất đang tranh chấp")

    if ly_do:
        return {
            "ket_luan": "❌ Chưa đủ điều kiện thừa kế",
            "ly_do": ly_do,
            "huong_xu_ly": []
        }

    return {
        "ket_luan": "✅ Đủ điều kiện làm thủ tục thừa kế",
        "ly_do": [],
        "huong_xu_ly": [
            "Lập văn bản khai nhận / phân chia di sản",
            "Công chứng theo quy định",
            "Nộp hồ sơ sang tên",
            xu_ly_thue(d["quan_he_nhan_than"])
        ]
    }



