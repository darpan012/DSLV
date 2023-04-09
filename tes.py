str = """"
absl-py                      1.3.0
astunparse                   1.6.3
attrs                        22.1.0
cachetools                   5.2.0
certifi                      2022.9.24
charset-normalizer           2.1.1
contourpy                    1.0.6
cvzone                       1.5.6
cycler                       0.11.0
flatbuffers                  22.10.26
fonttools                    4.38.0
gast                         0.4.0
google-auth                  2.14.1
google-auth-oauthlib         0.4.6
google-pasta                 0.2.0
grpcio                       1.50.0
h5py                         3.7.0
idna                         3.4
keras                        2.11.0
kiwisolver                   1.4.4
libclang                     14.0.6
Markdown                     3.4.1
MarkupSafe                   2.1.1
matplotlib                   3.6.2
mediapipe                    0.9.0
numpy                        1.23.5
oauthlib                     3.2.2
opencv-contrib-python        4.6.0.66
opencv-python                4.6.0.66
opt-einsum                   3.3.0
packaging                    21.3
Pillow                       9.3.0
pip                          22.3.1
protobuf                     3.19.6
pyasn1                       0.4.8
pyasn1-modules               0.2.8
pyparsing                    3.0.9
python-dateutil              2.8.2
requests                     2.28.1
requests-oauthlib            1.3.1
rsa                          4.9
setuptools                   63.2.0
six                          1.16.0
tensorboard                  2.11.0
tensorboard-data-server      0.6.1
tensorboard-plugin-wit       1.8.1
tensorflow                   2.11.0
tensorflow-estimator         2.11.0
tensorflow-intel             2.11.0
tensorflow-io-gcs-filesystem 0.28.0
termcolor                    2.1.1
typing_extensions            4.4.0
urllib3                      1.26.12
Werkzeug                     2.2.2
wheel                        0.38.4
wrapt                        1.14.1
"""


l = str.split("\n")

mod = []
for i in l :
    mod.append(i.split(" "))
    
modules = []
for i in mod :
    for j in i :
        if j not in ["", " ", '"'] : modules.append(j)
    
versions = {}

for i in range(len(modules)) :
    if i % 2 == 0 : 
        versions.setdefault("name", []).append(modules[i])
    else : 
        versions.setdefault("version", []).append(modules[i])
# print(versions)


for k, v in zip(versions["name"], versions["version"]) :
    print(k,v,sep="==")