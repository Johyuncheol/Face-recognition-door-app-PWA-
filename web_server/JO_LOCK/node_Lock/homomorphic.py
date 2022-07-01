import cv2
import numpy as np


def homo(x):
    # homomorphic filter는 gray scale image에 대해서 밖에 안 되므로
    # YUV color space로 converting한 뒤 Y에 대해 연산을 진행
    img = x
    img_YUV = cv2.cvtColor(img, cv2.COLOR_BGR2YUV) #빛의 밝기를나타내는 휘도y 와 색상신호u,v 로구성   
    y = img_YUV[:,:,0] #빛의 밝기인 휘도 
 
    rows = y.shape[0] # 행개수    
    cols = y.shape[1] # 열개수 
 
    # 조명요소과 반사요소를 분리하기 위해 log를 취함
    imgLog = np.log1p(np.array(y, dtype='float') / 255) # y값을 0~1사이로 정규화 0~255는 큰차이라 정규화를 통해 비율로 사용
 
    # frequency를 이미지로 나타내면 4분면에 대칭적으로 나타나므로 
    # 4분면 중 하나에 이미지를 대응시키기 위해 row와 column을 2배씩 늘려줌(백터공간 정의하려면 선형결합연산(덧셈,곱셈)에 성립하고 닫혀있어야함 )
    M = 2*rows + 1
    N = 2*cols + 1
 
    # gaussian mask 생성 sigma = 10
    sigma = 10 # 차단주파수
    (X, Y) = np.meshgrid(np.linspace(0, N-1, N), np.linspace(0, M-1, M)) # 0~N-1(and M-1) 까지 1단위로 space를 만듬
    Xc = np.ceil(N/2) # 올림 연산
    Yc = np.ceil(M/2)
    gaussianNumerator = (X - Xc)**2 + (Y - Yc)**2 # 가우시안 분자 생성 e의 지수로 쓰일것
 
    # low pass filter와 high pass filter 생성
    LPF = np.exp(-gaussianNumerator / (2*sigma*sigma))
    HPF = 1 - LPF # LPF와 HPF의 관계
 
    # LPF랑 HPF를 0이 가운데로 오도록iFFT함. 
    # 에너지를 각 귀퉁이로 모아 줌
    LPF_shift = np.fft.ifftshift(LPF.copy())
    HPF_shift = np.fft.ifftshift(HPF.copy())
 
    ### Log를 씌운 이미지를 FFT해서 LPF와 HPF를 곱해 LF성분과 HF성분을 나눔
    img_FFT = np.fft.fft2(imgLog.copy(), (M, N))
    img_LF = np.real(np.fft.ifft2(img_FFT.copy() * LPF_shift, (M, N))) # low frequency 성분 조명
    img_HF = np.real(np.fft.ifft2(img_FFT.copy() * HPF_shift, (M, N))) # high frequency 성분 반사 edge
 
    # 각 LF, HF 성분에  조정값 를 곱해주어 조명값과 반사값을 조절함
    gamma1 = 0.8
    gamma2 = 1.1
    img_adjusting = gamma1*img_LF[0:rows, 0:cols] + gamma2*img_HF[0:rows, 0:cols] #디지털이미지는 조명요소와 반사요소의 곱으로 결합 주파수영역이기에 덧셈으로
 
    # 조정된 데이터를 이제 exp 연산을 통해 이미지로 만들어줌
    img_exp = np.expm1(img_adjusting) # e^x - 1 역변환
    img_exp = (img_exp - np.min(img_exp)) / (np.max(img_exp) - np.min(img_exp)) # 0~1사이로 정규화
    img_out = np.array(255*img_exp, dtype = 'uint8') # 255를 곱해서 intensity값을 만들어줌
 
    # YUV에서 Y space를 filtering된 이미지로 교체해주고 RGB 
    img_YUV[:,:,0] = img_out
    result = cv2.cvtColor(img_YUV, cv2.COLOR_YUV2BGR)
    result = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    #result1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #cv2.imshow('homomorphic', result)
    #cv2.imshow('homomorphic1', result1)


    return(result)

