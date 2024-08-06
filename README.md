# Multimodal

## CUMMOSI dataset download

## 🚀 Installation

The first step is to download the SDK:

```bash
git clone https://github.com/CMU-MultiComp-Lab/CMU-MultimodalSDK.git
```

Next, you need to install the SDK on your python enviroment.

```bash
cd CMU-MultimodalSDK
pip install .
```

## MELD dataset download

```bash
wget http://web.eecs.umich.edu/~mihalcea/downloads/MELD.Raw.tar.gz
```

## 🚀 Installation

Since the MELD dataset does not provide audio data, we can use ffmpeg to manually obtain the audio data.

The first step is to download the ffmpeg:
``` bash
wget https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-i686-static.tar.xz
xz -d ffmpeg-git-amd64-static.tar.xz
tar -xvf ffmpeg-git-amd64-static.tar
cd ./ffmpeg-git-amd64-static
./ffmpeg
```

## Extracting audio data
```bash
python /MELD/split_audio_from_video.py
```
Download the pre-trained audio feature extractor wave2vec:
```bash
wegt https://dl.fbaipublicfiles.com/fairseq/wav2vec/wav2vec_large.pt
```

```bash
python wav2vec_embedding.py
```


## IEMOCAP dataset download

To obtain the IEMOCAP data you just need to fill out an electronic release form below.

```bash
https://sail.usc.edu/iemocap/iemocap_release.htm
```
