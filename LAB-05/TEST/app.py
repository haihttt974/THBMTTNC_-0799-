from flask import Flask, render_template, jsonify
import os
import subprocess
import threading
import time
import platform

# Nếu là Windows, import win32 để đẩy cửa sổ Qt lên trên
if platform.system() == "Windows":
    import win32gui
    import win32con

# === Flask app khởi tạo ===
app = Flask(__name__, template_folder="templates")

# === Đưa cửa sổ lên foreground (Windows only) ===
def bring_qt_to_front(window_title_contains: str):
    time.sleep(1.5)  # đợi Qt form kịp mở
    def enum_handler(hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            if window_title_contains.lower() in title.lower():
                win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                win32gui.SetForegroundWindow(hwnd)
    win32gui.EnumWindows(enum_handler, None)

# === Chạy Qt script tương ứng và đẩy lên top nếu cần ===
def run_qt_script(script_filename):
    # Lấy đường dẫn chính xác từ TEST/ đến LAB-03/
    script_path = os.path.abspath(os.path.join("..", "..", "LAB-03", script_filename))
    print(f"[INFO] Đang chạy Qt: {script_path}")
    
    subprocess.Popen(["python", script_path], shell=True)

    # Nếu Windows → cố đẩy form lên trước
    if platform.system() == "Windows":
        window_title = script_filename.replace(".py", "")
        threading.Thread(target=bring_qt_to_front, args=(window_title,)).start()

# === Trang chủ giao diện web ===
@app.route("/")
def home():
    return render_template("index.html")

# === Các API mở từng giao diện mã hóa ===
@app.route("/open/caesar")
def open_caesar():
    threading.Thread(target=run_qt_script, args=("caesar_cipher.py",)).start()
    return jsonify({"status": "success", "message": "Đã mở Caesar Cipher Qt"})

@app.route("/open/vigenere")
def open_vigenere():
    threading.Thread(target=run_qt_script, args=("vigenere_cipher.py",)).start()
    return jsonify({"status": "success", "message": "Đã mở Vigenère Cipher Qt"})

@app.route("/open/railfence")
def open_railfence():
    threading.Thread(target=run_qt_script, args=("railfence_cipher.py",)).start()
    return jsonify({"status": "success", "message": "Đã mở Rail Fence Cipher Qt"})

@app.route("/open/playfair")
def open_playfair():
    threading.Thread(target=run_qt_script, args=("playfair_cipher.py",)).start()
    return jsonify({"status": "success", "message": "Đã mở Playfair Cipher Qt"})

# === Chạy Flask ===
if __name__ == "__main__":
    print("🚀 Flask server tại: http://127.0.0.1:5050")
    app.run(port=5050, debug=True)
