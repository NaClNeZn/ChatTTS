import ChatTTS
import torch
import torchaudio

"""
基础用法
"""
chat = ChatTTS.Chat()
# 设置为True以获得更好的性能
chat.load(compile=False)

texts = ["您好，您吃了吗"]

wavs = chat.infer(texts)

for i in range(len(wavs)):
    """
    In some versions of torchaudio, the first line works but in other versions, so does the second line.
    """
    try:
        torchaudio.save(f"basic_output{i}.wav", torch.from_numpy(wavs[i]).unsqueeze(0), 24000)
    except:
        torchaudio.save(f"basic_output{i}.wav", torch.from_numpy(wavs[i]), 24000)
