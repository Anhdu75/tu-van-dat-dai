from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from rules import tu_van_cho_tang, tu_van_chuyen_nhuong, tu_van_thua_ke

app = FastAPI(title="Tư vấn thủ tục đất đai")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "ket_qua": None}
    )


@app.post("/xu-ly", response_class=HTMLResponse)
def xu_ly(
    request: Request,
    loai_giao_dich: str = Form(...),

    nguoi_con_song: bool = Form(False),
    co_so_do: bool = Form(False),
    dang_tranh_chap: bool = Form(False),
    dang_the_chap: bool = Form(False),
    dong_so_huu: bool = Form(False),
    tat_ca_dong_y: bool = Form(False),
    tu_nguyen: bool = Form(False),

    quan_he_nhan_than: str = Form(...)
):
    data = {
        "nguoi_con_song": nguoi_con_song,
        "co_so_do": co_so_do,
        "dang_tranh_chap": dang_tranh_chap,
        "dang_the_chap": dang_the_chap,
        "dong_so_huu": dong_so_huu,
        "tat_ca_dong_y": tat_ca_dong_y,
        "tu_nguyen": tu_nguyen,
        "quan_he_nhan_than": quan_he_nhan_than,
    }

    if loai_giao_dich == "cho_tang":
        ket_qua = tu_van_cho_tang(data)
    elif loai_giao_dich == "chuyen_nhuong":
        ket_qua = tu_van_chuyen_nhuong(data)
    elif loai_giao_dich == "thua_ke":
        ket_qua = tu_van_thua_ke(data)
    else:
        ket_qua = {
            "ket_luan": "Chưa chọn loại giao dịch hợp lệ",
            "ly_do": [],
            "huong_xu_ly": []
        }

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "ket_qua": ket_qua}
    )
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9000)








