# Поскольку функция отображает окно сообщения, 
# ее тестирование может потребовать использования моков и прослушивания сигналов.

from bookkeeper.msg import message_box

def test_message_box(mocker):
    mock_messagebox = mocker.patch('PySide6.QtWidgets.QMessageBox')
    message_text = "Test Message"
    message_box(message_text)

    mock_messagebox.assert_called_once()        
    mock_messagebox.return_value.setWindowTitle.assert_called_with('Внимание!')
    mock_messagebox.return_value.setText.assert_called_with(message_text)
    mock_messagebox.return_value.exec.assert_called_once()  # Проверяем вызов exec()


# Здесь используется библиотека pytest-mock для удобного использования моков