如果无法下载模型，请去下载  https://github.com/jianchang512/ChatTTS-ui/releases/download/v1.0/all-models.7z


下载后解压后，会看到asset文件夹，该文件夹内有多个pt文件，将所有pt文件复制到本目录下


可以修改core.py中的compile bool = True，改为False，性能有所改善。


CPU:
```shell
docker run -d \
  --privileged \
  --name chat-tts \
  -p 9999:9999 \
  -e LOG_LEVEL=DEBUG \
  registry.cn-hangzhou.aliyuncs.com/nacl-public/chat-tts:v1.0-cpu 
```

GPU:
```shell
docker run -d \
  --privileged \
  --runtime=nvidia \
  --name chat-tts \
  -p 9999:9999 \
  -e LOG_LEVEL=DEBUG \
  -e NVIDIA_DRIVER_CAPABILITIES=compute,utility \
  -e NVIDIA_VISIBLE_DEVICES=all \
  --gpus all \
  registry.cn-hangzhou.aliyuncs.com/nacl-public/chat-tts:v1.0-gpu 
```