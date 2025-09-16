# ui_serial_temp_hum_time.py
import sys
import time
import serial
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont


# ---- Cấu hình cổng COM ----
SERIAL_PORT = "COM5"     # thay bằng COM thật của bạn
BAUDRATE = 115200        # tốc độ baud

class SerialReader:
    """Lớp đọc dữ liệu từ cổng COM"""
    def __init__(self, port=SERIAL_PORT, baudrate=BAUDRATE):
        try:
            self.ser = serial.Serial(port, baudrate, timeout=1)
            print(f"Đã mở {port} @ {baudrate}")
        except Exception as e:
            print("Không thể mở cổng serial:", e)
            self.ser = None

    def read_sensor(self):
        """Đọc 1 dòng dữ liệu dạng 'temp,hum'"""
        if not self.ser:
            return None
        try:
            line = self.ser.readline().decode("utf-8").strip()
            if not line:
                return None
            parts = line.split(",")
            if len(parts) < 2:
                return None
            temp = float(parts[0].strip())
            hum = float(parts[1].strip())
            return temp, hum
        except Exception:
            return None


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Thời gian - Nhiệt độ - Độ ẩm (UART)")
        self.setMinimumSize(420, 220)

        # Serial
        self.serial_reader = SerialReader()

        # Fonts
        title_font = QFont("Arial", 14, QFont.Weight.Bold)
        big_font = QFont("Arial", 28, QFont.Weight.Bold)
        small_font = QFont("Arial", 12)

        # Widgets
        self.title_label = QLabel("Trạm cảm biến (UART)")
        self.title_label.setFont(title_font)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Thời gian hệ thống (đồng hồ chạy liên tục)
        self.clock_label = QLabel("--:--:--")
        self.clock_label.setFont(big_font)
        self.clock_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Nhiệt độ + độ ẩm
        self.temp_label = QLabel("Nhiệt độ: -- °C")
        self.temp_label.setFont(small_font)
        self.hum_label = QLabel("Độ ẩm: -- %")
        self.hum_label.setFont(small_font)

        # Thời gian đọc cảm biến
        self.sensor_time_label = QLabel("Thời gian :")
        self.sensor_time_label.setFont(QFont("Arial", 12))
        self.sensor_time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Trạng thái kết nối
        self.status_label = QLabel("Đang kết nối COM...")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.title_label)
        layout.addWidget(self.clock_label)

        row = QHBoxLayout()
        row.addWidget(self.temp_label)
        row.addWidget(self.hum_label)
        layout.addLayout(row)

        layout.addWidget(self.sensor_time_label)
        layout.addWidget(self.status_label)
        self.setLayout(layout)

        # Timer cập nhật đồng hồ hệ thống
        self.clock_timer = QTimer(self)
        self.clock_timer.timeout.connect(self.update_clock)
        self.clock_timer.start(1000)
        self.update_clock()

        # Timer đọc dữ liệu sensor
        self.sensor_timer = QTimer(self)
        self.sensor_timer.timeout.connect(self.update_sensor)
        self.sensor_timer.start(1000)  # đọc mỗi 1 giây

    def update_clock(self):
        """Đồng hồ hệ thống"""
        now = time.localtime()
        self.clock_label.setText(time.strftime("%H:%M:%S", now))

    def update_sensor(self):
        """Đọc sensor từ UART + hiển thị"""
        data = self.serial_reader.read_sensor()
        if data is None:
            self.status_label.setText(f"Chưa nhận dữ liệu từ {SERIAL_PORT}")
            return

        temp, hum = data
        self.temp_label.setText(f"Nhiệt độ: {temp:.1f} °C")
        self.hum_label.setText(f"Độ ẩm: {hum:.1f} %")

        # Ghi lại thời gian đọc cảm biến
        now = time.localtime()
        self.sensor_time_label.setText("Thời gian " + time.strftime("%H:%M:%S", now))

        self.status_label.setText(f"Dữ liệu từ {SERIAL_PORT} @ {BAUDRATE}")


def main():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
