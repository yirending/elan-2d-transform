import plotly.offline as pyo

import numpy as np

def eigenplot2(inputs):

    t=np.linspace(0, 2*np.pi, 50)
    x=np.cos(t)
    y=np.sin(t)

    matrix = dict(x11=inputs[0], x12=inputs[1], x21=inputs[2], x22=inputs[3])

    new_x = matrix['x11']*x + matrix['x12']*y
    new_y = matrix['x21']*x + matrix['x22']*y

    lim = max(max(abs(x)), max(abs(new_x)), max(abs(y)), max(abs(new_y)))

    # calculating eigenvalue and eigenvectors

    data = np.reshape(inputs,[2,2])

    eig = np.linalg.eig(data)

    if isinstance(eig[1][0][0], complex)==True or isinstance(eig[0][0], complex)==True:

        data=[dict(x=new_x, y=new_y, name='transformed', mode='markers', marker=dict(size=10, color='red')),
           dict(x=[0,matrix['x11']], y=[0,matrix['x21']], mode='lines', line=dict(color='green')),
           dict(x=[0,matrix['x12']], y=[0,matrix['x22']], mode='lines', line=dict(color='red')),
           dict(x=[0,-matrix['x11']], y=[0,-matrix['x21']], mode='lines', line=dict(color='blue')),
           dict(x=[0,-matrix['x12']], y=[0,-matrix['x22']], mode='lines', line=dict(color='orange'))]

    else:
        eig1 = eig[1].transpose()[0]/np.linalg.norm(eig[1].transpose()[0])
        eig2 = eig[1].transpose()[1]/np.linalg.norm(eig[1].transpose()[1])

        eig1 = [matrix['x11']*eig1[0] + matrix['x12']*eig1[1], matrix['x21']*eig1[0] + matrix['x22']*eig1[1]]
        eig2 = [matrix['x11']*eig2[0] + matrix['x12']*eig2[1], matrix['x21']*eig2[0] + matrix['x22']*eig2[1]]

        if eig[0][0] == 0 or eig[0][1] == 0:

            data=[dict(x=new_x, y=new_y, name='transformed', mode='markers', marker=dict(size=10, color='red')),
               dict(x=[0,matrix['x11']+0.001], y=[0,matrix['x21']+0.001], mode='lines', line=dict(color='green')),
               dict(x=[0,matrix['x12']+0.001], y=[0,matrix['x22']+0.001], mode='lines', line=dict(color='red')),
               dict(x=[0,-matrix['x11']+0.001], y=[0,-matrix['x21']+0.001], mode='lines', line=dict(color='blue')),
               dict(x=[0,-matrix['x12']+0.001], y=[0,-matrix['x22']+0.001], mode='lines', line=dict(color='orange')),
               dict(x=[0,eig1[0]+0.001], y=[0,eig1[1]+0.001], mode='lines', name='eigenvector', line=dict(color='black', width='5')),
               dict(x=[0,eig2[0]+0.001], y=[0, eig2[1]+0.001], mode='lines', name='eigenvector', line=dict(color='black', width='5')),
               ]
        else:

            data=[dict(x=new_x, y=new_y, name='transformed', mode='markers', marker=dict(size=10, color='red')),
               dict(x=[0,matrix['x11']], y=[0,matrix['x21']], mode='lines', line=dict(color='green')),
               dict(x=[0,matrix['x12']], y=[0,matrix['x22']], mode='lines', line=dict(color='red')),
               dict(x=[0,-matrix['x11']], y=[0,-matrix['x21']], mode='lines', line=dict(color='blue')),
               dict(x=[0,-matrix['x12']], y=[0,-matrix['x22']], mode='lines', line=dict(color='orange')),
               dict(x=[0,eig1[0]], y=[0,eig1[1]], mode='lines', name='eigenvector', line=dict(color='black', width='5')),
               dict(x=[0,eig2[0]], y=[0, eig2[1]], mode='lines', name='eigenvector', line=dict(color='black', width='5')),
               ]


    layout = dict(xaxis=dict(range=[-lim, lim], autorange=True, zeroline=False,),
                  yaxis=dict(range=[-lim, lim], autorange=True, zeroline=False,
                        scaleanchor ='x', scaleratio = 1),
                  title='Linear transformation of plane', hovermode='closest')

    figure = dict(data=data, layout=layout)

    return figure



def eigenplot(inputs):

    t=np.linspace(0, 2*np.pi, 50)
    x=np.cos(t)
    y=np.sin(t)

    matrix = dict(x11=inputs[0], x12=inputs[1], x21=inputs[2], x22=inputs[3])

    new_x = matrix['x11']*x + matrix['x12']*y
    new_y = matrix['x21']*x + matrix['x22']*y


    lim = max(max(abs(x)), max(abs(new_x)), max(abs(y)), max(abs(new_y)))


    # calculating eigenvalue and eigenvectors

    data = np.reshape(inputs,[2,2])

    eig = np.linalg.eig(data)

    if isinstance(eig[1][0][0], complex)==True or isinstance(eig[0][0], complex)==True:

        data=[dict(x=x, y=y, mode='markers', name='unit circle', marker=dict(size=5, color='blue')),
               dict(x=[0,1], y=[0,0], mode='lines', name='x-axis', line=dict(color='green' )),
               dict(x=[0,0], y=[0,1], mode='lines', name='y-axis', line=dict(color='red')),
               dict(x=[0,-1], y=[0,0], mode='lines', name='x-axis', line=dict(color='blue')),
               dict(x=[0,0], y=[0,-1], mode='lines', name='x-axis', line=dict(color='orange'))]
    else:
        eig1 = eig[1].transpose()[0]/np.linalg.norm(eig[1].transpose()[0])
        eig2 = eig[1].transpose()[1]/np.linalg.norm(eig[1].transpose()[1])

        data=[dict(x=x, y=y, mode='markers', name='unit circle', marker=dict(size=5, color='blue')),
               dict(x=[0,1], y=[0,0], mode='lines', name='x-axis', line=dict(color='green' )),
               dict(x=[0,0], y=[0,1], mode='lines', name='y-axis', line=dict(color='red')),
               dict(x=[0,-1], y=[0,0], mode='lines', name='x-axis', line=dict(color='blue')),
               dict(x=[0,0], y=[0,-1], mode='lines', name='x-axis', line=dict(color='orange')),
               dict(x=[0,eig1[0]], y=[0,eig1[1]], mode='lines', name='eigenvector', line=dict(color='black', width='5')),
               dict(x=[0,eig2[0]], y=[0, eig2[1]], mode='lines', name='eigenvector', line=dict(color='black', width='5')),
                   ]


    layout = dict(xaxis=dict(range=[-lim, lim], autorange=True, zeroline=False,),
                  yaxis=dict(range=[-lim, lim], autorange=True, zeroline=False, scaleanchor ='x',
                        scaleratio = 1),
                  title='Linear transformation of plane', hovermode='closest')

    figure = dict(data=data, layout=layout)

    return figure
