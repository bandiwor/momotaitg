# Татьяна Момот - Телеграм Бот

Татьяна Момот - это интеллектуальный Телеграм бот, созданный с использованием библиотеки `aiogram` и модели `AutoModelForSeq2SeqLM`. Бот запоминает контекст беседы и обеспечивает более естественное взаимодействие с пользователями.

## Возможности

- Запоминание контекста беседы.
- Использование модели `AutoModelForSeq2SeqLM` для генерации текста.
- Возможность настройки модели, контекста и базы данных.

## Установка

### Требования

- Python 3.12
- pip (пакетный менеджер Python)
- Git

### Шаги по установке

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. Создайте виртуальное окружение:

    ```bash
    python -m venv venv
    ```

3. Активируйте виртуальное окружение:

    - **Windows:**

        ```bash
        venv\Scripts\activate
        ```

    - **Mac/Linux:**

        ```bash
        source venv/bin/activate
        ```

4. Установите зависимости из `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

5. Создайте бота через [BotFather](https://core.telegram.org/bots#botfather) и получите токен API.

6. Создайте файл `.env.local` и добавьте в него ваш токен:

    ```env
    TELEGRAM_BOT_API_TOKEN=your-telegram-bot-token
    ```

7. Опционально, вы можете изменить следующие параметры в `.env.local`:

    ```env
    TEXT_GENERATION_MODEL=your-model-name
    TEXT_GENERATION_MODEL_CONTEXT=your-prompt-context
    DB_FILENAME=your-database-filename.db
    ```

## Запуск бота

После выполнения всех шагов установки, запустите бота:

```bash
python main.py
```

# Вклад в проект
Мы приветствуем ваши вклад в проект! Если у вас есть идеи или вы нашли ошибки, пожалуйста, создайте issue или отправьте pull request.

## Лицензия
Этот проект лицензирован под MIT License.

_**_Надеемся, что вам понравится использовать Татьяну Момот! Если у вас есть вопросы или предложения, пожалуйста, не стесняйтесь обращаться._**_

Этот `README.md` файл содержит всю необходимую информацию для установки и настройки бота, а также приглашает к участию в проекте.

