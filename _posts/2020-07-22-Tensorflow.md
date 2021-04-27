---
layout: post
title:  Tensorflow
date:   2020-06-22 19:31:29 +0900
category: AI
--- 
# Tensorflow

*   텐서플로우는 Google이 지원하고 실제 구글에서도 사용을 하고 있는 &quot;데이터 플로우 그래프를 이용한 수치 계산을 위한 오픈 소스 라이브러리&quot; 입니다.
*   2015년 11월에 처음 공개된 오픈 소스로 머신 러닝(Machine Learning)에서 현재 제일 활발히 이용 되는 기계학습 전용 라이브러리 입니다. 텐서플로우가 머신러닝이나 딥러닝에서 주로 쓰이는 이유는 &#39;분산, 묶음&#39;이 주된 이유 입니다.
*   분산: GPU를 이용한 병렬처리 등이 가능
*   묶음: TensorFlow, TensorBoard, TensorFlow Serving이라는 소프트웨어들의 묶음

\*TensorFlow: 모델 정의, 데이터 학습

\*TensorBoard: 네트워크 시각화 프로그램

\*TensorFlow Serving: 이미 학습된 텐서플로우 모델을 쉽게 활용할 수 있게 하는 소프트웨어. 모델을 만들고 돌려보는 작업을 훨씬 빠르게 반복적으로 할 수 있도록 해줍니다.

그 외의 프레임워크들 Caffee: C++로 작성된 신경망으로 영상처리에 집중

Chainer: Python 기반으로 한 컴퓨터에서 여러 개의 GPU를 활용

Nervana Neon: Python 기반으로 한 컴퓨터에서 여러 개의 GPU를 활용

Deeplearning4j: Java기반으로 Spark, Hadoop, 다른 자바 기반의 분산 소프트웨어와 결합되어서 활용

Theano: Python 기반으로 유연하고, 쉽고, 사용자 친화적이며 Tensorflow와 비슷

Torch: Lua로 작성되어여러 대혀 회사에서 지원 받음

## tensorflow/stream\_executor/cuda/cuda\_driver.cc 오류

```ruby
py379) goalpae@fintech:~/project/FinBot$ rasa shell
2020-11-16 20:37:51.762905: E tensorflow/stream_executor/cuda/cuda_driver.cc:314] failed call to cuInit: CUDA_ERROR_NO_DEVICE: no CUDA-capable device is detected

-- 현재 개발 서버는 ADM 계열이라 Tensorflow GPU 가 support 되지 않는다
따라서 설치된 tensorflow를 삭제 하고 tensorflow-cpu 버전을 설치 한다
$ pip uninstall tensorflow
$ pip install tensorflow-cpu
```

END