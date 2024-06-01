import os
import random
import argparse

import torch
import gradio as gr
import numpy as np

import ChatTTS
from openai import OpenAI

def generate_seed():
    new_seed = random.randint(1, 100000000)
    return {
        "__type__": "update",
        "value": new_seed
        }

chat_history = ""

def generate_audio(text, temperature, top_P, top_K, audio_seed_input, text_seed_input, refine_text_flag, text_output):
    global chat_history

    openai_api_key = "EMPTY"
    openai_api_base = "http://192.168.1.4:11434/v1"
    client = OpenAI(
            api_key=openai_api_key,
            base_url=openai_api_base,
        )

    prompt = chat_history + "\nUser:" + text + "\nAssistant:"
        
    qwen_response = client.chat.completions.create(
         model='qwen:14b',
         messages=[
             {"role": "user", "content": prompt},
          ],
        )
    chat_history += "\nUser:" + text + "\nAssistant:" + qwen_response.choices[0].message.content.strip()
    qwen_response = qwen_response.choices[0].message.content.strip()
    chat_response = qwen_response.replace('\n', ' ')
    chat_response = qwen_response.replace('-', ' ')
    chat_response = ' '.join(chat_response.split())



    if len(chat_response) > 100:
        chat_responses = [chat_response[i:i+100] for i in range(0, len(chat_response), 100)]
    else:
        chat_responses = [chat_response]

    torch.manual_seed(audio_seed_input)
    rand_spk = chat.sample_random_speaker()
    params_infer_code = {
        'spk_emb': rand_spk, 
        'temperature': temperature,
        'top_P': top_P,
        'top_K': top_K,
        }
    params_refine_text = {'prompt': '[oral_2][laugh_0][break_6]'}
    
    torch.manual_seed(text_seed_input)

    audio_data_list = []
    text_data_list = []

    for chat_response in chat_responses:
        if refine_text_flag:
            text = chat.infer(chat_response,
                      skip_refine_text=False,
                      refine_text_only=True,
                      params_refine_text=params_refine_text,
                      params_infer_code=params_infer_code
                          )
            text_data = text[0] if isinstance(text, list) else text
            text_data_list.append(text_data)

        wav = chat.infer(chat_response,
             skip_refine_text=True,
             params_refine_text=params_refine_text,
             params_infer_code=params_infer_code
                 )
        audio_data = np.array(wav[0]).flatten()
        audio_data_list.append(audio_data)
    merged_audio_data = np.concatenate(audio_data_list, axis=0)
    merged_text_data = ' '.join(text_data_list)

    sample_rate = 24000

    return [(sample_rate, merged_audio_data), merged_text_data]


def main():

    with gr.Blocks() as demo:


        with gr.Row():
            refine_text_checkbox = gr.Checkbox(label="Refine text", value=True)
            temperature_slider = gr.Slider(minimum=0.00001, maximum=1.0, step=0.00001, value=0.3, label="Audio temperature")
            top_p_slider = gr.Slider(minimum=0.1, maximum=0.9, step=0.05, value=0.7, label="top_P")
            top_k_slider = gr.Slider(minimum=1, maximum=20, step=1, value=20, label="top_K")

        with gr.Row():
            audio_seed_input = gr.Number(value=2, label="Audio Seed")
            generate_audio_seed = gr.Button("\U0001F3B2")
            text_seed_input = gr.Number(value=42, label="Text Seed")
            generate_text_seed = gr.Button("\U0001F3B2")

        
        text_output = gr.Textbox(label="Output Text",interactive=False)
        audio_output = gr.Audio(label="Output Audio", autoplay=True)

        default_text = "你好"        
        text_input = gr.Textbox(label="Input Text", lines=4, placeholder="Please Input Text...", value=default_text)

        generate_button = gr.Button("Generate")
        generate_audio_seed.click(generate_seed, 
                                  inputs=[], 
                                  outputs=audio_seed_input)
        
        generate_text_seed.click(generate_seed, 
                                 inputs=[], 
                                 outputs=text_seed_input)
        
        generate_button.click(generate_audio, 
                              inputs=[text_input, temperature_slider, top_p_slider, top_k_slider, audio_seed_input, text_seed_input, refine_text_checkbox], 
                              outputs=[audio_output, text_output])

    parser = argparse.ArgumentParser(description='ChatTTS demo Launch')
    parser.add_argument('--server_name', type=str, default='0.0.0.0', help='Server name')
    parser.add_argument('--server_port', type=int, default=1111, help='Server port')
    parser.add_argument('--local_path', type=str, default=None, help='the local_path if need')
    args = parser.parse_args()

    print("loading ChatTTS model...")
    global chat
    chat = ChatTTS.Chat()

    if args.local_path == None:
        chat.load_models()
    else:
        print('local model path:', args.local_path)
        chat.load_models('local', local_path=args.local_path)

    demo.launch(server_name=args.server_name, server_port=args.server_port, inbrowser=True)


if __name__ == '__main__':
    main()
