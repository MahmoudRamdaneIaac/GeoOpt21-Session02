from flask import Flask 
import ghhops_server as hs

#notice, we import another file as a library
import geometry as geo

#we also import random library to generate some randomness 
import random as r

#finally we bring rhino3dm to create rhino geometry in python
import rhino3dm as rg

app = Flask(__name__)
hops = hs.Hops(app)


@hops.component(
    "/SpheresFromPoints",
    name = "Spheres From Points",
    inputs=[
        hs.HopsPoint("Center of Spheres", "Center", "Center of Spheres", hs.HopsParamAccess.LIST),
        hs.HopsNumber("Radius of Spheres", "Radius", "Radius of Spheres", hs.HopsParamAccess.ITEM),
       

    ],
    outputs=[
       hs.HopsBrep("Sphere","Sphere","List of generated Spheres ", hs.HopsParamAccess.LIST)
    ]
)
def moreRandomPoints(count,rX, rY):

    randomPts = geo.createRandomPoints(count, rX, rY)
    Sphere= rg.sphere
    return randomPts

def Sphere()






if __name__== "__main__":
    app.run(debug=True)