import time

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import config


_start_load_time = time.time()
print(f'Model "{config.TEXT_GENERATION_MODEL}" is loading...')

_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
_tokenizer = AutoTokenizer.from_pretrained(config.TEXT_GENERATION_MODEL)
_model = AutoModelForSeq2SeqLM.from_pretrained(config.TEXT_GENERATION_MODEL).to(_device).eval()

_end_load_time = time.time()
_load_time = round(_end_load_time - _start_load_time, 2)
print(f'Model "{config.TEXT_GENERATION_MODEL}" is loaded in {_load_time} seconds.')


def _get_name_of_writer(writer_id: int):
    return 'Собеседник: ' if writer_id == 0 else 'Ты: '


def _make_prompt(history: list[tuple[int, str]]):
    context = "\n".join([_get_name_of_writer(pair[0]) + ' ' + pair[1] for pair in history])

    return '<SC6>' + config.TEXT_GENERATION_MODEL_CONTEXT + "Продолжи диалог:\n" + context + '\nТы: <extra_id_0>'


def generate(history: list[tuple[int, str]]):
    prompt = _make_prompt(history)
    data = _tokenizer(prompt, return_tensors="pt").to(_device)

    output_ids = _model.generate(
        **data, do_sample=True, temperature=0.95, max_new_tokens=1024, top_p=0.95, top_k=10, repetition_penalty=1.4,
        no_repeat_ngram_size=3)[0]

    output = _tokenizer.decode(output_ids.tolist(), skip_special_tokens=True)
    return output.replace('<extra_id_0>', '', 1).replace('<extra_id_1>', '', 1)
