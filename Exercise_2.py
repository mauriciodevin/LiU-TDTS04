-------------------------------------------------------------Exercise 2 ----------------------------------------------------------------------------
''' Importando Bibliotecas '''
from scipy.io import loadmat
import matplotlib.pyplot as plt
import numpy as np

''' Carregando os arquivos '''
data_raw = loadmat('\\Users\\mauricio\\Documents\\Maurício Devincentis\\UFABC\\Matérias\\Matérias 7º Quad\\Física Médica 2\\rawdata.mat')

''' Salvando rawdata em uma variável '''
raw_data = data_raw['rawdata'] #Python reconheceu o arquivo como um dicionário, por isso salvamos desse modo
''' Função para plotar o Espaço K '''
def Plot_K_Space(i, e, slice):
    x = ("Espaço K - Slice " + str(i+1) + " Sub-amostrado a cada " + str(e) + " linhas")
    plt.figure()
    plt.title(x)
    plt.imshow(abs(slice), cmap="gray",vmin=0.0, vmax=35000)
    plt.show()
''' Função para reconstrução da imagem após a transformada de Fourier 2D '''
def Plot_FFT2(i, e, slice):
    x = ("Imagem após FFT - Slice " + str(i+1)+ " Sub-amostrado a cada " + str(e) + " linhas")
    plt.figure()
    plt.title(x)
    plt.imshow(abs(slice), cmap="gray",vmin=0.0, vmax=1500000)
    plt.show()
''' Passo para a sub amostragem relacionada ao número de linhas '''
linhas_2 = 2
linhas_4 = 4
''' Slice 13 sub-amostrado a cada 2 e 4 linhas '''
Plot_K_Space(12, linhas_2, raw_data[:,0:127:linhas_2,12])
Plot_K_Space(12, linhas_4, raw_data[:,0:127:linhas_4,12])
''' Slice 13 sub-amostrado a cada 2 e 4 linhas '''
Plot_FFT2(12, linhas_2, np.fft.fftshift(np.fft.fft2(raw_data[:,0:127:linhas_2,12]),1))
Plot_FFT2(12, linhas_4, np.fft.fftshift(np.fft.fft2(raw_data[:,0:127:linhas_4,12]),1))


