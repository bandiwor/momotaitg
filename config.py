import os
from typing import Optional
import dotenv as _dotenv


_dotenv.load_dotenv('.env')
_dotenv.load_dotenv('.env.local')


class _DotEnvValueException(Exception):
    def __init__(self, key: str, description: str = '', _dot_env_filename: str = '.env'):
        error = f'Environment key "{key}" is None. Please add it to {_dot_env_filename}.'
        if description:
            error += f'\nDescription: {description}'

        super().__init__(error)


def _get_env_value(key: str, default: Optional[str] = None, exception: Optional[str] = None,
                   error_description: Optional[str] = None, dot_env_filename: Optional[str] = '.env') -> str:
    value = os.environ.get(key)
    if value is None and default is None:
        exception = exception or _DotEnvValueException(key, error_description, dot_env_filename)
        raise exception
    return value or default


TEXT_GENERATION_MODEL = _get_env_value(
    "TEXT_GENERATION_MODEL",
    error_description="Название модели на hugging face, для генерации текста в диаологах. "
                      "Модель должна поддерживать русский язык"
)

TEXT_GENERATION_MODEL_CONTEXT = _get_env_value(
    "TEXT_GENERATION_MODEL_CONTEXT",
    error_description="Контекст для модели, здесь можно указать основную информацию.Например Ты девушка, художница. "
                      "Увлекаешься нейросетевым искусством. Умеешь программировать. Любишь рисовать."
)

DB_FILENAME = _get_env_value(
    "DB_FILENAME",
    error_description="Путь к файл с базой данных sqlite. Нужна для хранения истории сообщений."
)

TELEGRAM_BOT_API_TOKEN = _get_env_value(
    "TELEGRAM_BOT_API_TOKEN",
    error_description="API токен бота в Telegram. Создать бота можно в @botfather.",
    dot_env_filename=".env.local"
)
