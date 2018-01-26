FROM continuumio/miniconda3:4.3.27p0
# https://hub.docker.com/r/continuumio/anaconda/

# TODO create non-root user

WORKDIR /home/usr

RUN conda install -y --quiet \
        jupyter \
        pyyaml \
        pypandoc

VOLUME /home/usr
EXPOSE 8888


CMD ["jupyter", "notebook", \
    "--notebook-dir=/home/usr/", \
    "--ip='*'", "--port=8888", \
    "--no-browser",\
    "--allow-root" \
    ]

# For Windows users# Note: <> denotes changes to be made
# #Create a conda environment
# conda create --name <environment-name> python=<version:2.7/3.5>
#
# #To create a requirements.txt file:
# conda list #Gives you list of packages used for the environment
#
# conda list -e > requirements.txt #Save all the info about packages to your folder
#
# #To export environment file
# activate <environment-name>
# conda env export > <environment-name>.yml
#
# #For other person to use the environment
# conda env create -f <environment-name>.yml
