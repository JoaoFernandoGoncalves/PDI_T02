import numpy as np
import cv2 as cv
import glob

def highBoostFilter(idImagem):
    img = cv.imread(idImagem, 0)

    '''normalização da imagem'''
    img = img / 255

    '''Embaça a imagem'''
    imgBlur = cv.GaussianBlur(img, (3, 3), 0, 0)

    '''Faz a máscara'''
    imgMask = img - imgBlur

    '''Aplica o High Boost filter na imagem'''
    print("\n********************Aplicacao do********************\n*****************Filtro High Boost******************")

    k = 0
    kMax = int(input("\nDeseja aumentar o K até quanto: "))
    kInc = int(input("Deseja incrementar o K de quanto em quanto: "))

    while k < kMax and cv.waitKey(0):

        imgHB = img + k * imgMask
        k = k + kInc
        cv.imshow(f"Imagem com filtro High Boost p/ [K = {k}]", imgHB)
    
    cv.waitKey(0)
    cv.destroyAllWindows()
    
    print("\n****************************************************\n")

idImagens = glob.glob('Imagens\*.tif')

def main():
    id = 0
    total = len(idImagens)

    print("\n")

    while id != total:
        for indice, img in enumerate(idImagens):
            print(f"Opcao {indice}: {img}")

        print(f"Opcao {total}: encerrar programa")


        id = int(input("\nDigite o numero da imagem que deseja adcionar o filtro High Boost: "))

        if id == total:
            break

        highBoostFilter(idImagens[id])

if __name__ == "__main__":
    main()