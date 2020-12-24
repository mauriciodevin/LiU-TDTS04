-------------------------------------------------------------Exercise 3 ----------------------------------------------------------------------------

''' Importando Bibliotecas '''
from scipy.io import loadmat
import matplotlib.pyplot as plt
import numpy as np

''' Carregando os arquivos '''
data_spike = loadmat('\\Users\\mauricio\\Documents\\Maurício Devincentis\\UFABC\\Matérias\\Matérias 7º Quad\\Física Médica 2\\spike.mat')

''' Salvando spike em uma variável '''
raw_data = data_spike['spike'] #Python reconheceu o arquivo como um dicionário, por isso salvamos desse modo

''' Função para plotar o Espaço K '''
def Plot_K_Space(slice):    
    plt.figure()
    plt.title("Espaço K")
    plt.imshow(abs(slice), cmap="gray",vmin=0.0, vmax=35000)
    #plt.colorbar()
    plt.show()
    
''' Função para reconstrução da imagem após a transformada de Fourier 2D '''
def Plot_FFT2(slice):    
    plt.figure()
    plt.title("Imagem após transformação por FFT ")
    plt.imshow(abs(slice), cmap="gray",vmin=0.0, vmax=2000000)
    #plt.colorbar()
    plt.show()

''' Slice único - Espaço K com spike'''
Plot_K_Space(raw_data)   

''' Slice 13 - Reconstrução da imagem após a transformada de Fourier 2D com spike '''
Plot_FFT2(np.fft.fft2(raw_data))  


