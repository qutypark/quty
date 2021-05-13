[참고강의: Coursera의 DeepLearning.AI TensorFlow Developer ](https://www.coursera.org/professional-certificates/tensorflow-in-practice)

## 1. TensorFlow란 무엇인가 [TensorFlow](https://www.tensorflow.org/overview?hl=ko)

TensorFlow는 기계학습(Machine Learning = ML)을 위한 엔드 투 엔드 플랫폼으로,<br>
초보자도 손쉽게 모델을 빌딩할 수 있는 라이브러리들을 보유하고 있습니다. <br>
Python 기반 딥러닝(Deep Learning) API인, <br>
[Keras](https://keras.io)도 TensorFlow 환경에서 기동됩니다. 

위의 용어들을 부가적으로 설명하면 아래와 같습니다. 

####  기계학습(Machine Learning)

Traditional Programming과 대비되는 Machine Learning의 특징은

'데이터'와 '답'을 바탕으로 -> **'규칙(패턴)'** 을 학습시킨다는 것입니다. <br>
따라서 기계는 학습한 "규칙"을 바탕으로, 인간이 도출하기 어려운 답을 낼 수 있습니다. 

<img src="https://qph.fs.quoracdn.net/main-qimg-b9d72d501d7ce19f8aecfd9c1a1735dc" width=40% height=40%>

####  엔드 투 엔드(End to End)
AI와 ML분야에서의 엔드 투 엔드란 "처음부터 끝까지",<br>
즉 Input에서 Ouput을 내기까지의 모든 단계를 모델이 학습하여 실행한다는 것입니다.<br> 

ML의 하위분야인, 딥러닝의 학습 과정이 이에 해당하는데<br>
- ML은 Feature Selection과 같은 추가 단계가 필요되지만<br>
- 딥러닝은 모든 단계를 기계가 학습함을 알 수 있습니다.<br>

<img src="https://894532.smushcdn.com/2098219/wp-content/uploads/2019/04/MLvsDL.png" width=40% height=40%>


## 2. Neuron Networks

