import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

def generate_save_plot(filename):
    iris = pd.read_csv('data/iris.data', sep=',', header=None)
    iris.columns = ["SepalLength", "SepalWidth", "PetalLength", "PetalWidth", "Species"]
    
    setosa = iris[iris['Species']=='Iris-setosa']
    versicolor = iris[iris['Species']=='Iris-versicolor']
    virginica = iris[iris['Species']=='Iris-virginica']
    
    # Plot distributions specific to species
    plt.figure()
    fig,ax=plt.subplots(1,2,figsize=(12,5))

    setosa.plot(x="SepalLength", y="SepalWidth", kind="scatter",ax=ax[0], label='setosa',color='r')
    versicolor.plot(x="SepalLength",y="SepalWidth",kind="scatter",ax=ax[0], label='versicolor',color='b')
    virginica.plot(x="SepalLength", y="SepalWidth", kind="scatter", ax=ax[0], label='virginica', color='g')

    setosa.plot(x="PetalLength", y="PetalWidth", kind="scatter",ax=ax[1], label='setosa',color='r')
    versicolor.plot(x="PetalLength",y="PetalWidth",kind="scatter",ax=ax[1], label='versicolor',color='b')
    virginica.plot(x="PetalLength", y="PetalWidth", kind="scatter", ax=ax[1], label='virginica', color='g')

    ax[0].set(title='Sepal Comparison ', ylabel='SepalWidth')
    ax[1].set(title='Petal Comparison',  ylabel='PetalWidth')
    ax[0].legend()
    ax[1].legend()
    
    # Save the figure to file
    # Can save axes as seperate figures by defining area
    plt.savefig(f'{filename}.png')  
    plt.close(fig)
    
    
if __name__ == '__main__':
    filename = sys.argv[1]
    
    generate_save_plot(filename)
    
    if os.path.isfile(f'{filename}.png'):
        print('Image saved successfully.')
    else:
        print('Error saving file!')
    