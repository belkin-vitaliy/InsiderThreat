InsiderThreat 🛡️
Проект для выявления инсайдерских угроз с использованием поведенческого анализа (UEBA), графовых нейросетей (GCN) и временных моделей (LSTM).

📌 Описание
Данный проект реализует гибридную модель анализа поведения пользователей в корпоративной сети на основе:

графов взаимодействий (user–resource),

временной динамики событий,

расчёта поведенческого риска.

Проект включает генерацию данных, построение графов, обучение моделей и визуализацию отчётов.

🛠️ Технологии
Python 3.10+

Pandas, NumPy

PyTorch, PyTorch Geometric (GCN/GCN+LSTM)

Matplotlib / Seaborn

Jupyter Notebook

📁 Структура проекта
Папка/Файл	Назначение
data/	CSV-файлы: nodes.csv, edges.csv, resources.csv
Build_Graph_From_CSV.ipynb	Построение графа из CSV
GCN-GCNLSTM-Training.ipynb	Обучение моделей GCN и GCN+LSTM
InsiderThreat-UEBA-Reports-Risk.ipynb	Отчёт по UEBA с визуализацией рисков
InsiderThreat-UBA-Reports-SoftColors.ipynb	Графический отчёт с цветовой кодировкой
GenData*.ipynb	Генерация искусственных данных
PrepareEdges*.ipynb, Node.ipynb, resources.ipynb	Предобработка узлов, рёбер, ресурсов
.idea/	Файлы конфигурации среды разработки (PyCharm)

🚀 Быстрый старт
Установите зависимости:

bash
Копировать
Редактировать
pip install -r requirements.txt
Если requirements.txt отсутствует, используйте:

bash
Копировать
Редактировать
pip install torch torch-geometric pandas matplotlib seaborn
Запустите ноутбуки по очереди:

GenData.ipynb — генерация или загрузка данных

Build_Graph_From_CSV.ipynb — построение графа

GCN-GCNLSTM-Training.ipynb — обучение моделей

InsiderThreat-UEBA-Reports-Risk.ipynb — анализ и визуализация результатов

📊 Визуализация
В проекте реализована цветовая кодировка рисков и интерактивные графики для оценки поведения пользователей, включая уровень доступа, типы событий и временные характеристики.

🧠 Модель
GCN — извлекает структурные зависимости пользователей и ресурсов.

LSTM — моделирует поведение во времени.

Гибрид GCN + LSTM — сочетает преимущества графов и временных рядов.

📄 Лицензия
Лицензия не указана. Добавьте файл LICENSE, если распространяется публично.

📬 Контакты
Автор проекта: belkin-vitaliy

