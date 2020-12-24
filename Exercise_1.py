-------------------------------------------------------------Exercise 1 ----------------------------------------------------------------------------

from scipy.io import loadmat
import matplotlib.pyplot as plt
import numpy as np

''' Carregando os arquivos '''
data_raw = loadmat('\\Users\\mauricio\\Documents\\Maurício Devincentis\\UFABC\\Matérias\\Matérias 7º Quad\\Física Médica 2\\rawdata.mat')
''' Salvando rawdata em uma variável '''
raw_data = data_raw['rawdata'] #Python reconheceu o arquivo como um dicionário, por isso salvamos desse modo
''' Função para plotar o Espaço K '''
def Plot_K_Space(i, slice):
    x = ("Espaço K - Slice " + str(i+1))
    plt.figure()
    plt.title(x)
    plt.imshow(abs(slice), cmap="gray",vmin=0.0, vmax=35000) #Normalização 
    plt.show()  
''' Função para reconstrução da imagem após a transformada de Fourier 2D '''
def Plot_FFT2(i,slice):
    x = ("Imagem após transformação por FFT - Slice " + str(i+1))
    plt.figure()
    plt.title(x)
    plt.imshow(abs(slice), cmap="gray",vmin=0.0, vmax=1500000) #Normalização 
    plt.show()
''' Loop while para geração do Espaço-K dos slices requisitados '''
i = 5
while (i<=21):
    Plot_K_Space(i, raw_data[:,:,i])
    i = i +4      
''' Loop while para reconstrução das imagens após transformada de Fourier 2D dos slices requisitados '''
e = 5
while(e<=21):
    Plot_FFT2(e,np.fft.fft2(raw_data[:,:,e]))
    e = e +4


    


