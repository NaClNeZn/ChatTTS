import ChatTTS
import torch
import torchaudio

"""
进阶用法
"""

chat = ChatTTS.Chat()
# 设置为True以获得更好的性能
chat.load(compile=False)
texts = ["您好，您吃了吗"]

###################################
# Sample a speaker from Gaussian.

rand_spk = chat.sample_random_speaker()
print(rand_spk) # save it for later timbre recovery

params_infer_code = ChatTTS.Chat.InferCodeParams(
    spk_emb = rand_spk, # add sampled speaker
    temperature = .3,   # using custom temperature
    top_P = 0.7,        # top P decode
    top_K = 20,         # top K decode
)

###################################
# For sentence level manual control.

# use oral_(0-9), laugh_(0-2), break_(0-7)
# to generate special token in text to synthesize.
params_refine_text = ChatTTS.Chat.RefineTextParams(
    prompt='[oral_2][laugh_0][break_6]',
)

wavs = chat.infer(
    texts,
    params_refine_text=params_refine_text,
    params_infer_code=params_infer_code,
)

###################################
# For word level manual control.

text = 'What is [uv_break]your favorite english food?[laugh][lbreak]'
wavs = chat.infer(text, skip_refine_text=True, params_refine_text=params_refine_text,  params_infer_code=params_infer_code)
"""
In some versions of torchaudio, the first line works but in other versions, so does the second line.
"""
try:
    torchaudio.save("word_level_output.wav", torch.from_numpy(wavs[0]).unsqueeze(0), 24000)
except:
    torchaudio.save("word_level_output.wav", torch.from_numpy(wavs[0]), 24000)
