# LegalDocClassifier
## ЦП 2024. Кейс "Семантическая классификация документов"

## Файлы проекта
[03.ipynb](https://github.com/invincible/LegalDocClassifier/blob/main/03.ipynb) Разведочный анализ данных + TfIdf + LogisticRegression (0.85);

[cat.ipynb](https://github.com/invincible/LegalDocClassifier/blob/main/cat.ipynb) CatBoost на доп фичах и чистом тексте, кастомный токенизатор. (**0.96**);

[textclass.ipynb](https://github.com/invincible/LegalDocClassifier/blob/main/textclass.ipynb) Проверка различных гипотез: LogisticRegression (**0.97**), CatBoostClassifier (0.93), DeepPavlov/rubert-base-cased-sentence (0.88);

[Server](https://github.com/invincible/LegalDocClassifier/tree/main/Server) Серверная часть API (FastAPI) + фронтенд (Streamlit)
