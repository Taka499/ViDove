
import openai


def LLM_task(model_name, input, task, temp = 0.15):
    """
    Translates input sentence with desired LLM.

    :param model_name: The name of the translation model to be used.
    :param input: Sentence for translation.
    :param task: Prompt.
    :param temp: Model temperature.
    """
    if model_name == "gpt-3.5-turbo" or model_name == "gpt-4":
        response = openai.ChatCompletion.create(
            model=model_name,
            messages=[
                {"role": "system","content": task},
                {"role": "user", "content": input}
            ],
            temperature=temp
        )
        return response['choices'][0]['message']['content'].strip()
    # Other LLM not implemented
    else:
        raise NotImplementedError