import streamlit as st
import requests

# Заголовок приложения
st.title("Загрузка и классификация документов")

# Отображение файлового поля для выбора одного или нескольких файлов
uploaded_files = st.file_uploader("Выберите файлы для загрузки", accept_multiple_files=True)

# Список для хранения информации о загруженных файлах
file_info_list = []

# Проверка, были ли выбраны файлы
if uploaded_files:
    # Итерация по всем выбранным файлам
    for uploaded_file in uploaded_files:
        # Отправка файла на 1й ендпоинт для классификации
        response = requests.post("http://localhost:8000/classify", files={"file": uploaded_file})
        # Получение типа документа из ответа API
        document_type = response.json()["document_type"]
        # Добавление информации о файле в список
        file_info_list.append({"filename": uploaded_file.name, "document_type": document_type})
    # Отображение таблицы с информацией о загруженных файлах
    st.table(file_info_list)
    # Отображение кнопки для загрузки файлов на сервер
    if st.button("Загрузить все файлы на сервер"):
        # Итерация по всем загруженным файлам
        for uploaded_file in uploaded_files:
            # Отправка файла на 2й ендпоинт для сохранения на сервере
            requests.post("http://localhost:8000/upload", files={"file": uploaded_file})
        # Отображение сообщения об успешной загрузке файлов
        st.success("Файлы успешно загружены на сервер")

# Отображение таблицы с ранее загруженными файлами
response = requests.get("http://localhost:8000/files")
uploaded_files = response.json()
st.table(uploaded_files)
