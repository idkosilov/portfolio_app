from PySide6.QtCore import QDate
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem

from portfolio_app.app_ui import Ui_MainWindow
from portfolio_app.portfolio_optimizer import PortfolioOptimizer
import matplotlib


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.current_date_edit.setDate(QDate.currentDate())

        self.window_size_map = {"3 месяца": 90,
                                "Полгода": 180,
                                "Год": 360,
                                "2 года": 360 * 2,
                                "3 года": 360 * 3,
                                "4 года": 360 * 4,
                                "5 лет": 360 * 5}

        self.window_size_combobox.addItems(list(self.window_size_map.keys()))
        self.risk_spinbox.setMinimum(0.00)
        self.risk_spinbox.setMaximum(100.00)
        self.risk_spinbox.setValue(0.05)

        self.next_day.clicked.connect(
            lambda: self.current_date_edit.setDate(self.current_date_edit.date().addDays(1))
        )

        self.previous_day.clicked.connect(
            lambda: self.current_date_edit.setDate(self.current_date_edit.date().addDays(-1))
        )

        self.optimize_button.clicked.connect(self.calculate_portfolio)
        self.portfolio_optimizer = PortfolioOptimizer('data.csv',
                                                      self.window_size_map[self.window_size_combobox.currentText()],
                                                      self.current_date_edit.date().toPython(),
                                                      self.risk_spinbox.value())

        self.portfolio_data = [[ticker, '0.0', '0.0'] for ticker in self.portfolio_optimizer.tickers()]

        for i, data in enumerate(self.portfolio_data):
            self.tickers_table.insertRow(i)
            for j, value in enumerate(data):
                self.tickers_table.setItem(i, j, QTableWidgetItem(str(value)))

    def calculate_portfolio(self):
        self.portfolio_optimizer.window_size = self.window_size_map[self.window_size_combobox.currentText()]
        self.portfolio_optimizer.current_date = self.current_date_edit.date().toPython()
        self.portfolio_optimizer.risk = self.risk_spinbox.value()

        weights, ret_tangent, std_tangent = self.portfolio_optimizer.optimize()

        self.label_7.setText(f"Доходность: {round(ret_tangent, 3)}")
        self.label_9.setText(f"Стандартное отклонение: {round(std_tangent, 3)}")

        self.ef_image.setPixmap(QPixmap('ef_scatter.png'))
        self.covariance_img.setPixmap(QPixmap('covariance.png'))
        self.assets_img.setPixmap(QPixmap('assets.png'))

        for row in self.portfolio_data:
            ticker = row[0]
            if ticker in weights.keys():
                row[1] = str(weights[ticker])
                row[2] = str(weights[ticker] - float(row[2]))

        self.portfolio_data.sort(key=lambda x: x[1], reverse=True)

        for i, data in enumerate(self.portfolio_data):
            for j, value in enumerate(data):
                self.tickers_table.setItem(i, j, QTableWidgetItem(str(value)))


def main():
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec()


if __name__ == "__main__":
    main()
